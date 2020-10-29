import pyttsx3
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('Profitable Candlestick Trading  (2002).pdf', 'rb'))
speaker = pyttsx3.init()
text=str()
for page_num in range(pdfReader.numPages):
    text=text+pdfReader.getPage(page_num).extractText()
    speaker.save_to_file(text, 'CandleStickTrading.mp3')
    speaker.runAndWait()
speaker.stop()
print(text)