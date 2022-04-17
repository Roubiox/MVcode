from PIL import Image, ImageDraw
from math import *

def bin_word_list(messageInit):
    final_List = []
    for i in range(0,len(messageInit),7):
        sum = 0
        pond_sum = 0
        for j in range(7):
            if(i+j < len(messageInit)):
                char_bin = list(str(dec_to_bin(ord(messageInit[i+j]))))
                while(len(char_bin) < 8):
                    char_bin.insert(0,'0')
                final_List.append(char_bin)
                sum += ord(messageInit[i+j])
                pond_sum += ord(messageInit[i+j])*j+1
        str_sum = list(str(dec_to_bin(sum)))
        while(len(str_sum)<16):
            str_sum.insert(0,'0')
        str_sum1 = str_sum[:8]
        str_sum2 = str_sum[8:]
        final_List.append(str_sum1)
        final_List.append(str_sum2)
        str_Pond_sum = list(str(dec_to_bin(pond_sum)))
        while(len(str_Pond_sum)<16):
            str_Pond_sum.insert(0,'0')
        str_Pond_sum1 = str_Pond_sum[:8]
        str_Pond_sum2 = str_Pond_sum[8:]
        final_List.append(str_Pond_sum1)
        final_List.append(str_Pond_sum2)
    return final_List

def dec_to_bin(x):
    return int(bin(x)[2:])

def dessin(Listecaractere):
    draw = 0
    Qrcode = Image.new('RGBA', (width, height), WHITE)
    draw = ImageDraw.Draw(Qrcode)
    
    x= 70
    if logo :
        LogoImage = Image.open(LogoLink)
        LogoImage = LogoImage.resize((140,140))
        Qrcode.paste(LogoImage,(int(width/2-x),int(height/2-x)))
    
    j=-1
    i=0
    size = len(Listecaractere)
    for i in range(size):
        if i%nbCaractereLine == 0: 
            j+=1
        position = [(taille+(taille*(i%nbCaractereLine))/2) , taille+taille*j+(j*5)]
        if position[0]+taille2 >= width/2-x and position[0]-taille2 <= width/2+x and position[1]+taille2 >= height/2-x and position[1]-taille2 <= height/2+x and logo:
            pass
        else :
            triangle(draw,i,position,taille,Listecaractere[i])
    border(draw)
    Qrcode.show(draw)
    Qrcode.save("MVcode.png")

def triangle(draw,i,position,taille,binary):
    
    if i%2 == 0:
        #NORMALE
        #                       x1              Y1           |       x2                  y2            |      x3                  Y3
        #draw.polygon([(position[0]-taille2,position[1]+taille2),(position[0]+taille2,position[1]+taille2),(position[0],position[1]-(taille2*2)*0.36)], fill=COLOR[1], outline=COLOR[1])
        if   binary[0] == '0' and binary[1] == '0' : draw.polygon([(position[0]-taille2,position[1]+taille2),(position[0]+taille2,position[1]+taille2),(position[0],position[1]-(taille2*2)*0.36)], fill= CYAN , outline=BLACK)
        elif binary[0] == '0' and binary[1] == '1' : draw.polygon([(position[0]-taille2,position[1]+taille2),(position[0]+taille2,position[1]+taille2),(position[0],position[1]-(taille2*2)*0.36)], fill= YELLOW , outline=BLACK)
        elif binary[0] == '1' and binary[1] == '0' : draw.polygon([(position[0]-taille2,position[1]+taille2),(position[0]+taille2,position[1]+taille2),(position[0],position[1]-(taille2*2)*0.36)], fill= MAGENTA , outline=BLACK)
        elif binary[0] == '1' and binary[1] == '1' : draw.polygon([(position[0]-taille2,position[1]+taille2),(position[0]+taille2,position[1]+taille2),(position[0],position[1]-(taille2*2)*0.36)], fill= GREEN, outline=BLACK)
        
        #POINTS
        
        if binary[7] == '1': draw.ellipse((position[0]-taille8           ,position[1]-taille4       ,position[0]+taille8         ,position[1]        ),fill = BLACK)#en haut
        if binary[6] == '1': draw.ellipse((position[0]-taille4           ,position[1]               ,position[0]                 ,position[1]+taille4),fill = BLACK)#millieu gauche
        if binary[5] == '1': draw.ellipse((position[0]                   ,position[1]               ,position[0]+taille4         ,position[1]+taille4),fill = BLACK)#millieu droite
        if binary[4] == '1': draw.ellipse((position[0]-taille4-taille8   ,position[1]+taille4       ,position[0]-taille8         ,position[1]+taille2),fill = BLACK)#en bas a gauche
        if binary[3] == '1': draw.ellipse((position[0]-taille8           ,position[1]+taille4       ,position[0]+taille8         ,position[1]+taille2),fill = BLACK)#en bas a centre
        if binary[2] == '1': draw.ellipse((position[0]+taille8           ,position[1]+taille4       ,position[0]+taille4+taille8 ,position[1]+taille2),fill = BLACK)#en bas a droite   
    else:
        #REVERSE
        if   binary[0] == '0' and binary[1] == '0' :  draw.polygon([(position[0]+taille2,position[1]-taille2),(position[0]-taille2,position[1]-taille2),(position[0],position[1]+(taille2*2)*0.36)],fill= CYAN , outline=BLACK)
        elif binary[0] == '0' and binary[1] == '1' : draw.polygon([(position[0]+taille2,position[1]-taille2),(position[0]-taille2,position[1]-taille2),(position[0],position[1]+(taille2*2)*0.36)],fill= YELLOW , outline=BLACK)
        elif binary[0] == '1' and binary[1] == '0' : draw.polygon([(position[0]+taille2,position[1]-taille2),(position[0]-taille2,position[1]-taille2),(position[0],position[1]+(taille2*2)*0.36)],fill= MAGENTA , outline=BLACK)
        elif binary[0] == '1' and binary[1] == '1' : draw.polygon([(position[0]+taille2,position[1]-taille2),(position[0]-taille2,position[1]-taille2),(position[0],position[1]+(taille2*2)*0.36)],fill= GREEN, outline=BLACK)
        
        #POINTS
        if binary[7] == '1': draw.ellipse((position[0]-taille8           ,position[1]            ,position[0]+taille8        ,position[1]+taille4), fill= BLACK)  #en bas            = => en haut
        if binary[6] == '1': draw.ellipse((position[0]                   ,position[1]-taille4    ,position[0]+taille4        ,position[1]        ), fill= BLACK) #en milleu a droit  = => en milleu gauche
        if binary[5] == '1': draw.ellipse((position[0]-taille4           ,position[1]-taille4    ,position[0]                ,position[1]        ), fill= BLACK) #en milleu a gauche = => en milleu droit
        if binary[4] == '1': draw.ellipse((position[0]+taille8           ,position[1]-taille2    ,position[0]+taille4+taille8,position[1]-taille4), fill= BLACK) #en haut a droite   = => en bas gauche
        if binary[3] == '1': draw.ellipse((position[0]-taille8           ,position[1]-taille2    ,position[0]+taille8        ,position[1]-taille4), fill= BLACK) #en haut a millieu  = => en bas centre
        if binary[2] == '1': draw.ellipse((position[0]-taille4-taille8   ,position[1]-taille2    ,position[0]-taille8        ,position[1]-taille4), fill= BLACK) #en haut a gauche   = => en bas a droite

def InitTaille():
    global taille, nbCaractereLine , height,allCaractere
    
    
    #allCaractere = message + correction
    allCaractere =  nbcaractere + ceil(nbcaractere/7)*4
    for i in range(16) :
        taille = LISTETAILLE[i]
        nbCaractereLine = LISTENBCARACTTERELINE[i]
        if taille * allCaractere/nbCaractereLine + taille < height-taille:
            break

def border(draw):
    #Angles pour montrer le sens
    draw.polygon([(0,0)             ,(0,taille)             ,(taille2,taille)               ,(taille2,taille2)              ,(taille,taille2)               ,(taille,0)]            , fill= CYAN , outline=BLACK)       #en haut a gauche
    draw.polygon([(width,0)         ,(width-taille,0)       ,(width-taille,taille2)         ,(width-taille2,taille2)        ,(width-taille2,taille)         ,(width,taille)]        , fill= MAGENTA , outline=BLACK)    #en haut a droite
    draw.polygon([(width,height)    ,(width,height-taille)  ,(width-taille2,height-taille)  ,(width-taille2,height-taille2) ,(width-taille,height-taille2)  ,(width-taille,height)] , fill= YELLOW , outline=BLACK)     #en bas a droite
    draw.polygon([(0,height-taille) ,(taille2,height-taille),(taille2,height-taille2)       ,(taille,height-taille2)        ,(taille,height)                ,(0,height)]            , fill= GREEN , outline=BLACK)      #en bas a gauche
    
    #information a coder
    informationBin = []
    #----------------------------------------------
    tmp = list(str(dec_to_bin(version)))
    while len(tmp) != 3 : 
        tmp.insert(0,'0')
    informationBin.extend(tmp)
    #----------------------------------------------
    tmp = list(str(dec_to_bin(nbcaractere)))
    while len(tmp) != 10 : 
        tmp.insert(0,'0')
    informationBin.extend(tmp)
    #----------------------------------------------
    tmp = list(str(dec_to_bin(redondance)))
    while len(tmp) != 4 : 
        tmp.insert(0,'0')
    informationBin.extend(tmp)
    #----------------------------------------------
    tmp = list(str(dec_to_bin(taille)))
    while len(tmp) != 7 : 
        tmp.insert(0,'0')
    informationBin.extend(tmp)
    #----------------------------------------------
    informationBin.append('1') if logo else informationBin.append('0')
    #----------------------------------------------
    
    sizeWidth  = int((width  - 2* taille ) / taille2)
    informationBin = informationBin * int((4 * sizeWidth)/len(informationBin)) #redondance max
    #position des angles
    coter = [[(taille,0) , (taille+taille2,taille2)] , [(width-taille2,taille) , (width,taille+taille2)] , [(width-taille,height-taille2) , (width-taille-taille2,height)] , [(0,height-taille) , (taille2,height-taille-taille2)]]
    
    #Dessin des informations(cube)
    side = -1
    k= -1
    position = [(0,0),(0,0)]
    for i in range(len(informationBin)):
        if i%sizeWidth == 0:
            side += 1
            k = 0
        if side == 0:
            position = [(coter[side][0][0] + taille2 * k  ,coter[side][0][1])               ,(coter[side][1][0] + taille2 * k ,coter[side][1][1])]                  #haut
        elif side == 1:
            position = [(coter[side][0][0]                ,coter[side][0][1] + taille2 * k) ,(coter[side][1][0]               ,coter[side][1][1]+ taille2 * k)]     #droite
        elif side == 2:
            position = [(coter[side][0][0] - taille2 * k  ,coter[side][0][1])               ,(coter[side][1][0] - taille2 * k ,coter[side][1][1])]                  #bas
        else:
            position = [(coter[side][0][0]                ,coter[side][0][1] -  taille2 * k),(coter[side][1][0]               ,coter[side][1][1] -  taille2 * k)]   #gauche
        dessinCube(draw,position,informationBin[i])
        k += 1

def dessinCube(draw,position,caractere):
    if caractere == '1':
        draw.rectangle([position[0],position[1]], fill=BLACK, outline=BLACK, width=1)
    else:
        draw.rectangle([position[0],position[1]], fill=WHITE, outline=BLACK, width=1)

def Start():
    global redondance,logo,messageInit,nbcaractere,message
    
    while redondance == None:
        print("\n--------------------------------------------------------------------")
        print("| redondance       |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("--------------------------------------------------------------------")
        print("| nb Caractere max | 728 | 364 | 242 | 182 | 145 | 121 | 104 |  91 |")
        print("--------------------------------------------------------------------\n")
        tmp = input("Entrer la valeur de la redondance : ")
        if int(tmp) <= 0 or int(tmp) > 8 : print("Valeur pas bonne")
        else: redondance = int(tmp)
    
    while messageInit == None:
        print("Entrer votre message (limite = ",MAXLIST[redondance-1],"caractere ) : ")
        tmp = input()
        if len(tmp) <= 0  or len(tmp) > MAXLIST[redondance-1]: 
            print("Message incorecte , Votre message contien ",len(tmp)," Caractere")
        else:
            messageInit = tmp
    message = messageInit * redondance
    nbcaractere = len(message)
    
    while logo == None:
        tmp = input("Voulez Vous un logo ?(Yes/No) :").lower()
        if      tmp == 'no' : logo = False
        elif    tmp == 'yes': logo = True
        else:   print("Valeur pas bonne")


#Set UP des couleur en RGBA
CYAN    = (0,255,255,255)
MAGENTA = (255,0,255,255)
YELLOW  = (255,255,0,255)
GREEN   = (0,255,0,255)
BLACK   = (0,0,0,255)
WHITE   = (255,255,255,255)

#Set UP des Listes
MAXLIST               = [728,364,242,182,145,121,104,91]                        #Liste max caractere celon la redondance
LISTETAILLE           = [100,95,90,85,80,75,70,65,60,55,50,45,40,35,30,25]      #Liste de la taille d'un triangle
LISTENBCARACTTERELINE = [ 11,12,12,13,14,15,17,18,20,22,24,27,31,36,43,52]      #Liste du nombre de caractere max par ligne celon la taille


#Information a set up
version = 1                     #Version du QrCode
redondance = None               #Redondance du message
messageInit = None              #message
message = None                  #message x Redondance
nbcaractere = None              #nombre de caractere de la variable "message"
logo = None                     #Si il y a un logo
LogoLink = "img/logo.jpg"       #lien du Logo

#Taille de L'image
width = 700
height = 700

taille = 0                      #Taille d'un triangle            
nbCaractereLine = 0             
allCaractere = 0                #Totaliter des caractere a ecrire Read Solomon compris




Start()
InitTaille()

#Set UP taille pour faciliter la creation d'un triangle
taille2 = taille/2
taille4 = taille/4
taille8 = taille/8

Listecaractere = bin_word_list(message)     #integraliter des caractere a dessiner
dessin(Listecaractere)


print("\n------------------| Information |------------------")
print("\t|Version\t\t= ",version)
print("\t|nb Caractere\t\t= ",nbcaractere)
print("\t|Redondance\t\t= ",redondance)
print("\t|all caractere\t\t= ",allCaractere)
print("\t|Taille\t\t\t= ",taille)
print("\t|NbCaracter Ligne\t= ",nbCaractereLine)
print("\t|Logo\t\t\t= ",logo)
print("---------------------------------------------------\n")
