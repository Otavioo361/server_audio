import Pyro4
import os
import time
import tempfile
from gtts import gTTS
import threading


@Pyro4.expose
class Request:
    def __init__(self, username, text):
        self.username = username
        self.text = text

    def process(self):
        tts = gTTS(self.text, lang='pt-br')
        tts.save('audio.mp3')
        os.startfile('audio.mp3', 'play')
        # linux
        #os.system ('mpg321 audio.mp3')
        time.sleep(1)
        os.remove('audio.mp3')


@Pyro4.expose
class TextToSpeech:

    def __init__(self):
        self.authenticated_users = set()
        self.requests = []
        self.request_lock = threading.Lock()
        self.request_thread = threading.Thread(target=self.process_requests)
        self.request_thread.start()

    def authenticate(self, username, password):
        # verifica se o nome de usuário e a senha fornecidos correspondem a um usuário válido
        # retorna True se a autenticação for bem-sucedida, caso contrário, False
        if username == "otavio" and password == "otavio123":
            self.authenticated_users.add(username)
            return True
        else:
            return False

    def convert_text_to_speech(self, username, text):
        # verifica se o usuário está autenticado
        if username in self.authenticated_users:
            # cria um novo objeto Request com as informações do usuário e do texto
            request = Request(username, text)
            # adiciona o objeto Request à lista de solicitações
            with self.request_lock:
                self.requests.append(request)
            return True
        else:
            return False

    def process_requests(self):
        while True:
            # verifica se há solicitações pendentes
            with self.request_lock:
                if len(self.requests) == 0:
                    time.sleep(1)
                    continue
                # obtém a próxima solicitação na lista de solicitações
                request = self.requests[0]
                del self.requests[0]
            # processa a solicitação
            request.process()


daemon = Pyro4.Daemon()
tts = TextToSpeech()
uri = daemon.register(tts)
print(f"URI do servidor: {uri}")
daemon.requestLoop()
