
# 특정 경로에 있는 파일명 한 번에 바꾸기

import os

file_path = "C:/Users/User/datasets_for_practice"
print(os.listdir(file_path))

# list comprehension 사용해서 경로 내 모든 파일에 대해 절대경로 지정하기
file_path_abs = [os.path.join(file_path, i) for i in os.listdir(file_path)]

for file in file_path_abs:
    dir_path = os.path.dirname(file)                       # 경로
    file_name = os.path.basename(file)                     # 해당 경로 파일명들 차례로 가져옴
    
    # case1) 특정 글자 변경하기
    # i.e. daily_assigment_01 -> weekly_assignment_01
    file_name_new = file_name.replace("daily","weekly")    # 새로운 파일명
    os.rename(file, os.path.join(dir_path, file_name_new))
    
    # case2) 없던 글자 추가하기
    # i.e. daily_assignment.csv -> daily_assignment_final.csv
    # .을 기준으로 파일명과 확장자명 분리
    file_name_new = file_name.split(".")[0] + "_final." + file_name.split(".")[1]
    os.rename(file, os.path.join(dir_path, file_name_new))
