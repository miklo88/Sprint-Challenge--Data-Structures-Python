class RingBuffer:
    def __init__(self, capacity):
#setting where to store the items and the capacity of the buffer
        self.items = []
        self.capacity = capacity
        self.oldest = 0

    def append(self, item):
#adding appending items to the buffer. if we have room in the capacity then add an item
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.oldest] = item
            self.oldest += 1
#if the oldest item is equal to the capacity of the list then replace its value.
        if self.oldest == self.capacity:
            self.oldest = 0 

    def get(self):
        #gather all the values in the buffer
        return self.items
        # pass

# buffer = RingBuffer(3) #buffer size is 3
# # buffer = RingBuffer(5) #seeing if it works up to 5 elements
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# #seeing if it updates the oldest item
# buffer.append('d')
# # print(buffer.get()) 
# #returns ['d','b','c']
# # buffer.append('e')
# # buffer.append('f')
# print(buffer.get())
# #returns ['d','e','f']
'''
UPER notes
set length of size. non-growable/scaleable. just the values will change. not the size of the buffer.
the oldest element is deleted when a new element inserted. IF there is no room. How much room do I have?

this reminds me of the recyle bin on a mac lol
bet i could use the sentinal node I was talking to hira about here.
RingBuffer class
two methods 
append - add to the ring buffer
get - returns all elements in the buffer in their inserted order. 
No values of NONE should be returned if present in the ring buffer. 
So i need to be able to add to the buffer. and if the buffer exceeds a certain size or
length. then remove the oldest value in the list.

need to define a list and items that go in a list.
'''
    #### Task 1. Implement a Ring Buffer Data Structure
'''
A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and
a new element is inserted, the oldest element in the ring buffer is overwritten with the
newest element. This kind of data structure is very useful for use cases such as storing 
logs and history information, where you typically want to store information up until it reaches a certain age, after 
which you don't care about it anymore and don't mind seeing it overwritten by newer data.
Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and
`get`. The `append` method adds the given element to the buffer. The `get` method returns
all of the elements in the buffer in a list in their given order. It should not return any
`None` values in the list even if they are present in the ring buffer.
For example:

```python
buffer = RingBuffer(3)
buffer.get()   # should return []
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.get()   # should return ['a', 'b', 'c']
# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
buffer.get()   # should return ['d', 'b', 'c']
buffer.append('e')
buffer.append('f')
buffer.get()   # should return ['d', 'e', 'f']
```
'''