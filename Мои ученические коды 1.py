HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход с программы"""

tasks = {}

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    day = input("Введите интересующую вас дату для отображения списка задач: ")
    if day in tasks:
      for task in tasks[day]:
        print("- ", task)
    else:
      print("Такой даты нету в списке дел")
  elif command == "exit":
    break
  elif command == "add":
    day = input("Введите число выполнения задачи: ")
    task = input("Введите название задачи: ")
    print("Задача", task, "добавлена на", day)
    if day in tasks:
      tasks[day].append(task)
    else:
      tasks[day] = [task]
      print("Создана новая дата выполнения задачи")
  else:
    break

print("Спасибо за использование! До свидания!")