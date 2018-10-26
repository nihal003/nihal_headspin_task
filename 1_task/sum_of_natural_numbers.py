
sum=0 #Initialize variable "sum" as 0.

for i in range(4,1000): #variable "i" is given in a loop from 4 to 1000 to check if it is divisible by 5 or 4
    if i%5==0 or i%4==0:
        sum=sum+i #if yes then "i" is added to "sum"
print("sum=",sum) #After the loop print the output as "sum".
