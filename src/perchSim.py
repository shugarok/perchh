import brutzones
import mvtDrw
import outils



def main():
    coordPerch = outils.demander_coord_perch()
    coordPoly = outils.demander_coord_poly() 
    nbRepeat = 100000000    
    deplacements = outils.repeat_mvt(nbRepeat, coordPerch, coordPoly)
    print(deplacements)


    tImagePerchMov=        #int
    mvtDrw.mainZone(coordPerch, coordPoly, deplacements, tImagePerchMov)


    tImage=                 #int
    brutzones.mainbrutZone(coordPoly, tImage)

main()
