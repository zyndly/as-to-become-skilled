"""
pip install PyPDF2
pip install pyttsx3

"""
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages

for num in range(0, pages):
    page = reader.getPage(num)
    text = page.extractText()
    audio = pyttsx3.init()
    audio.say(text)
    audio.runAndWait()
