import datetime

today_now = datetime.datetime.now()
date_ymd = today_now.strftime("%Y%m%d")
date_ymd_hm = today_now.strftime("%Y%m%d_%H%M")
backup_day_a = today_now.strftime("%A")
