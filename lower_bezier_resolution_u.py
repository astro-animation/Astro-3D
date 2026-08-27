import bpy

# Lower the selected Bézier curve's Resolution U to 3

obj = bpy.context.active_object

if obj and obj.type == 'CURVE':
    obj.data.resolution_u = 3
    print(f"Resolution U changed to 3 for: {obj.name}")
else:
    print("Please select a Bézier curve object.")
