import math

def prime(init,finish):
    primes=[]
    for x in range(init,finish+1):
        a=[]
        for s in range(1,(x//2)+1):
            if(x%s==0):
                a.append(s)
        if(len(a)==1):
            primes.append(x)
    return primes

# HASH INICIAL PARA LA UBICACION DE LOS PRODUCTOS

COST_HASH_VALUE=[]

for x in prime(2,311):
    COST_HASH_VALUE.append(hex(int(math.modf(math.sqrt(x))[0]*(1<<32))))


print(len(COST_HASH_VALUE))



# CONSTANTES REDONDAS QUE SE UTILIZAN PARA GENERAR EL HASH REDONDO DE LA CLAVE DE 64 BITS
CONST_HASH_ROUND=[]

for x in prime(0,311):
    CONST_HASH_ROUND.append(hex(int(math.modf(x**(1./3.))[0]*(1<<32))))

print(CONST_HASH_ROUND)


#GENERNADO BUCLE PARA LA MUTACION DEL MENSAJE 

#EL MENSAJE:

msg=input("Inserte su mensaje:  ")

#ROTATE Function:

def rotateBytes(number,rotate):
    return number>>rotate|number<<(32-rotate)&0xFFFFFFFF   

# CONVERSION ME NSAJE BINARYO
BINARY=""
for x in msg:
    BINARY+=bin(ord(x))

print( "Binario de la cadena",BINARY.replace("b",""))
BINARY = BINARY.replace("b","")
LOG_BINARY=len(BINARY)
print("Logtidud del binaryo de la cadena",len(BINARY))    

complement=LOG_BINARY<<64-LOG_BINARY

print(complement)
