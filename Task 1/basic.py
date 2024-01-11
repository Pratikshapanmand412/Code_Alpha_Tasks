from  PIL import Image # PIL -Image module
import pytesseract as tess # Processing Image
from gtts import gTTS # Google translate
import os # accessing file
tess.pytesseract.tesseract_cmd = r'C:\Users\pratiksha panmand\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def Image_to_sound(image):
    try:
        open_image = Image.open(image)
        text = tess.image_to_string(open_image)
        text_file = " ".join(text.split("\n"))
        print(text_file)
        speech = gTTS(text_file,lang="en",slow=False,tld="com.au")
        speech.save("sound.mp4")
        os.system("sound.mp4")
        return True
    
    except Exception as bug:
        print("The error while executing the code\n",bug)
        return

if __name__ == "__main__":
    Image_to_sound("img.jpeg")
    input() 


   



