from abc import ABC, abstractmethod
import os 
os.system("cls||clear")

class Endereco:
     def __init__(self, logradouro : str, numero: str, complemento: str, cep: str, cidade: str) -> None:
          self.logradouro = logradouro
          self.numero = numero
          self.complemento = complemento
          self.cep = cep 
          self.cidade = cidade

class Funcionario (ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
            self.nome = nome 
            self.telefone = telefone 
            self.email = email
            self.endereco = endereco 

    def exibir_dados (self) -> str:
       return f"Nome: {self.nome} \nIdade: {self.idade} \nEmail: {self.email} \nEndereço: {self.endereco}"
    
    def calcular_salario (self) -> float:
            pass
class Engenheiro (Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea : str) -> None:
          self.crea = crea 
          
class Medico (Funcionario):     
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        self.crm = crm 




aluno1 = Aluno ("Marta",20, Endereço("Av.pajussara", 44))

print(aluno1.exibir_dados())