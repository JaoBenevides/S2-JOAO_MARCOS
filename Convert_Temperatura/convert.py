print("Converta a temperatura de Celsius(1) para Fahrenheit(2) e vice-versa")

lot = int(input("Digite qual temperatura sera convertida: "))

def v(lot):
    if lot == 1:
      celsius = float(input("Digite a temperatura em Celsius: "))
      jao = (celsius*9/5)+32
      print (celsius,"=",jao,"Fahrenheit")
      

    else:
        lot == 2
        Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        jao2 = (Fahrenheit-32)*5/9
        print(Fahrenheit, "=", jao2, "Celsius")
        
    
v(lot)
