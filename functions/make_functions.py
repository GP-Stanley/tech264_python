def divide(a : int = 2, b: int =5)-> float:           # if you call this function without a and b, the default is used.
    return a/b

a: int = 4                                  # defined the type as an 'int'.
b: int = 6                                  # a and b both overwrite the set parameters above.

print(divide(a, b))                       # 0.6666666666666666
print(divide())