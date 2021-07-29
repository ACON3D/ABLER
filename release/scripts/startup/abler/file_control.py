bl_info = {
    "name": "ACON3D Panel",
    "description": "",
    "author": "hoie@acon3d.com",
    "version": (0, 0, 1),
    "blender": (2, 93, 0),
    "location": "",
    "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "ACON3D"
}
import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.app.handlers import persistent

from .lib import materials, common


@persistent
def load_handler(dummy):
    common.switchToRendredView()
    common.turnOnCameraView(False)
    common.setupSharpShadow()
    bpy.ops.workspace.append_activate(idname="ACON3D")
    materials.applyAconToonStyle()


class ImportOperator(bpy.types.Operator, ImportHelper):
    """Import objects from a .blend file"""
    bl_idname = "acon3d.import_blend"
    bl_label = "Import"

    filter_glob: bpy.props.StringProperty(
        default='*.blend', options={'HIDDEN'}
    )

    def execute(self, context):
        FILEPATH = self.filepath

        collection = bpy.data.collections.new("Imported")
        bpy.context.scene.collection.children.link(collection)

        with bpy.data.libraries.load(FILEPATH) as (data_from, data_to):
            data_to.collections = data_from.collections
            data_to.objects = [name for name in data_from.objects]
        
        children_names = {}

        for coll in data_to.collections:
            for child in coll.children.keys():
                children_names[child] = True
        
        for coll in data_to.collections:
            
            found = False
            for child in children_names:
                if coll.name == child:
                    found = True
            
            if not found:
                collection.children.link(coll)
        
        materials.applyAconToonStyle()
        common.switchToRendredView()
        common.turnOnCameraView()

        return {'FINISHED'}


class Acon3dImportPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "ACON3D_PT_import"
    bl_label = "File Control"
    bl_category = "ACON3D"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(icon="FILE")

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.scale_y = 1.0
        row.operator("wm.open_mainfile")
        row.operator("acon3d.import_blend")


classes = (
    Acon3dImportPanel,
    ImportOperator,
)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    bpy.app.handlers.load_post.append(load_handler)


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)
    
    bpy.app.handlers.load_post.remove(load_handler)