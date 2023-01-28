name_user = input()
print("Имя:" + name_user)
lastname_user = input()
print("Фамилия:" + lastname_user)
age_user = int(input())
print("Год рождения:", age_user)

if age_user <= 2000:
    print("Выпускник")
elif 2000 < age_user <= 2002:
    print("4 курс")
elif 2002 < age_user <= 2003:
    print("3 курс")
elif 2003 < age_user <= 2004:
    print("2 курс") 
elif 2004 < age_user <= 2005:
    print("1 курс") 
else :
    print("Абитуриент")  

