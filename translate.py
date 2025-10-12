from googletrans import Translator

t = Translator()
src = input('Текст для перевода: ')
print(t.translate(src, src='ru', dest='en').text)
