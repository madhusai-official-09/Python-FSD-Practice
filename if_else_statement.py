# Write a Python program that checks if a given year is a leap year.
# year = int(input("Enter a year:"))
# res = "Leap Year" if (year%4==0 and year%100!=0) or (year%400==0) else "Not a leap year"
# print(res) 

# Write a Python program that checks if a given character is a vowel or a consonant.

ch = input("Enter a character: ")
if ch in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    print("The character is a vowel.")
else:
    print("The character is a consonant.")