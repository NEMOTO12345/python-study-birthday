# 1.名前を入力させる
name = input('名前を入力してください→')
# 2.生年月日を入力させる
birth_year = int(input('誕生日の西暦を入力してください→'))
birth_month = int(input('誕生日の月を入力してください→'))
birth_day = int(input('誕生日の日を入力してください→'))
# 3.出力
# ①ーさんはー曜日生まれ。
# ②ーさんはー日生きています。
# ③ーさんの10000日の記念日はー年ー月ー日です。
# ④ーさんの今日の運勢はーです。

import datetime
import random

weekdays = ['月','火','水','木','金','土','日']
today = datetime.date.today()
birth = datetime.date(birth_year,birth_month,birth_day)
anv = birth + datetime.timedelta(days=10000)
anv_list = (str(anv).split('-'))
fortune = ['恋愛運','金運','総合運','仕事運']
fortunetoday = random.choice(fortune)


lifelen = today - birth
# ①
print(name,'さんは',weekdays[birth.weekday()],'曜日生まれです。',sep='')
# ②
print(name,'さんは',lifelen.days,'日生きています。',sep='')
# ③
print(name,'さんの10000日の記念日は',anv_list[0],'年',anv_list[1],'月',anv_list[2],'日生きています。',sep='')
# ④
print(name,'さんの運勢は',fortunetoday,'上昇です。',sep='')

