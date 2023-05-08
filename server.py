import Pyro4
import os
import tempfile
from gtts import gTTS


@Pyro4.expose
class TextToSpeech:

    def __init__(self):
        self.authenticated_users = set()

    def authenticate(self, username, password):
        # verifica se o nome de usuário e a senha fornecidos correspondem a um usuário válido
        # retorna True se a autenticação for bem-sucedida, caso contrário, False
        if username == "otavio" and password == "otavio123":
            self.authenticated_users.add(username)
            return True
        else:
            return False

    def convert_text_to_speech(self, username, text):
        temp_file = tempfile.NamedTemporaryFile(delete=False)

        # verifica se o usuário está autenticado
        if username in self.authenticated_users:
            # converte o texto em áudio usando a biblioteca gTTS

            tts = gTTS(text, lang='pt-br')
            tts.write_to_fp(temp_file)
            temp_file.close()
            os.startfile(temp_file.name, 'open', 'wmplayer.exe')
            # reproduz o áudio usando o player
            return True
        else:
            return False


daemon = Pyro4.Daemon()
tts = TextToSpeech()
uri = daemon.register(tts)
print(f"URI do servidor: {uri}")
daemon.requestLoop()
