job = "software developer"
freq = {}  #create a dictionary
for i in job:
    if(i in freq):
        freq[i] = freq[i]+1

    else:
        freq[i] = 1

print(freq)

