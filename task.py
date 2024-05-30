def main():
    print("Personal Task Manager")

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

    while True:
        command = input("Comando (add/exit): ")
        if command == "add":
            task = input("Tarefa: ")
            add_task(task)
        elif command == "exit":
            break

def list_tasks():
    for i, task in enumerate(tasks):
        status = "Concluída" if task["completed"] else "Não Concluída"
        print(f"{i + 1}. {task['task']} [{status}]")

    while True:
        command = input("Comando (add/list/exit): ")
        if command == "add":
            task = input("Tarefa: ")
            add_task(task)
        elif command == "list":
            list_tasks()
        elif command == "exit":
            break

if __name__ == "__main__":
    main()