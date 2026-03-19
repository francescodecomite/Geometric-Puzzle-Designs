TAILLE=500
from math import *


# Largeur du tour de la boite
ep=50
# valeur de l'arrondi des rectangles
rx=20
ry=20

decalx=0 # decalage du dessin pour tenir dans la feuille
decaly=0

LARGEUR=480
HAUTEUR=310


# Entête du fichier SVG.
def debut(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    # Le nom du fichier SVG, 
    image=open("cruiser.svg","w")
    image.write(entete)
    return image

# Fin du fichier SVG
def fin(image):
    pied="</svg>\n"
    image.write(pied)
    image.close()

def cercle(cx,cy,rayon,couleur="blue"):
    return "<circle cx=\""+str(cx+decalx)+"\" cy=\""+str(cy+decaly)+"\"  r=\""+str(rayon)+"\"  fill=\"none\" stroke=\""+couleur+"\"/>\n"

def rectangle(largeur=100,hauteur=100,percent="",transform="",rx=5,ry=5,couleur="lime"):
    s="<rect x=\""+str(0+decalx)+"\" y=\""+str(0+decaly)+"\" width=\""+str(largeur)+"\" height=\""+str(hauteur)+"\" rx =\""+str(rx)+"\" ry=\""+str(ry)+"\" fill=\"none\" stroke=\""+couleur+"\" transform=\""+transform+"\"/>\n"
    return s

def ligne(debut,fin,transform="",couleur="blue"):
     s="<line x1=\""+str(debut[0]+decalx)+"\" y1=\""+str(debut[1]+decaly)+"\" x2=\""+str(fin[0]+decalx)+"\" y2=\""+str(fin[1]+decaly)+"\" stroke=\""+couleur+"\"   transform=\""+transform+"\" />\n"
     return s
 
if __name__=="__main__":
  
   
    image=debut(c=TAILLE)
    #bord exterieur (bords arrondis)

    image.write(rectangle(largeur=480+2*ep,hauteur=310+2*ep,rx=rx,ry=ry,couleur="green"))
   
    # rectangle interieur (bords droits)
    decalx+=ep
    decaly=ep
    image.write(rectangle(largeur=480,hauteur=310,rx=0,ry=0,couleur="blue"))
    A=155.14*sin(pi/6)
    B=310-A
    #P1=(271.118*sin(pi/6),310-271.118*cos(pi/6))
    P2=(480-271.118*cos(pi/6),271.118*sin(pi/6))
    image.write(cercle(P2[0],P2[1],5,couleur="red"))
    
    image.write(ligne((480,0),P2))
   
    u=200.982*cos(pi/3)
    v=155.14*cos(pi/6)
    w=200.982*sin(pi/3)
    image.write(ligne(P2,(480-v,310),couleur="red"))
    P1=(299.34*cos(pi/6),310-299.34*sin(pi/6))
    image.write(ligne((0,310),P1))
    P3=(480-299.34*cos(pi/6),299.34*sin(pi/6))
    image.write(cercle(P3[0],P3[1],5,couleur="red"))
    image.write(ligne((480,0),P3))
    
    fin(image)

    #image.write(ligne((0*cote,0*cote),(0*cote,3*cote)))
    
    
