import  sxtwl
lunar = sxtwl.Lunar()  #实例化日历库

year = int(input("请输入年份，例：2020\n"))

ymc = [u"十一", u"十二", u"正", u"二", u"三", u"四", u"五", u"六", u"七", u"八", u"九", u"十" ]
rmc = [u"初一", u"初二", u"初三", u"初四", u"初五", u"初六", u"初七", u"初八", u"初九", u"初十",
 u"十一", u"十二", u"十三", u"十四", u"十五", u"十六", u"十七", u"十八", u"十九",
  u"二十", u"廿一", u"廿二", u"廿三", u"廿四", u"廿五", u"廿六", u"廿七", u"廿八", u"廿九", u"三十", u"卅一"]

#day = lunar.getDayBySolar(1996, 2, 12)
#
#print(u"公历:", day.y, u"年", day.m, u"月", day.d, u"日")
#if day.Lleap:
#    print(u"阴历:润", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
#else:
#    print(u"阴历:", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")

day = lunar.getDayByLunar(year, 12, 24) 
print(u"公历:", day.y, u"年", day.m, u"月", day.d, u"日")
if day.Lleap:
    print(u"阴历:润", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
else:
    print(u"阴历:", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
