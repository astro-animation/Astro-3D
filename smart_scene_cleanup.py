import bpy

"""
Smart Scene Cleanup
Removes unused data blocks and optionally orphaned collections.
Keeps cameras, lights, meshes, materials, and objects that are still in use.
"""

def purge_orphans():
    for _ in range(3):
        try:
            bpy.ops.outliner.orphans_purge(
                do_local_ids=True,
                do_linked_ids=True,
                do_recursive=True
            )
        except RuntimeError:
            break

# Remove objects with invalid / missing data.
for obj in list(bpy.data.objects):
    if obj.type == 'MESH' and obj.data is None:
        bpy.data.objects.remove(obj, do_unlink=True)

purge_orphans()

print("Smart scene cleanup complete.")
