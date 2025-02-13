scores = [90, 67, 88, 100]
for score in scores:
    print(score)

for i in range(len(scores)):
    print(score)

# JavaScript is different to looping on each element
# Use for (const element of array1) {
        #   console.log(element);
        # }
print(range(1, 8)) # not work
print([x for x in range(1, 8)]) # works

def fizzBuzz(start=1, end = 10):
    for num in range(start, end+1):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)


fizzBuzz()