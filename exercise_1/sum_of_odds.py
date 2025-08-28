"""This function is called 'sum_of_odds'.
It takes 2 positive integers a and b, which are assigned variable names n1 and n2 respectively,
and returns the sum of all odd integers from a to b inclusively."""


def sum_of_odds (n1, n2):

    sum = 0

    if n1 <= 0 or n2 <= 0:
        print("You haven't provided 2 positive integers!")   #if either number is negative
    
    elif n1%2 !=0 and n2%2 !=0:                              #if both integers are odd
        for i in range (n1, n2+1, 2):
            sum += i
        
        print(sum)
    

    elif n1%2 == 0 and n2%2 ==0:                             #if both integers are even
        for i in range (n1+1, n2, 2):
            sum +=i
        
        print (sum)
    
    elif n1%2 !=2 and n2%2 ==0:                              #if n1 odd, and n2 even
        for i in range (n1, n2, 2):
            sum += i
        
        print(sum)

    
    elif n1%2 ==0 and n2%2 !=0:                              #if n1 even, and n2 odd
        for i in range (n1+1, n2+1, 2):
            sum += i
        
        print(sum)
    

if __name__ == "__main__":
    sum_of_odds (10, 25)



