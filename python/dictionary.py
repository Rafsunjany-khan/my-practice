# python dictionary contain two pair value "KEY" & "VALUE"

"""dict = {'key': 'value'}
print(dict)
print(type(dict))
dict = {
    "name": "Rafsunajany",
    "age": 26,
    "education": "BSC in CSE",
}
print(len(dict))
print(dict['name'])
print(dict.get('age'))
print(dict.keys())
print(dict.values())
print(dict.items())
#adding key and value
dict["university"] = "daffodil"
print(dict)
#update value
dict['age'] = 27
print(dict)
# key check
if "name" in dict:
    print("Yes, it is here")
else:
    print("I am sorry")
#change items
dict['name'] = 'sharod'
print(dict)
# update Dictionary
dict.update({'age': 28})
print(dict)
# remove items
dict.pop('university')
print(dict)
# The popitem() method removes the last inserted item
dict.popitem()
print(dict)
# del keyword
del dict["age"]
print(dict)
# clear
dict.clear()
print("clear =", dict)"""
dict = {'key': "abcd",
        'key1': "efghi",
        'key2': 22,
        'key3': [1,2,4,5,6,7,8],
        'key4': {"counter_no": 'sha-1',
                 "bus_no": [{'Ga': 1010, 'arrival_time': 5}
        ]},
        'key5': ('apple', 'banana', 'orange', 'egg'),
        'key6': True,
        }
x = dict['key4']
for y in x.values():
    print(y)



