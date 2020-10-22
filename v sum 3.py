n=list(input().split())
ans=""
for i in range(len(n)-1):
    s=n[i]
    ans+=(s[0].upper()+'.')
ans+=n[-1].title()
print(ans)



