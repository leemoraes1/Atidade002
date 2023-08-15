#variaveis #
Peso=float (input ("qual o seu peso? "))
Altura=float (input ("qual a sua altura? "))
imc=0


#calculo imc#
imc = (Peso/Altura**2) 
print ("seu IMC é: {0}".format(imc))
#classificação# 
if imc < 16:
    print ("magreza")
elif (imc>=16 ) and (imc<17):
    print ("magreza moderada ")
elif(imc >=17) and (imc<=18.5):
    print("magreza leve")
elif(imc>=18.5) and (imc<25):
    print("saudável")
elif (imc>=25) and (imc<30):
    print ("sobrepeso")
elif(imc>=30) and (imc<35):
    print("obesidade grau 1")
elif(IMC>=35) and (imc <40):
    print ("obesidade grau 2")
else:
    print("obesidade grau 3(mórbida)")
