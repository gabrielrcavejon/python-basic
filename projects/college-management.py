def show_menu():
  print()
  print("1 - Adicionar aluno")
  print("2 - Listar alunos")
  print("3 - Remover aluno")
  print("4 - Procurar aluno")
  print("5 - Listar aprovados")
  print("6 - Listar reprovados")
  print("7 - Procurar pelo nome do aluno")
  print("8 - Média da turma B1")
  print("9 - Média da turma B2")
  print("10 - Média da turma geral")
  print("11 - Diário da turma")
  print("0 - Sair")
  print()
  return int(input("Escolha uma opção: "))
    
def add_student():
  while True:
    ra = input("Digite o RA (Registro Acadêmico, 5 caracteres): ")
    if not len(ra) == 5:
      print("RA inválido. Deve ter 5 caracteres.")
    else:
      if ra in students:
        print("RA já existente, digite outro RA.")
      else:
        break

  while True:
    name = input("Digite o Nome (27 caracteres): ")
    if (len(name) > 27):
      print("Nome inválido. No máximo 27 caracteres.")
    else:
      break
  
  while True:
    note_B1 = input("Digite a Nota da B1 (0 a 10): ")
    try:
      note_B1 = float(note_B1)
      if note_B1 >= 0 and note_B1 <= 10:
        break
      else:
        print("Nota inválida. Valor tem que estar entre 0 e 10.")
    except ValueError:
      print("Nota inválida. Valor tem que estar entre 0 e 10.")
          
  while True:
    note_B2 = input("Digite a Nota da B2 (0 a 10): ")
    try:
      note_B2 = float(note_B2)
      if note_B2 >= 0 and note_B2 <= 10:
        break
      else:
        print("Nota inválida. Valor tem que estar entre 0 e 10.")
    except ValueError:
      print("Nota inválida. Valor tem que estar entre 0 e 10.")
          
  students[ra] = {
    "name": name,
    "note_B1": note_B1,
    "note_B2": note_B2
  }

def show_student():
  for ra, student in students.items():
    print(f"RA: {ra}, Nome: {student['name']}, Nota B1: {student['note_B1']}, Nota B2: {student['note_B2']}")

def remove_student():
  while True:
    ra = input("Digite o RA para remover (Registro Acadêmico, 5 caracteres): ")
    if not len(ra) == 5:
      print("RA inválido. Deve ter 5 caracteres.")
    else:
      if ra in students:
        del students[ra]
        print(f"Aluno com RA {ra} removido com sucesso.")
        break
      else:
        print(f"Aluno com RA {ra} não localizado.")
        break

def search_student():
  ra = input("Digite o RA do aluno que deseja buscar: ")
  if ra in students:
    student = students[ra]
    print(f"RA: {ra}, Nome: {student['name']}, Nota B1: {student['note_B1']}, Nota B2: {student['note_B2']}")
  else:
    print(f"Aluno com RA {ra} não encontrado.")

def list_approved():
    print("Lista de Alunos Aprovados (Nota >= 7):")
    approved = [student for student in students.values() if ((student['note_B1'] + student['note_B2']) / 2) >= 7]
    if approved:
        for student in approved:
            print(f"Nome: {student['name']}, Nota Mádia: {(student['note_B1'] + student['note_B2']) / 2}")
    else:
        print("Nenhum aluno aprovado.")

def list_disapproved():
    print("Lista de Alunos Reprovados (Nota < 7):")
    disapproved = [student for student in students.values() if (student['note_B1'] + student['note_B1'] / 2) < 7]
    if disapproved:
        for student in disapproved:
            print(f"Nome: {student['name']}, Nota Mádia: {student['note_B1'] + student['note_B1'] / 2}")
    else:
        print("Nenhum aluno reprovado.")

def search_student_by_name():
    name = input("Digite o Nome do aluno que deseja buscar: ")
    found = [student for student in students.values() if student['name'].lower() == name.lower()]
    if found:
        for student in found:
            print(f"Nome: {student['name']}, Nota Mádia: {(student['note_B1'] + student['note_B2']) / 2}")
    else:
        print(f"Aluno com nome {name} não encontrado.")

def calculate_average_b1():
    note_b1 = [student['note_B1'] for student in students.values()]
    if note_b1:
        average = sum(note_b1) / len(note_b1)
        print(f"Média da turma B1: {average:.2f}")
    else:
        print("Nenhuma nota de B1 disponível.")

def calculate_average_b2():
    note_b2 = [student['note_B2'] for student in students.values()]
    if note_b2:
        average = sum(note_b2) / len(note_b2)
        print(f"Média da turma B2: {average:.2f}")
    else:
        print("Nenhuma nota de B2 disponível.")

def calculate_general_average():
    notes = [student['note_B1'] + student['note_B2'] for student in students.values()]
    if notes:
        average = sum(notes) / (2 * len(notes))
        print(f"Média geral da turma: {average:.2f}")
    else:
        print("Nenhuma nota disponível.")

def show_details():
  print("--------------------------------------------------------")
  print("                   Diário da turma                      ")
  print("--------------------------------------------------------")
  print("RA    Nome                      Nota B1  Nota B2   Média")
  print("--------------------------------------------------------")
  
  for ra, student in students.values():
        print(f"{ra.ljust(5)} {student['name'].ljust(27)} {str(student['note_B1']).rjust(7)} {str(student['note_B2']).rjust(7)} {str((student['note_B1'] + student['note_B2']) / 2).rjust(7)}")

  print("--------------------------------------------------------")

  note_b1 = [student['note_B1'] for student in students.values()]
  if note_b1:
    average_b1 = sum(note_b1) / len(note_b1)
  else:
    average_b1 = 0

  note_b2 = [student['note_b2'] for student in students.values()]
  if note_b2:
    average_b2 = sum(note_b2) / len(note_b2)
  else:
    average_b2 = 0

  notes = [student['note_B1'] + student['note_B2'] for student in students.values()]
  if notes:
    average = sum(notes) / (2 * len(notes))
  else:
    average = 0

  print(f"{'Médias da Turma': <34} {average_b1: >7.2f} {average_b2: >7.2f} {average: >7.2f}")
  print("--------------------------------------------------------")


########################################################################
    
students = {}

print("Bem-vindo ao sistema ajeitar.")
print()

while True:
  try:
    escolha = show_menu()
  
    match escolha: 
      case 0:
        print("Obrigado por usar o sistema.")
        break
      case 1:
        add_student()
      case 2:
        show_student()
      case 3:
        remove_student()
      case 4:
        search_student()
      case 5:
        list_approved()
      case 6:
        list_disapproved()
      case 7:
        search_student_by_name()
      case 8:
        calculate_average_b1()
      case 9:
        calculate_average_b2()
      case 10:
        calculate_general_average()
      case 10:
        calculate_general_average()
      case 11:
        show_details()
  except ValueError:
    print()
    print("Digite um valor válido.")