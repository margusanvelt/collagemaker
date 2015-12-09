#SIMPLE COLLAGE MAKER
#PLACES 4 PICTURES ON A CANVAS SELECTED BY THE USER


from PIL import Image
from resizeimage import resizeimage
import glob
import PIL


location = raw_input("Tell me the path to your files\n i.e. /home/user/folder/")

pildid = glob.glob(location + "*.JPG")
CANVAS_X=input("Tell me the width:")
try:
    CANVAS_Y=input("Tell me the height:")
except:
    CANVAS_Y = CANVAS_X * 2 / 3 

CORNERS = [(0,0),(CANVAS_X/2,0),(0,CANVAS_Y/2),(CANVAS_X/2,CANVAS_Y/2)]

def feeder():
    counter = 0
    while len(pildid)>=4:
        corners = CORNERS[:]
        print corners
        kanvas = Image.new('RGBA', (CANVAS_X, CANVAS_Y))
        
        # Siin teeme neli pilti mis l2hevad nelikusse
        for x in range(0,4):
            pilt = Image.open(pildid.pop(0))
            if pilt.height > pilt.width:
                pilt = pilt.rotate(90, expand = 1)
            #CHECK IF THE PICTURE PASSES THE SIZE REQUIREMENT, IF SO RUNS RESIZEIMAGE
            if pilt.size[0] >= CANVAS_X/2:
                pilt = resizeimage.resize_contain(pilt,[CANVAS_X/2, CANVAS_Y/2])
            #IF THE REQUIREMENT IS NOT MET, THE PICTURE WILL BE UPSCALED
            else:           
                if pilt.height == pilt.width or pilt.height/CANVAS_Y > pilt.width/CANVAS_Y:
                    baseheight = CANVAS_Y/2
                    wpercent = (baseheight/float(pilt.size[0]))
                    hsize = int((float(pilt.size[1])*float(wpercent)))
                    pilt = pilt.resize((baseheight,hsize), PIL.Image.ANTIALIAS) 
                else:
                    basewidth = CANVAS_X/2
                    wpercent = (basewidth/float(pilt.size[0]))
                    hsize = int((float(pilt.size[1])*float(wpercent)))
                    pilt = pilt.resize((basewidth,hsize), PIL.Image.ANTIALIAS)



            kanvas.paste(pilt, corners.pop(0))
        kanvas.save('/tmp/collab{0}.jpg'.format(counter))
        counter += 1
        print kanvas
feeder()    

"""basewidth = CANVAS_X/2
pilt = Image.open(pildid.pop(0))
wpercent = (basewidth/float(pilt.size[0]))
hsize = int((float(pilt.size[1])*float(wpercent)))
pilt = pilt.resize((basewidth,hsize), PIL.Image.ANTIALIAS)"""
