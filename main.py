print('calcule a media')
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
n4  = float(input("digite a quarta nota: "))
media = (n1 + n2 + n3 + n4)/4
print("a media das notas é: {:.2f}".format(media))









print('\n\n')

print("==========converta metros para centimetro============\n")

metros = float(input("digite a quantidade de metros para converter para em centimentros: \n").replace(',','.'))

cent = metros*100
a = cent
print("a quantidade de metros digitado em centimetros em :{:.2f} centimetros".format(a))