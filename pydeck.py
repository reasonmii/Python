


''' pydeck 공간데이터 시각화 라이브러리 ★★★
★ 대용량 처리 및 레더링에 적합
★ pandas.DataFrame 을 사용
   ※ mapboxgl : geojson parsing 후, 바로 데이터 값에 따른 색상, 높이 등의 시각화 요소를 다르게 할 수 있었지만, pydeck은 불가능
   만약 렌더링이 잘 안되는 경우 pandas.DataFrame 이 맞는지 우선적으로 확인할 것
★ 다양한 layer가 많음
★ layer 쌓기 가능

설명출처 : https://dailyheumsi.tistory.com/147
'''

# geojson file의 경우) data를 pandas.DataFrame으로 변경하기
import geopandas as gpd
df = gpd.read_file(data)
df.head()

# pydeck에서는 항상 geometry에 연속된 포인트들을 갖는 리스트 값 필요
# 아래와 같은 형식을 인식하지 못함
# (POLYGON ((126.9768888427482 37.57565077944879...
# 변경 작업

def multipolygon_to_coordinates(x):
    lon, lat = x[0].exterior.xy
    return [[x, y] for x, y in zip(lon, lat)]

df['coordinates'] = df['geometry'].apply(multipolygon_to_coordinates)
del df['geometry']

# 인구 별로 색 다르게 하기
# pydeck은 dataframe만 보고 렌더링 하기 때문에,
# 렌더링 전 색상, 크기 등 시각화 하고 싶은 기준들을 새로운 컬럼으로 추가해줘야 함

# 인구를 0 ~ 1 사이의 값으로 변환.
df['정규화인구'] = df['인구'] / df['인구'].max()


# =================== PolygonLayer (Choropleth) 시각화 =================== 

# Make layer
layer = pdk.Layer(
    'PolygonLayer', # 사용할 Layer 타입
    df, # 시각화에 쓰일 데이터프레임
    get_polygon='coordinates', # geometry 정보를 담고있는 컬럼 이름
    get_fill_color='[0, 255*정규화인구, 0]', # 각 데이터 별 rgb 또는 rgba 값 (0~255)
    pickable=True, # 지도와 interactive 한 동작 on
    auto_highlight=True # 마우스 오버(hover) 시 박스 출력
)

# Set the viewport location
center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


# =================== 인구 기준으로 지도에 높이를 반영해 3D로 표시 ===================
layer.extruded = True;
layer.get_elevation = '인구';
layer.elevation_scale = 0.05

view_state.bearing=15
view_state.pitch=45

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


# =================== pydeck class ===================

# pdk.Layer
# 어떤 레이어를 지도 위에 올릴 때
# id : 같은 타입의 여러 개의 레이어를 지도에 쌓는 경우, 각 레이어를 다른 id 로 설정
pdk.Layer(
    type = "미리 정의된 레이어 타입",
    id = "이 레이어의 아이디 (optional)",
    data = "pandas.DataFrame 또는 geojson url",
)


# pdk.ViewState
# 지도 렌더링할 때, 초기화 뷰에 대한 설정
pdk.ViewState(
    longitude = "중심 경도 (default 0)",
    latitude = "중심 위도 (default 0)",
    zoom = "줌 레벨 (default 0)",
    pitch = (default 0),
    bearing = (default 0),
    **kwargs,
)


# pdk.Deck
# 만들어진 레이어, 뷰 정보, 맵 스타일 등 모든 요소를 모아 출력시킬 수 있는 클래스
pdk.Deck(
    layers=[],
    views=[{"controller": true, "type": "MapView"}],
    map_style='mapbox://styles/mapbox/dark-v9',
    mapbox_key=None,
    initial_view_state={"bearing": 0, 
                        "latitude": 0.0, 
                        "longitude": 0.0,
                        "maxZoom": 20,
                        "minZoom": 0, 
                        "pitch": 0, 
                        "zoom": 1},
    width='100%',
    height=500,
    tooltip=True,
)


# =================== Point layer ===================

# 서울시내 공중화장실 데이터
geo_data = 'data/toilet_seoul_sample.geojson'

import geopandas as gpd
df = gpd.read_file(geo_data)
df['lat'] = df['geometry'].apply(lambda coord: coord.y)
df['lng'] = df['geometry'].apply(lambda coord: coord.x)
del df['geometry']

df = pd.DataFrame(df)
df.head()

# 모든 point를 지도에 그대로 출력
# pickable=True, auto_highlight=True 를 주면 위와 같이 마우스 오버시 데이터 정보 나

layer = pdk.Layer(
    'ScatterplotLayer',
    df,
    get_position='[lng, lat]',
    get_radius=50,
    get_fill_color='[255, 255, 255]',
    pickable=True,
    auto_highlight=True
)

center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()

# 이용량에 따라 색 변경
# 각 Point 의 지름 반지름 설정, 높이 설정 등은 get_radius, get_elevation 조절
df['정규화이용량'] = df['이용량'] / df['이용량'].max()
layer.get_fill_color = '[255*정규화이용량, 255*정규화이용량, 255]'

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


### Heatmap layer ===================
# 밀집도를 한 눈에 파악하기 좋음
# 밀도가 높은 곳은 더 진한 색상
# colorRange, intensity, getWeight 등의 파라미터를 통해 색상, 밀도, 가중치 설정 가능

layer = pdk.Layer(
    'HeatmapLayer',
    df,
    get_position='[lng, lat]'
)

center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


### Grid layer ===================

# 1) CPUGridLayer (GPUGridLayer)
# pydeck 에서만 제공하는 아주 강력한 레이어
# Point 들을 일정한 그리드 단위로 묶어서 표현
layer = pdk.Layer(
    'CPUGridLayer', # 대용량 데이터의 경우 'GPUGridLayer'
    df,
    get_position='[lng, lat]',
    pickable=True,
    auto_highlight=True
)

center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()

# 레고 블록처럼 높이도 추가 가능
layer.extruded = True
layer.elevation_scale = 3 # default 1

view_state.bearing = -15
view_state.pitch = 45

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()

# 2) HexagonLayer
# 위와 동일하지만 모양이 육각형
layer.type = 'HexagonLayer'

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()

# ScreenGridLayer
# 위와 동일하지만 모양이 정사각형 스크린
layer.type = 'ScreenGridLayer'
layer.cellSizePixels = 10 # default 100

view_state.bearing = 0
view_state.pitch = 0

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()

### Text layer ===================
# 데이터 Point 좌표에 텍스트를 출력
# 단, 한글은 렌더링 불가능
# only characters in the Ascii code range 32-128

df['text'] = 'text'

layer = pdk.Layer(
    'TextLayer',
    df[:100],
    get_position='[lng, lat]',
    get_text='text',
    get_color='[0, 255, 255]',
    font_family='consolas',
    sizeScale=0.5,
    pickable=True,
    auto_highlight=True
)

center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


# =================== Points (Path or Polygon) 단위 ===================
# geometry 데이터가 2개 이상의 좌표가 들어간 데이터 사용 시
# Points(Path) 단위의 레이어들은 geometry 정보가 OD, LineString(또는 Polygon, MultiPolygon) 단위의 데이터들

### OD layers ===================
# Point(Origin)와 Point(Destination) 를 연결하는 레이어

# 따릉이 OD 데이터 예시
# 출발지와 도착지의 위도, 경도를 가지고 있는 데이터

import pandas as pd

df = pd.read_csv('data/seoul_bike_sample.csv')
df.head()
df['정규화이용'] = df['이용'] / df['이용'].max()
df['정규화이용시간'] = df['이용시간(분)'] / df['이용시간(분)'].max()

# 1) LineLayer
# o-d 를 잇는 직선
# 이용 값이 클수록 선의 굵기를 굵게하고,
# 이용시간 값에 따라 색상 다르게 적용

layer = pdk.Layer(
    'LineLayer',
    df,
    get_source_position='[대여대여소경도, 대여대여소위도]',
    get_target_position='[반납대여소경도, 반납대여소위도]',
    get_width='1 + 10 * 정규화_이용',
    get_color='[255, 255 * 정규화이용시간, 120]',
    pickable=True,
    auto_highlight=True
)

# pydeck.data_utils.compute_view 는 Points 들의 경도, 위도를 리스트로 주면, 알아서 view_state 를 만들어줍니다.
view_state = pydeck.data_utils.compute_view(df[['대여대여소경도', '대여대여소위도']].values)
view_state.zoom = 13

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


# 2) ArcLayer
# o-d 를 잇는 곡선
# 이용 값이 클수록 선의 굵기를 굵게하고,
# origin 과 destination 에 따라 색을 다르게

layer = pdk.Layer(
    'ArcLayer',
    df,
    get_source_position='[대여대여소경도, 대여대여소위도]',
    get_target_position='[반납대여소경도, 반납대여소위도]',
    get_width='1 + 10 * 정규화_이용',
    get_source_color='[255, 255, 120]',
    get_target_color='[255, 0, 0]',
    pickable=True,
    auto_highlight=True
)

# pydeck.data_utils.compute_view 는 Points 들의 경도, 위도를 리스트로 주면, 알아서 view_state 를 만들어줍니다.
view_state = pydeck.data_utils.compute_view(df[['대여대여소경도', '대여대여소위도']].values)
view_state.zoom = 12
view_state.bearing = -15
view_state.pitch = 45

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


### Path Layer ===================
# 한 데이터가 2개 이상의 Point 들을 보유
# Point 들을 차례대로 연결시켜 Path 를 그리기

# 샘플 : 서울시 특정 지역의 도로 데이터

import geopandas as gpd
import shapely

# Shapely 형태의 데이터를 받아 내부 좌표들을 List안에 반환합니다.
def line_string_to_coordinates(line_string):
    if isinstance(line_string, shapely.geometry.linestring.LineString):
        lon, lat = line_string.xy
        return [[x, y] for x, y in zip(lon, lat)]
    elif isinstance(line_string, shapely.geometry.multilinestring.MultiLineString):
        ret = []
        for i in range(len(line_string)):
            lon, lat = line_string[i].xy
            for x, y in zip(lon, lat):
                ret.append([x, y])
        return ret

df = gpd.read_file(geo_data)
df['geometry'] = df['geometry'].apply(line_string_to_coordinates)
df = pd.DataFrame(df) # geopanadas 가 아닌 pandas 의 데이터프레임으로 꼭 바꿔줘야 합니다.
df.head()

# 도로폭에 따라 색과 굵기를 달리하여 시각화
df['정규화도로폭'] = df['도로폭'] / df['도로폭'].max()

layer = pdk.Layer(
    'PathLayer',
    df,
    get_path='geometry',
    get_width='도로폭',
    get_color='[255, 255 * 정규화도로폭, 120]',
    pickable=True,
    auto_highlight=True
)

center = [126.950, 37.495]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=12)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()


### Trips Layer ===================
# Path Layer 와 동일하되 시간의 개념이 추가
# [시간지점, 위도, 경도] 를 담고 있는 data input
# 시간에 따라 어떻게 움직이는지 시각화










