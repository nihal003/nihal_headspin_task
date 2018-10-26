# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import fractions                    #Imported the module fractions for using built in function gcd() used to find greatest common divisor (gcd)

def lcm(n):
    x=1
    for i in range(1,n+1):
        x=(x*i)/fractions.gcd(x,i)  #Initialised variable "x" as "i" is used to calculate the formula "x=(x*i)/fractions.gcd(x,i)" in a loop from 1 to 20.
    return x

ans=lcm(20)
print(ans)                         #After the loop "x" is printed for the output
