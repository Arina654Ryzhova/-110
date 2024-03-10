import csv 

with open('students.csv', encoding ='utf-8') as file:
    reader = csv.reader(file, delimiter = ',')
    answer = list(reader)[1:]
    count_class = {}
    sum_class = {}
    for id, Name, titleProject_id, level, score in answer:
        if 'Хадаров Владимир' in Name:
            print(f'Ты получил: {score}, за проект - {titleProject_id}')
            break
        
        count_class[level] = count_class.get(level, 0) +1 
        if score != 'None':
            score = int (score)
        else:
            score = 0
        sum_class[level] = sum_class.get (level, 0) + score
    for el in answer:
        if el[-1] == 'None':
            el[-1] = round (sum_class[el[-2]] / count_class[el[-2]],3)