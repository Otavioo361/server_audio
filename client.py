import Pyro4
import time

uri = input("Entre com a URI do servidor: ")
username = input("Entre com o nome de usuário: ")
password = input("Entre com a senha: ")

tts = None
for i in range(3):
    try:
        tts = Pyro4.Proxy(uri)
        break
    except:
        print(f"Tentativa {i+1} de conexão falhou.")
        time.sleep(5)

if tts is None:
    print("Não foi possível conectar ao servidor.")
else:
    if tts.authenticate(username, password):
        while True:
            text = input(
                "Entre com o texto que deseja converter em áudio ou digite 'exit' para sair: ")
            if text == "exit":
                break
            if tts.convert_text_to_speech(username, text):
                print("Áudio gerado com sucesso!")
            else:
                print("Usuário não autenticado!")
    else:
        print("Falha na autenticação!")
