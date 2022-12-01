pickle : 파이썬의 모든 object를 있는 그대로 저장</br>
ex) tensor는 tensor 형태로 저장됨

```
!pip install --upgrade pandas==1.4.4

import pickle

data.to_csv('fileName.pkl')
data = pd.read_pickle('fileName.pkl')
```

