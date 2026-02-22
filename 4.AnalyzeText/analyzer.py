# KeyPhraseExtraction
# https://languageservicerargscf.cognitiveservices.azure.com/language/:analyze-text?api-version=2024-11-01
# Headers: Content-Type, Ocp-Apim-Subscription-Key
# Payload
# {
#   "kind": "KeyPhraseExtraction",
#   "parameters": {
#     "modelVersion": "latest"
#   },
#   "analysisInput": {
#     "documents": [
#       {
#         "id": "1233",
#         "language": "es",
#         "text": "La tecnología ha sido la fuerza impulsora detrás de muchas de ellas. La Inteligencia Artificial (IA) se ha erigido hoy como uno de los catalizadores más poderosos. No solo promete cambiar la forma en que trabajamos, sino construir un mundo laboral mejor, donde los empleados puedan centrarse en generar valor. Y donde las empresas decididas a abrazar esta tecnología podrán competir con independencia de sus recursos y tamaño."
#       }
#     ]
#   }
# }



# SentimentAnalysis
# https://languageservicerargscf.cognitiveservices.azure.com/language/:analyze-text?api-version=2024-11-01
# Headers: Content-Type, Ocp-Apim-Subscription-Key
# Payload
# {
#   "kind": "SentimentAnalysis",
#   "parameters": {
#     "modelVersion": "latest",
#     "opinionMining": "True"
#   },
#   "analysisInput": {
#     "documents": [
#       {
#         "id": "1",
#         "language": "es",
#         "text": "No basta con tener un plan de atención al cliente. Es necesario ejecutarlo eficazmente para obtener beneficios. Pero antes de analizar cómo se ve una ejecución eficaz, es importante comprender qué es un mal servicio al cliente."
#       }
#     ]
#   }
# }



# LanguageDetectionResults
# https://languageservicerargscf.cognitiveservices.azure.com/language/:analyze-text?api-version=2024-11-01
# Headers: Content-Type, Ocp-Apim-Subscription-Key
# Payload
# {
#   "kind": "LanguageDetection",
#   "parameters": {
#     "modelVersion": "latest"
#   },
#   "analysisInput": {
#     "documents": [
#       {
#         "id": "1",
#         "text": "No basta con tener un plan de atención al cliente. Es necesario ejecutarlo eficazmente para obtener beneficios. Pero antes de analizar cómo se ve una ejecución eficaz, es importante comprender qué es un mal servicio al cliente."
#       }
#     ]
#   }
# }



# Detectar y eliminar información confidencial, personas, telefono, correo, etc
# PiiEntityRecognition
# https://languageservicerargscf.cognitiveservices.azure.com/language/:analyze-text?api-version=2024-11-01
# Headers: Content-Type, Ocp-Apim-Subscription-Key
# Payload
# {
#   "kind": "PiiEntityRecognition",
#   "parameters": {
#     "modelVersion": "latest"
#   },
#   "analysisInput": {
#     "documents": [
#       {
#         "id": "1",
#         "language": "es",
#         "text": "No basta con tener un plan de atención al cliente. Es necesario ejecutarlo eficazmente para obtener beneficios. Pero antes de analizar cómo se ve una ejecución eficaz, es importante comprender qué es un mal servicio al cliente. Para mas informacion debes llamar al 0414-66162667 para comunicarte con la representante RozaMelTrozo Paradiso Bravo o a su correo rosa.padadise@gmail.com"
#       }
#     ]
#   }
# }

# https://microsoftlearning.github.io/mslearn-ai-language/

# Q/A pending because 
# https://language.cognitive.azure.com/questionAnswering/projects/LearnFAQ/manageSources
# Pendiente, entrenamiento no disponible
# https://learn.microsoft.com/en-us/answers/questions/1165457/adding-question-answering-url-sources-started-to-f