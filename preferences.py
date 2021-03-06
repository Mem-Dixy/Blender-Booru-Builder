# <pep8-80 compliant>


import bpy


def content():
    return bpy.context.preferences.addons[__package__].preferences


class BooruAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    root: bpy.props.StringProperty(
        name="Root Image Folder",
        description="Location of your image collection.",
        subtype='DIR_PATH'
    )

    filepath: bpy.props.StringProperty(
        name="Example File Path",
        description="Location of your image collection.",
        subtype='FILE_PATH',
    )

    number: bpy.props.IntProperty(
        name="Example Number",
        description="Location of your image collection.",
        default=4
    )

    change: bpy.props.IntProperty(
        name="Prove this worked",
        description="Location of you.",
        default=4
    )

    boolean: bpy.props.BoolProperty(
        name="Example Boolean",
        description="Location of your image collection.",
        default=False
    )

    blender_id_password: bpy.props.StringProperty(
        name='Password',
        default='',
        options={'HIDDEN', 'SKIP_SAVE'},
        subtype='PASSWORD'
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a preferences view for our add-on")
        layout.prop(self, "root")
        # unused
        layout.prop(self, "filepath")
        layout.prop(self, "change")
        layout.prop(self, "number")
        layout.prop(self, "boolean")


def register():
    bpy.utils.register_class(BooruAddonPreferences)


def unregister():
    bpy.utils.unregister_class(BooruAddonPreferences)
