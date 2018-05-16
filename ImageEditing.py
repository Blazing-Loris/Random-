from PIL import Image, ImageFilter

#PASTING TWO IMAGES

joker = Image.open("joker2.jpg")
paste = Image.open("paste.jpg")
area = (800,100,1150,450)
joker.paste(paste, area)

joker.show()
image = Image.open("joker3.jpg")

#MERGING TWO IMAGES

r1, g1, b1 = joker.split()
r2, g2, b2 = image.split()
newimg = Image.merge("RGB", (r1, g2, b1))
joker.show()
image.show()
newimg.show()
#Saves the file
newimg.save('newimg.jpg', format='JPEG', subsampling=0, quality=100)

#TRANSFORMATION IN IMAGES

joker = Image.open("joker.jpg")

square = joker.resize((1900,500))
flip = joker.transpose(Image.FLIP_LEFT_RIGHT)
rotate = joker.transpose(Image.ROTATE_90)

square.show()
flip.show()
rotate.show()

#MODES AND FILTERS

joker = Image.open("joker.jpg")

blur = joker.filter(ImageFilter.BLUR)

detail = joker.filter(ImageFilter.DETAIL)

edges = joker.filter(ImageFilter.FIND_EDGES)

detail.show()
edges.show()
#Saves the file
edges.save("JOKER_EDGES2.jpg", format ='JPEG', subsampling = 0, quality = 100)
blur.show()
joker.show()
