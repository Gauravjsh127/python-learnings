"""
Python String examples

More Details can be find here : https://www.tutorialspoint.com/python/python_strings.htm

"""

class solution:
    def __init__(self, mystring):
        """
        Initialization
        """
        self.string = mystring

    def display(self):
        """
        Display string
        """
        print(self.string)

    def append(self, extra):
        """
        Add an item to the end of the string
        """
        self.string = self.string + extra

    def accessing_via_index(self, startIndex, endIndex):
        """
        Insert an item at a given position
        """
        print(self.string[startIndex:endIndex])

    def count(self, substring, beg, end):
        """
        Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
        """
        print(self.string.count(substring, beg, end))

    def size(self):
        """
        Return the size of the string
        """
        print(len(self.string))

    def find(self, substring, beg, end):
        """
        determines if string str occurs in string, or in a substring of string if starting index beg and ending index end are given.
        """
        print(self.string.count(substring, beg, end))


if __name__ == "__main__":
    mystring = 'this is stringsasasaasass example....wow!!!'
    soln = solution(mystring)
    soln.display()
    soln.append('extra')
    soln.display()
    soln.accessing_via_index(2, 8)
    soln.accessing_via_index(1, 4)
    soln.count('o', 2, 48)
    soln.size()
    str2 = "stringsasasaasass"
    soln.find(str2, 0 , 40)