
import sys
import pickle
#ALL_JOGO = [0, 1]
infile = open('ALL_JOGO.txt', 'rb')
NEW_ALL_JOGO = pickle.load(infile)
ALL_JOGO = NEW_ALL_JOGO
#ALL_PLACAR = [0, 12]
infile2 = open('ALL_PLACAR.txt', 'rb')
NEW_ALL_PLACAR = pickle.load(infile2)
ALL_PLACAR = NEW_ALL_PLACAR
#MIN_TEMP = 0
infile3 = open('MIN_TEMP.txt', 'rb')
NEW_MIN_TEMP = pickle.load(infile3)
MIN_TEMP = NEW_MIN_TEMP
#MAX_TEMP = 0
infile4 = open('MAX_TEMP.txt', 'rb')
NEW_MAX_TEMP = pickle.load(infile4)
MAX_TEMP = NEW_MAX_TEMP
#CONT_MIN = 0
infile5 = open('CONT_MIN.txt', 'rb')
NEW_CONT_MIN = pickle.load(infile5)
CONT_MIN = NEW_CONT_MIN
#CONT_MAX = 0
infile6 = open('CONT_MAX.txt', 'rb')
NEW_CONT_MAX = pickle.load(infile6)
CONT_MAX = NEW_CONT_MAX

print( "LISTA PLACAR:", ALL_PLACAR )
print( "LISTA JOGO:", ALL_JOGO)

print("Olá Maria! Vamos checar suas estatisticas?")

JOGO = int(input("Digite abaixo em qual jogo da temporada esta (numero):"))
print("\n")
if JOGO in ALL_JOGO[:]:
    print("Este jogo já existe! Aqui esta as informações abaixo:")
    print("Jogo:", ALL_JOGO[JOGO])
    print("Placar:", ALL_PLACAR[JOGO])
    print("Maximo da temporada:", MAX_TEMP)
    print("Minimo da temporada:", MIN_TEMP)
    sys.exit()
else:
    ALL_JOGO.append(JOGO)
filename = 'ALL_JOGO.txt'
outfile = open(filename, 'wb')
pickle.dump(ALL_JOGO, outfile)
outfile.close()

PLACAR = int((input("Digite quantos pontos fez neste jogo:")))
ALL_PLACAR.insert(2, PLACAR)
i = min(ALL_PLACAR[1:])
if i in ALL_PLACAR[1:]:
    if i <= PLACAR: MIN_TEMP = i
    if MIN_TEMP != PLACAR and MIN_TEMP < PLACAR: CONT_MIN = CONT_MIN + 1
print(i)
x = max(ALL_PLACAR[1:])
if x in ALL_PLACAR[1:] >= ALL_PLACAR[1:]: MAX_TEMP = x

if MAX_TEMP != PLACAR and MAX_TEMP > PLACAR: CONT_MAX = CONT_MAX + 1
print(x)

filename2 = 'ALL_PLACAR.txt'
outfile2 = open(filename2,'wb')
pickle.dump(ALL_PLACAR,outfile2)
print("\n")


filename3 = 'MAX_TEMP.txt'
outfile3 = open(filename3,'wb')
pickle.dump(MAX_TEMP,outfile3)

filename4= 'MIN_TEMP.txt'
outfile4 = open(filename4,'wb')
pickle.dump(MIN_TEMP,outfile4)


filename5= 'CONT_MIN.txt'
outfile5 = open(filename5,'wb')
pickle.dump(CONT_MIN,outfile5)


filename6= 'CONT_MAX.txt'
outfile6 = open(filename6,'wb')
pickle.dump(CONT_MAX,outfile6)



Consulta = int((input ("Sistemas de consulta: Digite o jogo: ")))
print("\n")
if Consulta in ALL_JOGO[:]:
   print("Jogo:", ALL_JOGO[Consulta])
   print("Placar:", ALL_PLACAR[Consulta])
   print("Minimo da temporada:", MIN_TEMP)
   print("Maximo da temporada:", MAX_TEMP)
   print("Quebra de recorde minimo:", CONT_MIN)
   print("Quebra de recorde Maximo:", CONT_MAX)
else:
    print("Não existe este Jogo")
    sys.exit()



outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
print(ALL_PLACAR)
print(ALL_JOGO)


sys.exit()