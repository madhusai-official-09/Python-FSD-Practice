# 1. Most frequent element
''' x = [[10,20,30],[20,40,10],[50,20,30],[60,10,20]]
z = []
for i in range(0,len(x)):
    temp = x[i]
    for j in temp:
       z.append(j)
f = 0
for k in z:
    cnt = z.count(k)
    if cnt>f:
        f = cnt
        num = k
print("Element: ",num)
print("Frequency: ",f) '''
   
# 2. Sort dictionary by values descending 
''' dic = {"A":45,"B":80,"C":25,"D":60,"E":90}
li = list(dic.items())
for i in range(0,len(li)-1):
    for j in range(i+1,len(li)):
        if li[i][1]<li[j][1]:
            li[i],li[j] = li[j],li[i]
res ={k:v for k,v in li}
print(res) '''

# 3. First repeating element
''' def firstrepeatingnumber(li):
    for i in li:
        if li.count(i)>1:
            return i
li = [10, 25, 30, 15, 25, 40, 30]
res = firstrepeatingnumber(li)
print("First Repeating Element:",res) '''

# 4. Remove all vowels
''' def removevowels(s):
    output = ""
    vowels = "aeiouAEIOU"
    for i in s:
        if i not in vowels:
            output += i
    return output

st = "Hello World"
res = removevowels(st)
print(res) '''


