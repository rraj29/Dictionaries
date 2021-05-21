fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cidar",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit, growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "Every child's favourite",
       "sprouts": "Mmm, lovely",
       "spinach": "Can I have some more fruits, please?"}
print(veg)

veg.update(fruit)
print(veg)
fruit.update(veg)
print(fruit)
veg["potato"]="Yummy and tasty"
print(veg)
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)