# To-Be-Data-Engineer  
  
  
## 설명
- 아래 링크의 사용자 activity 로그를 활용해 요구하는 값을 구하는 Spark Application 을 작성하세요.
- https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store

#### 1. 해당 전체 기간에서, KST 기준으로 active user 수가 제일 큰 날짜를 구하세요.  

- UTC 기준 event_time -> KST 기준으로 변환
- user_session 기준 DAU 계산  
  
  
#### 2. 1의 날짜에서, 가장 긴 세션 10개에 대해 "user_id, session_id, 세션시간"를 구하세요.
