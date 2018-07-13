from googletrans import Translator
translator = Translator()

def translate(text):
    print(translator.translate(text, dest='en').text)


print('Ingrese texto')
text = input()
translate(text)
