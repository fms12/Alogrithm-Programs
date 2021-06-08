def prime(n):
    isprime =[True for i in range(n+1)]
    p=2
    while(p*p<=n):
      if(isprime[p]==True):
        for j in range(2*p,n,p):
          isprime[j] = False
      p+=1
    for k in range(2,n+1):
      if(isprime[k]):
        print(k)    



n=int(input())
prime(n)


