import bpy

class STB_Properties(bpy.types.PropertyGroup):
    session_token: bpy.props.StringProperty(
        name = "Session token",
        description = "Session authentication token provided by ChatGPT"
    )
def register():
    bpy.types.Scene.SpeakToBlend = bpy.props.PointerProperty (type = STB_Properties)