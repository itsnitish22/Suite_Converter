from docx2pdf import convert        #Conversion of document to pdf module

name = input("Enter the name of file with extension:\n")

convert(name)
convert(name, r"D:\Project2", name)

# print("Your file has been converted successfully".center(400))
