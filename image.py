from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8)) 
        for i in range(self.H):
            for k in range(self.W):
                if self.pixels[i][k] >= S:
                    im_bin.pixels[i][k] = 255
                else:
                    im_bin.pixels[i][k] = 0
    
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):

        lmin = self.W-1
        lmax = 0
        cmin = self.H-1
        cmax = 0
        
        im_loc = Image()
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c] == 0:
                    if l < lmin:
                        lmin = l
                    if l > lmax:
                        lmax = l
                    if c < cmin:
                        cmin = c
                    if c > cmax:
                        cmax = c
            im_recadree = Image()            
            im_loc.set_pixels(self.pixels[lmin:lmax+1,cmin:cmax+1])
            return im_recadree
        

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        newIm = Image()
        pixels_resized = resize(self.pixels, (new_H,new_W), 0)
        newIm.set_pixels(np.uint8(pixels_resized*255))
        return newIm
    
    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        simi = 0
        compte = 0
        for l in range (len(self.pixels)):
            for c in range (len(self.pixels[0])):
                compte += 1
                if self.pixels[l][c] == im.pixels[l][c]:
                    simi += 1
            return (simi/compte)


