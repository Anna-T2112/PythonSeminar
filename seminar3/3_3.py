#3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.
#А русские буквы оцениваются так:
#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков.
#Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы и заранее известно какой алфавит надо использовать.
#Примеры/Тесты:
#Input:   ноутбук
#Output:  12
#Input:   notebook
#Output:  14


def calculateScrabble(word,language):
    one_point = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
    two_points = ["D", "G"]
    three_points = ["B", "C", "M","P"]
    four_points = ["F", "H", "V", "W", "Y"]
    five_points = ["K"]
    eight_poinst = ["J","X"]
    ten_points = ["Q","Z"]

    one_point_russia = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
    two_point_russia = ["Д", "К", "Л", "М", "П", "У"]
    three_point_russia = ["Б", "Г", "Ё", "Ь", "Я"]
    four_point_russia = ["Й", "Ы"]
    five_point_russia = ["Ж", "З", "Х", "Ц", "Ч"]
    eight_poinst_russia = ["Ш", "Э", "Ю"]
    ten_poinst_russia = ["Ф", "Щ", "Ъ"]

    upper_word = word.upper()
    result = 0
    if language=="en":
        for elem in upper_word:
            result += one_point.count(elem)+two_points.count(elem)*2+three_points.count(elem)*3+four_points.count(elem)*4 + five_points.count(elem)*5 + eight_poinst.count(elem)*8+ten_points.count(elem)*10  
    elif language=="ru":
        for elem in upper_word:
            result += one_point_russia.count(elem)+two_point_russia.count(elem)*2+three_point_russia.count(elem)*3+four_point_russia.count(elem)*4 + five_point_russia.count(elem)*5 + eight_poinst_russia.count(elem)*8+ten_poinst_russia.count(elem)*10  
    
    return result

print("Введите слово: ")
word = input()
print("Введите язык (ru или en): ")
language = input()
result = calculateScrabble(word,language)
print("%d очков" % result)