#
# dict={
#     1:'Akin',
#     2:'Nanju'
# }
# print(dict[1])

info={'name':'Akin', 'Surname':'Nanju', 'age':19, 'eligible':'Yes','cars':['BMW','LAMBO','ROLLS','FERRARI'],'salary':19000}
print(info["name"]) #If there in no value then it will return error in program
print(info.get("name2")) #If there is no value in program then it will return none
print(info)
print(info.get('cars'))
print(info.keys()) #it is used to print the keys used in dictionery
print(info.values()) #It is used to print the values stored in dictionery
print(info.items()) #It is used to print values in pair
for i in info:
    print(f"The value of corresponding  key {i} is {info[i]} ")
    print(i)


item={'milk':50, 'cabbage':55, 'tomato':60, 'carrot':60}
print(item.get('milk'))
print(item.keys())
print(item.values())



