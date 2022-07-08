


pd.merge(data1, data2.groupby(['STATION_ID']).sum(), on='STATION_ID', how='left')   

# data1 columnName 
# 001 이면 자전거도로유, 002면 자전거도로무로 표시
data1.loc[(data1['columnName'] == '001'), 'columnName'] = '자전거도로유'
data1.loc[(data1['columnName'] == '002'), 'columnName'] = '자전거도로무'






