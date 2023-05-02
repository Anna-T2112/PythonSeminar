import csv
from datetime import *

class note:
    def __init__(self, id, header,body,created,updated):
        self.id = id
        self.header = header
        self.body = body
        self.created = created
        self.updated = updated

notes=[]

def get_last_id():
    if (len(notes)==0):
        return 1

    return len(notes)+1

def read(id):
    result = next((e for e in notes if id== e.id), None)
    if (result == None):
        print("Заметка с идентификатором "+str(id)+" не найдена")
        return

    print(result.header + "\n" + result.body)

def check_note_exist(id):
    result = next((e for e in notes if id== e.id), None)
    if (result==None):
        return False
    else:
        return True

def show_by_date(date):
    filtered = filter(lambda item:item.created.date()==date.date(),notes)
    for item in filtered:
        print(item.header+"\n"+item.body+"\n")

def write(note):
    notes.append(note)
    print(note.header+" добавлена в справочник.")

def update(id,body,header):
    result = next((e for e in notes if id== e.id), None)
    if (result==None):
        print("Заметка с идентификатором "+str(id)+" не найдена")
        return
    result.header = header
    result.body = body
    result.updated = datetime.now()
    print("Заметка "+str(id)+" обновлена")

def delete(id):
    result = next((e for e in notes if id== e.id), None)
    if (result==None):
        print("Заметка с идентификатором "+str(id)+" не найдена")
        return

    notes.remove(result)
    print("Заметка с идентификатором "+str(id)+" удалена.")

def export(file_name):
    fields = ['Идентификатор', 'Заголовок', 'Заметка', 'Дата создания','Дата обновления'] 
    with open(file_name, 'w') as f:        
        write = csv.writer(f,delimiter=';')      
        write.writerow(fields)
        for item in notes:
            row = [item.id,item.header,item.body,item.created.strftime("%d.%m.%Y"),item.updated.strftime("%d.%m.%Y")]
            write.writerow(row)
    print("Справочник экспортирован в файл "+ file_name)

def print_commands():
    print("Выберите одну из возможных функций: ")
    print("Для чтения заметки введите read")
    print("Для чтения всех заметкок введите readAll")
    print("Для добавления заметки введите add")
    print("Для обновления заметки введите update")
    print("Для удаления заметки введите delete")
    print("Для экспорта заметок в файл введите export")
    print("Для импорта заметок введите import")
    print("Для выбора заметки по дате введите noteDate")
    print("Для выхода exit")

def import_file(file_name):
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file,delimiter=';')
        for row in csvreader:
            if row[0]=="Идентификатор":
                continue
            
            new_note = note(row[0],row[1],row[2],datetime.strptime(row[3],"%d.%m.%Y"),datetime.strptime(row[4],"%d.%m.%Y"))
            notes.append(new_note)

    print("Справочник импортирован из файла "+ file_name)

print_commands()
res=get_last_id()
print(res)
neeed_exit=False
while not neeed_exit:
    print("Введите команду:")
    command = str(input())

    if command == "read":
        print("Введите идентификатор заметки.")
        read(int(input()))

    elif command == "readAll":
        for item in notes:
            print(item.header+"\n"+item.body+"\n")

    elif command == "add":
        print("Введите заголовок заметки:")
        header = str(input())
        print("Введите текст заметки:")
        body = str(input())
        newNote = note(get_last_id(),header,body,datetime.now(),datetime.now())
        write(newNote)

    elif command == "update":
        print("Введите идентификатор заметки:")
        id = int(input())
        result = check_note_exist(id)
        if (result==False):
            print("Заметка с идентификатором "+id+" не найдена")
            continue

        print("Введите заголовок заметки:")
        header = str(input())
        print("Введите текст заметки:")
        body = str(input())
        update(id,body,header)
    
    elif command == "delete":
        print("Введите идентификатор заметки:")
        id = int(input())
        delete(id)
    elif command == "export":
        print("Введите путь до файла экспорта:")
        file_name = str(input())
        export(file_name)
    elif command == "import":
        print("Введите путь до файла импорта:")
        file_name = str(input())
        import_file(file_name)
    elif command == "noteDate":
        print("Введите дату в формате dd.MM.YYYY(21.12.1988):")
        value = datetime.strptime(str(input()), '%d.%m.%Y')
        show_by_date(value)
    elif command == "exit":
        neeed_exit = True
