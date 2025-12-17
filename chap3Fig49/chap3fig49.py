TAILLE=500
from math import *

#Comme son nom l'indique, découpes pour la figure 49 chapitre 3 page 37

# Taille du coté d'un carré élémentaire
cote=50
# Largeur du tour de la boite
ep=25
# valeur de l'arrondi des rectangles
rx=20
ry=20

decalx=0 # decalage du dessin pour tenir dans la feuille
decaly=0
#Dimensions de la boite.

u=cote/sqrt(5)
v=2*u
x=cote*sqrt(5)
grandCote=(v+u+2*x)
alpha=atan(1/2)
sinus=sin(alpha)
cosinus=cos(alpha)

# Entête du fichier SVG.
def debut(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    # Le nom du fichier SVG, 
    image=open("chapitre3Figure49.svg","w")
    image.write(entete)
    return image

# Fin du fichier SVG
def fin(image):
    pied="</svg>\n"
    image.write(pied)
    image.close()


def rectangle(largeur=100,hauteur=100,percent="",transform="",rx=5,ry=5,couleur="lime"):
    s="<rect x=\""+str(0+decalx)+"\" y=\""+str(0+decaly)+"\" width=\""+str(largeur)+"\" height=\""+str(hauteur)+"\" rx =\""+str(rx)+"\" ry=\""+str(ry)+"\" fill=\"none\" stroke=\""+couleur+"\" transform=\""+transform+"\"/>\n"
    return s

def ligne(debut,fin,transform="",couleur="blue"):
     s="<line x1=\""+str(debut[0]+decalx)+"\" y1=\""+str(debut[1]+decaly)+"\" x2=\""+str(fin[0]+decalx)+"\" y2=\""+str(fin[1]+decaly)+"\" stroke=\""+couleur+"\"   transform=\""+transform+"\" />\n"
     return s
    

def equilateral(c=TAILLE,transform=""):
    hauteur=c*sqrt(3)/2
    return "<polygon points=\"0 "+str(c)+" ,"+str(c/2)+" "+str(c-hauteur)+" , "+str(c)+" "+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+"/>\n"

def cercle(cx,cy,rayon,couleur="blue"):
    return "<circle cx=\""+str(cx+decalx)+"\" cy=\""+str(cy+decaly)+"\"  r=\""+str(rayon)+"\"  fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc1(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 0 "+str(cote)+" "+str(cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc2(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 1 "+str(cote)+" "+str(-cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc3(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 0 "+str(cote)+" "+str(-cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"

def arc4(depx,depy,couleur="blue"):   
    return "<path d=\" M "+str(depx+decalx)+" "+str(depy+decaly)+" \n a "+str(cote)+" "+str(cote)+" 0 0 1 "+str(cote)+" "+str(cote)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"



if __name__=="__main__":
  
   
    image=debut(c=TAILLE)
    #bord exterieur (bords arrondis)

    image.write(rectangle(largeur=grandCote+2*ep,hauteur=grandCote+2*ep,rx=rx,ry=ry))
   
    # rectangle interieur (bords droits)
    decalx+=ep
    decaly=ep
    image.write(rectangle(largeur=grandCote,hauteur=grandCote,rx=0,ry=0,couleur="blue"))
   

    # toutes les lignes
    # Ligne 'horizontale' du haut
    image.write(ligne((0,u),(v,0)))
    image.write(ligne((v,0),(v+u,v)))
    image.write(ligne((v+u,v),(v+x,0)))
    image.write(ligne((v+x,0),(v+x+u,v)))
    image.write(ligne((v+x+u,v),(v+2*x,0)))
    image.write(ligne((v+2*x,0),(v+u+2*x,v)))
    # Ligne 'verticale' de gauche
    image.write(ligne((0,u),(v*cosinus,x)))
    image.write(ligne((v*cosinus,x),(0,x+u)))
    image.write(ligne((0,x+u),(v*cosinus,2*x)))
    image.write(ligne((v*cosinus,2*x),(0,2*x+u)))
    image.write(ligne((0,2*x+u),(u,u+v+2*x)))
    # Ligne 'horizontale' du bas
    image.write(ligne((u,u+v+2*x),(x,u+v+2*x-2*cote*sinus)))
    image.write(ligne((x,u+v+2*x-2*cote*sinus),(x+u,u+v+2*x)))
    image.write(ligne((x+u,u+v+2*x),(u+x+2*cote*cosinus,u+v+2*x-2*cote*sinus)))
    image.write(ligne((u+x+2*cote*cosinus,u+v+2*x-2*cote*sinus),(2*x+u,u+v+2*x)))
    image.write(ligne((2*x+u,u+v+2*x),(u+v+2*x,2*x+v)))
    # Ligne verticale de droite
    image.write(ligne((u+v+2*x,2*x+v),(u+v+2*x-2*cote*sinus,v+x+cote*sinus)))
    image.write(ligne((u+v+2*x,2*x+v),(u+v+2*x-3*cote*sinus,2*x+v-3*cote*cosinus)))
    #image.write(ligne((u+v+2*x-2*cote*sinus,v+x+cote*sinus),(u+v+2*x,x+v)))
    image.write(ligne((u+v+2*x,2*x+v),(u+v+2*x-2*cote*sinus,v+x+cote*sinus)))
    image.write(ligne((u+v+2*x-2*cote*sinus,v+cote*sinus),(v+u+2*x,v)))
    # Deuxieme ligne verticale à partir de la gauche
    
    fin(image)

    #image.write(ligne((0*cote,0*cote),(0*cote,3*cote)))
    
    
