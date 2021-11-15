"""
4. 1의 날짜에서 view → cart → purchase 이벤트 진행에 따른 funnel 수치를 구하세요
"""

import pandas as pd

# read csv file
hd_df = pd.read_csv('hot_day.csv')

# 자료형 변환
hd_df['kst_time'] = pd.to_datetime(hd_df['kst_time'])

# 필요한 컬럼만 분리
sep_hd_df = hd_df[['kst_time', 'event_type', 'user_session']].copy()

# 시간 기준 세션과 이벤트 타입에 따라 그룹핑
grouped = sep_hd_df.groupby(['user_session', 'event_type'])["kst_time"].min()

# funnel step 생성
funnel_steps = pd.DataFrame({'steps': [1,2,3]}, index = ['view', 'cart', 'purchase'])

# 이벤트 타입 기준 funnel step과 merge
grouped = pd.DataFrame(grouped).merge(funnel_steps, left_on = 'event_type', right_index = True)

# funnel 제작
funnel = grouped.reset_index().pivot(index='user_session', columns = 'steps', values = 'kst_time')
funnel.columns = funnel_steps.index

# funnel 수치 계산
step_values = [funnel[column].notnull().sum() for column in funnel.columns]