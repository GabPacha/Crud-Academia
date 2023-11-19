from conexao import *


#def inserirAluno(nome, matricula, cpf, endereco, email):
 #       meucursor.execute(
  #          '''INSERT INTO Alunos (Matricula_Alunos, Nome_Aluno, CPF_Aluno, Endereco, Email)
   #            VALUES (%s,%s, %s, %s, %s)''',
#        (nome, matricula, cpf, endereco, email)
def inserirAluno():
    nome = input("Digite o nome do aluno:")
    matricula = input("Digite a Matrícula do Aluno:")
    cpf = input("Digite o CPf do aluno:")
    telefone = input("Digite o telefone do aluno:")
    endereco = input("Digite o endereço do aluno:")
    email = input("Digite o e-mail do aluno")

    meucursor.execute(
        '''INSERT INTO alunos (nome,matricula, cpf, telefone, email , endereco) 
           VALUES (%s,%s, %s, %s, %s, %s)''',
        (nome, matricula, cpf, telefone, email, endereco)
    )
    banco.commit(),
    print("Aluno inserido com sucesso.")

def inserirModalidade():
    nome=input("Digite o nome da modalidade:")
    meucursor.execute(
        'INSERT INTO modalidades (nome) VALUES (%s)',
        (nome,)
    )
    banco.commit()
    print("Modalidade inserida com sucesso.")

def inserirFuncionario():
    nome=input("Digite o nome do funcionário:")
    cpf_funcionarios= input("Digite o cpf do funcionario:")
    departamento=input("Digite o departamento do funcionário:")
    salario=input("Digite o salário do funcionário:")
    quant_filhos=input("Digite a quantidade de filhos que o funcionário tem:")

    meucursor.execute(
        '''INSERT INTO func (nome,cpf_funcionarios,departamento,salario,quant_filhos)
        VALUES (%s,%s,%s,%s,%s)''',
        (nome,cpf_funcionarios,departamento,salario,quant_filhos)
    )
    banco.commit()
    print("Funcionário inserido com sucesso.")


def inserirPersonal():
    cpf=input("Digite o CPF do personal:")
    cref=input("Digite o CREF do personal:")
    nome=input('Digite o nome do personal:')
    telefone=input("Digite o telefone do personal:")
    email=input("Digite o email do personal:")
    meucursor.execute(
        '''INSERT INTO personal(cpf,cref,nome,telefone,email)
        VALUES (%s,%s,%s,%s,%s)''',
        (cpf,cref,nome,telefone,email)
    )
    banco.commit()
    print("Personal inserido com sucesso.")

def deletarAluno():
    cpf=input("Digite o CPF do aluno que deseja deletar:")
    meucursor.execute(
        "DELETE FROM alunos WHERE cpf = %s",
        (cpf,)
    )
    banco.commit()
    print("Aluno deletado com sucesso.")


def deletarModalidade():
    nome= input("Digite o nome da modalidade que deseja deletar:")
    meucursor.execute(
        "DELETE FROM modalidades WHERE nome= %s",
        (nome,)
    )
    banco.commit()
    print("Modalidade deletada com sucesso.")

def deletarFucionario():
    id_funcionarios=input("Digite a ID do funcionário que deseja deletar:")
    meucursor.execute(
        "DELETE FROM func WHERE id_funcionarios= %s",
        (id_funcionarios,)
    )
    banco.commit()
    print("Funcionário deletado com sucesso.")



def deletarPersonal():
    cref=input("Digite o CREF do personal que deseja deletar:")
    meucursor.execute(
        "DELETE FROM personal WHERE cref= %s",
        (cref,)
    )
    banco.commit()
    print("Personal deletado com sucesso.")


def lerTabelaAlunos():
    meucursor.execute(
        "SELECT * FROM alunos"
    )

    resultado=meucursor.fetchall()
    for x in resultado:
        print(x)


def lerTabelaModalidades():
    meucursor.execute(
        "SELECT * FROM modalidades"
    )
    resultado=meucursor.fetchall()
    for x in resultado:
        print(x)

def lerTabelaFuncionarios():
    meucursor.execute(
        "SELECT * FROM func"
    )
    resultado=meucursor.fetchall()
    for x in resultado:
        print(x)


def lerTabelaPersonal():
    meucursor.execute(
        "SELECT * FROM personal"
    )
    resultado=meucursor.fetchall()
    for x in resultado:
        print(x)



