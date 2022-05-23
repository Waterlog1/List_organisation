cars= [ "bmw", "toyota", "vauxhall", "mercedes"]
cars.sort()
print(cars)

# The above .sort() method allows for a list to be sorted alphabetically (assuming they all the cases e.g lower/upper). List will the become cars= ["bmw" , "mercedes", "toyota", "vauxhall"]#
# Using the sort method is permanate and the order can not be changed after.
# The below .sort(reverse=True) allows a list to be sorted in reverse alpahbetical order#

cars= ["bmw", "toyota", "vauxhall", "mercedes"]
cars.sort(reverse=True)
print(cars)

cars= [ "bmw", "toyota", "vauxhall", "mercedes"]

print("\nHere is the original list:")
print(cars)
# Using SORTED to sort a list alphabetically is only temporary but then it can be reverted back as seen below. This is not the same for using sort.

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

# if wanted to sort items into for example order that the cars were owned you can use the reverse() method. This literally reverses the current order# Example below
cars= [ "bmw", "toyota", "vauxhall", "mercedes"]
print (cars)

cars.reverse()
print(cars)

# Using the len function to figure out the length of a list#

cars= [ "bmw","toyota", "vauxhall", "mercedes"]
print(len(cars))

