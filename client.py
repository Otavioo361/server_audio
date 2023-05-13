import Pyro4

# Substitua pelo IP do servidor
uri = "PYRO:server@{server_ip}:5050".format(server_ip="127.0.0.1")
server = Pyro4.Proxy(uri)
while True:
    if Pyro4.errors.CommunicationError:
        print("Erro: servidor fechado")
        break
    while True:
        
        
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
        token = server.authenticate(username, password)
        if token is not None:
            break
        else:
            print("Usuário ou senha incorretos")

    while True:
        message = input("Digite uma mensagem para enviar ao servidor,(exit) para finalizar: ")
        while message == "":
            message = input("Digite uma mensagem para enviar ao servidor,(exit) para finalizar: ")
        if message != "exit":           
            server.receive_messagem(message,token)            
        else:
            break
