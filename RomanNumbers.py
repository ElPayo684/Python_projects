class Solution(object):
    def romanNumber(self, number):
        digit = 0
        cont = 0
        print(number)
        print("------------- Inicio del ciclo -------------------")
        # print(f"Valor inicial: {digit}")
        last_num = None # Lo correcto es inicializar last_num antes del bucle para que exista siempre
        for i in range(len(number)):
            actual_num = number[i]
            next_num = None # Lo correcto es inicializar next_num antes de la condicion para que exista siempre
            print(f"Numero actual = {actual_num}")
            if i+1 < len(number):
                next_num = number[i+1]
                print(f"Siguiente numero = {next_num}")
            if i > 0:
                last_num = number[i-1]
                print(f"Numero anterior = {last_num}")

            if actual_num == next_num:
                cont += 1
            else:
                cont = 0

            if cont > 2:
                print("error")
                return 0
            else: 
                if actual_num == "I":
                    if next_num == "V":
                        digit += 4
                        print("+4")
                    elif next_num == "X":
                        digit += 9
                        print("+9")
                    else:
                        digit += 1
                        print("+1")
                if actual_num == "V":
                    if last_num == "I":
                        digit
                        print("Salto")
                    else:
                        digit += 5
                        print("+5")
                if actual_num == "X":
                    if last_num == "I":
                        digit
                        print("Salto")
                    elif next_num == "L":
                        digit += 40
                        print("+40")
                    elif next_num == "C":
                        digit += 90
                        print("+90")
                    else:
                        digit += 10
                        print("+10")
                if actual_num == "L":
                    if last_num == "X":
                        digit
                        print("Salto")
                    else:
                        digit += 50
                if actual_num == "C":
                    if last_num == "X":
                        digit
                        print("Salto")
                    elif next_num == "D":
                        digit += 400
                        print("+400")
                    elif next_num == "M":
                        digit += 900
                        print("+900")
                    else:
                        digit += 100
                        print("+100")
                if actual_num == "D":
                    if last_num == "C":
                        digit
                        print("Salto")
                    else:
                        digit += 500
                        print("+500")
                if actual_num == "M":
                    if last_num == "C":
                        digit
                        print("Salto")
                    else:
                        digit += 1000
                        print("+1K")
            print(f"Valor: {digit}")
            print(f"Conntador: {cont}")
            print("--------------------------------------------")
        print("------------- Fin del ciclo -------------------")
        return digit
    

valid_numbers = ["I", "V", "X", "L", "C", "D", "M"]
sol = Solution()
number = "mc"

is_valid = all(ch.upper() in valid_numbers for ch in number)
if is_valid:
    result = sol.romanNumber(number.upper())
    if result == 0:
        print(f"El número {number} no es válido en el sistema romano.")
    else:
        print(f"El equivalente al numero romano \"{number.upper()}\" en sistema decimal es: {result}")
else:
    print(f"El número ingresado {number} no contiene caracteres válidos.")