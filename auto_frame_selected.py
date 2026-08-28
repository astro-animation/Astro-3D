import bpy
from mathutils import Vector

"""
Auto Frame Selected
Moves the active camera so all selected mesh objects fit inside the frame.
Useful for automated presentation renders and asset previews.
"""

scene = bpy.context.scene
camera = scene.camera

if camera is None:
    raise RuntimeError("No active scene camera exists.")

objects = [o for o in bpy.context.selected_objects if o.type == 'MESH']
if not objects:
    raise RuntimeError("Select at least one mesh object.")

# Collect world-space bounding-box corners.
corners = []
for obj in objects:
    corners.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)

center = sum(corners, Vector()) / len(corners)

max_distance = max((corner - center).length for corner in corners)
padding = 1.35

# Position camera along its local -Z axis.
camera_distance = max(max_distance * padding, 0.5)
camera.location = center + Vector((0, 0, camera_distance))

# Point camera toward the center.
direction = center - camera.location
camera.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()

scene.camera = camera

print(f"Camera framed {len(objects)} selected object(s).")
