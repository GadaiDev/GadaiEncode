import base64
import sys
import os
txt = []
out = ""
if len(sys.argv) == 1:
    print("NANKA")
elif len(sys.argv) > 2:
    if sys.argv[1] == "-w":
        filelist = sys.argv[3:]
        for i in filelist:
            fload = open(i,"r",encoding="utf-8").read()
            txt.append(i+"*"+base64.b64encode(fload.encode()).decode())
        txt = ":".join(txt)
        for j in txt:
            out+=chr(ord(j)*61)
        open(f"{sys.argv[2]}","wb").write(out.encode())
    if sys.argv[1] == "-r":
        if not os.path.isdir("Out"):
            os.mkdir("Out")
        txts = open(sys.argv[2],"rb").read().decode()
        
        intxt = ""
        
        for i in txts:
            intxt+= chr(int(ord(i)/61))
        
        for j in intxt.split(":"):
            x = j.split("*")
            if "/" in x[0]:
                y = x[0].split("/")
                if not os.path.isdir("Out/"+"/".join(y[0:len(y)-1])):
                    os.mkdir("Out/"+"/".join(y[0:len(y)-1]))
            open(f"Out/{x[0]}","w",encoding="utf-8").write(base64.b64decode(x[1]).decode())