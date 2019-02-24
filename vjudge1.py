def find():
    a="CODEFORCES"
    b=raw_input()
    j=0
    c=0
    if(a in b):
        return "YES"
    elif(len(a)>len(b)):
        return "NO"
    else:
        for i in b:
            if(a[j]==i):
                if(a[j]=='S'):
                    return "YES"
                j+=1
            else:
                c+=1
                if(c>1):
                    d=len(b)
                    b=b[b.index(i)-1:d]
                    break
        if a[j:len(a)] in b:
            return "YES"
        
            
                
                
str=find()
if(str==None):
    print("NO")
else:
    print(str)
