import os

todo = []
done = []

def todo_list():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
▀█▀ █▀█ ▄▄ █▀▄ █▀█   █░░ █ █▀ ▀█▀
░█░ █▄█ ░░ █▄▀ █▄█   █▄▄ █ ▄█ ░█░

            ~ todo help
    \n\n""")
    while True:
        e = input(">>> ")

        if e == "todo help":
            print('-> todo help:- displays all the commands\n-> todo add <task>:- adds the given task to your to-do list\n-> todo remove <task/task no.>:- removes the given task from your to-do list\n-> todo done <task/task no.>:- marks the given task as done\n-> todo list:- displays all the tasks in your to-do list\n-> todo clear:- clears your to-do list\n-> todo cls:- clears the console\n-> todo exit:- exits the program\n')
        
        elif e.startswith("todo add"):
            if e[9:] not in todo and e[9:] not in done:
                todo.append(e[9:])
                print(f"Added \"{e[9:]}\" to your to-do list on serial no. {todo.index(e[9:])+1}.\n")
            else:
                print("The provided task already exists in your to-do list or you already completed this task.\n")

        elif e.startswith("todo remove"):
            if e[12:].isnumeric():
                if int(e[12:]) <= len(todo):
                    value = todo[(int(e[12:])-1)]
                    todo.pop(int(e[12:])-1)
                    print(f"Removed {value} from your to-do list.\n")
                else:
                    print("Provide the right serial no.\n")
            else:
                if e[12:] in todo:
                    value = e[12:]
                    todo.remove(value)
                    print(f"Removed {value} from your to-do list.\n")
                else:
                    print("Provide the correct name of task.\n")

        elif e.startswith("todo done"):
            if e[10:].isnumeric():
                if int(e[10:]) <= len(todo):
                    value = todo[(int(e[10:])-1)]
                    done.append(value)
                    todo.pop(int(e[10:])-1)
                    print(f"Marked {value} as done.\n")
                else:
                    print("Provide the right serial no.\n")
            else:
                if e[10:] in todo:
                    value = e[10:]
                    done.append(value)
                    todo.remove(value)
                    print(f"Marked {value} as done.\n")
                else:
                    print("Provide the correct name of task.\n")

        elif e.startswith("todo list"):
            print("TO-DO:")
            if not len(todo) == 0:
                for index, item in enumerate(todo):
                    print(f"{index+1}) {item}")
                print()
            else:
                print("Your to-do list is empty.\n")
            
            print("DONE:")
            if not len(done) == 0:
                for item in done:
                    print(f'- {item}')
                print()
            else:
                print("You haven't done any tasks yet.\n")

        elif e.startswith("todo clear"):
            if len(todo) == 0:
                print("Your to-do list is already empty.\n")
            else:
                todo.clear()
                print("Cleared yout to-do list.\n")

        elif e.startswith("todo cls"):
            os.system('cls' if os.name == 'nt' else 'clear')
            todo_list()

        elif e.startswith("todo exit"):
            exit()

        else:
            print("This command doesn't exist.\n")
        
todo_list()
