import pygame
import base64
import io
import tempfile
"""
    ' soundpad ' ou leitor de audio Base64 , simplificado
    para uso geral.
    
"""
# criado por: DogeDaVala

# inicialização do pygame e pygame.mixer
pygame.init()
pygame.mixer.init()

# Áudios em base64 , substitua (coloque aqui sua string base 64) pela sua string de Base64
"""
    voçe pode aumentar o numero de audios colocando uma virgula no final
    da ultima string depois das aspas duplas , isso fara com que voçe 
    consiga criar uma nova string , copie o formato adicionando o 4 e
    por ai em diante.
    
    numero : determinão qual o audio
    
    aspas duplas : as tres aspas  duplas tem que 
    ser sempre colocadas e a string tem que ficar
    no meio delas.
    
"""
audios_base64 = {
    
    "1":"""coloque aqui sua string base 64""", # sua string de audio vai aqui
    
    "2":"""coloque aqui sua string base 64""",
    
    "3":"""coloque aqui sua string base 64"""
    
    }

# Função para ajustar o padding e decodificar 
# caso não intenda como funcione não mexa aqui!
def ajustar_padding(base64_string):
    base64_string = base64_string.strip().replace("\n", "").replace(" ", "")
    while len(base64_string) % 4 != 0:
        base64_string += "="
    return base64.b64decode(base64_string)

# Função para tocar o áudio usando pygame.mixer.music com arquivo temporário
def tocar_audio(encoded_audio):
    audio_data = ajustar_padding(encoded_audio)
    audio_stream = io.BytesIO(audio_data)
    
    # Criar um arquivo temporário para armazenar o áudio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:  # Usando .mp3
        temp_file.write(audio_data)
        temp_file_path = temp_file.name
    
    # Carregar o áudio com pygame.mixer.music
    try:
        pygame.mixer.music.load(temp_file_path)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.3) # aqui voçe seta o volume

      # aqui e um loop para fazer o audio tocar ate o fim 
        while True:
            if pygame.mixer.music.get_busy():
                action = input("Digite 'pause' para pausar ou 'unpause' para despausar: ").strip().lower()
                if action == 'pause':
                    pygame.mixer.music.pause()
                    print("Áudio pausado. Digite 'unpause' para retomar.")
                elif action == 'unpause':
                    pygame.mixer.music.unpause()
                    print("Áudio retomado.")
                elif action == 'stop':
                    pygame.mixer.music.stop()
                    print("Áudio parado.")
                    break
            else:
                break
    except pygame.error as e:
        print(f"Erro ao carregar ou tocar o áudio: {e}")


# Menu de seleção de áudio
    """
    
        para mudar o nome do audio que voçe 
        queira colocar na string e so substituir
        (nome_do_seu_audio) logo abaixo com o nome
        que voçe queira.
        
        aviso ! para cada string de audio adicionada acima
        recomendo adicionar outro print com o nome do audio
        e seu numero respectivo.
        
    """
def menu_audio():
    print('------------ selecione um audio --------------')
    print('1. nome_do_seu_audio')
    print('2. nome_do_seu_audio')
    print('3. nome_do_seu_audio')
    print('0. para sair')
    return input("Digite o número da opção desejada: ")

# Loop principal e finalização do programa
while True:
    escolha = menu_audio()
    if escolha == "0":
        print("Saindo do programa...")
        break
    elif escolha in audios_base64:
        tocar_audio(audios_base64[escolha])
    else:
        print("Opção inválida! Tente novamente.")

print("Programa encerrado.")
