#PRINT FIZZ FOR NUMBERS DIVISIBLE FOR 3
#PRINT BUZZ FOR NUMBERS DIVISIBLE FOR 5
#PRINT FIZZBUZZ FOR NUMBERS DIVISIBLE FOR 3 AND 5


#LIST COMPREHENSIONS CONCEPT
nums = [n for n in range(1,100)]

#CONDITIONS TO FIZZBUZZ
for i in nums:
    if i % 3 == 0 and i % 5 == 0:
        print('FIZZBUZZ')
    elif i % 3 == 0:
        print('FIZZ')
    elif i % 5 == 0:
        print('BUZZ')
    else:
        print(i)


