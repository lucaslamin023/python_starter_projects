inventory = []
answer = "S"
while answer == "S":
  equipament = [input("Equipamento: "), float(input("Valor: ")), int(input("Serial: ")), input("Departamento: ")]

resposta = input("Digite S para continuar: ").upper()

for element in inventory:
    print("Nome.........: ", element[0])
    print("Valor........: ", element[1])
    print("Serial.......: ", element[2])
    print("Departamento.: ", element[3])
    
while True:
    answ = input("Deseja buscar algum equimento? [S | N]\n").upper()
    if answ == "S":
        busca = input("Digite o nome do equipamento que deseja buscar: ")
        for element in inventory:
            if busca == element[0]:
                print("Valor..: ", element[1])
                print("Serial.:", element[2])
                break
    elif answ == "N":
        break
    else:
        print("Digite S para sim, ou N para não!")
    
answ = input("Deseja alterar o preço de algum equimento? [S | N]\n").upper()
while True:
    if answ in "S":
        while True:
            print("1) Aumentar | 2) Diminuir")
            editType = int(input("Escolha o tipo de alteração: "))
            if editType == 1 or editType == 2:
                break
            else:
                print("Escolha entre aumentar ou diminuir")
        edit = input("Insira o produto que deseja alterar: ")
        per = float(input("Insira o percentual da alteração: "))
        
        for element in inventory:
            if edit == element[0]:
                if editType == 1:
                    element[1] = (element[1] + (element[1] * per / 100))
                else:
                    element[1] = (per * element[1])/100
    elif answ not in "Nn":
        print("Responda com S ou N")
    else:
        break

values=[]
for elemento in inventory:
    values.append(elemento[1])
if len(values)>0:
    print("O equipamento mais caro custa: ", max(values))
    print("O equipamento mais barato custa: ", min(values))
    print("O total de equipamentos é de: ", sum(values))