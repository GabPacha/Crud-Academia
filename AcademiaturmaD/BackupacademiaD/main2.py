from funcao import *
while True:
    tabelaselecionada=int(input("   MENU    \n"
                   " Informe a tabela que você quer mexer:\n"
                   
                   "1-Alunos:\n"
                   "2-Modalidades:\n"
                   "3-Funcionários:\n"
                   "4-Personal:\n"
                   "5-Para sair:\n"))
    print()
    if tabelaselecionada<0 or tabelaselecionada>5:
        print("Numero inválido, escolha novamente.")
    if tabelaselecionada== 5:
        break
    elif tabelaselecionada > 0 and tabelaselecionada < 5:

        while True:
            tabeladeacao=int(input("   MENU\n"
                           "Informe o que voce deseja fazer:\n"
                           ""
                           "1-Inserir:\n"
                           "2-Ler:\n"
                           "3-Deletar:\n"
                           "4-Voltar para o menu anterior:\n"))
            if tabeladeacao==4:
                break
            elif tabeladeacao<1 or tabeladeacao>4:
                break
            elif tabeladeacao==1:


                if tabelaselecionada==1:
                    inserirAluno()


                elif tabelaselecionada==2:
                    inserirModalidade()

                elif tabelaselecionada == 3:
                    inserirFuncionario()

                elif tabelaselecionada == 4:
                    inserirPersonal()


            elif tabeladeacao == 2:


                if tabelaselecionada == 1:
                    lerTabelaAlunos()

                elif tabelaselecionada==2:
                    lerTabelaModalidades()

                elif tabelaselecionada==3:
                    lerTabelaFuncionarios()

                elif tabelaselecionada==4:
                    lerTabelaPersonal()


            elif tabeladeacao == 3:


                if tabelaselecionada == 1:
                    deletarAluno()

                elif tabelaselecionada == 2:
                    deletarModalidade()

                elif tabelaselecionada == 3:
                    deletarFucionario()
                elif tabelaselecionada == 4:
                    deletarPersonal()






meucursor.close()
banco.close()