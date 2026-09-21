import bpy
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 3))
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=(0, 0, 4.4))
bpy.context.active_object.name = "head"
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.4, location=(0, 0, 5.2))
bpy.context.active_object.name = "Top"
snow = bpy.data.materials.new(name="Snow")
snow.diffuse_color = (1, 1, 1, 1)
bpy.data.objects["head"].data.materials.append(snow)
bpy.data.objects["Top"].data.materials.append(snow)
