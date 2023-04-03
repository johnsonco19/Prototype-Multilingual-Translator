from translate import Translator
translator_german = Translator(to_lang="German")
translator_chinese = Translator(to_lang="zh")
translation1 = translator_german.translate("Good Morning!")
translation2 = translator_chinese.translate("Good Morning!")
print(translation1)
print(translation2)
