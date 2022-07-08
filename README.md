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

<b>Spyder shortcut</b>
- ctrl 1 : 1 line block
- ctrl 4 : multi lines block
- ctrl 5 : unblock
