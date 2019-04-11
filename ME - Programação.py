import pickle
import random
arq = open("sistemahospitalar.pck", "wb")
lista_paciente = []
lista_medico = []
mediconome = []
pacientenome = []
lista_consulta = []
pickle.dump(lista_medico,arq)
pickle.dumps(lista_medico)
arq.close()
arq = open('sistemahospitalar.pck', 'rb')
class Consulta:
    Id = 0
def exibirMenu():
    print("1 - Cadastro de Paciente ")
    print("2 - Cadastro do Medico ")
    print("3 - Marcar Consulta")
    print("4 - Listar Pacientes ")
    print("5 - Listar Medicos ")
    print("6 - Remover Médico ")
    print("7 - Listar Consultas ")
    print("8 - Remover Consulta ")
    print("9 - Folha de Pagamento(Médico)")
    print("10 - Sair")
    opcao = int(input("Ecolha uma opcao:"))
    return opcao

def cadastrodepaciente():
    nome = input("Nome Completo: ")
    nacionalidade = input("Nacionalidade: ")
    naturalidade = input("Naturalidade: ")
    datadenascimento = input("Data de Nascimento")
    # idade = calcular se a ano de nascimento - ano atual e if se ja passou da data de niver ou não
    profissao = input("Profissão")
    email = input("Email:")  # VERIFICAR SE É VALIDO
    telefone = input("Telefone:")
    rg = input("RG:")
    cpf = input("CPF:")
    endereço = input("Endereço:")
    numerocasa = input("Número:")
    bairro = input("Bairro:")
    cidade = input("cidade:")
    uf = input("UF:")
    cep = input("CEP:")
    planodesaude = input("Plano de Saúde")
    paciente = [nome, nacionalidade, naturalidade, datadenascimento, profissao, email, telefone, rg, cpf, endereço,
                numerocasa, bairro, cidade, uf, cep, planodesaude]
    pacientenome.append(nome)
    lista_paciente.append(paciente)

def cadastromedico():
    nome = input("Nome Completo: ")
    nacionalidade = input("Nacionalidade: ")
    naturalidade = input("Naturalidade: ")
    datadenascimento = input("Data de Nascimento")
    # idade = calcular se a ano de nascimento - ano atual e if se ja passou da data de niver ou não
    crm = input("CRM:")
    especialidade = input("Especialização:")
    email = input("Email:")  # VERIFICAR SE É VALIDO
    telefone = input("Telefone:")
    rg = input("RG:")
    cpf = input("CPF:")
    endereço = input("Endereço:")
    numerocasa = input("Número:")
    bairro = input("Bairro:")
    cidade = input("Cidade:")
    uf = input("UF:")
    cep = input("CEP:")
    planodesaude = input("Plano de Saúde")
    medico = [nome, nacionalidade,naturalidade,datadenascimento,crm,especialidade, email, telefone, rg, cpf,endereço,numerocasa,bairro,cidade,uf
              ,cep, planodesaude]
    mediconome.append(nome)
    lista_medico.append(medico)

def marcarconsulta():
    medico_consulta = input("Qual o nome do Medico?")
    if medico_consulta in mediconome:
        print("O dr.{} está disponivel para atendimento, por favor continue".format(medico_consulta))
        paciente_consulta = input("Nome do Paciente:")
        if paciente_consulta in pacientenome:
            print("Por favor {} escolha a data e hora da sua consulta".format(paciente_consulta))
            dia = input("Dia:")
            mes = input("Mês:")
            hora = input("Hora")
            print("\nConsulta Marcada. Obrigada")
        else:
            print("Paciente não encontrado, por favor realize o cadastro")
    else:
        print("Medico não encontrado, por favor verifique a lista e escolha outro")
    id_consulta = random.randint(1,100000)
    consulta = Consulta()
    Consulta.Id = Consulta.Id+1
    consulta.Id = Consulta.Id
    consulta = [consulta.Id, medico_consulta, paciente_consulta, dia, mes, hora]
    lista_consulta.append(consulta)
    return consulta



def excluirmedico():
    medicoexcluido = input("Nome do Medico que deseja excluir:")
    if medicoexcluido in mediconome:
        mediconome.remove(medicoexcluido)
        print("Medico Excluido com Sucesso")
    else:
        print("não foi possivel concluir a exclusão")


def excluirconsulta():
    print("\n consultas agendadadas", lista_consulta)
    idConsultaExcluida = int(input("Selecione o id da consulta que deseja excluir"))
    lista_consulta.pop(idConsultaExcluida-1)
    print("Consulta Excluida com Sucesso")

def folhadepagamento():
    valor = float(input("Salário:"))
    hrsextras = float(input("Encargos e horas extras:"))
    inss = (valor*(27.8/100))
    irrf = (8/100)*inss
    salario = valor + hrsextras + inss + irrf
    folha_de_pagamento = [valor, hrsextras, inss, irrf, salario]
    return folha_de_pagamento


while True:
    opcao = exibirMenu()
    if opcao == 10:
        break
    elif opcao == 1:
        cadastrodepaciente()
    elif opcao == 2:
        cadastromedico()
    elif opcao == 3:
        marcarconsulta()
    elif opcao == 4:
        print("\nLista de pacientes")
        print(pacientenome)
    elif opcao == 5:
        print("Lista de Médicos:")
        print(mediconome)
    elif opcao == 6:
        excluirmedico()
    elif opcao == 7:
        print(lista_consulta)
    elif opcao == 8:
        excluirconsulta()
    elif opcao == 9:
        print(folhadepagamento())