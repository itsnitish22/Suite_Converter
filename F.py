import fitz                         #PDF Manipulation

name=input("Enter name of the file with extension")
doc = fitz.open(name)       #Opening the Pdf file

for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("converted%s.png" % (i))       #saving the images
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("converted%s.png" % (i))      #saving the images
            pix1 = None
        pix = None

print("Your file has been converted successfully".center(400))