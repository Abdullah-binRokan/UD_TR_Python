# Write your function definition here
def start_K(string):
    if string[0] == "K":
        return True
    else:
        return False

        #------Shorter solution----
        #----------------------
        # return string[0] == "K"
        #----------------------

# A function call like this should return True:
print(start_K("Kelly"))

# And one like this should return False:
print(start_K("Abe"))
