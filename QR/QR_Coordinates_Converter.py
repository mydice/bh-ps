from PIL import Image

# position detection pattern
def pattern0(coodinate = (0,0)):
    clist = []
    (x,y) = coodinate
    for i in range(x,x+7):
        clist.append((i,y))
        clist.append((i,y+6))
    for j in range(y+1,y+6):
        clist.append((x,j))
        clist.append((x+6,j))
    for i in range(x+2,x+5):
        for j in range(y+2,y+5):
            clist.append((i,j))
    return clist
    
# timing pattern
def pattern1(coodinate = (0,0),LL = 29):
    clist = []
    (x,y) = coodinate
    for i in range(x+8,x+LL-8,2):
        clist.append((i,y+6))
    for j in range(y+8,y+LL-8,2):
        clist.append((x+6,j))
    return clist

# Alignment pattern
def pattern2(coodinate = (0,0)):
    clist = []
    (x,y) = coodinate
    for i in range(x,x+5):
        clist.append((i,y))
        clist.append((i,y+4))
    for j in range(y+1,y+4):
        clist.append((x,j))
        clist.append((x+4,j))
    clist.append((x+2,y+2))
    return clist


def pixel_to_coordinate(plist, width = 100, op = (0,0), scaler = 1):
    clist = []
    (x0,y0) = op
    for p in plist:
        (i,j) = (p%width,int(p/width))
        C = (int((i-x0)/scaler),int((j-y0)/scaler))
        clist.append(C)
        
    clist = list(set(clist))
    clist.sort(key = lambda tup: tup[0])
    return clist

def coordinate_to_pixel(clist, w = 100, op = (0,0), scaler = 1):
    plist = []
    (x0,y0) = op
    for (x,y) in clist:
        plist = plist + [j*w+i 
                         for i in range(x0+x*scaler,x0+(x+1)*scaler)
                         for j in range(y0+y*scaler,y0+(y+1)*scaler)]
    return plist


def black_or_white(x):
    if x > 127:
        x = 255
    else:
        x = 0
    return x


def add_grid(img, rgb_pixels0=[0,255], scaler=17, op=[0,0], ib=1, 
            grey=128, white=255, black=0):
    
    w,h = img.size
    rgb_pixels = rgb_pixels0

    # hard-coded
    for i in range(34):
        for j in range(0,33*scaler):
            if rgb_pixels[op[1]*w+op[0]+i*w*scaler+j]==white:
                rgb_pixels[op[1]*w+op[0]+i*w*scaler+j] = grey
            
    for i in range(ib,37*scaler*w,w):
        for j in range(34):
            if rgb_pixels[i+j*scaler] == white:
                rgb_pixels[i+j*scaler] = grey

    mode = img.mode
    imn = Image.new(mode,(w,h))
    imn.putdata(data = rgb_pixels)
    imn.save('QR_AnswerSheet_Grid.jpeg','JPEG', quality=95)

    return "grids added"


def main():
    
    black = 0
    white = 255

    img = Image.open("QR_AnswerSheet.png")
    img = img.convert("L")
    w,h = img.size
    rgb_pixels0 = list(img.getdata())
    rgb_pixels0 = [black_or_white(x) for x in rgb_pixels0]

    # original point
    ib = rgb_pixels0.index(black,0)
    op = (ib%w,int(ib/w))
    # scaler
    scaler = 1
    while rgb_pixels0[ib+scaler*(w+1)]==black:
        scaler = scaler + 1

    #add_grid(img, rgb_pixels0, scaler, op, ib)

    #initialize, convert QR answersheet to coordinates
    #(0,0) on top left corner
    plist0 = [i for i in range(0,len(rgb_pixels0)) if rgb_pixels0[i]==black]
    clist0 = pixel_to_coordinate(plist0,w,op,scaler)
#    fo = open('QR_AnswerSheet.txt','w')
#    for CC in clist0:
#        fo.write(str(CC[0]+1) + ',' + str(33-CC[1]) + '\n')
#    fo.close()

    clist= clist0
    
    # read answer
    # bottom left is (1,1)
    fo = open('answer300.txt') 
    lines = fo.readlines()
    for line1 in lines:
        c=line1.split(',')
        if len(c)<2 or c[1]=='\n':
            CC = (int(c[0])//100, int(c[0])%100)
        else:
            CC = (int(c[0]), int(c[1]))
        CC = (CC[0]-1, 33-CC[1]) #hardcoded, map top left corner to bottom left corner
        clist.append(CC)
    fo.close()

    # Coordinates to image
    rgb_pixels = [white]*len(rgb_pixels0)
   
    plist = coordinate_to_pixel(clist,w,op,scaler)

    for p in plist:
        rgb_pixels[p] = black
    
    mode = img.mode
    imn = Image.new(mode,(w,h))
    imn.putdata(data = rgb_pixels)
    #imn.show()
    imn.save('QR_complete.png')
    

if __name__=="__main__":
    
    main()
    

