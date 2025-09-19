#pass para sem atributos por enquant

class  Pessoa :
    pass
    nome = "João"
    idade = 20

pessoa1 = Pessoa()
print(pessoa1.nome)

pessoa1.nome = "maria"
print(pessoa1.nome)


pessoa1 = Pessoa()
print(pessoa1.idade)

pessoa1.idade = 30
print(pessoa1.idade)


#maneira def com os atributos

class  Pessoa2 :
    def  __init__ ( self , nome , idade ):
        self . nome = nome
        self . idade = idade

    def mudar_nome ( self , nome ):
        self . nome = nome
    def novel_idade ( self , idade ):
        self . idade = idade

    
    def pessoas ( self ):
        print (f"Nome: { self . nome } , Idade: { self . idade }" )

Pessoa2 = Pessoa2("Ana", 25)
Pessoa2.pessoas()
Pessoa2.mudar_nome("Carla")
Pessoa2.novel_idade(28)
Pessoa2.pessoas()


# pessoa deixa mensagem
class  Pessoa3 :
    def  falar ( self , mensagem ):
        print (f"{ self . nome } está falando: { mensagem }" )

pessoa3 = Pessoa3()
pessoa3.nome = "Carlos"
pessoa3.falar("Olá, tudo bem?")

#Construtor da Classe
class  Pessoa4 :
    def  __init__ ( self , nome , idade ):
        self . nome = nome
        self . idade = idade

pessoa = Pessoa4("João", 30)
print(pessoa.nome)
print(pessoa.idade)


#Herança de Classes
class Estudante(Pessoa4):
    def  __init__ ( self , nome , idade , matricula ):
        super() . __init__ ( nome , idade )
        self . matricula = matricula
    def  falar ( self , mensagem ):
        print (f"{ self . nome } está estudando: { mensagem }" )

estudante1 = Estudante("Joao", 30, "12345")
print(estudante1.nome)  
print(estudante1.idade)  
print(estudante1.matricula)  
estudante1.falar("Olá!")  


#Crie uma classe chamada ‘Pessoa’ com os atributos ‘nome’, ‘idade’ e ‘altura’.
# Com isso, peça ao usuário para digitar essas três informações salvando-as no objeto da classe. 
# Ao final mostre na tela os valores.
class Pessoa5:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

pessoa = Pessoa5(nome, idade, altura)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}m")

#Crie uma classe chamada ‘Produto’ com os atributos ‘nome’, ‘marca’, ‘peso’ e ‘quantia’.
# Com isso, peça ao usuário para digitar as informações de três produtos diferentes 
# e ao final mostre para cara produto os dados de seus atributos.

class Produto:
    def __init__(self, nome, marca, peso, quantia):
        self.nome = nome
        self.marca = marca
        self.peso = peso
        self.quantia = quantia

produto1 = Produto(input("Digite o nome do produto 1: "),
                    input("Digite a marca do produto 1: "), 
                   float(input("Digite o peso do produto 1 (em kg): ")),
                     int(input("Digite a quantia do produto 1: ")))
produto2 = Produto(input("Digite o nome do produto 2: "),
                    input("Digite a marca do produto 2: "),
                     float(input("Digite o peso do produto 2 (em kg): ")),
                        int(input("Digite a quantia do produto 2: ")))
produto3 = Produto(input("Digite o nome do produto 3: "),
                    input("Digite a marca do produto 3: "),
                        float(input("Digite o peso do produto 3 (em kg): ")),
                            int(input("Digite a quantia do produto 3: ")))

print(f"Produto 1 - Nome: {produto1.nome}, Marca: {produto1.marca}, Peso: {produto1.peso}kg, Quantia: {produto1.quantia}")
print(f"Produto 2 - Nome: {produto2.nome}, Marca: {produto2.marca}, Peso: {produto2.peso}kg, Quantia: {produto2.quantia}")
print(f"Produto 3 - Nome: {produto3.nome}, Marca: {produto3.marca}, Peso: {produto3.peso}kg, Quantia: {produto3.quantia}")

#Crie uma classe chamada ‘Calculadora’ com os métodos ‘soma’, ‘sub’, ‘multi’ e ‘div’. Cada método possui dois parâmetros de entrada do tipo decimal e retorna o resultado de sua operação. Realize o teste de todos os métodos.
class Calculadora:
    # Método de soma
    def soma(self, a: float, b: float) -> float:
        return a + b

    # Método de subtração
    def sub(self, a: float, b: float) -> float:
        return a - b

    # Método de multiplicação
    def multi(self, a: float, b: float) -> float:
        return a * b

    # Método de divisão
    def div(self, a: float, b: float) -> float:
        if b == 0:
            return "Erro: divisão por zero!"
        return a / b


# ---------------------------
# Testando a classe
# ---------------------------
calc = Calculadora()

print("Soma: ", calc.soma(10.5, 5.2))
print("Subtração: ", calc.sub(10.5, 5.2))
print("Multiplicação: ", calc.multi(10.5, 5.2))
print("Divisão: ", calc.div(10.5, 5.2))
print("Divisão por zero: ", calc.div(10.5, 0))

    
    # . Crie uma classe chamada ‘Media’ com os métodos ‘mediaSimples’ e ‘mediaPonderada’ (com pesos 3 e 4). Cada método possui dois parâmetros de entrada do tipo decimal e retorna o resultado de sua operação. Realize o teste de todos os métodos.
class Media:
    # Método de média simples
    def mediaSimples(self, a: float, b: float) -> float:
        return (a + b) / 2

    # Método de média ponderada (pesos 3 e 4)
    def mediaPonderada(self, a: float, b: float) -> float:
        return (a * 3 + b * 4) / (3 + 4)


# ---------------------------
# Testando a classe
# ---------------------------
m = Media()

print("Média Simples (7.0, 9.0): ", m.mediaSimples(7.0, 9.0))
print("Média Ponderada (7.0, 9.0): ", m.mediaPonderada(7.0, 9.0))

print("Média Simples (5.5, 8.5): ", m.mediaSimples(5.5, 8.5))
print("Média Ponderada (5.5, 8.5): ", m.mediaPonderada(5.5, 8.5))
