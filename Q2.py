"""
2. 1의 날짜에서, 가장 긴 세션 10개에 대해 "user_id, session_id, 세션시간"를 구하세요
"""

import pandas as pd

# read csv file
hd_df = pd.read_csv('hot_day.csv')

# 자료형 변환
hd_df['kst_time'] = pd.to_datetime(hd_df['kst_time'])

# 시간 기준 가장 마지막에 찍힌 세션
max_grouped = hd_df.groupby(['user_session', 'user_id'])['kst_time'].max()
max_time_df = pd.DataFrame(max_grouped)
max_time_df.columns = ['latest']

# 시간 기준 가장 처음에 찍힌 세션
min_grouped = hd_df.groupby(['user_session', 'user_id'])['kst_time'].min()
min_time_df = pd.DataFrame(min_grouped)
min_time_df.columns = ['start']

# 세션 시간 계산
new_df = pd.concat([max_time_df, min_time_df], axis = 1)
new_df['session_time'] = new_df['latest']-new_df['start']

# 세션 시간 기준 상위 10개 분리
new_df.sort_values(by=['session_time'], axis=0, ascending=False, inplace=True)
result = new_df.drop(['latest', 'start'], axis = 1)
result = result[:10]