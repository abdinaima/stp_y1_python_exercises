
"""This function is called 'sum_of_odds'.
It takes 2 positive integers a and b, which are assigned variable names n1 and n2 respectively,
and returns the sum of all odd integers from a to b inclusively."""


def sum_of_odds (n1, n2):

    sum = 0

    if not isinstance(n1, int) or not isinstance(n2, int):
        raise TypeError ("You need to provide 2 integers!")

    if n1 <= 0 or n2 <= 0:
        raise ValueError ("Both numbers need to be positive!")     #if either number is negative
    
    
    elif n1%2 !=0 and n2%2 !=0:                                   #if both integers are odd
        for i in range (n1, n2+1, 2):
            sum += i
        
        return sum
    

    elif n1%2 == 0 and n2%2 ==0:                                  #if both integers are even
        for i in range (n1+1, n2, 2):
            sum +=i
        
        return sum
    
    
    elif n1%2 !=2 and n2%2 ==0:                              #if n1 odd, and n2 even
        for i in range (n1, n2, 2):
            sum += i
        
        return sum

    
    elif n1%2 ==0 and n2%2 !=0:                              #if n1 even, and n2 odd
        for i in range (n1+1, n2+1, 2):
            sum += i
        
        return sum
    

if __name__ == "__main__":
    
    print(sum_of_odds(10, 25))



