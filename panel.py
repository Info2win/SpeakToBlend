import bpy

class _PT_Panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "SpeakToBlend"
    bl_category = "SpeakToBlend"
    
    def draw(self,context):
        """Defines how the UI will look like."""

        layout = self.layout
        #Create a field to input session_token
        layout.prop(context.scene.SpeakToBlend,"session_token")

        #Create Speak Button
        layout.operator("speak_to_blend",text="Speak")




    
