# 1.名前を入力させる
name = input('名前を入力してください→')
# 2.生年月日を入力させる
birth_year = input('誕生日の西暦を入力してください→')
birth_month = input('誕生日の月を入力してください→')
birth_day = input('誕生日の日を入力してください→')
# 3.出力
# ーさんはー曜日生まれ。
# ーさんはー日生きています。
# ーさんの10000日の記念日はー年ー月ー日です。
# ーさんの今日の運勢はーです。

import datetime

today = datetime.date.today()

