import bpy, math


def changeSunRotation(self, context):
    acon_sun = bpy.data.objects.get("ACON_sun")
    if not acon_sun: acon_sun = createAconSun()

    prop = context.scene.ACON_prop

    acon_sun.rotation_euler.x = math.radians(90) - prop.sun_rotation_x
    acon_sun.rotation_euler.y = 0
    acon_sun.rotation_euler.z = prop.sun_rotation_z


def toggleSun(self, context):
    acon_sun = bpy.data.objects.get("ACON_sun")
    if not acon_sun: acon_sun = createAconSun()

    prop = context.scene.ACON_prop

    acon_sun.data.use_shadow = prop.toggle_sun
    acon_sun.hide_viewport = not prop.toggle_sun
    acon_sun.hide_render = not prop.toggle_sun
    acon_sun.data.use_shadow = prop.toggle_shadow


def changeSunStrength(self, context):
    acon_sun = bpy.data.objects.get("ACON_sun")
    if not acon_sun: acon_sun = createAconSun()

    prop = context.scene.ACON_prop

    acon_sun.data.energy = prop.sun_strength


def toggleShadow(self, context):
    acon_sun = bpy.data.objects.get("ACON_sun")
    if not acon_sun: acon_sun = createAconSun()

    prop = context.scene.ACON_prop

    acon_sun.data.use_shadow = prop.toggle_shadow


def setupSharpShadow():
    bpy.context.scene.eevee.shadow_cube_size = "4096"
    bpy.context.scene.eevee.shadow_cascade_size = "4096"
    bpy.context.scene.eevee.use_soft_shadows = True

    acon_sun = bpy.data.objects.get("ACON_sun")

    if not acon_sun: acon_sun = createAconSun()

    acon_sun.data.angle = 0
    acon_sun.data.use_contact_shadow = 1


def createAconSun():
    acon_sun_data = bpy.data.lights.new("ACON_sun", type="SUN")
    acon_sun_data.energy = 1
    acon_sun = bpy.data.objects.new("ACON_sun", acon_sun_data)
    acon_sun.rotation_euler.x = math.radians(90 - 35)
    acon_sun.rotation_euler.y = 0
    acon_sun.rotation_euler.z = math.radians(65)
    bpy.context.scene.collection.objects.link(acon_sun)

    return acon_sun
