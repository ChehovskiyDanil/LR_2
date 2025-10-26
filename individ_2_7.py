import math

temp=[]
hour=float(0)
minute=float(0)
angle=float(input("Введите занчение угла чаовой стрелки в пределах 0 < y < 27: "))
if not (0<angle<27):
    print("не верный тип значений")
else:

    for hour in range(24):
        for minute in range(60):
            hour_angle=30*hour+0.5*minute
            minute_angle=6*minute
            dif=abs(hour_angle-minute_angle)
            if dif == angle:
                temp.append((hour,minute))

if temp:
    print("Время, при которых угол равен заданому: ")
    for hour, minute in temp:
        print(hour,":", minute)
else:
    print("Нет времени, при котором угол равен заданому")