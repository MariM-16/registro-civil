from person import Person

people = []

def print_menu_and_select():
    print ("\nSelecciona una de las siguientes opciones ")
    print ("1. Crear una persona ")
    print ("2. Envejecer una persona ")
    print ("3. Mostrar personas ")
    print ("4. Cambiar nombre ")
    print ("0. Salir ")
    return int(input())

def create_person():
    name = input("Ingrese el nombre de la persona: ")
    age = int(input("Ingrese la edad de la persona: "))
    people.append(Person(name,age))

def show_people():
    print("\nPesonas creadas: \n")
    for (i,_) in enumerate(people):
        print(f"{i}: {people[i].name} = {people[i].age}" ) #preguntar esto porque no entendi

def person_selector():
    return int(input("A quien quieres seleccionar? "))

def grow_old_person(): #envejecer a personas pero debo primero mostrar a todas
    show_people()
    i = person_selector()
    years = int(input("En cuántos años lo quieres envejecer? "))
    try:
        people[i].age += years
        return
    except ValueError as e:
        print(e)
    
def change_name():
    i = person_selector()
    name = input("Ingresa el nuevo nombre ")
    people[i].name = name

def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            create_person()
        if selection == 2:
            grow_old_person()
        if selection == 3:
            show_people()
        if selection == 4:
            change_name()



if __name__ == "__main__":
    menu()