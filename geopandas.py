

import geopandas as gpd
gpd.__version__

# Geopandas가 제공하는 기본 데이터셋
# ['naturalearth_cities', 'naturalearth_lowres', 'nybb']
gpd.datasets.available

# World map
# python -m pip install descartes
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()

world.crs           # EPSG:4326
type(world.crs)     # 저장형식 : dictionary

# Korea map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
southkorea = world[world.name=='South Korea']
southkorea.plot()



