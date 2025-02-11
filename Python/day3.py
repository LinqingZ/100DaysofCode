# ascii.co.uk/art art website to find art piece
import random

print(random.random()) # random floating number 0 to 1
print("Heads" if random.randint(0, 1) == 0 else "Tails")
output = [1, 2, 3, 4]
random.shuffle(output)
print(random.shuffle(output)) # return None
print(output)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
pop_left = queue.popleft()                 # The first to arrive now leaves
print(pop_left)


squares = list(map(lambda x: x**2, range(10)))
# same as above
squares = [x**2 for x in range(10)]
print("Square", squares)

print("Random choose from queue: ",random.choice(queue))


for i in reversed(range(1, 10, 2)):
    print("reversed", i)


list1= [1,2,3]
list2=[4, 5, 6]
print([list1, list2])

print(sorted(['', 'Trondheim', 'Hammer Dance']))

#  How to use python Walrus Operator :=, using in the expression only (text := True)
(text := True)
print(text)



numbers = [2, 8, 0, 1, 1, 9, 7, 7]

description = {
    "length": (num_length := len(numbers)),
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}

print(description)
# {'length': 8, 'sum': 35, 'mean': 4.375}
# https://realpython.com/python-walrus-operator/

x = 3
print(f"{x:=8}")



from collections import Counter
  
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# with dictionary
count = Counter({'A':3, 'B':5, 'C':2})
print(count)

count.update(['A', 1])
print(count)