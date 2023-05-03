meuvetor = [4, 15, 10]
print ('Valores acrescntados previamente meuvetor = [4, 15, 10]')
print ('O vetor 1 é ', meuvetor[0])
print ('O vetor 2 é', meuvetor[1])
print ('O vetor 3 é', meuvetor[2])
#obs: dentro da variavel temos 3 valores quando se esta [] significa que é um vetor
#para obter a informação X do vetor temos que ter em mente que ela se inicia por 0
#sesse caso possuo 3 vetores dentro da variavel meuvetor, que inicia de 0, 1, 2
meuv = range(1, 11)
print ('Usndo range para determinar quantidade de voteres na variavel meuv = range(10)')
print ('O vetor 1 é ', meuv[0])
print ('O vetor 2 é ', meuv[1])
print ('O vetor 3 é ', meuv[2])
print ('O vetor 4 é ', meuv[3])
print ('O vetor 5 é ', meuv[4])
print ('O vetor 6 é ', meuv[5])
print ('O vetor 7 é ', meuv[6])
print ('O vetor 8 é ', meuv[7])
print ('O vetor 9 é ', meuv[8])
print ('O vetor 10 é ', meuv[9])
#range(10) diz que minha variavel possui vetor com 10 possições
# Cria uma lista com 10 vetores vazios
meuvv = [[] for i in range(10)]

# Loop para pedir valores para cada vetor
for i in range(10):
  print(f"Digite os valores para o vetor {i+1}:")
  # Loop para detectar o valor do vetor
  for j in range(1):
      valor = input(f"Digite o valor{j+1} ou 'fim' para parar: ")
      # Caso o valor seja Fim
      if valor == 'fim':
          break
      # Caso o valor seja vazio
      elif valor == '':
        meuvv[i] == []

      else:
        meuvv[i].append(valor)
  else:
      continue
  break

for i, vetor in enumerate(meuvv):
  # Se existe valor no vetor
  if len(vetor) == 1:
    print(f"Vetor {i+1}: {vetor}")
  else:
    print(f"Nao ha valor no Vetor {i+1}")