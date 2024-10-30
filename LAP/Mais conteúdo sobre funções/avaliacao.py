def maior ():
  x = int(input("Digite sua idade :"))
  if x < 18:
    print("Você é de menor")
    return x
  else:
    print("Você é de maior")
    return x


def par():
  par = int(input("Digite o número"))
  if par % 2 == 0:
     print(f"O número {par} é Par")
  else:
     print(f"O número {par} é Impar")

maior()

print("================= insira um número e verifique se ele é par ou não")
par()

print("================= insira 10 idades para verificar se você é de maior ou de menor")

for x in range (2):
 func = maior()
 print(func)
 if func > 18:
    if func %2 == 0:
      print("Sua idade é par")
    else:
      print("Sua idade é impar")