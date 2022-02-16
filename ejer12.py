class Cuenta:
    def __init__(self, saldo) :
        self.saldo= saldo
    
    def dinero_restante (self, retirada):
        return self.saldo- retirada
    
    def setsaldo (self, retirada):
        self.saldo= self.saldo - retirada
dinero= 100
retirar= 50
cuenta1=Cuenta(dinero)
if cuenta1.dinero_restante (retirar)<0:
    print("dinero insuficiente")
else: 
    cuenta1.setsaldo(retirar)
    print(cuenta1.saldo)