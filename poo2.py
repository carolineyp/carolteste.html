class Cliente :
    def __init__(self,nome,cpf,email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
    def exibir_dados (self):
        print(f"nome:{self.nome}")
        print(f"cpf:{self.cpf}")
        print(f"email:{self.email}")

    def alterarnome (self,novonome):
         self.nome = novonome

cliente = Cliente("Joao", 300009799, "joao@gmail.com")
print(cliente.nome)  
print(cliente.cpf)  
print(cliente.email)  
cliente.exibir_dados()  

cliente.alterarnome("carol")
cliente.exibir_dados()

                         



         
    
