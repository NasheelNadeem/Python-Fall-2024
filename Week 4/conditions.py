"""
def is_equilateral (a,b,c):
    if a==b and b==c and c==a:
        return "Yes"
    else:
        return "No"
    
def main():
    a=1
    b=1
    c=1
    msg= is_equilateral(a,b,c)
    print(msg)

main()
"""
def grades(marks):
    if marks>90:
        print("Student achieved grade A")
    else:
        print("Student did not achieve grade A")
    
def main():
    student1marks=int(input("Student 1 Marks: "))
    grades(student1marks)

    student2marks=int(input("Student 2 Marks: "))
    grades(student2marks)
    
    student3marks=int(input("Student 3 Marks: "))
    grades(student3marks)
main()
