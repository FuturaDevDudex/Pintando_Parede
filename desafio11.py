nome = input('Qual o seu nome ? ') 
print('================================================================')

print(f'{nome}, antes de realizar a pintura, segue abaixo algumas orientações! \n 1°:. Isolar o ambiente protegendo o piso, portas e paredes. Para realizar está etapa é preciso de uma lona preta e uma fita crepe \n 2°:. Terá que realizar pre-paração da parede com uma licha de 80(licha de ferro). Situação utilizada caso a parede esteja no reboco \n 3°:.Para passar a massa corrida nas paredes, ira precisar de uma empenadeira e uma espatula. Ao utilizar a empenadeira deixe inclina um pouco para a parede \n Observação:. Após esperar a massa secar, terá que "consertar" passando a licha 80, para prossegeuir com a próxima etapa \n 4°:. O aconselhado é que utilize uma tinta o qual tenha um custo beneficio. Materiais adicional é um rolo e pincel de tinta ')

altura = float(input('Largura da parede: '))
largura = float(input('Altura da parede: '))

área = altura * largura
tinta = área / 2

print (f' Sua parede possui a dimesão de {altura}x{largura} e sua área é de {área}m2 \n Para pintar essa parede, você precisará de {tinta}L de tinta ')