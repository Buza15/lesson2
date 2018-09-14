def task1():
    pass

a = int(input("Enter a number: "))
c = input("choose into (b) or into (k): ")

if c == 'b':
    print("%d Байт = %d Килобайт" % (a, a*1024))
elif c == 'k':
    print("%d Килобайт = %d Байт" % (a, a/1024))

print('#####' * 10)

    
def task2():
    pass
    
n = int(input("Enter a number: "))
s = 0
m = 1
while n > 0:
    s += n%10
    m *= n%10
    n = n//10

print("Summ: ", s)
print ("Multiply", m)

def task3():
    pass


def task4():
    pass


def task5():
    pass
