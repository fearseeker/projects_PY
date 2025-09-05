while True:
    try:
        a = int(input("введить першу сторону: "))
        b = int(input("введить другу сторону: "))
        c = int(input("введить третю: "))
        if a <= 0 or b <= 0 or c <= 0:
            print("Сторона не може бути меньше або 0")
            continue
        break
    except ValueError:
        print("Введить ціле число")
nums = [a,b,c]
def Istriangl(nums):
    if (nums[0]*nums[0]) + (nums[1]*nums[1]) == nums[2]*nums[2] or (nums[1]*nums[1]) + (nums[2]*nums[2]) == nums[0]*nums[0] or (nums[2]*nums[2]) + (nums[1]*nums[1]) == nums[0]*nums[0]:
        print(bool(1))
    else:
        print(bool(0))
Istriangl(nums)