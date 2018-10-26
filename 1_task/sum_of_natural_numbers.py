#  If we list all the natural numbers below 10 that are multiples of 4 or 5, we get 4, 5, and 8. 
 # The sum of these multiples is 17. Then find the sum of all the multiples of 4 or 5 below 1000. 

sum=0                   #Initialize variable "sum" as 0.

for i in range(4,1000): #variable "i" is given in a loop from 4 to 1000 to check if it is divisible by 5 or 4
    if i%5==0 or i%4==0:
        sum=sum+i        #if yes then "i" is added to "sum"
print("sum=",sum)        #After the loop print the output as "sum".
