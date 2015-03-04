__author__ = 'rahn niejasny'
import os, time, shutil
path = r"c:\users\franczak\TMP"
now = time.time()
sign="!!!"

for obj in os.listdir(path):
    f=path+"\\"+obj
    if sign in obj[:3]:
        print("Usuwam: "+f)
        shutil.rmtree(f)
    if os.path.getmtime(f) < now-2592000:
        print("Zamieniam: "+f)
        newname=path+"\\"+sign+obj
        os.rename(f,newname)



