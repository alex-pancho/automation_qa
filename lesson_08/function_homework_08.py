def sum_of_numbers(a, b):
    '''Calculating the sum of two numbers'''
    return a + b

    

def calc_average(numbers):
    '''Calculating the average'''
    average = sum(numbers)/len(numbers)
    return(average)



def longest_word(list_word):
    '''return longest word from list'''
    lon_word = max(list_word, key=len)
    return(lon_word)
list_word = ["Сніг", "свят"]
print(longest_word)
