from googletrans import Translator
translator = Translator()

# detect lang-- can be used to figure out what lang was inputed
# returns ----> Detected(lang=ar, confidence=None)
print(translator.detect('مرحبًا')) 

# translate arabic to english
translated = translator.translate('مرحبًا', src='ar', dest='en')

print(translated.text)

