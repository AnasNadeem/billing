# with open('file.txt', 'r+') as f:
#     # print(f.readlines())
#     contents = f.read().replace('invoice', 'Invoice:2012')
#     f.seek(0)
#     f.truncate()
#     f.write(contents)
#     # f.seek(10)
#     # print(f.tell())
#     # f.write('add')
#     # print(f.tell())
#     # addtxt = 'fnother txt'
#     # antxt = '\nanother'
#     # moretxt = '\n\t\tanother txt'
#     # f.write(addtxt)
#     # f.write(antxt)
#     # f.write(moretxt)
#     # a = f.seek(2)
#     # f.write('my name')
#     # print(a)
#     # txt = f.read()
#     # print(txt)
#     # f.write('hei')


# with open('file.txt', 'r') as rf:
#     size = 4
#     rf_chunk = rf.read(size)
#     while len(rf_chunk) > 0:
#         print(rf_chunk, end='')
#         rf_chunk = rf.read(size)
        
with open('file.txt', 'r') as rf:
    line = rf.readlines()
    # bill_no = line[3]
    # prod_list1 = line[10]
    prod_list = {}
    for key, value in range(10,15):
        # prod_list[i] = line[i]
        # prod_list[key] = line[]
    print(prod_list)
prod_list={} 
for i in range(10, 15):
    prod_list["string{}".format(i)] = "Hello"

print(prod_list)
    # bill_list2 = line[11]
    # print(prod_list1)
    # cus_name = line[5]
