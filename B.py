from pdf2docx import Converter      #Conversion of Pdf to Document

name=input("Enter name of your file with extension")
pdf_file =name

docx_file = r'converted.docx'       #declaring docx file name

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()      #closed the pdf file

print("Your file has been converted successfully".center(400))