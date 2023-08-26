import pyttsx3 as pys
from PyPDF2 import PdfReader

engine = pys.init()
reader = PdfReader("./4000 Essential English Words  Book 1.pdf")

# set rate and female voice
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

text = "Wa fin Aba Wail, How Are you today, Raada mekayenashe Big data"

# getPage(n)
# text = reader.getPage(3).extract_text()
"""for i in range(start, end):
    text += reader.pages[i].extract_text()
"""
engine.say(text)
engine.runAndWait()