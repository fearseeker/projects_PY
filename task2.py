while True:
    try:
        a1 = int(input("перше число: "))
        b1 = int(input("друге число: "))
        c1 = int(input("третє число: "))
        d1 = int(input("четверте число: "))
        nums1 = [a1, b1, c1, d1]

        if a1 <= 0 or b1 <= 0 or c1 <= 0 or d1 <= 0:
            print("число не може бути меньше або 0")
            continue
        break
    except ValueError:
        print("Введить ціле число")
print("ви створили масив захисників")

while True:
    try:
        a2 = int(input("перше число: "))
        b2 = int(input("друге число: "))
        c2 = int(input("третє число: "))
        d2 = int(input("четверте число: "))
        nums2 = [a2, b2, c2, d2]
        if a2 <= 0 or b2 <= 0 or c2 <= 0 or d2 <= 0:
            print("число не може бути меньше або 0")
            continue
        break
    except ValueError:
        print("Введить ціле число")
print("ви створили масив атакуючих")

for i in range(len(nums1)):
    if nums1[i-1] == 0:
        nums1.remove(0)
for o in range(len(nums2)):
    if nums2[o-1] == 0:
        nums2.remove(0)
i=0
z=0
p=0
if len(nums1) > len(nums2):
    p+= len(nums1) - len(nums2)
else:
    z+= len(nums2) - len(nums1)
while True:
    if i >= len(nums2) or i >= len(nums1):
        break
    if nums1[i] > nums2[i]:
        p+=1
    elif nums1[i] == nums2[i]:
        p+=1
        z+=1
    else:
        z+=1
    i+=1
if z == p:
    if sum(nums2) > sum(nums1):
        z+=1
    elif sum(nums1) == sum(nums2):
        z+=1
        p+=1
    else:
        p+=1
if p>z or p==z:
    print(bool(1))
else:
    print(bool(0))
