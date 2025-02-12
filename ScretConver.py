import math
import os
a = int(input("Inserte Cuantos dijitos decea convertir a texto: "))
dict = {}
for x,y in enumerate(range(a)):
    a = int(input("Inserte el {0}º dijito".format(y)))
    key = a
    if(a<=25 and a>=0):
        key = chr(a+97)
    elif(a>=26 and a<= 51):
        key = chr(a+39)
    elif(a==52):
        key = "_"
    else:
        key = "None"

    dict[a] = key
    print("Number : {0} =>  Key: {1}".format(a,key)) 
    
