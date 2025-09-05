import datetime
def date(d,wd,rd,time):
    i=0
    result = []
    while True:
        if d <= 0:
            break
        result.append(time.strftime('%Y, %m, %d, 0, 0'))
        if i%2 > 0:
            time += datetime.timedelta(days=wd)
            d-=wd
        else:
            time += datetime.timedelta(days=rd)
            d-=rd
        i+=1
    return result

while True:
    try:
        d = int(input("введить дні: "))
        wd = int(input("введить кількість робочих днів: "))
        rd = int(input("введить кількість вихідних: "))
        if d <= 0 or wd <= 0 or rd <= 0:
            print("Днів не може бути 0 або меньше 0")
            continue
        break
    except ValueError:
        print("Введить ціле число")

time = datetime.date(year= int(input("введить рік: ")), month = int((input("введить місяць: "))), day = int(input("введить день: ")))
for l in date(d,wd,rd,time):
    print(l)
