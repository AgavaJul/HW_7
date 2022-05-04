import os

list_1 = []
count = 0

for filename in os.listdir("HW_7_2"):
    with open(os.path.join("HW_7_2", filename), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count = len(lines)
        with open(os.path.join("HW_7_2", filename), 'w', encoding='utf-8') as modified: 
            modified.write(f'{filename}\n{count}\n')
            for i in range(len(lines)):
                modified.write(lines[i])
        with open(os.path.join("HW_7_2", filename), 'r', encoding='utf-8') as file:
            lines_1 = file.readlines()
        list_1.append(lines_1)
        list_1.sort(key=len)
        with open ('4.txt', 'w', encoding='utf-8') as f:
            for item in list_1:
                f.write('\n')
                for element in item:
                    f.write(element)
        
