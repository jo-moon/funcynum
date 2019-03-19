def sum_array(array):

    '''Return sum of all items in array

        args:
            an array of numbers, int, float and negative numbers are acceptable

        returns:
            the sum of the array: output is relative to input in terms of datatype

         examples:
             >>>sum_array([1, 2, 3, 4, 5])
             15
             >>>sum_array([8, 6, -4, 9, -1])
             18
             >>>sum_array([2.5, 3.8, 4, -2])
             8.3
    '''
    # if the array does not contain anything, it cannot be summed
    if len(array) == 0:
        return 0

    # the function adds the first item to the next of the array for each iteration.
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence

     args:
         n (int): value indicating a position in the fibonacci sequence

     returns:
         the integer value at poisition n

     examples:
         >>>fibonacci(4)
         3
         >>>fibonacci(8)
         21
    '''
    #base cases- the first 2 elements in the fibonacci sequence are both 1,
    #only once these cases are identified can the function run
    if n == 1:
        return 1
    elif n == 2:
        return 1

    #recursive case, returns the term at position n
    #the nth term is the sum of the 2 terms before it i.e int at position n-1 +  int at position n-2.
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!

        args:
            n: integer value

        returns:
            int: the value of n * n-1 * n-2... * 2 * 1

        examples:
            >>>factorial(4)
            24
            >>>factorial(6)
            720
    '''
    #base case- factorials only calculate until they reach 1, not 0
    if n == 1:
        return n

    # the function then multiplies n by n-1 for each recursion
       else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse
         args:
             word (str): a single string value of any length

         returns:
             word (str) in its reversed form, or word backward

         examples:
             >>>reverse('hello')
             'olleh'
             >>>reverse('what time is it')
             'ti si emit tahw'
    '''
    # if the string has a length of 0 it cannot be reversed
    # if string has a length of 1, the reverse is the same as the string

    if len(word) == 0:
        return word
    if len(word) == 1:
        return word

    # the function takes the string and moves the first item to the end for each recursion
    else:
        return reverse(word[1:]) + word[0]
