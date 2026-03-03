import azure.cognitiveservices.speech as speechsdk

# Creando nuestro objeto cliente
speech_config = speechsdk.SpeechConfig(
    subscription="EhdTiEBE1tzPwey2wSdNgDDECHurrkaFWORNliZeA72RRsocACMQJQQJ99CCACYeBjFXJ3w3AAAYACOGKbIR",
    region="eastus"
)

# idioma reconocido (speech to text)
speech_config.speech_recognition_language = "es-BO"

# Definimos el archivo de audio para hacer la comnversión
audio_config = speechsdk.audio.AudioConfig(filename="audioTTS.wav")

# Objeto recognizer
recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Imprimir resultado
result = recognizer.recognize_once_async().get()
print(f"Resultado del reconocimiento: {result.text}")


