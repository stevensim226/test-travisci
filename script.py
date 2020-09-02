print("Hello World!")
print("This is from Travis CI!")
print(11 + 11)

try:
    import numpy
except:
    print("Cannot import numpy")
else:
    print("Successfully imported numpy")