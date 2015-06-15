# -*- coding: utf-8 -*-
from img2ascii import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputpath",type =str ,help="Image file path")
parser.add_argument("-r",'--resize',type =float ,help="The zoom percentage for output,please use decimal")
args = parser.parse_args()
print args.inputpath
if not args.resize:
    args.resize=1.0
else:
    print args.resize
img = Img2ascii(args.inputpath,args.resize)
output = file(args.inputpath+'.txt','w')
for line in img.data:
    print >>output, line
output.close()
print 'Convert Done!'
