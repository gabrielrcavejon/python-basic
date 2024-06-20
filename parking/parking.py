def show_menu():
  """
  Author:
    Gabriel Cavejon

  Date:
    20/06/2024

  Função que mostra o menu

  """
  print()
  print("1 - Estacionar veículo")
  print("2 - Retirar veículo")
  print("3 - Veículos estacionados")
  print("4 - Está estacionado?")
  print("0 - Sair")
  print()
  return int(input("Escolha uma opção: "))

def park_vehicle(plate, mark, model, color, owner):
  """
  Author:
    Gabriel Cavejon

  Date:
    20/06/2024

  Função park_vehicle estaciona um veículo, que vem por parametro

  """
    
  cars[plate] = {
    "mark": mark,
    "model": model,
    "color": color,
    "owner": owner
  }

  print("Estacionado com sucesso!")
  print()

def remove_vehicle(plate):
  """
  Author:
    Gabriel Cavejon

  Date:
    20/06/2024

  Função remove_vehicle remove um veículo, que vem por parametro a placa

  """
  if plate in cars:
    del cars[plate]
    print(f"Veículo da placa {plate} removido com sucesso.")
  else:
      print(f"Veículo da placa {plate} não encontrado.")

  print()

def show_vehicles():
  """
  
  Author:
    Gabriel Cavejon

  Date:
    20/06/2024

  Função show_vehicles mostra todos os veículos estacionados no momento

  """
  print()
  print("Veículos estacionados:")
  print()

  for plate, info in cars.items():
    print(f"Placa: {plate}")
    print(f"Marca: {info['mark']}")
    print(f"Modelo: {info['model']}")
    print(f"Cor: {info['color']}")
    print(f"Proprietário: {info['owner']}")
    print()
    print("--------------------------------------")
    print()

def is_parked(plate):
  """
  
  Author:
    Gabriel Cavejon

  Date:
    20/06/2024

  Função is_parked recebe por parametro placa, e avisa se esta ou não estacionado, e se esta retorna os dados
  """
  print()

  if plate in cars:
      car = cars[plate]
      print(f"Placa: {plate}")
      print(f"Marca: {car['mark']}")
      print(f"Modelo: {car['model']}")
      print(f"Cor: {car['color']}")
      print(f"Proprietário: {car['owner']}")
  else:
      print("Veículo não localizado.")


################################################

cars = {}

park_vehicle("AAA1111", "MARK", "A1", "BLACK", "GABRIEL") # Veículo padrão

print("Bem-vindo ao sistema Parking.")
print()

while True:
  try:
    escolha = show_menu()
  
    match escolha: 
      case 0:
        print("Obrigado por usar o sistema.")
        break
      case 1:
        park_vehicle(
          input("Digite a placa do veículo: "), 
          input("Digite a marca do veículo: "),
          input("Digite o modelo do veículo: "),
          input("Digite a cor do veículo: "), 
          input("Digite o proprietário do veiculo: ") 
        )
      case 2:
        remove_vehicle(
          input("Digite a placa do veículo: ")
        )
      case 3:
        show_vehicles()
      case 4:
        is_parked(
          input("Digite a placa do veículo: ")
        )
  except ValueError:
    print()
    print("Digite um valor válido.")
