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

    return imagengrande

def suavizar(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = ( (p.getRed()*.393) + (p.getGreen()*.769) + (p.getBlue()*.189) )
            newgreen = ( (p.getRed()*.349) + (p.getGreen()*.686) + (p.getBlue()*.168) )
            newblue = ( (p.getRed()*.272) + (p.getGreen()*.534) + (p.getBlue()*.131) )

            newpixel = image.Pixel(newred, newgreen, newblue)

            img.setPixel(col, row, newpixel)
    
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)

bigimg = escalar(img)
bigimg.draw(win)

suave=suavizar(bigimg)
suave.draw(win)
