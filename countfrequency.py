List1=["adi","rahul","adi","ram","rahul","adi","zen","ram"]
freq={}
for name in List1:
    if name not in freq:
        freq[name]=1
    else:
        freq[name]+=1
print(freq)