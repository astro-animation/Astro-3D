import bpy
import math

# Process every mesh object
for obj in bpy.context.scene.objects:
    if obj.type != 'MESH':
        continue

    # Select only this object
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Make sure a UV map exists
    if not obj.data.uv_layers:
        obj.data.uv_layers.new(name="UVMap")

    # Edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Select all geometry
    bpy.ops.mesh.select_all(action='SELECT')

    # Smart UV Project
    bpy.ops.uv.smart_project(
        angle_limit=math.radians(66.0),
        island_margin=0.0,
        area_weight=0.0,
        correct_aspect=True,
        scale_to_bounds=False
    )

    # Object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    obj.select_set(False)

print("Smart UV Project completed with 66° and 0.000 island margin.")
