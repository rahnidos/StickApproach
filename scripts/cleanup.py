__author__ = 'rahn niejasny'
import os, time, shutil, sys, argparse
parser=argparse.ArgumentParser(description='Cleaning personal files - the stick approach')
parser.add_argument('-p', action="store", dest="p", help="Path")
parser.add_argument('-d', action="store", dest="d", type=int, help="Days - files older than X days will be tagged to removal", default=30)
parser.add_argument('-t', action="store", dest="t", help="Tag string will be added at the beginning of file name", default="!!!")
args=parser.parse_args()
path=args.p
sign=args.t
dayz=args.d*86400

if os.path.isdir(path): pass
else: sys.exit("Path do not exist!")
now = time.time()

for obj in os.listdir(path):
    f=path+"\\"+obj
    if sign in obj[:3]:
#        print("Removing: "+f)
        if os.path.isdir(f): shutil.rmtree(f)
        else: os.remove(f)
        continue
    if os.path.getmtime(f) < now-dayz:
#        print("Tagging: "+f)
        newname=path+"\\"+sign+obj
        os.rename(f,newname)




