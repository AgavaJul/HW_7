
j = 0
k = 1
cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    list_1 = []
    for line in file:
        list_1.append(line.strip())       
    mylist = []
    mydict ={}
    for i in range(len(list_1)):
        if i == 0 or list_1[i] == '': 
            if i==0: j=0
            else: j=i+1
            mylist.clear()
            for k in range(int(list_1[j+1])):
                tempstr = list_1[j+2+k].split("|")
                mylist.append({'ingrеdient_name':tempstr[0], 'quantity':tempstr[1], 'measure': tempstr[2]})
            cook_book[list_1[j]] =[]
            for k in range(len(mylist)):
                cook_book[list_1[j]].append(mylist[k])

print(cook_book)
#задача 2

def get_shop_list_by_dishes (dishes, person_count):
    shop_list = {}
    dict_1 = {}
    for i in dishes:
        for ingredient in cook_book[i]:
            dict_1 = {k: v for k, v in ingredient.items() if k != 'ingrеdient_name'}
            dict_1['quantity'] = int(ingredient['quantity']) * person_count
            list_1 = ingredient.get('ingrеdient_name')
            shop_list[list_1] = dict_1 
    print(shop_list)

get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 4)


