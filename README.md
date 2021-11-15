# To-Be-Data-Engineer  
  
## 설명
- 아래 링크의 사용자 activity 로그를 활용해 요구하는 값을 구하는 Spark Application 을 작성하세요.
- https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store  
  
- **python 사용 이유:** pandas 라이브러리 사용을 위해(groupby 등 다양한 내장 함수 사용 목적)  


### 1. 해당 전체 기간에서, KST 기준으로 active user 수가 제일 큰 날짜를 구하세요.  
----  
> - UTC 기준 event_time → KST 기준으로 변환  
> - user_session 기준 DAU 계산  
![1번](https://user-images.githubusercontent.com/69496202/141769475-e5337a7e-98c1-48c4-9877-acac96b89b82.PNG)

  
----  
### 2. 1의 날짜에서, 가장 긴 세션 10개에 대해 "user_id, session_id, 세션시간"를 구하세요.  
----  
> - 1의 날짜 부분 별도 csv 파일로 저장  
> - KST변환 시간 최댓값 기준, 최솟값 기준 user_session, user_id 그룹 생성  
> - 시간 연산 후 내림차순 정렬, 상위 10개 출력  
![2번](https://user-images.githubusercontent.com/69496202/141769676-426a2841-eb3b-4f39-8a9d-a4f29b278dee.PNG)

----  
### 3. 1의 날짜의 15분단위로 active user 수를 구하세요  
----  
> - 매 시간별 15분 단위로 슬라이싱  
> - user_session 이용 그룹 생성  
![3번](https://user-images.githubusercontent.com/69496202/141769794-a0f0c13f-f7c1-41ec-9019-2ce7ddf79a10.PNG)

----  
### 4. 1의 날짜에서 view → cart → purchase 이벤트 진행에 따른 funnel 수치를 구하세요    
----  
> - view → cart → purchase 순서의 funnel steps 생성
>   >   - {view: 1, cart: 2, purchase: 3}  
>   >   
> - user_session과 event_type에 따른 그룹 생성  
> - funnel steps와 merge  
> - funnel 제작  
> - funnel 수치 계산  
> - 계산 결과에 따른 시각화  
![4번](https://user-images.githubusercontent.com/69496202/141770008-e5f74bdd-201b-481c-8222-990594202cf6.png)
