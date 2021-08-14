import bpy
from . import shadow
from .materials import materials_handler
from types import SimpleNamespace
from math import radians


def genSceneName(name, i=1):
    found = None
    combinedName = name + str(i)

    for scene in bpy.data.scenes:
        if scene.name == combinedName:
            found = True
            break

    if found: return genSceneName(name, i+1)
    else: return combinedName


def add_scene_items(self, context):
    items = []
    for item in bpy.data.scenes:
        items.append((item.name, item.name, ""))

    return items


def loadScene(self, context):
    current_scene = context.scene
    target_scene = bpy.data.scenes[current_scene.ACON_prop.scene]

    if current_scene is target_scene: return

    override = SimpleNamespace()
    override.scene = target_scene
    
    materials_handler.toggleToonEdge(self, override)
    materials_handler.changeLineProps(self, override)
    materials_handler.toggleToonFace(self, override)
    materials_handler.toggleTexture(self, override)
    materials_handler.toggleShading(self, override)
    materials_handler.changeToonDepth(self, override)
    materials_handler.changeToonShadingBrightness(self, override)
    shadow.toggleSun(self, override)
    shadow.changeSunStrength(self, override)
    shadow.toggleShadow(self, override)
    shadow.changeSunRotation(self, override)
    materials_handler.changeImageAdjustBrightness(self, override)
    materials_handler.changeImageAdjustContrast(self, override)
    materials_handler.changeImageAdjustColor(self, override)
    materials_handler.changeImageAdjustHue(self, override)
    materials_handler.changeImageAdjustSaturation(self, override)
    
    context.window.scene = target_scene

    target_scene.ACON_prop.scene = current_scene.ACON_prop.scene


def setupPresets():
    context = bpy.context
    old_scene = context.scene

    # create indoor-daytime preset
    sceneName = "Indoor Daytime"
    new_scene = bpy.data.scenes.get(sceneName)

    if not new_scene:
        new_scene = old_scene.copy()
        new_scene.name = sceneName

    if old_scene.camera is new_scene.camera:
        new_scene.camera = old_scene.camera.copy()
        new_scene.camera.data = old_scene.camera.data.copy()
        new_scene.collection.objects.link(new_scene.camera)
    
        try: new_scene.collection.objects.unlink(old_scene.camera)
        except: print("Failed to unlink camera from old scene.")
    
    prop = new_scene.ACON_prop
    prop.toggle_toon_edge = True
    prop.edge_min_line_width = 1
    prop.edge_max_line_width = 1
    prop.edge_line_detail = 1.5
    prop.toggle_toon_face = True
    prop.toggle_texture = True
    prop.toggle_shading = True
    prop.toon_shading_depth = "3"
    prop.toon_shading_brightness_1 = 3
    prop.toon_shading_brightness_2 = 5
    prop.toggle_sun = True
    prop.sun_strength = 0.7
    prop.toggle_shadow = True
    prop.sun_rotation_x = radians(45)
    prop.sun_rotation_z = radians(45)
    prop.image_adjust_brightness = 0.7
    prop.image_adjust_contrast = 0.5
    prop.image_adjust_color_r = 0.95
    prop.image_adjust_color_g = 0.95
    prop.image_adjust_color_b = 1.05
    prop.image_adjust_hue = 0.5
    prop.image_adjust_saturation = 1
    new_scene.eevee.use_bloom = True
    new_scene.eevee.bloom_threshold = 2
    new_scene.eevee.bloom_knee = 0.5
    new_scene.eevee.bloom_radius = 6.5
    new_scene.eevee.bloom_color = (1, 1, 1)
    new_scene.eevee.bloom_intensity = 0.1
    new_scene.eevee.bloom_clamp = 0
    new_scene.camera.data.lens = 25
    new_scene.render.resolution_x = 4800
    new_scene.render.resolution_y = 2700

    # create indoor-sunset preset
    sceneName = "Indoor Sunset"
    new_scene = bpy.data.scenes.get(sceneName)

    if not new_scene:
        new_scene = old_scene.copy()
        new_scene.name = sceneName

    if old_scene.camera is new_scene.camera:
        new_scene.camera = old_scene.camera.copy()
        new_scene.camera.data = old_scene.camera.data.copy()
        new_scene.collection.objects.link(new_scene.camera)
    
        try: new_scene.collection.objects.unlink(old_scene.camera)
        except: print("Failed to unlink camera from old scene.")
    
    prop = new_scene.ACON_prop
    prop.toggle_toon_edge = True
    prop.edge_min_line_width = 1
    prop.edge_max_line_width = 1
    prop.edge_line_detail = 1.5
    prop.toggle_toon_face = True
    prop.toggle_texture = True
    prop.toggle_shading = True
    prop.toon_shading_depth = "3"
    prop.toon_shading_brightness_1 = 3
    prop.toon_shading_brightness_2 = 5
    prop.toggle_sun = True
    prop.sun_strength = 1
    prop.toggle_shadow = True
    prop.sun_rotation_x = radians(15)
    prop.sun_rotation_z = radians(45)
    prop.image_adjust_brightness = 0
    prop.image_adjust_contrast = 0
    prop.image_adjust_color_r = 1.1
    prop.image_adjust_color_g = 0.9
    prop.image_adjust_color_b = 0.9
    prop.image_adjust_hue = 0.5
    prop.image_adjust_saturation = 1
    new_scene.eevee.use_bloom = True
    new_scene.eevee.bloom_threshold = 1
    new_scene.eevee.bloom_knee = 0.5
    new_scene.eevee.bloom_radius = 6.5
    new_scene.eevee.bloom_color = (1, 1, 1)
    new_scene.eevee.bloom_intensity = 0.5
    new_scene.eevee.bloom_clamp = 0
    new_scene.camera.data.lens = 25
    new_scene.render.resolution_x = 4800
    new_scene.render.resolution_y = 2700

    # create indoor-nighttime preset
    sceneName = "Indoor Nighttime"
    new_scene = bpy.data.scenes.get(sceneName)

    if not new_scene:
        new_scene = old_scene.copy()
        new_scene.name = sceneName

    if old_scene.camera is new_scene.camera:
        new_scene.camera = old_scene.camera.copy()
        new_scene.camera.data = old_scene.camera.data.copy()
        new_scene.collection.objects.link(new_scene.camera)
    
        try: new_scene.collection.objects.unlink(old_scene.camera)
        except: print("Failed to unlink camera from old scene.")
    
    prop = new_scene.ACON_prop
    prop.toggle_toon_edge = True
    prop.edge_min_line_width = 1
    prop.edge_max_line_width = 1
    prop.edge_line_detail = 1.5
    prop.toggle_toon_face = True
    prop.toggle_texture = True
    prop.toggle_shading = True
    prop.toon_shading_depth = "3"
    prop.toon_shading_brightness_1 = 3
    prop.toon_shading_brightness_2 = 5
    prop.toggle_sun = True
    prop.sun_strength = 0.5
    prop.toggle_shadow = False
    prop.sun_rotation_x = radians(65)
    prop.sun_rotation_z = radians(45)
    prop.image_adjust_brightness = 0.1
    prop.image_adjust_contrast = 0
    prop.image_adjust_color_r = 1.05
    prop.image_adjust_color_g = 1
    prop.image_adjust_color_b = 0.95
    prop.image_adjust_hue = 0.5
    prop.image_adjust_saturation = 1
    new_scene.eevee.use_bloom = True
    new_scene.eevee.bloom_threshold = 1
    new_scene.eevee.bloom_knee = 0.5
    new_scene.eevee.bloom_radius = 6.5
    new_scene.eevee.bloom_color = (0.9, 0.9, 1)
    new_scene.eevee.bloom_intensity = 0.5
    new_scene.eevee.bloom_clamp = 0
    new_scene.camera.data.lens = 25
    new_scene.render.resolution_x = 4800
    new_scene.render.resolution_y = 2700

    # create outdoor-daytime preset
    sceneName = "Outdoor Daytime"
    new_scene = bpy.data.scenes.get(sceneName)

    if not new_scene:
        new_scene = old_scene.copy()
        new_scene.name = sceneName

    if old_scene.camera is new_scene.camera:
        new_scene.camera = old_scene.camera.copy()
        new_scene.camera.data = old_scene.camera.data.copy()
        new_scene.collection.objects.link(new_scene.camera)
    
        try: new_scene.collection.objects.unlink(old_scene.camera)
        except: print("Failed to unlink camera from old scene.")
    
    prop = new_scene.ACON_prop
    prop.toggle_toon_edge = True
    prop.edge_min_line_width = 1
    prop.edge_max_line_width = 1
    prop.edge_line_detail = 1.5
    prop.toggle_toon_face = True
    prop.toggle_texture = True
    prop.toggle_shading = True
    prop.toon_shading_depth = "3"
    prop.toon_shading_brightness_1 = 3
    prop.toon_shading_brightness_2 = 5
    prop.toggle_sun = True
    prop.sun_strength = 1
    prop.toggle_shadow = True
    prop.sun_rotation_x = radians(60)
    prop.sun_rotation_z = radians(45)
    prop.image_adjust_brightness = 0.7
    prop.image_adjust_contrast = 0.5
    prop.image_adjust_color_r = 1
    prop.image_adjust_color_g = 1
    prop.image_adjust_color_b = 1
    prop.image_adjust_hue = 0.5
    prop.image_adjust_saturation = 1
    new_scene.eevee.use_bloom = False
    new_scene.eevee.bloom_threshold = 1
    new_scene.eevee.bloom_knee = 0.5
    new_scene.eevee.bloom_radius = 6.5
    new_scene.eevee.bloom_color = (1, 1, 1)
    new_scene.eevee.bloom_intensity = 0.1
    new_scene.eevee.bloom_clamp = 0
    new_scene.camera.data.lens = 35
    new_scene.render.resolution_x = 4800
    new_scene.render.resolution_y = 2700

    # create outdoor-sunset preset
    sceneName = "Outdoor Sunset"
    new_scene = bpy.data.scenes.get(sceneName)

    if not new_scene:
        new_scene = old_scene.copy()
        new_scene.name = sceneName

    if old_scene.camera is new_scene.camera:
        new_scene.camera = old_scene.camera.copy()
        new_scene.camera.data = old_scene.camera.data.copy()
        new_scene.collection.objects.link(new_scene.camera)
    
        try: new_scene.collection.objects.unlink(old_scene.camera)
        except: print("Failed to unlink camera from old scene.")
    
    prop = new_scene.ACON_prop
    prop.toggle_toon_edge = True
    prop.edge_min_line_width = 1
    prop.edge_max_line_width = 1
    prop.edge_line_detail = 1.5
    prop.toggle_toon_face = True
    prop.toggle_texture = True
    prop.toggle_shading = True
    prop.toon_shading_depth = "3"
    prop.toon_shading_brightness_1 = 3
    prop.toon_shading_brightness_2 = 5
    prop.toggle_sun = True
    prop.sun_strength = 1
    prop.toggle_shadow = True
    prop.sun_rotation_x = radians(15)
    prop.sun_rotation_z = radians(45)
    prop.image_adjust_brightness = 0
    prop.image_adjust_contrast = 0
    prop.image_adjust_color_r = 1.1
    prop.image_adjust_color_g = 0.9
    prop.image_adjust_color_b = 0.9
    prop.image_adjust_hue = 0.5
    prop.image_adjust_saturation = 1
    new_scene.eevee.use_bloom = True
    new_scene.eevee.bloom_threshold = 0.8
    new_scene.eevee.bloom_knee = 0.5
    new_scene.eevee.bloom_radius = 6.5
    new_scene.eevee.bloom_color = (1, 0.9, 0.8)
    new_scene.eevee.bloom_intensity = 0.5
    new_scene.eevee.bloom_clamp = 0
    new_scene.camera.data.lens = 35
    new_scene.render.resolution_x = 4800
    new_scene.render.resolution_y = 2700

    # create outdoor-nighttime preset
    sceneName = "Outdoor Nighttime"
    new_scene = bpy.data.scenes.get(sceneName)

    if not new_scene:
        new_scene = old_scene.copy()
        new_scene.name = sceneName

    if old_scene.camera is new_scene.camera:
        new_scene.camera = old_scene.camera.copy()
        new_scene.camera.data = old_scene.camera.data.copy()
        new_scene.collection.objects.link(new_scene.camera)
    
        try: new_scene.collection.objects.unlink(old_scene.camera)
        except: print("Failed to unlink camera from old scene.")
    
    prop = new_scene.ACON_prop
    prop.toggle_toon_edge = True
    prop.edge_min_line_width = 1
    prop.edge_max_line_width = 1
    prop.edge_line_detail = 1.5
    prop.toggle_toon_face = True
    prop.toggle_texture = True
    prop.toggle_shading = True
    prop.toon_shading_depth = "3"
    prop.toon_shading_brightness_1 = 3
    prop.toon_shading_brightness_2 = 5
    prop.toggle_sun = True
    prop.sun_strength = 0.4
    prop.toggle_shadow = False
    prop.sun_rotation_x = radians(60)
    prop.sun_rotation_z = radians(45)
    prop.image_adjust_brightness = -0.3
    prop.image_adjust_contrast = -0.25
    prop.image_adjust_color_r = 0.9
    prop.image_adjust_color_g = 0.9
    prop.image_adjust_color_b = 1.1
    prop.image_adjust_hue = 0.5
    prop.image_adjust_saturation = 1.2
    new_scene.eevee.use_bloom = True
    new_scene.eevee.bloom_threshold = 1
    new_scene.eevee.bloom_knee = 0.5
    new_scene.eevee.bloom_radius = 6.5
    new_scene.eevee.bloom_color = (1, 1, 1)
    new_scene.eevee.bloom_intensity = 1
    new_scene.eevee.bloom_clamp = 0
    new_scene.camera.data.lens = 35
    new_scene.render.resolution_x = 4800
    new_scene.render.resolution_y = 2700


    # set to original scene in ui panel
    context.scene.ACON_prop.scene = old_scene.name