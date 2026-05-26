from PIL import Image, ImageDraw  


def imgDrawPoint(x : int, y : int, color : int, size : int, tImagePerchMov : int):
    global img
    cx = tImagePerchMov//2 + x*50
    cy = tImagePerchMov//2 - y*50

    for dx in range(-size, size+1):
        for dy in range(-size, size+1):
            img.putpixel((cx + dx, cy + dy), color)

def imgDrawLine(x0 : int, y0 : int, x1 : int, y1 : int, color : int, size : int, tImagePerchMov : int):  
    global img
    x0 = tImagePerchMov//2 + x0*50
    y0 = tImagePerchMov//2 - y0*50
    x1 = tImagePerchMov//2 + x1*50
    y1 = tImagePerchMov//2 - y1*50
    
    drawl = ImageDraw.Draw(img)
    drawl.line([(x0, y0), (x1, y1)], fill=color, width=size)


def mainZone(coordPerch : list, coordPoly : list[list], deplacements : list[list], tImagePerchMov : int):
    global img
    img = Image.new('RGB', (tImagePerchMov,tImagePerchMov), (255, 255, 255))

    for i in range(len(coordPoly)):
        imgDrawPoint(coordPoly[i][0], coordPoly[i][1], (0, 0, 0), 2, tImagePerchMov)

    for i in range(len(coordPoly) - 1):
        imgDrawLine(coordPoly[i][0], coordPoly[i][1], coordPoly[i+1][0], coordPoly[i+1][1], (0, 0, 0), 2, tImagePerchMov)
    if len(coordPoly) > 1:
        imgDrawLine(coordPoly[-1][0], coordPoly[-1][1],coordPoly[0][0], coordPoly[0][1],(0, 0, 0), 2, tImagePerchMov)


    for i in range(len(deplacements)):
        imgDrawPoint(deplacements[i][0], deplacements[i][1], (255, 0, 0), 2, tImagePerchMov)

    for i in range(len(deplacements) - 1): 
        imgDrawLine(deplacements[i][0], deplacements[i][1], deplacements[i+1][0], deplacements[i+1][1], (255, 0, 0), 1, tImagePerchMov)


    img.show()
