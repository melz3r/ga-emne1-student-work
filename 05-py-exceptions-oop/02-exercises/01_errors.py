#int("two") - returns ValueError, as "two" can never be an integer
print(2)

#3 + " tickets" - returns TypeError, as you can only concatenate str (not "int") to str
print("3" + " tickets")

#[10, 20][2] - returns IndexError, as the list [10, 20] has only the indices 0 and 1, so index 2 does not exist - it is out of range.
print([10, 20][1])


