from PIL import Image
class Img2ascii:
    chars=[' ', ',', '+', '1', 'n','D','&','M']
    def getchar(self,pi):
        for i in range(0,8):
            if pi< (i+1)*32:
                return self.__class__.chars[7-i]
    def __init__(self,src,resize=1.0):
        img = Image.open(src)
        if img.mode=='P' or img.mode =='RGBA':
             im=Image.new('RGB',img.size,'white')
             im.paste(img.convert('RGBA'),img.convert('RGBA'))
             img= im
        img= img.convert('L')
        w,h =img.size
        h/=2
        w=int(w*resize)
        h=int(h*resize)
        img=img.resize((w,h),Image.ANTIALIAS)
        #img.save('tmp.jpg')
        pixs = img.load()
        self.data=[]
        for i in range(0,h):
            line =''
            for j in range(0,w):
                line+=self.getchar(pixs[j,i])
            self.data.append(line)
