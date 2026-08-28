import bpy

"""
Batch Bevel Setup
Adds a controlled Bevel modifier to every selected mesh.
Automatically enables hardened normals for cleaner hard-surface shading.
"""

WIDTH = 0.02
SEGMENTS = 3
ANGLE_LIMIT = 0.523599  # 30 degrees

objects = [o for o in bpy.context.selected_objects if o.type == 'MESH']

if not objects:
    raise RuntimeError("Select one or more mesh objects.")

for obj in objects:
    modifier = obj.modifiers.get("Production Bevel")

    if modifier is None:
        modifier = obj.modifiers.new(
            name="Production Bevel",
            type='BEVEL'
        )

    modifier.limit_method = 'ANGLE'
    modifier.angle_limit = ANGLE_LIMIT
    modifier.width = WIDTH
    modifier.segments = SEGMENTS
    modifier.harden_normals = True
    modifier.miter_outer = 'MITER_ARC'

    # Ensure smooth shading where possible.
    for poly in obj.data.polygons:
        poly.use_smooth = True

print(f"Configured production bevels on {len(objects)} mesh object(s).")
