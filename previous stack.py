l=[2,5,3,7,8,1,9]
st=[]
b=[]

for i in range(len(l)):

    while(len(st)>0 and l[i]<st[-1]):
        st.pop()

    if(len(st)==0):
        b.append(-1)
    else:
        b.append(st[-1])

    st.append(l[i])

      
   

print(b)
    


