import bpy
from revChatGPT.ChatGPT import Chatbot
import speech_recognition as sr


speach = "make 2 cubes next to eachother"
chatBot = None
class _OT_SendCommandToChatGPT(bpy.types.Operator):
    """This class is the operator class that sends text prompt to Chatgpt"""
    bl_label = "SpeakToBlend"
    bl_idname = "operator.speak_to_blend"
    bl_description = "Speak to do almost anything in Blender"

    def execute(self,context):
        #Speach Recognition

        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        speach = r.recognize_google(audio)

        #Talk with chatGPT
        global chatBot
        session_token = bpy.context.scene.SpeakToBlend.session_token
        command = f'Generate Python code for Blender {bpy.app.version_string} with the following: {speach}. Output only the code without explanations'

        if not chatBot :
            chatBot = Chatbot({"session_token":session_token})
        try:
            solution = chatBot.ask(command)
        except:
            chatBot.refresh_session()
            solution = chatBot.ask(command)
        
        code = solution['message'].split('```')[1]


        #Put Code into a Data Block
        text_block = bpy.data.texts.new(bpy.context.scene.SpeakToBlend.session_token)
        text_block.write(code)

        #Run Script
        context = bpy.context.copy()
        context['edit_text'] = text_block
        bpy.ops.text.run_script(context)

        return {'FINISHED'} 
        