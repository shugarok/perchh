def demander_coord_perch():
    perxy = []
    perx = int(input("Start x: "))
    pery = int(input("Start y: "))
    perxy.append(perx)
    perxy.append(pery)
    return perxy

def demander_coord_poly():
    qp=int(input("Nombre points polygone : "))
    points=[] 
    for _ in range(qp):
        x = input("x: ")
        y = input("y: ")
        points.append([int(x) , int(y)])
    return points

def distance(pt1 : list, pt2 : list):
     return (pt1[0] - pt2[0])**2  + (pt1[1] - pt2[1])**2

def calc_dist_min(perch : list, points : list[list]):
    dMin = distance(perch, points[0])
    for i in range(1, len(points)):
        newDist = distance(perch, points[i])
        if newDist < dMin:
            dMin = newDist
    pointsMin = []
    for i in range(0, len(points)):
        if distance(perch, points[i]) == dMin:
            pointsMin.append(points[i])
    return pointsMin

def new_coord(coordPerch : list, pointMin : list[list]):
    symx =  2*pointMin[0] - coordPerch[0] 
    symy =  2*pointMin[1] - coordPerch[1]  
    return [symx, symy]

def fin(pointsMin : list[list]):
    return len(pointsMin) > 1

def repeat_mvt(nbRepeat : int, coordPerch : list, coordPoly : list[list]):
    listePerch = [coordPerch]
    for i in range(nbRepeat):
        pointsMin = calc_dist_min(coordPerch, coordPoly)
        if fin(pointsMin):
            break
        if new_coord(coordPerch, pointsMin[0]) in listePerch:
            break
        else:
            coordPerch = new_coord(coordPerch, pointsMin[0])
            listePerch.append(coordPerch)
    return listePerch
