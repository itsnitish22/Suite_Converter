from PIL import Image               #Image Recognition

n = input("Enter number of images to be compiled")
n = int(n)

im_list = []
pdf1_filename = r"converted.pdf"       #declaring the pdf file to be saved

name = input("Enter name of the file with extension:\n")     #Taking first image file
im1 = Image.open(name)

for i in range(n-1):
    name = input("Enter name of the file with extension:\n")     #Taking rest of the image files
    im_list.append(Image.open(name))

im1.save(pdf1_filename, "PDF", resolution=100.0,save_all=True, append_images=im_list)       #Saving the pdf file with all the images

print("Your file has been converted successfully".center(400))
