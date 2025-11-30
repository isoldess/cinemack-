lugares_f1s1 = list(range(1,51))
lugares_f1s2 = list(range(1,51))
lugares_f2s1 = list(range(1,41))
lugares_f2s2 = list(range(1,41))
lugares_f3s1 = list(range(1,31))
lugares_f3s2 = list(range(1,31))
preco_s1 = [20,10,30]
preco_s2 = [15,7.5,22.5]
preco_s3 = [10,5,15]
vendas_f1s1 = []
vendas_f1s2 = []
vendas_f2s1 = []
vendas_f2s2 = []
vendas_f3s1 = []
vendas_f3s2 = []
estrelas_f1 = []
estrelas_f2 = []
estrelas_f3 = []
def filme(lugares,vendas):
    if lugares == [] :
        print("Não há assentos disponíveis")
        cine = menu()
    else:
        print(f"Assentos disponíveis:{len(lugares)}")
        tipo_ing = int(input("Escolha o tipo de ingresso(1-Inteira,2-Meia,3-VIP,4-Voltar):"))
        while tipo_ing < 1 and tipo_ing > 4 :
            tipo_ing = int(input("Escolha o tipo de ingresso(1-Inteira,2-Meia,3-VIP,4-Voltar):"))
        if tipo_ing == 1 :
            while True and lugares != [] :
                qnt_inteira = int(input(f"Assentos disponíveis:{len(lugares)}\n{lugares}\n Escolha seus assentos: "))
                vendas.append(1)
                lugares.remove(qnt_inteira)
                continuar = int(input(f"Deseja comprar mais um assento?(1-Sim,2-Não)\n{lugares}: "))
                if continuar == 2 :
                    cine = menu()
                    break
                if lugares == [] :
                    print("Não há como comprar mais assentos!")
                    cine = menu()
        elif tipo_ing == 2 :
            while True and lugares != []:
                qnt_meia = int(input(f"Assentos disponíveis:{len(lugares)}\n{lugares}\n Escolha seus assentos: "))
                vendas.append(2)
                lugares.remove(qnt_meia)
                continuar = int(input(f"Deseja comprar mais um assento?(1-Sim,2-Não)\n{lugares}: "))
                if continuar == 2 :
                    cine = menu()
                    break
                if lugares == []:
                    print("Não há como comprar mais assentos!")
                    cine = menu()
        elif tipo_ing == 3 :
            while True and lugares != []:
                qnt_vip = int(input(f"Assentos disponíveis:{len(lugares)}\n{lugares}\n Escolha seus assentos: "))
                vendas.append(3)
                lugares.remove(qnt_vip)
                continuar = int(input(f"Deseja comprar mais um assento?(1-Sim,2-Não)\n{lugares}: "))
                if continuar == 2 :
                    cine = menu()
                    break
                if lugares == []:
                    print("Não há como comprar mais assentos!")
                    cine = menu()
        else:
            cine = menu()
def avaliar():
    escolha = int(input("Qual filme deseja avaliar?\n1-Filme 1\n2-Filme 2\n3-Filme 3: "))
    while escolha <1 or escolha >3 :
        escolha = int(input("Qual filme deseja avaliar?\n1-Filme 1\n2-Filme 2\n3-Filme 3: "))
    if escolha == 1:
        est_f1 = int(input("Quantas estrelas deseja avaliar?(1 a 5): "))
        while est_f1 < 1 or est_f1 >5:
            est_f1 = int(input("Quantas estrelas deseja avaliar?(1 a 5): "))
        if est_f1 >= 1 and est_f1 <=5:
            estrelas_f1.append(est_f1)
            cine = menu()
    elif escolha == 2:
        est_f2 = int(input("Quantas estrelas deseja avaliar?(1 a 5): "))
        while est_f2 < 1 or est_f2 >5:
            est_f2 = int(input("Quantas estrelas deseja avaliar?(1 a 5): "))
        if est_f2 >= 1 and est_f2 <=5:
            estrelas_f2.append(est_f2)
            cine = menu()
    else:
        est_f3 = int(input("Quantas estrelas deseja avaliar?(1 a 5): "))
        while est_f3 < 1 or est_f3 >5:
            est_f3 = int(input("Quantas estrelas deseja avaliar?(1 a 5): "))
        if est_f3 >= 1 and est_f3 <=5:
            estrelas_f3.append(est_f3)
            cine = menu()
def sinopse():
    escolha = int(input("Qual filme deseja ver a sinopse?\n1-Filme 1\n2-Filme 2\n3-Filme 3: "))
    while escolha <1 or escolha >3 :
        escolha = int(input("Qual filme deseja ver a sinopse?\n1-Filme 1\n2-Filme 2\n3-Filme 3: "))
    if escolha == 1:
        print("O filme 1 é sobre os caçadores de demônios, liderados por Tanjiro e os Hashira, que são sugados para dentro do Castelo Infinito, a fortaleza de Muzan Kibutsuji. Lá, o Esquadrão de Caçadores de Demônios entra na luta final contra o principal vilão e suas forças demoníacas.")
        cine = menu()
    elif escolha == 2:
        print("O Filme 2 é um filme que compila os dois primeiros episódios da terceira temporada do anime, com cenas inéditas, servindo como introdução ao arco do Jogo do Abate (The Culling Game). A trama gira em torno do Incidente em Shibuya, onde um véu prende civis e o poderoso feiticeiro Satoru Gojo entra no confronto. Ao mesmo tempo, o plano de Kenjaku (no corpo de Noritoshi Kamo) transforma dez colônias do Japão em ninhos de maldições, e o feiticeiro Yuta Okkotsu é encarregado de executar Yuji por seus supostos crimes.")
        cine = menu()   
    else:
        print("O Filme 3 continua a história do anime, onde Denji, agora o Homem-Motosserra, se apaixona por Reze, uma garota misteriosa que ele conhece em um café. No entanto, essa paixão se revela perigosa quando ele descobre que ela é o Demônio Bomba, levando a uma batalha épica e arriscada entre eles. O filme explora temas de romance, caos e a dualidade de Denji, que precisa enfrentar seu novo amor enquanto se envolve em uma guerra de demônios e caçadores.")
        cine = menu()
def relatorio():
    print("Relatório Final")
    print(f"Filme 1 - Sessão 1:\nQuantidade de ingressos vendidos\n-Inteira:{vendas_f1s1.count(1)}\n-Meia:{vendas_f1s1.count(2)}\n-VIP:{vendas_f1s1.count(3)}\n")
    print(f"Receita por tipo(Sessão 1):\n-Inteira:R${vendas_f1s1.count(1) * preco_s1[0]:.2f}\n-Meia:R${vendas_f1s1.count(2) * preco_s1[1]:.2f}\n-VIP:R${vendas_f1s1.count(3) * preco_s1[2]:.2f}")
    print(f"Filme 1 - Sessão 2:\nQuantidade de ingressos vendidos\n-Inteira:{vendas_f1s2.count(1)}\n-Meia:{vendas_f1s2.count(2)}\n-VIP:{vendas_f1s2.count(3)}\n")
    print(f"Receita por tipo(Sessão 1):\n-Inteira:R${vendas_f1s2.count(1) * preco_s1[0]:.2f}\n-Meia:R${vendas_f1s2.count(2) * preco_s1[1]:.2f}\n-VIP:R${vendas_f1s2.count(3) * preco_s1[2]:.2f}")
    print(f"Filme 2 - Sessão 1:\nQuantidade de ingressos vendidos\n-Inteira:{vendas_f2s1.count(1)}\n-Meia:{vendas_f2s1.count(2)}\n-VIP:{vendas_f2s1.count(3)}\n")
    print(f"Receita por tipo(Sessão 1):\n-Inteira:R${vendas_f2s1.count(1) * preco_s2[0]:.2f}\n-Meia:R${vendas_f2s1.count(2) * preco_s2[1]:.2f}\n-VIP:R${vendas_f2s1.count(3) * preco_s2[2]:.2f}")
    print(f"Filme 2 - Sessão 2:\nQuantidade de ingressos vendidos\n-Inteira:{vendas_f2s2.count(1)}\n-Meia:{vendas_f2s2.count(2)}\n-VIP:{vendas_f2s2.count(3)}\n")
    print(f"Receita por tipo(Sessão 1):\n-Inteira:R${vendas_f2s2.count(1) * preco_s2[0]:.2f}\n-Meia:R${vendas_f2s2.count(2) * preco_s2[1]:.2f}\n-VIP:R${vendas_f2s2.count(3) * preco_s2[2]:.2f}")
    print(f"Filme 3 - Sessão 1:\nQuantidade de ingressos vendidos\n-Inteira:{vendas_f3s1.count(1)}\n-Meia:{vendas_f3s1.count(2)}\n-VIP:{vendas_f3s1.count(3)}\n")
    print(f"Receita por tipo(Sessão 1):\n-Inteira:R${vendas_f3s1.count(1) * preco_s3[0]:.2f}\n-Meia:R${vendas_f3s1.count(2) * preco_s3[1]:.2f}\n-VIP:R${vendas_f3s1.count(3) * preco_s3[2]:.2f}")
    print(f"Filme 3 - Sessão 2:\nQuantidade de ingressos vendidos\n-Inteira:{vendas_f3s2.count(1)}\n-Meia:{vendas_f3s2.count(2)}\n-VIP:{vendas_f3s2.count(3)}\n")
    print(f"Receita por tipo(Sessão 1):\n-Inteira:R${vendas_f3s2.count(1) * preco_s3[0]:.2f}\n-Meia:R${vendas_f3s2.count(2) * preco_s3[1]:.2f}\n-VIP:R${vendas_f3s2.count(3) * preco_s3[2]:.2f}")
    if len(estrelas_f1) > 0:
        media_es1 = sum(estrelas_f1) / len(estrelas_f1)
    else:
        media_es1 = "Não houve avaliações"
    if len(estrelas_f2) > 0:
        media_es2 = sum(estrelas_f2) / len(estrelas_f2)
    else:
        media_es2 = "Não houve avaliações"
    if len(estrelas_f3) > 0:
        media_es3 = sum(estrelas_f3) / len(estrelas_f3)
    else:
        media_es3 = "Não houve avaliações"
    print(f"Média das Avaliações:\nFilme 1:{media_es1}\nFilme 2:{media_es2}\nFilme 3:{media_es3}")
    print(f"Total de ingressos vendidos:{len(vendas_f1s1)+len(vendas_f1s2)+len(vendas_f2s1)+len(vendas_f2s2)+len(vendas_f3s1)+len(vendas_f3s2)}\nReceita total do dia:R${(vendas_f1s1.count(1) * preco_s1[0]) + (vendas_f1s1.count(2) * preco_s1[1])+(vendas_f1s1.count(3) * preco_s1[2])+(vendas_f1s2.count(1) * preco_s1[0]) + (vendas_f1s2.count(2) * preco_s1[1])+(vendas_f1s2.count(3) * preco_s1[2])+(vendas_f2s1.count(1) * preco_s2[0]) + (vendas_f2s1.count(2) * preco_s2[1])+(vendas_f2s1.count(3) * preco_s2[2])+(vendas_f2s2.count(1) * preco_s2[0]) + (vendas_f2s2.count(2) * preco_s2[1])+(vendas_f2s2.count(3) * preco_s2[2])+(vendas_f3s1.count(1) * preco_s3[0]) + (vendas_f3s1.count(2) * preco_s3[1])+(vendas_f3s1.count(3) * preco_s3[2])+(vendas_f3s2.count(1) * preco_s3[0]) + (vendas_f3s2.count(2) * preco_s3[1])+(vendas_f3s2.count(3) * preco_s3[2]):.2f}")
def menu():
    opcoes = int(input("|---------------------CINEMACK---------------------|\nDigite o número correspondente para acessar a opção:\n1.Comprar ingressos para Filme 1 - Sessão 1\n2.Comprar ingressos para Filme 1 - Sessão 2\n3.Comprar ingressos para Filme 2 - Sessão 1\n4.Comprar ingressos para Filme 2 - Sessão 2\n5.Comprar ingressos para Filme 3 - Sessão 1\n6.Comprar ingressos para Filme 3 - Sessão 2\n7.Avaliar um filme\n8.Sinopse dos filmes\n9.Encerrar o dia e exibir o relatório: "))
    while opcoes <1 and opcoes >9:
        opcoes = int(input("|---------------------CINEMACK---------------------|\nDigite o número correspondente para acessar a opção:\n1.Comprar ingressos para Filme 1 - Sessão 1\n2.Comprar ingressos para Filme 1 - Sessão 2\n3.Comprar ingressos para Filme 2 - Sessão 1\n4.Comprar ingressos para Filme 2 - Sessão 2\n5.Comprar ingressos para Filme 3 - Sessão 1\n6.Comprar ingressos para Filme 3 - Sessão 2\n7.Avaliar um filme\n8.Sinopse dos filmes\n9.Encerrar o dia e exibir o relatório: "))
    if opcoes == 1:
        filme1se1 = filme(lugares_f1s1,vendas_f1s1)
    elif opcoes == 2:
        filme1se2 = filme(lugares_f1s2,vendas_f1s2)
    elif opcoes == 3:
        filme2se1 = filme(lugares_f2s1,vendas_f2s1)
    elif opcoes == 4:
        filme2se2 = filme(lugares_f2s2,vendas_f2s2)
    elif opcoes == 5:
        filme3se1 = filme(lugares_f3s1,vendas_f3s1)
    elif opcoes == 6:
        filme3se2 = filme(lugares_f3s2,vendas_f3s2)
    elif opcoes == 7:
        avaliacoes = avaliar()
    elif opcoes == 8:
        sinopses = sinopse()
    else:
        encerrar = relatorio()
cine = menu()






    



    
