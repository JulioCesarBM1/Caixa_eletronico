# Esse algoritmo realiza o saque de um caixa eletronico com uma variavel
print("Olá, Quanto você gostaria de sacar?")
saque = int(input())
if saque % 100 == 0:
    print("notas de 100: " + str(float(saque) / 100))
else:
    print("notas de 100: " + str(float(saque) / 100 - float(saque % 100) / 100))
    saque = saque - (float(saque) / 100 - float(saque % 100) / 100) * 100
    if saque % 50 == 0:
        print("notas de 50: " + str(float(saque) / 50))
    else:
        print("notas de 50: " + str(float(saque) / 50 - float(saque % 50) / 50))
        saque = saque - (float(saque) / 50 - float(saque % 50) / 50) * 50
        if saque % 20 == 0:
            print("notas de 20: " + str(float(saque) / 20))
        else:
            print("notas de 20: " + str(float(saque) / 20 - float(saque % 20) / 20))
            saque = saque - (float(saque) / 20 - float(saque % 20) / 20) * 20
            if saque % 10 == 0:
                print("notas de 10: " + str(float(saque) / 10))
            else:
                print("notas de 10: " + str(float(saque) / 10 - float(saque % 10) / 10))
                saque = saque - (float(saque) / 10 - float(saque % 10) / 10) * 10
                if saque % 5 == 0:
                    print("notas de 5: " + str(float(saque) / 5))
                else:
                    print("notas de 5: " + str(float(saque) / 5 - float(saque % 5) / 5))
                    saque = saque - (float(saque) / 5 - float(saque % 5) / 5) * 5
                    if saque % 2 == 0:
                        print("notas de 2: " + str(float(saque) / 2))
                    else:
                        print("notas de 2: " + str(float(saque) / 2 - float(saque % 2) / 2))
                        saque = saque - (float(saque) / 2 - float(saque % 2) / 2) * 2
                        if saque % 1 == 0:
                            print("notas de 1: " + str(float(saque) / 1))
                        else:
                            print("notas de 1: " + str(float(saque) / 1 - float(saque % 1) / 1))
                            saque = saque - (float(saque) / 1 - float(saque % 1) / 1) * 1
