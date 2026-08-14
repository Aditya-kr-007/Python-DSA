List1=["adi","rahul","adi","ram","rahul","adi","zen","ram"]
freq={}
for i in List1:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)