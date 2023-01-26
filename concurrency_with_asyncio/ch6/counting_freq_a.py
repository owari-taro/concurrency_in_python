import time
freqs={}

with open("data/googlebooks-eng-all-1gram-20120701-a","r")as reader:
    
    st=time.time()
    count=0
    for line in reader:
        if count%10_000==0:
            print(freqs)
        count+=1
        data=line.split("\t")
        word=data[0]
        count=int(data[2])
        if word in freqs:
            freqs[word]=freqs[word]+count
        else:
            freqs[word]=count
    end=time.time()

    print(f"{end-st}")
    

