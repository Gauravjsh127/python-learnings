"""
Python Queue example : Implemented via list

Summary
The functions associated with queue are:

    Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
    Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
    Front: Get the front item from queue – Time Complexity : O(1)
    Rear: Get the last item from queue – Time Complexity : O(1)


    Source : https://www.geeksforgeeks.org/queue-in-python/

"""

class solution:
    def __init__(self, myqueue=[]):
        """
        Initialization
        """
        self.queue = myqueue
        self.maxsize = 10

    def display(self):
        """
        Display queue
        """
        print(self.queue)

    def size(self):
        """
        Display queue size
        """
        print(len(self.queue))

    def Enqueue(self, elem):
        """
            Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1) 
        """
        if(len(self.queue) == self.maxsize):
            print('Overflow')
            return
        self.queue.append(elem)

    def Dequeue(self):
        """
            Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
        """
        if(len(self.queue) == 0):
            print('Underflow')
            return
        self.queue.pop(0)  # Delete last element

    def Front(self):
        """
            Get the front item from queue – Time Complexity : O(1)
        """
        print(self.queue[0])

    def Rear(self):
        """
            Get the last item from queue – Time Complexity : O(1)
        """
        print(self.queue[len(self.queue) - 1])

if __name__ == "__main__":
    myqueue = [1, 2, 3]
    soln = solution(myqueue)
    soln.Front()
    soln.Rear()
    soln.Enqueue(5)
    soln.Front()
    soln.Rear()
    soln.Dequeue()
    soln.Front()
    soln.Rear()

