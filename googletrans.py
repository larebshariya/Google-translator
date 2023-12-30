from googletrans import Translator

#initialize the Translator
translator = Translator()

text = input("Enter your Text: ")

source_lan = "en"
translated_to= "te" #hi is the code for Hindi Language

#translate text
translated_text = translator.translate(text, src=source_lan, dest = translated_to)

print(f"The Actual Text was {text}")
print(f"The Translated Text is: {translated_text.text}")