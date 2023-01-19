import bpy
from revChatGPT.ChatGPT import Chatbot
import speech_recognition as sr
import tempfile

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

        # If code starts with 'python' statement, remove the statemnt
        if code.split('\n')[0] == 'python':
            code.replace('python\n','')

        # Create a temporary file to store the code
        with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as temp:
            temp.write(bytes(code, 'utf-8'))
            temp.flush()
            
        # Run the code as a Blender script
        bpy.ops.script.python_file_run(filepath=temp.name)
        

        return {'FINISHED'} 
        