 match int(input("\nЧто сделать: ")):
        
        case 1:
            title = input("Введите задачу: ")
            tasks.append({'task': title, 'done': False})
            print("Задача добавлена \n")