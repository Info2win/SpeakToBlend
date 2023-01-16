import bpy

class STB_PT_(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "SpeakToBlend"
    bl_category = "SpeakToBlend"
    
    def draw(self,context):
        """Defines how the UI will look like."""

        layout = self.layout
        row0 = layout.row()
        row1 = layout.row()
        row0_col0 = row0.column()
        row0_col0.operator()



    
