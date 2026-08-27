import bpy

for index, obj in enumerate(bpy.context.selected_objects, start=1):
    obj.name = f"Object_{index:03d}"
