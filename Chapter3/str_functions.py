name="hello deekshith"

print(len(name))

print(name.endswith("ith"))

print(name.startswith("Dee"))

print(name.capitalize())


print(name.upper()) #→ Converts string to uppercase.


print(name.replace("hello","Sandeep"))


#Case Conversion

str.upper(name) #→ Converts string to uppercase.

str.lower() #→ Converts string to lowercase.

str.title() #→ Capitalizes first letter of each word.

str.capitalize()# → Capitalizes first letter of the string.

str.swapcase() #→ Swaps uppercase ↔ lowercase.

#Searching

str.find(name)# → Returns index of first occurrence of name (or -1 if not found).

str.rfind(name) #→ Returns index of last occurrence of name.

str.index(name) #→ Like find(), but raises ValueError if not found.

str.count(name) #→ Returns number of occurrences of name.

#Replacing & Modifying

str.replace(e,k) #→ Replaces all occurrences of old with new.

str.strip() #→ Removes leading/trailing whitespace.

str.lstrip() #→ Removes leading whitespace.

str.rstrip() #→ Removes trailing whitespace.

#Splitting & Joining

str.split(sep) #→ Splits string into list using sep (default: whitespace).

str.rsplit(sep) #→ Splits from the right side.

str.splitlines() #→ Splits string into lines.

sep.join(list) #→ Joins list elements into a string with separator sep.

#Checking Content

str.isalpha() #→ True if all characters are alphabets.

str.isdigit() #→ True if all characters are digits.

str.isalnum() #→ True if all characters are alphanumeric.

str.isspace() → True if string contains only whitespace.

str.isupper() → True if all characters are uppercase.

str.islower() #True if all characters are lowercase.

str.istitle() #True if string follows title case.

#Formatting

str.format() #Formats string with placeholders.

f"{}" #f-strings (modern formatting).

str.zfill(width) #Pads string with zeros to given width.

str.center(width) #Centers string in given width.

str.ljust(width) #Left-aligns string.

str.rjust(width) #Right-aligns string.