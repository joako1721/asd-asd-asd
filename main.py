from colorama import init, Fore, Style
import random, time
ASDFAWSDFASDDFASDF = "HOLA AMIGO"
# .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
#| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#| |  ____  ____  | || |     ____     | || |   _____      | || |      __      | | | |      __      | || | ____    ____ | || |     _____    | || |    ______    | || |     ____     | |
#| | |_   ||   _| | || |   .'    `.   | || |  |_   _|     | || |     /  \     | | | |     /  \     | || ||_   \  /   _|| || |    |_   _|   | || |  .' ___  |   | || |   .'    `.   | |
#| |   | |__| |   | || |  /  .--.  \  | || |    | |       | || |    / /\ \    | | | |    / /\ \    | || |  |   \/   |  | || |      | |     | || | / .'   \_|   | || |  /  .--.  \  | |
#| |   |  __  |   | || |  | |    | |  | || |    | |   _   | || |   / ____ \   | | | |   / ____ \   | || |  | |\  /| |  | || |      | |     | || | | |    ____  | || |  | |    | |  | |
#| |  _| |  | |_  | || |  \  `--'  /  | || |   _| |__/ |  | || | _/ /    \ \_ | | | | _/ /    \ \_ | || | _| |_\/_| |_ | || |     _| |_    | || | \ `.___]  _| | || |  \  `--'  /  | |
#| | |____||____| | || |   `.____.'   | || |  |________|  | || ||____|  |____|| | | ||____|  |____|| || ||_____||_____|| || |    |_____|   | || |  `._____.'   | || |   `.____.'   | |
#| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
init()
print(Style.BRIGHT + Fore.RED + "HOLA :D")
aaa = [Fore.RED, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE]

global cont
cont = 0
cantidad_de_spam = 4
segundos_entre_jutsu = 0.5

primer_mensaje = "che elegi cantidad de jutsus XD: "
segundo_mensaje = "che elegi segundos entre jutsu XD (min 0.1 max 1.5): "
primer_input = "".join([random.choice(aaa) + c for c in primer_mensaje])
segundo_input = "".join([random.choice(aaa) + c for c in segundo_mensaje])

while True:
    primer_input = "".join([random.choice(aaa) + c for c in primer_mensaje])
    segundo_input = "".join([random.choice(aaa) + c for c in segundo_mensaje])
    try:
        print(primer_input, end='')
        cantidad_de_spam = int(input())
        print(segundo_input, end='')
        segundos_entre_jutsu = float(input())
        if(segundos_entre_jutsu < 0.1 or segundos_entre_jutsu > 1.5): raise
        break
    except:
        pass

def ASDFASDFdfqwef():
    global cont
    while(cont < cantidad_de_spam):
        print(random.choice(aaa) + "SELECCIONANDO COLOR" + "." * cont)
        cont += 1
        time.sleep(segundos_entre_jutsu)
    if(cont >= cantidad_de_spam):
        print("IMPRIMIENDO RESULTADO")
        cont = 0

def loasdASDFoASDFasdfASDFA(f):
    def wrapper():
        while 1:
            ASDFASDFdfqwef()
            f()
    return wrapper

@loasdASDFoASDFasdfASDFA
def HOLA():
    AAAAAAA = random.randint(0, 4)
    print("\n" + aaa[AAAAAAA] + ASDFAWSDFASDDFASDF + "\n")

#:3
HOLA()
