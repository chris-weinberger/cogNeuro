import random


# this program assumes there are 32 orthogonal vectors to choose from. Then, it will randomly select 8 from that list

num_selected = 0
total = 32
want = 8

selected = []

while(num_selected < want):
    new_num = random.randint(1,total)
    while new_num in selected:
        new_num = random.randint(1,total)
    selected.append(new_num)
    num_selected += 1

print(selected)

# Next, choose 4 more different values to represent the abstract category output vectors, 

#these were the original random values chosen by the program, change as you see fit
selected = [9, 26, 4, 27, 10, 25, 13, 17]

print(selected)

abstract_output = []
abstract_want = 4
num_selected = 0
while(num_selected < abstract_want):
    new_num = random.randint(1,total)
    while ((new_num in selected) or (new_num in abstract_output)):
        new_num = random.randint(1,total)
    abstract_output.append(new_num)
    num_selected += 1

# Next, choose 16 more different values to represent the specific category output vectors
specific_output = []
specific_want = 16
num_selected = 0
while(num_selected < specific_want):
    new_num = random.randint(1,total)
    while ((new_num in selected) or (new_num in abstract_output) or (new_num in specific_output)):
        new_num = random.randint(1,total)
    specific_output.append(new_num)
    num_selected += 1

print(abstract_output)
print(specific_output)