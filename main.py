#calcular imc
def calcularIMC():
  peso = float(input('peso'))
  altura = float(input('altura'))
  imc = peso / (altura * altura)
  print(imc)
#calcular soma
def calcularsoma():
  a = float(input('numero'))
  b = float(input('numero'))
  soma = a + b
  print(soma)

calcularsoma()
calcularIMC()
