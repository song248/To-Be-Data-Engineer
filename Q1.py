"""
1. 해당 전체 기간에서, KST 기준으로 active user 수가 제일 큰 날짜를 구하세요
"""
import pandas as pd
from datetime import datetime, timedelta

# read csv file
commerce_df = pd.read_csv('C:/Users/songtg/Desktop/DE/2019-Nov.csv')

# 필요한 컬럼만 사용
new_commerce_df = commerce_df[['event_time', 'event_type', 'user_id', 'user_session']].copy()

# KST 변환
kst_list = []
for time in new_commerce_df['event_time']:
    kst_list.append(time[:19])
new_commerce_df['kst_time'] = kst_list
new_commerce_df['kst_time'] = pd.to_datetime(new_commerce_df['kst_time'])
new_commerce_df['kst_time'] = new_commerce_df['kst_time'] + timedelta(hours=9)
new_commerce_df.drop(['event_time'], axis = 1, inplace=True)

# 일자별 분류
kst_day = []
for time in new_commerce_df['kst_time']:
    kst_day.append(time.day)
new_commerce_df['kst_day'] = kst_day

# DAU가 가장 많은 날 result에 저장
day_df = new_commerce_df[['kst_day','user_session']]
result = day_df.drop_duplicates()
grouped = result.groupby(['kst_day']).size()
result = grouped.index[grouped== max(grouped)][0]