import azure.cognitiveservices.speech as speechsdk

# Creando nuestro objeto cliente
speech_config = speechsdk.SpeechConfig(
    subscription="EhdTiEBE1tzPwey2wSdNgDDECHurrkaFWORNliZeA72RRsocACMQJQQJ99CCACYeBjFXJ3w3AAAYACOGKbIR",
    region="eastus"
)

# Voz sintetizada
speech_config.speech_synthesis_voice_name = "es-PA-MargaritaNeural"

# Formato de salida
audio_config = speechsdk.audio.AudioOutputConfig(filename="audioTTS.wav")

# Construir objeto que va a sintetizar esto
synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

result = synthesizer.speak_text_async("Hola ! esto es una demo de prueba de texto a voz").get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Audio generado correctamente !")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speechsdk.SpeechSynthesisCancellationDetails(result)
    print(f"Error al generar el audio: {cancellation_details.reason} - {cancellation_details.error_details}")
