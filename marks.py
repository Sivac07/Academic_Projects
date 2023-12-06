def grace_mark(m1 , m2):
    m1 += 10
    m2 += 20
    return m1, m2
m1 = int(input("Enter the Mark 1: "))
m2 = int(input("Enter the Mark 2: "))
updated_m1, updated_m2 = grace_mark(m1, m2)
print(f"The mark of M1 = {updated_m1} and M2 = {updated_m2}")
