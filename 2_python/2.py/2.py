import fractions

def lcm(n):
    x=1
    for i in range(1,n+1):
        x=(x*i)/fractions.gcd(x,i)
    return x

ans=lcm(20)
print(ans)