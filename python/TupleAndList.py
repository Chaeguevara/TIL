#tuple
te=()
t = (2,"mit",3)
print(t)
print(t[0])
print((2,"mit",3)+(5,6))
print(t[1:2])
print(t[1:3])
print(len(t))
#t[1] = 4

# swap data
x= "Hi, there"
y = "Hello, there"
print("x: " + x + '\n' +
     "y: " + y + '\n')
(x,y) = (y,x)

print("After swap data... \n" + 
      "x: " + x + '\n' +
     "y: " + y + '\n')

def quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    return (q, r)

(quot, rem) = quotient_and_remainder(4,5)
print("Print quotient and remainder by 4/5: \n"+
      "Quotient: " + str(quot) +'\n'+
      "Remainder: " + str(rem) +'\n')

def get_data(aTuple):
    nums = ()
    words =()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

aTuple = ((1,'a'),(2,'b'),(3,'c'),(4,'c'),(5,'b'))

print("aTuple: " + str(aTuple) + '\n'+
      "min_n: " + str(get_data(aTuple)[0]) + '\n' +
      "max_n: " + str(get_data(aTuple)[1]) + '\n' +
      "unique_words: " + str(get_data(aTuple)[2]) + '\n')

L =[1,2,3,4,5,6,7,8,9,10]

total = 0
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L:
    total += i
print(str(total)+'\n')

L1 = [2,1,3]
print ("L1: "+ str(L1))
L2 = [4,5,6]
print ("L2: "+ str(L2))
L3 = L1 + L2
print ("L3 = L1 + L2 \n"+ str(L3))
L1.extend([0,6])
print("L1 = L1.extend([0,6]) \n" + 
      "Now L1 = " + str(L1))
