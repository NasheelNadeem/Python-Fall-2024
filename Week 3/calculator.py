PI= 3.14159
def circumference(radius):
    
    c=2 * PI * radius
    return c

def area(radius):
    a=PI * (radius*radius)
    return a
def main():
    radius=float(input("Enter radius of circle: "))
    t=area(radius)
    x=circumference(radius)
    print("area is",t,"circumference is",x)

main()






