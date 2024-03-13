import PyPDF3
import pyttsx3 
path = open('Apostila SQL.pdf', 'rb') 
pdfReader = PyPDF3.PdfFileReader(path) 
from_page = pdfReader.getPage(24) 
text = from_page.extractText() 
speak = pyttsx3.init() 
speak.say(text) 
speak.runAndWait()