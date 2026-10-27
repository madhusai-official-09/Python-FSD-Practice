# Write a Python program to identify all vowels in a given string and reverse their positions while keeping all consonants in their original positions.
# Input:
# Output:
# Original string: education
# Vowels: euaio
# Reversed vowels: oiaue
# Result: odicatuen

s = "education"
vowels = "aeiouAEIOU"
org_vowel = ""
rev_vowel = ""
result = ""
for i in s:
    if i in vowels:
        org_vowel += i
for i in org_vowel:
        rev_vowel = i + rev_vowel
c_rev = rev_vowel
for i in s:
    if i in vowels:
        result += c_rev[0]
        c_rev = c_rev[1:]
    else:
        result += i
print(f"Original string: {s}")
print(f"Vowels: {org_vowel}")
print(f"Reversed Vowels: {rev_vowel}")
print(f"Result: {result}")