import Pyro4
import os
from gtts import gTTS


@Pyro4.expose
class TextToSpeech:

    def convert_text_to_speech(self, text):
        tts = gTTS(text, lang='pt-br')
        tts.save('audio.mp3')
        os.system("parole audio.mp3")
        return


daemon = Pyro4.Daemon()        # Cria um objeto daemon do Pyro4
# Registra a classe TextToSpeech como um objeto Pyro4
uri = daemon.register(TextToSpeech)

print(f"URI do servidor: {uri}")

daemon.requestLoop()   # Mantém o servidor rodando
