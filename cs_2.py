# n = 100
# for i in range(1,n+1):
#     num = i
#     temp = i
#     count = 0
#     while i>0:
#         i//=10
#         count+=1
#     d = 10**(count-1)
#     power_cnt = 0
#     s = 0
#     while temp>0:
#         digit = temp//d
#         power_cnt+=1
#         power=digit**power_cnt
#         s+=power
#         temp=temp%d
#         d=d//10
#     if s==num:
#         print(num)



# n = 30
# for i in range(1,n+1):
#     s = 0
#     num = i
#     while i>0:
#         d = i%10
#         s+=d
#         i//=10
#     if num%s==0:
#         print(num)

# rows = 5
# s = 0
# for i in range(1,rows+1):
#     s+=i
#     num =s 
# for i in range(1,rows+1):
#     for j in range(1,rows-i+2):
#         print(num,end=" ")
#         num-=1
#     print()

# rows = 5
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(chr(64+j),end="")
#     print()
