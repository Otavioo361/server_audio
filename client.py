import Pyro4
uri = input("Entre com a URI do servidor: ")
username = input("Entre com o nome de usuário: ")
password = input("Entre com a senha: ")

tts = Pyro4.Proxy(uri)

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
