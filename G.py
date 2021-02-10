from PIL import Image               #Image Recognition

name2=input("Enter the file name without extension:\n")
name4=input("Enter current file's extension\n")
name3=input("Enter the extension in which you want your new file\n")

im = Image.open(name2+name4)        #Opening the image file that is to be converted

rgb_im = im.convert('RGB')          #Converting RGBA image into RGB type
rgb_im.save(name2+name3)            #Saving the new converted image

print("Your file has been converted successfully".center(400))
