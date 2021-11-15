"""
3. 1의 날짜의 15분단위로 active user 수를 구하세요
"""

import pandas as pd

# read csv file
hd_df = pd.read_csv('hot_day.csv')

# 자료형 변환
hd_df['kst_time'] = pd.to_datetime(hd_df['kst_time'])

# 15분 단위로 분리
def cut_15(date):
    hour, minute = date.hour, date.minute
    if hour < 10:    hour = '0'+str(hour)
    else: hour = str(hour)
        
    if 0 <= minute < 15:
        return hour+':00:00-'+hour+':14:59'
    elif 15 <= minute < 30:
        return hour+':15:00-'+hour+':29:59'
    elif 30 <= minute < 45:
        return hour+':30:00-'+hour+':44:59'
    elif 45 <= minute < 60:
        return hour+':45:00-'+hour+':59:59'
    else:
        return 'NaN'

quarter_list = []
for date in hd_df['kst_time']:
    quarter_list.append(cut_15(date))
hd_df['quarter_time'] = quarter_list

# 필요한 컬럼만 분리
new_hd_df = hd_df[['quarter_time', 'user_session']].copy()
result = new_hd_df.drop_duplicates()
result = result.groupby(['quarter_time']).size()