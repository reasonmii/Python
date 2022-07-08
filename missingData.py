

# 결측값
.fillna(0) : 0으로 표
.fillna('missing')
.fillna(method = 'ffill')  # 바로 앞 값으로 표시
.fillna(method = 'pad') 
.fillna(method = 'bfill')  # 바로 뒤 값으로 표시
.fillna(method = 'backfill') 
# 앞/뒤 방향으로 결측값 채우는 회수를 제한
.fillna(method='ffill', limit=number)
.fillna(method='bfill', limit=number)
# 변수 별 평균값
df.fillna(df.mean())
df.where(pd.notnull(df), df.mean(), axis='columns')
df.fillna(df.mean()['C1'])   # C1 컬럼 평균값으로 모든 결측값 대체
df.mean()['C1':'C2']         # C1,C2 각각 평균값으로 C1,C2 결측값만 대체
# 다른 변수 값으로 대체
df['C2_New'] = np.where(pd.notnull(df['C2']) == True, df['C2'], df_2['C1'])



