import fileinput

inputData = ""
counter = 0

for line in fileinput.input():
    inputData += line
    counter += 1
    if (counter == 2):
        break
    
size, arr = inputData.splitlines()

arr = arr.split( )

print(max(set(arr), key = arr.count))

