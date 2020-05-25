String_num = input()
Len = len(String_num)
if String_num[0] == '-':
    print('-', end='')

for i in range(Len):
    for j in range(9):
        if ord(String_num[i]) == ord(str(j)):
            print(String_num[i], end='')



