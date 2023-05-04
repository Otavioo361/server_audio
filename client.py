import Pyro4

uri = input("Entre com a URI do servidor: ")
text = input("Entre com o texto a ser convertido: ")

# Cria um objeto proxy para se comunicar com o servidor
text_to_speech = Pyro4.Proxy(uri)
audio_data = text_to_speech.convert_text_to_speech(
    text)  # Chama o método remoto
