backslash_five = r"\five\ "
slashes_alive = r"'//alive\\'"

print('one', end=', ')
print("'two'", end=', ')
print('"three"', end=', ')
print('four', end=", ")
print(f"{backslash_five}\n\tonce", end=', ')
print(f"'I' caught a fish \n\t\t{slashes_alive}")


"""
OTHER SOLUTION
"""

print('One, \'two\', \"three\", four, \\five\\\n\tonce,\'I\' caught a fish\n\t\t\'//alive\\\\\'')