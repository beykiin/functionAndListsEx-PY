# NORMAL LİSTE
# listem=["ahmet",123,123.123]
# print(listem)
# listem.append(34) 
# print(listem)
# listem.pop()
# print(listem)

# listem.insert(1,10)
# print(listem)
# listem=[1,2,5,8,7,9,4,6,5,87,2,1,0]
# listem.sort()
# print(listem)
# listem.reverse()
# print(listem)
# listem.sort(reverse=True)
# print(listem)
# print(listem.index(87))
# print(listem.__contains__(1))
# print(listem.count(1))
# listem=["ahmet","pancar","Baki","umut","Osman"]
# listem.sort()
# print(listem)
# listem.remove("Osman")
# print(listem)
# listem.extend(["Kaan","kenan","burak"])
# print(listem)
# liste2=listem.__add__(["davut"])

# print(liste2)
# liste2=listem.copy()
# print(liste2)
# x=listem.pop(0)
# print(listem)
# print(x)
# listem[3]="123"
# print(listem)

# tuple list
# tList=(1,23,55,68,55,74,32,1,2,45)
# print(tList)
# print(len(tList))
# listem=list(tList)
# print(listem)
# listem.append(123)
# tList=tuple(listem)
# print(tList)
# print(max(tList))

# set list
# sList={34,55,4,52,48,98,87,58,45,44,47,10,22,47}
# sList2={"ahmet","pancar","Baki","umut","Osman"}
# print(sList2)
# print(sList)
# print(type(sList))
# print(sList.union({55,4}))
# print(sList.intersection({55,4}))
# print(sList.difference({55,4}))
# print(sList.symmetric_difference({55,4}))
# print(sList.issubset({55,4}))
# print(sList.isdisjoint({55,4}))
# print(sList.issuperset({55,4}))
# print(sList.pop())
# print(sList)

# dict list
# dList={
#     "name":"Ahmet",
#     "age":25,
#     "city":{"il":"İstanbul",
#             "ilçe":"bayrampaşa"}}
# print(dList["name"])
# print(dList["city"]["ilçe"])
# dList["renk"]="kırmızı"
# print(dList)
# dList.pop("renk")
# print(dList)
# dList["city"]["renk"]="kırmızı"
# print(dList["city"])
# dList["city"].pop("renk")
# print(dList["city"])
# dList["name"]="pancar"
# print(dList)

# Klavyeden 0 girilene kadar sayısal değer alın ve girmiş olduğunuz değerleri çift ve tek olarak ayrı bir şekilde tutun kullanıcı sıfıra bastıktan sonra tek ve çiftleri ekranda gösterin

# cift=[]
# tek=[]
# while True:
#     sayi=int(input("Çıkmak için 0 giriniz. Devam etmek için lütfen sayı giriniz: "))
#     if sayi%2==0:
#         cift.append(sayi)
#     else:
#         tek.append(sayi)
#     if sayi==0:
#         print(f"Girdiğiniz çift sayılar: {cift}\nGirdiğiniz tek sayılar: {tek}")
#         break


# tek=[]
# cift=[]
# while True:
#     sayi=int(input("Lütfen bir sayı giriniz: "))
#     if sayi<0:
#         print("Negatif sayı kullanılamaz.")
#     if sayi==0:
#         break
#     elif sayi>0 and sayi%2==0:
#         cift.append(sayi)
#     else:
#         tek.append(sayi)

# print(f"\nGirdiğiniz çift sayılar: {cift}\nGirdiğiniz tek sayılar: {tek}")

# Klavyeden alınan değerin uzunluğu çift ise bu değerin yarısını alıp klavyeden alınan başka değeri ilave edin ve bu oluşan yeni değerin harflerinde kaç adet a olduğunu gösterin tek ise yarısını alın ve içerisinde kaç adet p olduğunu gösteren programı yazınız

girdi=input("Lütfen birşeyler yaz: ")
metin=[]
if len(girdi)%2==0:
    for i in range(int(len(girdi)/2)):
        metin.append(girdi[i])
    girdi2=input("Lütfen bir şeyler daha yaz: ")
    metin.extend(list(girdi2))
    print(metin.count("a"))
else:
    for i in range(int(len(girdi)/2)):
        metin.append(girdi[i])
    print(metin.count("p"))




