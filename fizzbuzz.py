def fizzbuzz(n):
    
    # create empty list
    result = []

    # fill in the list
    for i in range(n):
        if i%15==0:
            result.append('Fizzbuzz')
        elif i%3==0:
            result.append('Fizz')
        elif i%5==0:
            result.append('Buzz')
        else:
            result.append(i)

    # return the list
    return result

print(fizzbuzz(20))