layout='''+---+.TsZyFeLk.+---+
| @ |.uRaXgDmJ.| @ |
+---+.VqBwHcNi.+---+
......wPcViBoH......
NmJiFeXoDuJaPgYxSrGf
oLkHgDyNeTkZqFzWtQhE
......ZmFsLyRe+-+pId
+---+.aLgRmXsD|X|OjC
| @ |.BkHqNwTc+-+nKb
+---+.cJiPoVuBaVuMlA'''
item="#"*24
print(item)
print(repr(layout),end="@")
print(item)
print(item)
print(layout,end="@")
print(item)
#Clear repr Sisof
size=(repr.__call__.__sizeof__())
mask_rep=[1,0]*12
mask="101010010101101010010101"

w=20
h=10
space=" "
marker=[5,3]
markerAlign=[3,3]
BPass=8
EData=0
LenData=164
print(f"Content Legth: {len(layout)} \nContent Legth No Spaces : {len(layout.replace('\n',''))}")
data2x2=[]
for v,x in enumerate(layout.split("\n")):
    print(x)
    rec=[]
    for z,y in enumerate(x):
        #if((z > 5 and v > 4 and v < h-4)  and ( z < w-5 and v>4 ) and ((z < w-6 or z > w-3)  and (v < h-4 or v > h-1))  ):
        # print(y)
        print("Z:",z)
        print("V:",v)
        print("W:",w)
        print("H:",h)
        print(item) 
        if(  ( (z > 5 and z < w-6) or ((v > 3))) and (v<h-4 or z > 5 ) ):
            if( (v>h-2 or v<h-4 or z<w-6 or z>w-4 ) ):
                rec.append(y)
            else:
                if(rec!=[]):
                    data2x2.append("".join(rec))
                    rec = []

            # print(z)
            # print(y)
            # print(v)
            

            # rec.append(y)
    data2x2.append("".join(rec))

print(data2x2)
# msf=[5]*8+ [0]*(h-8)+[5,3,5,3,5,3,5]
msf=[5]*4+ [0]*(h-8)+[5,w-3,5,w-3,6,w-3,6]

print("Spaces : ",msf)
print(f"Longitud: {len(msf)}")
print(f"Altura: {h}")

    
# print("".join(data2x2))
#ORDENAR LA CADENA SEGUN EL ALGORITMO Y APLICAR LA MASCARA
rev = data2x2[::-1]
print(rev)
load = ""
for x in range(w):
    for p,s in enumerate(rev):
        print("Index P: ",s)
        print("Legth",len(s[x:]))
        print("Sumatoria",msf[::-1][p])
        print("Indice X",w-x)
        print("X",x)
        print("P",p)

        print("Sobra", (w-(-len(s[x:]) +len(s) +msf[::-1][p])))
        print("Final:", msf[::-1][p]+len(s[x:])-(w-(len(s)+msf[::-1][p])))
        # print("Logitud",(len(s[x:])+msf[::-1][p])  )
        print((len(s[x:])+msf[::-1][p]) % (w-x))
        if( len(s[x:])  )
        if( (msf[::-1][p] + len(s[x:]) )  % (w-x) == 0  ):
            m = msf[::-1][p]
            i = (len(s)+m ) - (w-x)
            print(i)
            if(i>=0 and i<len(s)):
                load+=s[::-1][i]
                print(s[::-1][i]) 
                print("Se agrego",i)
        else: 
            m = msf[::-1][p]
            i = (len(s)+m ) - (w-x-m)
            if(i>=0 and i<len(s) and (len(s)+m)>=(w-x) ):
                load+=s[::-1][i]
                print("Se agrego 2",i)

        print("#"*10)
    print(load)
    load+="|"
    print("#"*10)
    if(x==6):
        break
    # break
print(load)
