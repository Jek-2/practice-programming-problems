'''
Richard Ricardo
Programming Exercise 2
Implement the following in two lines of code
> If n is odd or if n is even and in between 6 and 20 (inclusive), print “Weird”
> If n is even and in between 2 and 5 (inclusive) or if n is even and > 20, print “Not Weird”
'''
number = int(input("Input a positive integer: "))
print("Weird") if 6<= number <=20 else print("Not Weird") if number % 2 == 0 and 2<= number <=5 or number % 2 == 0 and number >20 else None