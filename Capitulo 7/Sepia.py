import image

img = image.Image() #Añadir imagen
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(0,15)

def sepia():
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            nuevoRojo= ( (p.getRed()*.393) + (p.getGreen()*.769) + (p.getBlue()*.189) )
            nuevoVerde = ( (p.getRed()*.349) + (p.getGreen()*.686) + (p.getBlue()*.168) )
            nuevoAzul = ( (p.getRed()*.272) + (p.getGreen()*.534) + (p.getBlue()*.131) )

            newpixel = image.Pixel(nuevoRojo, nuevoVerde, nuevoAzul)
            img.setPixel(col, row, newpixel)
    
sepia()            
img.draw(win)
win.exitonclick()
