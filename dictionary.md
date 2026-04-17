dictionaries

1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data. (*Since Python 3.6x dictionaries have become ordered by default.)

Each dictionary is a set of key: value pairs. You can create it by using the following syntax:

###

my_dictionary = {
key1: value1,
key2: value2,
key3: value3,
}

2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the get() method (ex. 2):

###

pol_eng_dictionary = {
"kwiat": "flower",
"woda": "water",
"gleba": "soil"
}

item_1 = pol_eng_dictionary["gleba"] # ex. 1
print(item_1) # outputs: soil

item_2 = pol_eng_dictionary.get("woda") # ex. 2
print(item_2) # outputs: water

3. If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:

###

pol_eng_dictionary = {
"zamek": "castle",
"woda": "water",
"gleba": "soil"
}

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]
print(item) # outputs: lock

4. To add or remove a key (and the associated value), use the following syntax:

###

phonebook = {} # an empty dictionary

phonebook["Adam"] = 3456783958 # create/add a key-value pair
print(phonebook) # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook) # outputs: {}

4. 1. You can also insert an item into a dictionary by using the update() method, and remove the last element by using the popitem() method, e.g.:

###

pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'}

5. You can use the for loop to loop through a dictionary, e.g.:

###

pol_eng_dictionary = {
"zamek": "castle",
"woda": "water",
"gleba": "soil"
}

for item in pol_eng_dictionary:
print(item)

# woda

# gleba

6. If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:

###

pol_eng_dictionary = {
"zamek": "castle",
"woda": "water",
"gleba": "soil"
}

for key, value in pol_eng_dictionary.items():
print("Pol/Eng ->", key, ":", value)

7. To check if a given key exists in a dictionary, you can use the in keyword:

###

pol_eng_dictionary = {
"zamek": "castle",
"woda": "water",
"gleba": "soil"
}

if "zamek" in pol_eng_dictionary:
print("Yes")
else:
print("No")

8. You can use the del keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the clear() method:

###

pol_eng_dictionary = {
"zamek": "castle",
"woda": "water",
"gleba": "soil"
}

print(len(pol_eng_dictionary)) # outputs: 3
del pol_eng_dictionary["zamek"] # remove an item
print(len(pol_eng_dictionary)) # outputs: 2

pol_eng_dictionary.clear() # removes all the items
print(len(pol_eng_dictionary)) # outputs: 0

del pol_eng_dictionary # removes the dictionary

9. To copy a dictionary, use the copy() method:

pol_eng_dictionary = {
"zamek": "castle",
"woda": "water",
"gleba": "soil"
}

copy_dictionary = pol_eng_dictionary.copy()
