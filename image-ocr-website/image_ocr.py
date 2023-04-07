import pytesseract
from googletrans import Translator
import cv2 as cv


LANGUAGES={'afrikaans':'af','albanian':'sq',
'amharic':'am','arabic':'ar',
'armenian':'hy','azerbajani':'az',
'basque':'eu','belarusian':'be',
'bengali':'bn','bosnian':'bn','bulgarian':'bg',
'catalan':'ca','cebuano':'ceb',
'chichewa':'ny','chinese (simplified)':'zh-cn',
'chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr',
'czech':'cs','danish':'da','dutch':'nl','english':'en','esparanto':'eo',
'estonian':'et','filipino':'tl','finnish':'fi','french':'fr',
'frisian':'fy','galican':'gl',
'georgian':'ka','german':'de','greek':'el','gujurati':'gu',
'haitian creole':'ht','hausa':'ha',
'hawaiian':'haw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu',
'icelandic':'is','igbo':'ig',
'indonesian':'id','irish':'ga','italian':'it','japanese':'ja','jawanese':'jw',
'kannada':'kn','kazakh':'kk','khmer':'km',
'korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latvian':'lv',
'lithuanian':'lt','luxemborgish':'lb','macedonian':'mk','malagasy':'mg',
'malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr',
'mongolian':'mn','myanmar (burmese)':'my',
'nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa',
'polish':'pl','portugese':'pt','punjabi':'pa','romanian':'ro',
'russian':'ru','samoan':'sm','scots gaelic':'gd','sebian':'sr','sesotho':'st',
'sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl',
'somali':'so','spanish':'es','sundanese':'su','swahali':'sw','swedish':'sv',
'tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr',
'ukranian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','viatnamese':'vi',
'welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}

def extract_text(img):
    if img:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        text=pytesseract.image_to_string(img)
        if text=="":
            return "There is no text in the Image"
        else:
            return text

def translate_text(text,detected_lang,lang):
            translator=Translator(service_urls=['translate.googleapis.com'])
            translated_text=translator.translate(text,src=detected_lang,dest=lang)
            return translated_text
