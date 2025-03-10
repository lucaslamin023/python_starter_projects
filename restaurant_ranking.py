restaurants = [
    ['O Mineiro', 4.2,  1.7], ['Amor aos pedaços', 4.3, 1.2], ['We Coffe', 4.5, 0.8], ['Lamen Kazu', 4.8, 0.7], ['Mr. Pretzels', 4.7, 1.1], ['Brigadeira', 4.7, 1.2]
]

# função para obter o restaurante com maior nota

def bestRating():
    res_best_rating = restaurants[0]
     # para cada restaurante na lista, verifica se a nota dele é maior que o armazenado na variavel restaurante_maior_nota
    for restaurant in restaurants:
        if restaurant[1] > res_best_rating[1]:
            res_best_rating = restaurant
                # em caso de empate na nota, verifica qual tem a menor distância
        elif restaurant[1] == res_best_rating[1]:
            if restaurant[2] < res_best_rating[2]: 
                res_best_rating = restaurant
    return res_best_rating # por fim, a função retorna o restaurante com a maior nota

# função para retornar um restaurante do ranking

def searchRestaurant(name):
    out = False
    # o loop busca o restaurante pelo nome e o remove da lista de restaurantes
    for restaurant in restaurants:
        if restaurant[0].upper() == name.upper():
            restaurants.remove(restaurant)
            out = restaurant
    return out

# função para editar um restaurante

def newRate():
    rate = float(input("Avaliação de 1 a 5 do restaurante: "))
    while (rate < 1) or (rate > 5): # validando se a nota está nos parâmetros
                rate = float(input("A avaliação deve estar entre 1 e 5! \nTente novamente: "))
    return rate
def newDistance():
    distance = float(input("Distância em km do restaurante: "))
    while (distance < 0): # validando se a distancia é maior que zero
                distance = float(input("A distância deve ser maior que zero! \nTente novamente: "))
    return distance

# Menu

option = 0

while option != 3:
    print("="*52)
    print("| Escolha uma das opções: \n| 1 - Adicionar/Excluir Restaurantes \n| 2 - Vizualizar Ranking \n| 3 - Sair ")
    option = input("- ")
    if option in "123": # verificando se a variável option recebeu um valor válido
        option = int(option)

    # Adicionar Restaurantes
    if option == 1:
        print("="*52)
        i = 1
        add_or_remove = False
        add_answer = 'S'
        remove_answer = 'S'
       
        while add_or_remove != "3":
            add_or_remove = input("| O que deseja fazer: | 1 - Adicionar | 2 - Excluir | 3 - Voltar\n- ")
            if add_or_remove == "1":
                while add_answer == 'S': # criando um loop para adicionar novos restaurantes a partir de inputs
                    name = input("Nome do {}° restaurante: ".format(i))
                    new_restaurant = [name, newRate(), newDistance()]
                    restaurants.append(new_restaurant)
                    add_answer = input("Deseja continuar a adicionar restaurantes? [S - Sim | N - Não]\n- ").upper()
                    i+=1
                    print("="*40)
            elif add_or_remove == "2":
                while remove_answer == 'S':
                    search = input("| Digite 'Limpar' para remover todos os restaurantes | Ou o nome do restaurante que deseja remover. \n- ").upper()
                    if search == "LIMPAR":
                        restaurants.clear()
                        answer = False
                    else:
                        removed_restaurant = searchRestaurant(search)
                        if removed_restaurant == False:
                            print("O restaurante não foi encotrado! Digite o nome do restaurante que deseja remover.")
                        else:
                            remove_answer = input("Deseja continuar a excluir restaurantes? [S - Sim | N - Não]\n- ").upper()

    # Vizualizar Ranking
    elif option == 2:
        ranking = []
        nRanking = 1
        
        while len(restaurants) != 0:
            restaurant = bestRating() #obtém o resturante com a maior nota
            # remove o restaurante da lista desordenada e o adiciona na lista de raking
            restaurants.remove(restaurant)
            ranking.append(restaurant)
            #repete esse processo, obtendo novamente o restaurante com a maior nota na lista desordenada e o colocando na lista de raking
        
        print("=-"*27)
        print("|Rank| Restaurante | Nota | Distãncia")
        for restaurant in ranking: # loop para exibir cada elemento da lista ordenada
            print("| {}° | {} - {}★ - {}km".format(nRanking, restaurant[0], restaurant[1], restaurant[2]))
            nRanking += 1
        print("=-"*27)
        restaurants = ranking # retornando os elementos para lista restaurantes, para o caso do usuário escolher adicionar ou vizualizar os restaurantes novamente

        edit = input("Deseja editar algum restaurante? [S - Sim | N - Não]\n- ").upper()
        print("-_"*27)

    # Editar Restaurantes
        
        while edit == 'S':
            element = 1
            search = input("Digite o nome do restaurante que deseja editar: ")
            edit_restaurant = searchRestaurant(search)
            element = input("O que deseja alterar no restaurante {}?\n[1 - Nota | 2 - Distância | 3 - Ambos] - ". format(edit_restaurant[0]))
            if edit_restaurant == False:
                print("O restaurante não foi encotrado! Digite o nome do restaurante que deseja editar.")
            else:
                if element == '1':
                    changed_restaurant = [edit_restaurant[0], newRate(), edit_restaurant[2]]
                elif element == '2':
                    changed_restaurant = [edit_restaurant[0], edit_restaurant[1], newDistance()]
                elif element == '3':
                    changed_restaurant = [edit_restaurant[0], newRate(), newDistance()]
                
                restaurants.append(changed_restaurant)

            print("="*54)
            edit = input("Deseja editar outro restaurante? [S - Sim | N - Não]\n- ").upper()
            print("="*54)

    # Aviso caso o usuário escolha uma opção inválida
    elif type(option) is str: 
        print("="*90)
        print("Por favor, digite 1 para escolher a primeira opção, 2 para a segunda ou 3 para terceira!")