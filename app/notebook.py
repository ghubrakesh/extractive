from PIL import Image, ImageFont, ImageDraw
import pytesseract
import spacy
import re

nlp = spacy.load("en_core_web_sm")



def extract(text):

    doc = nlp(text)
    print(doc)
    emails = re.findall(r'\S+@\S+', text)
    phone_numbers = re.findall(r"\b[6-9]\s{0,1}\d\s{0,1}\d\s{0,1}\d\s{0,1}\d\s{0,1}\d\s{0,1}\d\s{0,1}\d\s{0,1}\d\s{0,1}\d\b", text)
    websites = re.findall(r'\s(?:https?://)?(?:www\.)?[a-zA-Z0-9-_.]+\.(?:com|in|dev|co\.in|com\.br|org|net|gov|edu|io|info)\s', text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return {
        "Emails": emails,
        "Phone_Numbers": phone_numbers,
        "website" : websites,
        "Named_Entities": entities
    }

def image_to_text(image):
    a = Image.open(image)
    text = pytesseract.image_to_string(a)
    # return {'text': text}
    return extract(text)