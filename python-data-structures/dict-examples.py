"""
Python Dict examples

Summary

Display
update
size
loop through
Check if Key Exists


clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


"""


class solution:
    def __init__(self, mydict=[]):
        """
        Initialization
        """
        self.dict = mydict

    def display(self):
        """
        Display dict
        """
        print(self.dict)

    def size(self):
        """
        Display dict size
        """
        print(len(self.dict))

    def get(self, key):
        """
            Access the items of a dictionary by referring to its key name, inside square brackets:
        """
        print(self.dict[key])
        print(self.dict.get(key))

    def update(self, key, new_value):
        """
            change the value of a specific item by referring to its key name
        """
        self.dict[key] = new_value

    def loop(self, ):
        """
            looping through a dictionary
        """
        print('key loop')
        for key in self.dict:
            print('key :' + key)
        print('Value loop')
        for value in self.dict.values():
            print('value :' + value)
        print('Key/Value loop')
        for key, value in self.dict.items():
            print('key :' + key)
            print('value :' + value)

    def keyexist(self, key):
        """
            check if key exist
        """
        if key in self.dict:
            print('Yes')
        else: 
            print('No')

    def valueExist(self, value):
        """
            check if value exist
        """
        for v in self.dict.values():
            if v == value:
                print('Yes in list')
                return
        print('Not in list')

    def removeKey(self, key):
        """
            Remove particular key
        """
        self.dict.pop(key)

    def deleteDict(self):
        """
        deleteDict
        """
        self.dict.clear()

if __name__ == "__main__":
    mydict = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964'
    }
    soln = solution(mydict)
    soln.display()
    soln.size()
    soln.get('model')
    soln.update('model', 'tesla')
    soln.get('model')
    soln.loop()
    soln.keyexist('my')
    soln.keyexist('model')
    soln.valueExist('my')
    soln.valueExist('tesla')
    soln.removeKey('model')
    soln.display()
    soln.deleteDict()
    soln.display()