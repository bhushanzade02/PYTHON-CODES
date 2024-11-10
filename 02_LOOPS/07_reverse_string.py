"""Reversing a String: Use a for loop to reverse a string provided by the user."""

bhus=input("enter a string")

reversed=""

for char in bhus:
    reversed=char+reversed


print(reversed)

