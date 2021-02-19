def summa_3(a, b, c):
  return a + b + c
  
def char_counting(line):
  count=0
  for char in line:
    if char.isalpha():
      count+=1
  return count

def calсulate_fibonacci(first_number, iterationsCount):
  result = [first_number, 1]
  while not len(result) == iterationsCount:
    last_number = len(result) - 1
    next_number = result[last_number] + result[last_number - 1] 
    result.append(next_number)
  return result

def division(a, b):
  if b==0:
    raise Exception ('Делить на ноль нельзя!')
  return a/b

def multi(a, b):
  return a*b

def equation (a, b, c):
  if a == 0:
    raise Exception ('При первом аргументе ноль невозможен')
  discr=b**2-4*a*c
  if discr>0:
    x1=(-b+(discr)**0.5)/(2*a)
    x2=(-b-(discr)**0.5)/(2*a)
    return x1, x2
  elif discr==0:
    x=-b/(2*a)
    return x
  else:
    return "Корней нет"

def circle_square (r):
  s=3.14*r**2
  return s

def hypotenuse(a,b):
  c=(a**2+b**2)**0.5
  return c

def circle_volume (r):
  v=4/3*3.14*r**3
  return v

def banhammer():
  r="╔═════╗╔════╗╔═╗╔═╗\n ║ ╔═══╝║ ╔╗ ║║ ║║ ║\n ║ ╚═══╗║ ╚╝ ║║ ╚╝ ║\n ║ ╔═╗ ║║ ╔╗ ║║ ╔╗ ║\n ║ ╚═╝ ║║ ║║ ║║ ║║ ║\n ╚═════╝╚═╝╚═╝╚═╝╚═╝"
  return r

import logging
logger=logging.getLogger(__name__)

input_file = open("data.txt", 'r')
for line in input_file:
  try:
    parametrs=line.split()  
    command = parametrs[0] 
    if command == 'sum':
      summ=summa_3(int(parametrs[1]), int(parametrs[2]), int(parametrs[3]))
      print(f'Сумма: {summ}')
    elif command == 'chars':
      if len(parametrs) < 2:
        raise Exception(f'Команда {parametrs[0]} не имеет параметров')
      char_count=char_counting(parametrs[1])
      print(f'Кол-во букв: {char_count}')
    elif command == 'fibonacci':
      fibonacci=calсulate_fibonacci(int(parametrs[1]), int(parametrs[2]))
      print(f'Fibonacci: {fibonacci}')
    elif command == 'div':
      div=division(int(parametrs[1]), int(parametrs[2]))
      print(f'Частное: {div}')
    elif command=='multi':
      mult=multi(int(parametrs[1]), int(parametrs[2]))
      print(f'Произведение: {mult}')
    elif command == 'equa':
      equ=equation(int(parametrs[1]), int(parametrs[2]), int(parametrs[3]))
      print(f'Корни уравнения: {equ}')
    elif command=='circSquare':
      square=circle_square(int(parametrs[1]))
      print(f'Площадь круга: {square}')
    elif command =='hypo':
      hypo=hypotenuse(int(parametrs[1]), int(parametrs[2]))
      print(f'Гипотенуза равна: {hypo}')
    elif command == 'vol':
      vol=circle_volume(int(parametrs[1]))
      print(f'Объём шара равен: {vol}')
    elif command == 'ban':
      print(f'    Привет, тебе...\n {banhammer()}')
    else:
      raise Exception(f'Команда {parametrs[0]} не найдена')     
  except Exception as e:
    print(f'#ERROR: В строке {line}: {e}')
input_file.close()