string = input()
string = string.split()
for i in range(0,len(string)):
    string[i] = int(string[i])
string[:] = [-1*x for x in string]
print(string)