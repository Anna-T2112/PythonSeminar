import csv

class human:
    def __init__(self, name, second_name,phone,description):
        self.name = name
        self.second_name = second_name
        self.phone = phone
        self.description = description

people=[]

def read(second_name):
    result = next((e for e in people if second_name.lower() in e.second_name.lower()), None)
    if (result == None):
        print("Человек не найден")
        return

    print(result.second_name + " " + result.name+" "+result.phone+" "+result.description)

def write(human):
    people.append(human)
    print(human.second_name+" добавлен в справочник.")

def update(second_name,human):
    result = next((e for e in people if second_name.lower() in e.second_name.lower()), None)
    if (result==None):
        print("Человек с фамилией "+second_name+"не найден")
        return

    result.name = human.name
    result.phone = human.phone
    result.description = human.description
    print("Данные человека "+human.name+" обновлены")

def delete(second_name):
    result = next((e for e in people if second_name.lower() in e.second_name.lower()), None)
    if (result==None):
        print("Человек с фамилией "+second_name+"не найден")
        return

    people.remove(result)
    print("Человек "+second_name+" удален из справочника.")

def export(file_name):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание'] 
    with open(file_name, 'w') as f:        
        write = csv.writer(f)      
        write.writerow(fields)
        for person in people:
            row = [person.second_name,person.name,person.phone,person.description]
            write.writerow(row)
    print("Справочник экспортирован в файл "+ file_name)

def print_commands():
    print("Выберите одну из возможных функций: ")
    print("Для чтения справочника введите read")
    print("Для добавления в справочник введите add")
    print("Для обновления справочника введите update")
    print("Для удаления из справочника введите delete")
    print("Для экспорта справочника в файл введите export")
    print("Для импорта данных из справочника введите import")
    print("Для выхода exit")

def import_file(file_name):
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0]=="Фамилия":
                continue
            
            new_person = human(row[1],row[0],row[2],row[3])
            people.append(new_person)

    print("Справочник импортирован из файла "+ file_name)

print_commands()
neeed_exit=False
while not neeed_exit:
    print("Введите команду:")
    command = str(input())
    if command == "read":
        print("Введите фамилию необходимого человека или ее часть.")
        read(str(input()))
    elif command == "add":
        print("Введите фамилию:")
        second_name = str(input())
        print("Введите имя:")
        name = str(input())
        print("Введите телефон:")
        phone = str(input())
        print("Введите описание:")
        description = str(input())
        person = human(name,second_name,phone,description)
        write(person)
    elif command == "update":
        print("Введите фамилию или ее часть:")
        second_name = str(input())
        print("Введите имя:")
        name = str(input())
        print("Введите телефон:")
        phone = str(input())
        print("Введите описание:")
        description = str(input())
        person = human(name,second_name,phone,description)
        update(second_name, person)
    elif command == "delete":
        print("Введите фамилию или ее часть:")
        second_name = str(input())
        delete(second_name)
    elif command == "export":
        print("Введите путь до файла экспорта:")
        file_name = str(input())
        export(file_name)
    elif command == "import":
        print("Введите путь до файла импорта:")
        file_name = str(input())
        import_file(file_name)
    elif command == "exit":
        neeed_exit = True
