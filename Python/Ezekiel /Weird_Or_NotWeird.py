#Activity #2
#If n is odd or if n is even and in between 6 and 20 (inclusive), print “Weird”
#If n is even and in between 2 and 5 (inclusive) or if n is even and > 20, print “Not Weird”
# Do this with 1 line 

print(list(map(lambda given: "negative number" if given < 1 else "weird" if given > 5 and given < 21 else "not weird" if given % 2 == 0 else " ",[int(input())])))

