#encoding UTF-8
import image

def escalar(imagenpequena):
    oldw = imagenpequena.getWidth()
    oldh = imagenpequena.getHeight()

    imagengrande = image.EmptyImage(oldw * 2, oldh * 2)
    for row in range(oldh):
        for col in range(oldw):
            oldpixel = imagenpequena.getPixel(col, row)

            imagengrande.setPixel(2*col, 2*row, oldpixel)
            imagengrande.setPixel(2*col+1, 2*row, oldpixel)
            imagengrande.setPixel(2*col, 2*row+1, oldpixel)
            imagengrande.setPixel(2*col+1, 2*row+1, oldpixel)

    return (imagengrande)
img = image.Image() #Añadir imagen
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)

bigimg = escalar(img)
bigimg.draw(win)
