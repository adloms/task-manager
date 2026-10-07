# Task Manager

tasks = []
is_running = True
task_num = 0

while is_running == True:
    
    print("\n1. Добавить задачу\n"
        "2. Показать все задачи\n"
        "3. Отметить задачу выполненой\n"
        "4. Удалить задачу\n"
        "5. Выход")

    match int(input("\nЧто сделать: ")):
        
        case 1:
            title = input("Введите задачу: ")
            tasks.append({'task': title, 'done': False})
            print("Задача добавлена \n")
            
        case 2:
            if not tasks:
                print("Список пуст") #Проверка на наличие записей
            else:
                print("\n*** Список задач ***") #Вывод списка записей
                for i, task in enumerate(tasks, 1):
                    status = "[x]" if task['done'] else "[ ]"
                    print(f"{i}. {task['task']} {status}")
                
        case 3:
            if not tasks:
                print("Список пуст") #Проверка на наличие записей
            else:    
                print("\n*** Список задач ***") #Вывод списка записей
                for i, task in enumerate(tasks, 1):
                    status = "[x]" if task['done'] else "[ ]"
                    print(f"{i}. {task['task']} {status}") 
                print()
                
                id = int(input("Введите номер выполненой задачи: ")) - 1
            
                if 0 <= id < len(tasks):
                    tasks[id]['done'] = True
                    print("Задача отмечена!\n")
                    
                else:
                    print("Неверный номер\n")
            
        case 4:
            if not tasks:
                print("Список пуст") #Проверка на наличие записей
            
            else:    
                print("\n*** Список задач ***") #Вывод списка записей
                for i, task in enumerate(tasks, 1):
                    status = "[x]" if task['done'] else "[ ]"
                    print(f"{i}. {task['task']} {status}") 
                print()
                
                id = int(input("Введите номер задачи: ")) - 1
                
                if 0 <= id < len(tasks):
                    print(f"Задача {tasks[id]['task'] } удалена!\n")
                    tasks.pop(id)
                    
                else:
                    print("Неверный номер\n") 
                           
        case 5:
            is_running = False
            print("Прощайте")
        case _:
            print("\nТакой опции нет\n")