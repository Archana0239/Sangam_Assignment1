name = input()
s1 = int(input())
s2 = int(input())
s3 = int(input())
total = s1 + s2 + s3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("Name:", name)
print("Total:", total)
print("Grade:", grade)