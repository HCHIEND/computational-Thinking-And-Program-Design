#1
num = int(input('請輸入座號:'))

ans_1 = num // 5
if(num % 5 != 0):
    ans_1 = ans_1 + 1

print("第" + str(ans_1) + "組")

#2
half = int(input('請輸入半徑:'))

ans_2_1 = half * half * 3.14
ans_2_2 = (half + half) * 3.14

print("圓面積為"+str(ans_2_1))
print("圓周長為"+str(ans_2_2))

#3
c = int(input('請輸入攝氏溫度:'))

ans_3 = c * 9 / 5 + 32

print("華氏溫度為"+str(ans_3))

#4
top = 300
bottom = 350
vest = 200

top_n = int(input('欲購買上衣數量:'))
bottom_n = int(input('欲購買上衣數量:'))
vest_n = int(input('欲購買上衣數量:'))

ans_4 = top * top_n + bottom * bottom_n + vest * vest_n

print("訂購服裝總金額為"+str(ans_4))

#5
bottle = 20
dozen = 200

bottle_n = int(input('欲購買飲料數量:'))

ans_5 = bottle_n // 12 * 200 + bottle_n % 12 * 20

print("總金額為"+str(ans_5))

#6
score_1 = int(input('第一次期中考成績為:'))
score_2 = int(input('第二次期中考成績為:'))
score_3 = int(input('期末考成績為:'))

ans_6_1 = score_1 + score_2 + score_3
ans_6_2 = ans_6_1 / 3

print("成績加總為"+str(ans_6_1))
print("成績平均為"+str(ans_6_2))
