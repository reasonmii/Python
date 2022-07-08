<b>Python Practice</b>
- Basic Practice : http://codingbat.com/python 
- More Mathematical Practice : https://projecteuler.net/archives 
- List of Practice Problems : http://www.codeabbey.com/index/task_list 
- A SubReddit Devoted to Daily Practice Problems : https://www.reddit.com/r/dailyprogrammer
- A very tricky website with very few hints and touch problems (Not for beginners but still interesting) : http://www.pythonchallenge.com/

---
<b>Web Frameworks for Python</b>
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - Create web pages with Python (HTML, CSS)
  - It uses decorators function a lot
- [Django](https://www.djangoproject.com/) : Building apps more quickly and with less code

---
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
<b>Anaconda</b>
- 데이터사이언스와 머신러닝 분야에서 파이썬을 사용하기 위해 기본적으로 설치하는 배포판
- 파이썬 설치 후 여러 패키지들을 따로 설치하지 않아도 되고 윈도우즈 환경에서 쉽게 가상환경을 만들어 버전 관리를 할 수 있는 유일한 도구
  - 웹사이트 :  https://www.anaconda.com/
  - 구글검색 : Anaconda Python → Download
- SciPy, Numpy, Matplotlib, Pandas 등을 비롯한 1400 패키지들 포함
- Spyder : 수십, 수 백, 수천 줄 코딩할 때 주로 사용
- Jupyter Notebook : 간단한 탐색적 분석할 때 주로 사용 (R, spark 사용 할 때 포함)

<b>Anaconda Navigator</b>
- UI 클라이언트로서 하부 컴포넌트를 쉽게 사용하도록 한 데스크탑 포털 기능

<b>Spyder shortcut</b>
- ctrl 1 : 1 line block
- ctrl 4 : multi lines block
- ctrl 5 : unblock
