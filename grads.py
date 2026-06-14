print("حاسبة الدرجات المدرسيه")
math = float (input("رجة الرياضيات : "))
arabic = float (input("درجة اللغة العربيه:"))
english = float(input("درجة اللغة الانجليزية : "))
total = math + arabic + english
average = total / 3
print (""+"="*6)
print ("تقرير الدرجات ")
print ("="*40)
print (math)
print (arabic)
print (english)
if average >=90 :
    print ("ممتاز أنت متفوق")
elif average >=80:
    print ("جيد جدا")
elif average >=70 :
    print ("جيد")
elif average >=60:
    print ("مقبول")
else : print ("راسب يابن العرص ")
