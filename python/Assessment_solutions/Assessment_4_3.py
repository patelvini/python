def permutationFun(lst):
    if len(lst) == 0: # if input is empty
        return []
    
    if len(lst) == 1: # if string has only one character
        return [lst]
    
    l = [] # empty list to store current permutation
    
    for i in range(len(lst)):
        m = lst[i] # iterate the input
        remLst = lst[:i] + lst[i+1:] # Extract remaining list 

        for p in permutationFun(remLst): #generate all permutation where m is 1st element
            print(p)
            l.append([m] + p)

    return l


str = input("Enter a string : ")
data = list(str)
set1 = set()
for p in permutationFun(data):
    temp = (''.join(p))
    set1.add(temp)          # remove duplicate entries

for i in set1:
    print(i)
