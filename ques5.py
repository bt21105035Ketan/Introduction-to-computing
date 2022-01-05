Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Given list
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Removing the fourth element and printing
color.remove(color[3])
print(color)
['Red', 'Green', 'White', 'Pink', 'Yellow']
# Adding purple in place of black and pink and printing
color[3:4] = ["Purple"]
print(color)
['Red', 'Green', 'White', 'Purple', 'Yellow']
