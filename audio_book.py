import pyttsx3
import PyPDF2
# from tkinter.filedialog import *




# import PyPDF2

# book = "80_20 Sales and Marketing. The Definitive Guide to Working Less and Making More.pdf"
# pdfReader = PyPDF2.PdfReader(book)

# # Rest of your code...




# # book = askopenfilename()
# # pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages

# for num in range(0, pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     player = pyttsx3.init()
#     player.say(text)
#     player.runAndWait()



# import pyttsx3
# import PyPDF2
# from tkinter.filedialog import askopenfilename

# # Select the PDF file using a file dialog
# book = askopenfilename()

# # Open the PDF file
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages

# # Initialize the pyttsx3 engine
# player = pyttsx3.init()

# # Loop through each page of the PDF
# for num in range(pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()

#     # Convert the extracted text to speech
#     player.say(text)
#     player.runAndWait()




from tkinter.filedialog import askopenfilename


book = askopenfilename()

pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.numPages

player = pyttsx3.init()

for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    player.say(text)
    player.runAndWait()
