#CGPA Calculator
course_num = int(input("Enter how many courses?: "))
cgpas = []
for i in range(course_num):
  cgpas.append(float(input(f"Enter {i+1}th cgpa: ")))
credits = []
for j in range(course_num):
  credits.append(float(input(f"Enter {j+1}th course's credit: ")))
prod = 0
for k in range(course_num):
  prod = prod + cgpas[k]*credits[k]
cgpa = prod/sum(credits)
print(f"your cgpa is: {cgpa}")
