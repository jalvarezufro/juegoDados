#funcion que convierte a base 'base' numeros enteros no negativos 'bumero' en
#sus respectivas bases 'vase'.
from Sistemasnumericosposicionales import *
#se cambio el nombre del archivo, en la Ln:7 se cambio la precondicion b<=9 por
#b<11, se agrego en la Ln:16; elif b==10: return True. Todo esto se hizo con      
#el objetivo de poder comprobar numeros decimales(base 10, siempre seran True)
#que no estan considerados en la Parte 1A.
def ConvertirAbase(base):
    again= "si"#se crea valor de verdad, 'si'
    while again=="si":#abre el ciclo, hasta romper el valor de verdad
        vase=input("base?")
        if vase==base:#primer filtro, comprueba que la base del numero ingresado sea diferente a la base a la cual se quiere transformar, ya que seria el mismo numero
            print "base incorrecta"
            if again=="no":#al responder 'no' en el valor de verdad, despues de una base incorrecta, termina la funcion
                return None
        else:#pasan el primer filtro
            bumero=input("numero?")
            fecimal=decimal(bumero,vase)#tranforma a decimal(base 10) el numero ingresado en su base
            if esNumero(bumero,vase)==False:#segundo filtro, compreuba que el numero ingresado este bien ingresado segun su base 
                print "numero incorrecto"
            else:#pasan el segundo filtro
                print "numero en base ",str(base)," = ", numero(fecimal,base)#transforma el decimal 'fecimal' a la base 'base'
        again=raw_input("otra conversión (si/no)?")#actualiza el valor de verdad 'si/no'                         

#se quito la Ln:6,'assert b>=2#precondicion', ya que da error con la funcion esNumero(x) y no entrega mensaje de error de base
def Mayor(mayor):
    vdv=True
    codi=input('n°?')
    lista=[]
    if codi==0:
            print "Fin de los datos"
            codi=1
            vdv=False
    while vdv:
        codigo=str(codi)
        numero=int(codigo[:-1])
        base=int(codigo[-1:])
        if base<2 and base>9:#la base nunca sera mayor a 9, ya que es solo el ultimo digito del 'codigo'
            print "base incorrecta"
            return Mayor(1)
        else:
            if esNumero(numero,base)==False:
                print "numero incorrecto"
                return Mayor(1)
                
            else:
                cecimal=decimal(numero,base)
                lista.append(cecimal)
                print 'decimal= ',cecimal
                return Mayor(1)
    if codi==1:
        return max(lista)
        

    

