# class Condicion:
#     contador = 0

#     def __init__(self, num1=0, num2=0):
#         self.numero1 = num1
#         self.numero2 = num2
#         # numero = num1 + num2
#         self.numero3 = num1
    
#     def usoIf(self):
#         if self.numero1 == self.numero2:
#             print("El numero1: {} es igual al numero2: {}.".format(self.numero1, self.numero2))
#         elif self.numero1 == self.numero3:
#             print("El numero1: {} es igual al numero3: {}.".format(self.numero1, self.numero3))
#         else:
#             print("Estos números no son iguales.")


# # cond1 = Condicion()
# # print(cond1.numero1)
# # print(cond1.numero2)

# cond2 = Condicion(50, 50)
# cond2.usoIf()
# print(cond2.numero1)


class Ciclos:
    def __init__(self, num1=5):
        self.numero = num1

    def usoWhile(self):
        carro = input("Ingrese una vocal: ")
        carro = carro.lower()
        while carro not in ("a", "e", "i", "o", "u"):
            carro = input("Vuelva a ingresar una vocal: ").lower()
        print('Felicidades, el caracter "{}" es una vocal...'.format(carro))


cicl1 = Ciclos()
cicl1.usoWhile()
