fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cidar",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit, growing in bunches",
         "lime": "a sour, green citrus fruit"}
#if we give same key for 2 different values, the last one will be its value
#"apple": "sweet, crunchy, fruit beer"      -> try keeping it in the above dict

print(fruit)
print(fruit["lemon"])
fruit["pear"]= "an odd shaped apple"
print(fruit)
fruit["lime"]= "great with tequila"
print(fruit)
del fruit["lemon"]
print(fruit)
#the next line will delete all the elements of the dictionary, hence commeneted it
#fruit.clear()
#if we ask to print a key which doesn't exist, it will give error.
#print(fruit["tomato"])

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    # description = fruit.get(dict_key,"We don't have a "+ dict_key)
    # print(description)
    # The above commented code does the same function as the below 5 line code.
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a {}".format(dict_key))


for snack in fruit:
    print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-"*40)

#for vreating an ordered dictionary
#now, they will always be in the same order
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# #ordered_keys = sorted(list(fruit.keys())     -> this will make the sorted list in just 1 line.
# for i in ordered_keys:
#     print(i+" - "+fruit[i])
#
for i in sorted(fruit.keys()):
    print(i+" - "+fruit[i])

print("*"*45)

# for val in fruit.values():  #this is less optimized
#     print(val)
# print("*"*45)
# for key in fruit:
#     print(fruit[key])
# print("*"*45)
# fruit_keys = fruit.keys()
# print(fruit_keys)
# print("*"*45)
# fruit_values= fruit.values()
# print(fruit_values)
# print("*"*45)


# fruit["tomato"]= "Not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuples = tuple(fruit.items())
print(f_tuples)

for snack in f_tuples:
    item,description = snack
    print(item +" is "+description )