def AddRemove(original, add, remove):
    return (list(set(original).union(set(add)).difference(set(remove))))

#I chose to convert from list to a set as a set doesn't contain duplicates of data
originalList =  list(['one', 'two', 'three',])
addToList = list( ['one', 'two', 'five', 'six'])
deleteFromList = list(['two', 'five'])

print("Original list:\t" + str(originalList))
print("Result:\t" +  str(sorted((AddRemove(originalList, addToList, deleteFromList)),key=lambda item:(len(item),item),reverse=True)))
