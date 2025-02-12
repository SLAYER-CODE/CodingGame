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

layout='''+---+ #  #  +---+
| @ |   ### | @ |
+---+    #  +---+
      ##         
##   #   ####    
#### #  #   #####
#   ## # ### ####
 # # ##   #   ## 
 ## ##### # #   #
      # ## +-+###
+---+   ###|X|## 
| @ | #### +-+# #
+---+ #   ## ##  '''


layout2='''+---+  ###    ### #  ## +---+
| @ | ### #  # #  # ##  | @ |
+---+ #  # ####    ## # +---+
       #  #   # #    #       
 # #    # #  #### ###  # #  #
  # #  #########     ## #    
   ##  #   ## ###  ### # ### 
 ### ## ## # ##  #  # #### # 
 ####   ## ######   #  ###   
# ##     ##     ### # # ### #
## # #### # ## ## ##   # #  #
 #  ##   #  # # #  #  #      
##### ##   ## # ## ## ##  #  
###     ### #  # #  # ##  #  
 ##    # ###  ## #   # ## #  
#  ##   #     # # ###   #### 
 # ## # # ## ###   ##  #     
 #### # #     #### #  #######
# ##  ##  #    ###### # # # #
 # # # #  # #  ##       # #  
# # #  #  ##  ### ## #  #####
      # #   ### ##  # #+-+# #
+---+    # #####      #|X|   
| @ | ##  #   #### ##  +-+###
+---+ ##    #### ###### #    '''
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

w=17
# w=20
h=13
# h=10
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
msf=[0]*5+[6]*4+ [0]*(h-8)+[6,w-3,6,w-3,6,w-3,6]

print("Spaces : ",msf)
print(f"Longitud: {len(msf)}")
print(f"Altura: {h}")
rev = data2x2[::-1]
print(rev)
mascara=""
load = ""
mask = ""
order = range(len(rev))[::-1]
unmask = ""
p=0
inject=1
for x in range(1,w+1)[::-1]:
    # if(x%2==1):
        # order = range(len(rev))[::-1]
    # else:
        # order = range(len(rev))
    m = ((x%2)+(p%2))%2
    order =  order[::-1]
    for p in order:
        s = rev[p]
        n = (p%2)
        # print(s)
        # print("X",x)
        # print("P",p)
        # print(f"Añadiendo caracter: {n} {p}")
        if (msf[::-1][p] + len(s)) >= x:
            index = x - msf[::-1][p] - 1  # Ajuste del índice
            if 0 <= index < len(s):  # Verifica si el índice es válido
                print(f"Añadiendo caracter: {s[index]} {inject} {inject%2}")
                # inject+=1
                load += s[index]  # Agrega el carácter correspondiente
                mask+=str(int(n))
                unmask+=str(int(int(bool(s[index].strip()) ^ (not int(m^n))  )))
            # else:
                # inject+=1
            if(index<=len(s)):
                inject+=1
        # inject+=1
    # if(inject==1):
        # inject+=0
    print("#"*10)
    # print(load)
    # load+="|"
    # print("#"*10)
# print("Select Data Qr Data")
# https://kick.com/capigg/clips/clip_01JC74V6KJ5PYX0J8F1ZQ8X7WW
# Decode Binry File System QR
decode="01001000 01100101 01101100 01101100 01101111 00100000 01000011 01101111 01100100 01101001 01101110 01000111 01100001 01101101 01100101 00100001"
# decode="01001000011001010110110001101100011011110010000001000011011011110110010001101001011011100100011101100001011011010110010100100001"
binari=""
binari2=""
print("Mascara:",mask)
print("Bites:",load)
print("Aplicate:",unmask)
for a,s in  enumerate(load):
    binari+=str(int(bool(s.split())) )
    binari2+=str(int(bool(s.split()) ^ a%2==0 ) )

# if(s == " "):
        # binari+="0"
    # else:
        # binari+="1"
print(binari)

def xor_bits(text, key):
    return ''.join(str(int(bit) ^ int(key[i % len(key)])) for i, bit in enumerate(text))

# print("Res:",not(int(binari[0])) )
decrypted_bits = ""
binari=unmask
bin = binari[8:]
if(not int(binari[0]) ):
    key = binari[1:8]    
    # print(key)
    print(len(bin))
    for i in range(0, len(bin), 7):
        block = bin[i:i+7]
        print(block)
        decrypted_block = xor_bits(block, key)
        decrypted_bits+=decrypted_block
    print("Texto descifrado en bits:\n", decrypted_bits)
print("Unmask:",len(unmask))
print("Mask:",len(mask))
print("Binari Len:",len(binari))
print("DecriptLen:",len(decrypted_bits))
# print("Original:",len( "".join(decode.split()) ))
print("Original",len("".join(map(lambda n:n[1:],decode.split()))))
print("Original Sin espacios:",len(decode))
# print(binari2)
print(unmask)

print("".join(map(lambda n:n[1:],decode.split())))
print("Binari",load[:127])
print("Binari",load[127:])
# print("".join(decode.split()))

print("B",binari)
print("M",mask)
print("D",unmask)
