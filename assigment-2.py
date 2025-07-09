# TASK 1
a = int(input('Enter a number: '))

if a % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')


# TASK 2
total_sum = 0
for number in range(1, 51):
    total_sum += number
print("The sum of all numbers from 1 to 50 is:", total_sum)
