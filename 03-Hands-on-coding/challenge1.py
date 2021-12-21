backslash_five = r"\five\ once"
slashes_alive = r"'//alive\\'"

print('one', end=', ')
print("'two'", end=', ')
print('"three"', end=', ')
print('four', end=", \n")
print(backslash_five, end=', ')
print(f"'I' caught a \n\tfish {slashes_alive}")