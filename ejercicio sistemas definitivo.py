ip=input("Introduzca la Ip")
posicion=ip.find('/') #Aquí pone la posición de la ip entre /
binario_ip= ""
binaro_ip2=""


if posicion>=0:  #Aquí comienza el de las ip
    ip1 = ip.split("/")
    ip2 = ip1[0].split(".")
    masc = ip1[1]
    if len(ip1) > 2:
        print("Solo se puede poner una '/' ")
else:
    ip2 = ip.split(".")
    masc = -1


if len(ip2)!=4:
    print("Error, la ip debe tener 4 dígitos.")
else:
    #https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str
    a=len(ip2[0])
    b=len(ip2[1])
    c=len(ip2[2])
    d=len(ip2[3])
    host= (2**32)-masc
    
    for numeros_ip in ip2:
        if not str.isnumeric(numeros_ip):
            #Aquí llega si hay un caracter de la ip que no es numérico
            print ( "Debes introducir caracteres númericos entre los puntos.")
    if(a<0 or a>255):
        print("Alguno de los valores no está entre 0 y 255.")
    else:
         #me da problema el binario y no se por qué.
        for i in ip2: 
        	ipbin=bin(int(i))
        	if len(ipbin)<0: 
        		dif=8 -len(ipbin)
        		diferencia=list(range(-1,int(dif+1),1))
        		for i in diferencia: 
        			ipbin+="0"
        	binario_ip+=ipbin[2:]



        
        if(a>0 and a<128):
            print("La dirección es de clase A")
            if (a==10 or a==172 or (a ==192 and b==168)):
            	print("La IP es Privada.")
            if(masc==8):
                print("La máscara de red en decimal es 255.0.0.0")
                print("La máscara de red en binario es ", binario_ip)
                print("Podemos poner ",host)
            elif(masc==16):
                print("La máscara de red en decimal es 255.255.0.0")
                print("La máscara de red en binario es ", binario_ip)
                print("Podemos poner ",host)
            elif(masc==24):
                print("La máscara de red en decimal es 255.255.255.0")
                print("La máscara de red en binario es ", binario_ip)
                print("Podemos poner ",host)
        elif(a>127 and a<192):
            print("La dirección es de clase B")

            print("La máscara de red es 255.255.0.0")
            print("La máscara de red en binario es ", binario_ip)
            print("Podemos poner ",host)
        elif(a>191 and a<224):
            print("La dirección es de clase C")
            print("La máscara de red es 255.255.255.0")
            print("La máscara de red en binario es ", binario_ip)
            print("Podemos poner ",host)
        elif(a>223 and a<240):
            print("La dirección es de clase D")
            print("La máscara de red es 255.255.255.0")
            print("La máscara de red en binario es ", binario_ip)
            print("Podemos poner ",host)
        elif(a>239 and a<256):
            print("La dirección es de clase E")
            print("La máscara de red es 255.255.255.0")
            print("La máscara de red en binario es ", binario_ip)
            print("Podemos poner ",host)
    if (ip2[0]==192) and (ip2[1]==168): 
        print("La Dirección IP es Privada.")
    else:
        print("La Dirección IP es Pública") #Aquí termina el de las ip