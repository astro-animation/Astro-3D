import bpy

bpy.ops.object.camera_add(location=(7, -7, 5))

camera = bpy.context.active_object
camera.name = "Camera"

bpy.context.scene.camera = camera
