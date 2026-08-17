# find the longest increasing sequence in a tuple
# output: (2,4,6,8) 
tu = (3,5,7,2,4,6,8,1,9)
n_tu = []
for i in range(len(tu)):
    for j in range(i+1, len(tu)):
        if tu[j] > tu[i]:
            n_tu.append(tu[i:j+1])
        else:
            n_tu.clear()
print(n_tu)
