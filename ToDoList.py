

# To-Do-Liste
todo_list = []
# Benutzereingabe abfragen und To-Do-Liste aktualisieren
def add_todo():
    todo = input("Geben Sie einen neuen Eintrag für die To-Do-Liste ein: ")
    todo_list.append(todo)
    print("Eintrag hinzugefügt.")
def remove_todo():
    print("Aktuelle To-Do-Liste:")
    print_todo_list()
    index = int(input("Geben Sie den Index des Eintrags ein, den Sie entfernen möchten: "))
    if index < 0 or index >= len(todo_list):
        print("Ungültiger Index.")
    else:
        removed_todo = todo_list.pop(index)
        print(f"Eintrag '{removed_todo}' entfernt.")
def print_todo_list():
    if len(todo_list) == 0:
        print("Die To-Do-Liste ist leer.")
    else:
        print("To-Do-Liste:")
        for index, todo in enumerate(todo_list):
            print(f"{index}: {todo}")
# Benutzereingaben verarbeiten
def process_user_input():
    print("Mögliche Aktionen:")
    print("1 - Eintrag hinzufügen")
    print("2 - Eintrag entfernen")
    print("3 - To-Do-Liste anzeigen")
    print("0 - Programm beenden")
    choice = int(input("Geben Sie die gewünschte Aktion ein: "))
    if choice == 1:
        add_todo()
    elif choice == 2:
        remove_todo()
    elif choice == 3:
        print_todo_list()
    elif choice == 0:
        return False
    else:
        print("Ungültige Auswahl.")
    return True
# Hauptprogramm
running = True
while running:
    running = process_user_input()