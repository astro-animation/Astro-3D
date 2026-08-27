import bpy

obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    modifier = obj.modifiers.new(
        name="Subdivision",
        type='SUBSURF'
    )
    modifier.levels = 2
    modifier.render_levels = 2
