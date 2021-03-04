import matplotlib.pyplot as plt
import csv


while True:
    opcao = input('1 -> Criar arquivo\n 2 -> Ler arquivo\n 3 -> Exibir gráfico\n 4 -> Sair do Programa\n Escolha uma opção:' )

    if opcao == '1':
        z = int(input('Digite a quantidade de produtos: '))
        x = open('tabela.csv', 'w')
        try:
            writer = csv.writer(x)
            writer.writerow(('nomep', 'valor'))
            for c in range(0, z):
                nomep = input('escreva o nome do produto: ')
                valor = float(input('digite o valor desse produto: '))
                writer.writerow((nomep, valor))
        finally:
            x.close()

    elif opcao == '2':
        print('\n')
        try:
            print(open('Tabela.csv', 'r').read())
        except:
            print('Arquivo não encontrado!')

    elif opcao == '3':
        try:
            nomep = []
            valor = []
            y = open('tabela.csv', 'r')
            r = csv.DictReader(y)
            for z in r:
                nomep.append(z['nomeproduto'])
                valor.append(float(z['valor']))
            try:
                plt.figure(figsize=(6, 6))
                plt.plot(nomep, valor)
                plt.show()
                plt.bar(nomep, valor)
                plt.show()
                fig1, x1 = plt.subplots(figsize=(6, 6))
                x1.pie(valor, labels=nomep, autopct='%1.1f%%', shadow=True, startangle=90)
                x1.axis('equal')
                plt.show()
            finally:
                y.close()

        except:
            print('Arquivo não encontrado!')

    elif opcao == '4':
        break