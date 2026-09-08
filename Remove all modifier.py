import bpy

# Remove all modifiers from all objects
for obj in bpy.context.scene.objects:
    if obj.modifiers:
        obj.modifiers.clear()
