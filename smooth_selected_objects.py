import bpy

for obj in bpy.context.selected_objects:
    if obj.type == 'MESH':
        for polygon in obj.data.polygons:
            polygon.use_smooth = True
