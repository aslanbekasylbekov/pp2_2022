s=input() 
t=input() 
ans=""
f=s.find(t)
if (not(f==-1)):
    ans+=str(f)  
r=s.rfind(t) 
if (not(r==f) and r!=-1):
    ans+=" "
    ans+=str(r)
if ans!=0:
    print (ans)