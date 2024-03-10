arr=[st[:-1].split(',') for st in open('students.csv','r',encoding='UTF-8') if 'None' not in st]
arr0=arr.pop(0)
idp=input() 
while idp != 'СТОП':
    rev = arr[::-1]
    f=True
    for ar in arr:
        if idp==ar[2]:
            sername, name= ar[1].split()[:2]
            print(f"Проект № {idp} делал: {name[0]}. {sername} он(а) получил(а) оценку - {ar[-1]}")
            f=False
    if f: print('Ничего не найдено')
    idp=input()        
           
