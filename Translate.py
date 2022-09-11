from google import Translator

def translate(matn):
    translator=Translator()
    # matn tilini aniqlaymiz
    til = translator.detect(matn).lang
    if til =='en':
        return translator.translate(matn,dest='uz').text
    else :
        return translator.translate(matn,dest='uz').text

