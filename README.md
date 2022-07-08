<b>python command</b>
- 관리자 권한으로 실행 `conda prompt`
- check libraries : `pip list`
- upgrade
```python
conda update conda
conda update anaconda
conda update spyder
python -m pip install --upgrade pip   # upgrade pip to the latest version
```
- install package
  - `python -m pip install <package-name>`
  - `python -m pip install --user <library>`  # 관리자 권한으로 설치
  - `conda install -c quantopian geopandas`
- uninstall and install to change version
```python
!pip uninstall torch
!pip install torch==1.11.0
import torch
torch.__version__
```
- check version
```python
import geopandas as gpd
gpd.__version__
```

---
<b>Spyder shortcut</b>
- ctrl 1 : 1 line block
- ctrl 4 : multi lines block
- ctrl 5 : unblock

---
<b>library</b>
- tqdm
  - 진행상황을 표시하는 바
  - 반복문에서 사용하면 어느정도로 진행했는지 알 수 있어서 좋음
- re
  - 분석을 위해 문자열 리스트 정형화
  - 공백문자 제거, 필요 없는 문장 부호 제거, 대소문자 맞추기 : `re.sub('[!#?]','',value)`
  - `문자열.strip()` : 문자열에서 양쪽 끝에 있는 공백과 \n 기호를 삭제, 중간에 존재하는 것은 제거 X
  - `문자열.title()` : 첫 글자 대문자

