def prime(i):
    prime=[]
    while i!=1:
        if i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%6!=0 and i%7!=0 and i%8!=0 and i%9!=0 and i%10!=0 :
            prime.append(i)
        i -= 1
    return prime

def listed(i, n):
    list=[]
    while i:
        if i%n==0:
            break
        i -= 1
    while i:
        list.append(i)
        i-=n
    return list

chances=7
def binary_search(list):
    print(list)
    bottom=0
    top=len(list)-1
    a=search(bottom, top, chances)
    return a
    
def search(bottom, top, chances):
    mid=(bottom+top)//2
    print(mid)
    print("The number you have guessed is:",list[mid])
    chances -= 1
    print("Number of chances left is:",chances)
    if chances==0:
        print("Sorry, I lose, can I try again")
        exit()
    feedback=input("If the number printed above is correct then enter 'c', if your number is greater than the given number then enter 'h' else enter 'l': ")
    if feedback=='c':
        print("The number you have guessed is:", list[mid])
        print("Thank You")
        exit()
    elif feedback=='l':
        bottom=mid+1
        search(bottom, top, chances)
    elif feedback=='h':
        top = mid-1
        search(bottom, top, chances)
    else:
        print("Invalid input")
        search(bottom, top, chances)
    return feedback

range=input("Please enter the range between which you would be selecting your number, NOTE:1 is not part of your range (Example: 100): ")
if range.isdigit():
    x=1
else:
    print("Invalid entry")
    range=input("Please enter the range between which you would be selecting your number (Example: 100): ")

print("Think of a number between your selected range, I'll guess it within 7 chances")
hint=input("Please enter any one number between 2-10 which divides the number you have guessed, else enter p: ")

if hint=='p' or hint=='P':
    list=prime(int(range))
else:
    list=listed(int(range), int(hint))

b=binary_search(list)