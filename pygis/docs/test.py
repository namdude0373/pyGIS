# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

plt.style.use("bmh")  # better for plotting geometries vs general plots.


d = {
    "name": [
        "Washington\n(38.90, -77.03)",
        "Baltimore\n(39.29, -76.61)",
        "Fredrick\n(39.41,-77.40)",
    ],
    "geometry": [
        Point(-77.036873, 38.907192),
        Point(-76.612190, 39.290386,),
        Point(-77.408456, 39.412006),
    ],
}

gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(12, 6))
gdf.plot(ax=ax)
plt.ylim([38.8, 39.6])
plt.xlim([-77.5, -76.2])

for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf.name):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")


# %%


# %%

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

plt.style.use("bmh")  # better for plotting geometries vs general plots.

d = {
    "name": ["Washington\n(38.90, -77.03)"],
    "geometry": [
        LineString(
            [
                Point(-77.036873, 38.907192),
                Point(-76.612190, 39.290386,),
                Point(-77.408456, 39.412006),
            ]
        )
    ],
}
gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(12, 6))
gdf.plot(ax=ax)


# %%
from shapely.geometry import Polygon

d = {
    "name": ["Washington\n(38.90, -77.03)"],
    "geometry": [
        Polygon(
            [
                Point(-77.036873, 38.907192),
                Point(-76.612190, 39.290386,),
                Point(-77.408456, 39.412006),
            ]
        )
    ],
}
gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(12, 6))
gdf.plot(ax=ax)


# %%
import numpy as np

X = np.random.randint(256, size=(10, 10))

fig = plt.figure(figsize=(8, 6))
plt.imshow(X)
plt.title("Plot 2D array")
plt.show()


# %%
import geopandas

l = geopandas.GeoSeries(
    [
        LineString(
            [
                Point(-77.036873, 38.907192),
                Point(-76.612190, 39.290386,),
                Point(-77.408456, 39.412006),
            ]
        )
    ]
)
l


# %%
from shapely.geometry import Polygon

p = geopandas.GeoSeries(
    [
        Polygon(
            [
                Point(-77.036873, 38.907192),
                Point(-76.612190, 39.290386,),
                Point(-77.408456, 39.412006),
            ]
        )
    ]
)
p


# %%
geopandas.datasets.available


# %%
cities = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
cities.head()


# %%
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))

world.cx


# %%
import pandas

name = "fudge"
name[0:3]


# %%
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_cities"))
northern_world = world.iloc[0:4]
northern_world.plot(figsize=(10, 3))


# %%


# %%


# %%
import geopandas
import contextily as ctx

cities = geopandas.read_file(geopandas.datasets.get_path("naturalearth_cities"))
cities = cities[cities.name == "Washington, D.C."]
cities = cities.to_crs(epsg=3857)  # project to webmercator

ax = cities.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, zoom=6, reset_extent=True)
# ctx.add_basemap(ax, url=ctx.providers.Stamen.Toner,zoom = 6, reset_extent = True)


# %%
import matplotlib.pyplot as plt

ghent_img, ghent_ext = ctx.bounds2img(
    w=-8.8, s=4.5, e=-8.4, n=4.9, ll=True, source=ctx.providers.Stamen.Toner, zoom=10,
)
plt.imshow(ghent_img, extent=ghent_ext)


# %%
# Import necessary modules first
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import fiona

# Create an empty geopandas GeoDataFrame
newdata = gpd.GeoDataFrame()
# Create a new column called 'geometry' to the GeoDataFrame
newdata["geometry"] = None

print(newdata)


# Coordinates of the Helsinki Senate square in Decimal Degrees
coordinates = (-77.04639494419096, 38.89934963421794)

# Create a Shapely polygon from the coordinate-tuple list
point = Point(coordinates)

# Let's see what we have
point


# %%
import pandas as pd
import geopandas

points = {
    "lon": [
        -77.0412826538086,
        -77.11681365966797,
        -77.01896667480469,
        -77.0412826538086,
    ],
    "lat": [
        38.99570671505043,
        38.936713143230044,
        38.807610542357594,
        38.99570671505043,
    ],
}
points = pd.DataFrame.from_dict(points)
points.to_csv("~/temp/points.csv")


# %%
path_to_csv = "~/temp/points.csv"
from fiona.crs import from_epsg

from geopandas import GeoDataFrame as gdf

df = pd.read_csv(path_to_csv)

# Create a geodataframe from the data using from_epsg to assign WGS84 coordinate reference system
points = gdf(
    df,
    geometry=geopandas.points_from_xy(x=points.lon, y=points.lat),
    crs=from_epsg(4326),
)
points


# %%
# Import necessary modules first
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import fiona

# Create an empty geopandas GeoDataFrame
newdata = gpd.GeoDataFrame()
# Create a new column called 'geometry' to the GeoDataFrame
newdata["geometry"] = None

print(newdata)

# Coordinates of the Helsinki Senate square in Decimal Degrees
coordinates = (-77.04639494419096, 38.89934963421794)

# Create a Shapely polygon from the coordinate-tuple list
point = Point(coordinates)

# Let's see what we have
point

# Insert the polygon into 'geometry' -column at index 0
newdata.loc[0, "geometry"] = point

# Let's see what we have now
newdata

# Add a new column and insert data
newdata.loc[0, "Location"] = "GWU Geography"

# Let's check the data
newdata

# Import specific function 'from_epsg' from fiona module
from fiona.crs import from_epsg

# Set the GeoDataFrame's coordinate system to WGS84
newdata.crs = from_epsg(code=4326)

# Let's see how the crs definition looks like
newdata.crs

# Determine the output path for the Shapefile
outfp = r"../temp/gwu_geog.shp"

# Write the data into that Shapefile
newdata.to_file(outfp)


# %%
for x, y in [
    [-77.0412826538086, 38.99570671505043],
    [-77.11681365966797, 38.936713143230044],
    [-77.01896667480469, 38.807610542357594],
    [-76.90910339355469, 38.892636142310295],
]:
    print(x, y)


# %%
coord_list = [
    [-77.0412826538086, 38.99570671505043],
    [-77.11681365966797, 38.936713143230044],
    [-77.01896667480469, 38.807610542357594],
    [-76.90910339355469, 38.892636142310295],
]
[(x, y) for x, y in coord_list]


# %%
from io import StringIO

data = """
ID,X,Y,Speed
1,  -87.78976,  41.97658,   16
1,  -87.48234,  41.677342,  17
2,  -87.73956,  41.876827,  16
2,  -87.68161,  41.79886,   16
2,  -87.5999,   41.7083,    16
3,  -87.59918,  41.908485,  17
3,  -87.59857,  41.708393,  17
3,  -87.64391,  41.675133,  17
"""

df = pd.read_table(StringIO(data), sep=",")
print(df.columns)
df


# %%


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, shape

import matplotlib.pyplot as plt

plt.style.use("bmh")  # better for plotting geometries vs general plots.

# zip the coordinates into a point object and convert to a GeoData Frame
geometry = [Point(xy) for xy in zip(df.X, df.Y)]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)
geo_df.plot()


# %%

geo_df2 = geo_df.groupby(["ID"])["geometry"].apply(lambda x: LineString(x.tolist()))
geo_df2 = gpd.GeoDataFrame(geo_df2, geometry="geometry", crs="EPSG:4326")
geo_df2.reset_index(inplace=True)
geo_df2.plot(column="ID")


# %%


# %%
# list of coordindate pairs
coordinates = [
    [-77.0412826538086, 38.99570671505043],
    [-77.11681365966797, 38.936713143230044],
    [-77.01896667480469, 38.807610542357594],
    [-76.90910339355469, 38.892636142310295],
]

# Create a Shapely polygon from the coordinate-tuple list
poly = Polygon(coordinates)

# create a dataframe with needed attributes and required geometry column
df = {"GWU": ["name1"], "geometry": poly}

# Convert shapely object to a geodataframe
poly = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

# Let's see what we have
poly.plot()


# %%

# Coordinates of the GW department of geography in Decimal Degrees
coordinate = [-77.04639494419096, 38.89934963421794]

# Create a Shapely polygon from the coordinate-tuple list
point_coord = Point(coordinate)

# create a dataframe with needed attributes and required geometry column
df = {"GWU": ["Dept Geography"], "geometry": [point_coord]}

# Convert shapely object to a geodataframe
point = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

# Let's see what we have
point.plot()


# %%
points = [Point(xy) for xy in zip(df.X, df.Y)]
geo_df = gpd.GeoDataFrame(df, geometry=points, crs=from_epsg(4326))


# list of coordindate pairs
coordinates = [
    [-77.0412826538086, 38.99570671505043],
    [-77.11681365966797, 38.936713143230044],
    [-77.01896667480469, 38.807610542357594],
    [-76.90910339355469, 38.892636142310295],
]

# Create a Shapely polygon from the coordinate-tuple list
ply_coord = Polygon(coordinates)

# create a dataframe with needed attributes and required geometry column
df = {"Attribute": ["name1"], "geometry": ply_coord}

# Convert shapely object to a geodataframe
poly = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

# Let's see what we have
poly.plot()


# %%
newdata = gpd.GeoDataFrame()
print(newdata)


# %%
import numpy as np

x = np.linspace(-90, 90, 6)
y = np.linspace(90, -90, 6)
X, Y = np.meshgrid(x, y)
X


# %%
Y


# %%
Z1 = np.abs(((X - 10) ** 2 + (Y - 10) ** 2) / 1 ** 2)
Z2 = np.abs(((X + 10) ** 2 + (Y + 10) ** 2) / 2.5 ** 2)
Z = Z1 - Z2
Z


# %%
X = np.random.randint(256, size=(10, 10))
plt.imshow(Z)
plt.title("Plot 2D array")
plt.show()


# %%
from rasterio.transform import Affine

xres = (x[-1] - x[0]) / len(x)
yres = (y[-1] - y[0]) / len(y)
print(Affine.translation(x[0] - xres / 2, y[0] - yres / 2))
transform = Affine.translation(x[0] - xres / 2, y[0] - yres / 2) * Affine.scale(
    xres, yres
)
print("--------------")
print(Affine.scale(xres, yres))
print("--------------")
print(transform)


# %%
xres


# %%
transform * (0, 0)


# %%
transform * (3, 3)


# %%
import numpy as np

x = np.linspace(-90, 90, 6)
y = np.linspace(90, -90, 6)
X, Y = np.meshgrid(x, y)
X

Y

import matplotlib.pyplot as plt

Z1 = np.abs(((X - 10) ** 2 + (Y - 10) ** 2) / 1 ** 2)
Z2 = np.abs(((X + 10) ** 2 + (Y + 10) ** 2) / 2.5 ** 2)
Z = Z1 - Z2

plt.imshow(Z)
plt.title("Temperature")
plt.show()


# %%
from rasterio.transform import Affine

xres = (x[-1] - x[0]) / len(x)
yres = (y[-1] - y[0]) / len(y)

transform = Affine.translation(x[0] - xres / 2, y[0] - yres / 2) * Affine.scale(
    xres, yres
)


# %%
import rasterio

#%%

with rasterio.open(
    "../temp/temperature.tif",
    mode="w",
    driver="GTiff",
    height=Z.shape[0],
    width=Z.shape[1],
    count=1,
    dtype=Z.dtype,
    crs="+proj=latlong",
    transform=transform,
) as new_dataset:
    new_dataset.write(Z, 1)

# %% [markdown]

import matplotlib.pyplot as plt

data = rasterio.open("../temp/temperature.tif")

plt.imshow(data.read(1), cmap="BrBG")
plt.title("Temperature")
plt.show()

# %%
data = rasterio.open(
    "../data/LC08_L1TP_224078_20200518_20200518_01_RT.TIF", nodata=0, mask=True
)
data.nodatevals = (0, 0, 0)

from rasterio.plot import show

show(data)

#%%
import rasterio

with rasterio.open(
    "../data/LC08_L1TP_224078_20200518_20200518_01_RT.TIF", mode="r", nodata=0
) as src:
    profile = src.profile
    print(src.read([1]))
    arr = src.read([3, 2, 1])
    # print("Array shape:", arr.shape)
    # print(profile)

# %%
from rasterio.plot import show

show(arr)

from scipy import stats

print(stats.describe(arr.ravel()))

#%%
scaled_arr = arr / 100
scaled_arr.dtype

# %%
profile = src.profile
profile.update(nodata=0, compress="lzw", dtype=scaled_arr.dtype)

with rasterio.open(
    "../temp/LS_scaled_20200518.tif", mode="w", **profile,
) as new_dataset:

    new_dataset.write(scaled_arr, [1, 2, 3])

#%%
import matplotlib.pyplot as plt

with rasterio.open("../temp/LS_scaled_20200518.tif", mode="r") as src:
    show(src, adjust=None)


# %%
import geowombat as gw
import matplotlib.pyplot as plt

fig, ax = plt.subplots(dpi=200)

with gw.config.update(sensor="bgr"):
    with gw.open("../data/LC08_L1TP_224078_20200518_20200518_01_RT.TIF") as src:
        print(src.band)
        temp = src.where(src != 0).sel(band=["red", "green", "blue"])
        temp.gw.imshow(robust=True, ax=ax)
        temp.gw.to_raster(
            "../temp/LS_scaled_20200518.tif", verbose=0, n_workers=4, overwrite=True
        )


# %%

############################
import numpy as np

x = np.linspace(-90, 90, 6)
y = np.linspace(90, -90, 6)
X, Y = np.meshgrid(x, y)
X

Y

import matplotlib.pyplot as plt

Z1 = np.abs(((X - 10) ** 2 + (Y - 10) ** 2) / 1 ** 2)
Z2 = np.abs(((X + 10) ** 2 + (Y + 10) ** 2) / 2.5 ** 2)
Z = Z1 - Z2


# %%
from rasterio.transform import Affine

xres = (x[-1] - x[0]) / len(x)
yres = (y[-1] - y[0]) / len(y)

transform = Affine.translation(x[0] - xres / 2, y[0] - yres / 2) * Affine.scale(
    xres, yres
)


#%%
import os
import subprocess

import numpy as np
import rasterio
from rasterio import transform
from rasterio.warp import reproject, Resampling

tempdir = "../temp"
tiffname = os.path.join(tempdir, "example.tif")

with rasterio.Env():

    # Consider a 512 x 512 raster centered on 0 degrees E and 0 degrees N
    # with each pixel covering 15".
    rows, cols = src_shape = (512, 512)
    dpp = 1.0 / 240  # decimal degrees per pixel
    west, south, east, north = (
        -cols * dpp / 2,
        -rows * dpp / 2,
        cols * dpp / 2,
        rows * dpp / 2,
    )
    src_transform = transform.from_bounds(west, south, east, north, cols, rows)
    src_crs = {"init": "EPSG:4326"}
    source = np.ones(src_shape, np.uint8) * 255

    # Prepare to reproject this rasters to a 1024 x 1024 dataset in
    # Web Mercator (EPSG:3857) with origin at -237481.5, 237536.4.
    dst_shape = (1024, 1024)
    dst_transform = transform.from_origin(-237481.5, 237536.4, 425.0, 425.0)
    dst_crs = {"init": "EPSG:3857"}
    destination = np.zeros(dst_shape, np.uint8)

    reproject(
        source,
        destination,
        src_transform=src_transform,
        src_crs=src_crs,
        dst_transform=dst_transform,
        dst_crs=dst_crs,
        resampling=Resampling.nearest,
    )

    # Assert that the destination is only partly filled.
    assert destination.any()
    assert not destination.all()

    # Write it out to a file.
    with rasterio.open(
        tiffname,
        "w",
        driver="GTiff",
        width=dst_shape[1],
        height=dst_shape[0],
        count=1,
        dtype=np.uint8,
        nodata=0,
        transform=dst_transform,
        crs=dst_crs,
    ) as dst:
        dst.write(destination, indexes=1)

# info = subprocess.call(['open', tiffname])

# %%
with rasterio.open(
    "../temp/Z.tif",
    "w",
    driver="GTiff",
    height=Z.shape[0],
    width=Z.shape[1],
    count=1,
    dtype=Z.dtype,
    crs="+proj=latlong",
    transform=transform,
) as dst:
    dst.write(Z, 1)
#%%


import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.warp import reproject, Resampling, calculate_default_transform
from matplotlib import pyplot

dst_crs = "EPSG:3857"  # web mercator(ie google maps)

with rasterio.open("../data/LC08_L1TP_224078_20200518_20200518_01_RT.TIF") as src:
    src_transform = src.transform

    # calculate the transform matrix for the output
    dst_transform, width, height = calculate_default_transform(
        src.crs,
        dst_crs,
        src.width,
        src.height,
        *src.bounds,  # unpacks outer boundaries (left, bottom, right, top)
    )

    # set properties for output
    dst_kwargs = src.meta.copy()
    dst_kwargs.update(
        {
            "crs": dst_crs,
            "transform": dst_transform,
            "width": width,
            "height": height,
            "nodata": 0,  # replace 0 with np.nan
        }
    )

    with rasterio.open("../temp/LC08_20200518_webMC.tif", "w", **dst_kwargs) as dst:
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=dst_transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest,
            )

        #%%
        from rasterio.plot import show

        show(src)

#%%

dst_crs = "EPSG:3857"  # web mercator(ie google maps)

with rasterio.open("../data/LC08_L1TP_224078_20200518_20200518_01_RT.TIF") as src:

    # calculate the transform matrix for the output
    dst_transform, width, height = calculate_default_transform(
        src.crs,  # source CRS
        dst_crs,  # destination CRS
        src.width,  # column count
        src.height,  # row count
        *src.bounds,  # unpacks outer boundaries (left, bottom, right, top)
    )

print("Source Transform:\n", src.transform, "\n")
print("Destination Transform:\n", dst_transform)


# %%

import geopandas
from shapely.geometry import Point, LineString, Polygon

s = geopandas.GeoSeries(
    [Point(1, 1), LineString([(1, -1), (1, 0)]), Polygon([(3, -1), (4, 0), (3, 1)]),]
)

print(s)

r = s.rotate(90)
r.plot()

# %%
c = s.scale(2, 3, origin=(0, 0))
c.plot()

t = s.translate(2, 3)
t.plot()
# %%
import geoplot

world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))

geoplot.polyplot(world, figsize=(8, 4))
# %%

# Using readlines()
with open("../../../census_api.txt", "r") as f:
    c = f.read()
    print(Lines)

# %%

import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

plt.style.use("bmh")

a_square = {
    "name": ["Washington\n(38.90, -77.03)"],
    "geometry": [Polygon([Point(0, 45), Point(5, 45), Point(5, 40), Point(0, 40)])],
}

# create a dataframe from the nodes and assign the CRS
gdf_square = gpd.GeoDataFrame(a_square, crs="EPSG:4326")
fig, ax = plt.subplots(figsize=(12, 6))
gdf_square.plot(ax=ax)
plt.ylim(38, 50)
plt.xlim(0, 20)
plt.show()

# %%
gdf_square_10w = gdf_square.to_crs("+proj=longlat +datum=WGS84 +lon_0=-10")

fig, ax = plt.subplots(figsize=(12, 6))
gdf_square_10w.plot(ax=ax)
plt.ylim(38, 50)
plt.xlim(0, 20)
plt.show()

# %%
import geoplot as gplt
import geoplot.crs as gcrs

ax = gplt.webmap(contiguous_usa, projection=gcrs.WebMercator())
gplt.pointplot(continental_usa_cities, ax=ax)

# %%
import geowombat as gw
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(dpi=200)

proj4 = "+proj=aea +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96 +x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs"
image = "../data/LC08_L1TP_224078_20200518_20200518_01_RT.TIF"
with gw.config.update(ref_crs=proj4):
    with gw.open(image, resampling="nearest") as src:
        # src.where(src != 0).sel(band=[3, 2, 1]).gw.imshow(robust=True, ax=ax)
        # plt.tight_layout(pad=1)
        # Write the data to a GeoTiff
        src.gw.to_raster(
            "../temp/LC08_20200518_aea.tif",
            verbose=0,
            n_workers=4,  # number of process workers sent to ``concurrent.futures``
            n_threads=2,  # number of thread workers sent to ``dask.compute``
            overwrite=True,
        )  # number of window chunks to send as concurrent futures

# %%

import matplotlib.pyplot as plt

fig, ax = plt.subplots(dpi=200)

image = "../temp/LC08_20200518_aea.tif"
with gw.open(image) as src:
    src.where(src != 0).sel(band=[3, 2, 1]).gw.imshow(robust=True, ax=ax)
    plt.tight_layout(pad=1)


# %%
import geowombat as gw
from geowombat.data import l8_224078_20200518
import matplotlib.pyplot as plt
from geowombat.data import (
    l8_224078_20200518_B2,
    l8_224078_20200518_B3,
    l8_224078_20200518_B4,
)


fig, ax = plt.subplots(dpi=200)
with gw.open(
    [l8_224078_20200518_B2, l8_224078_20200518_B3, l8_224078_20200518_B4],
    stack_dim="band",
    band_names=[1, 2, 3],
) as src:
    src.where(src != 0).sel(band=[3, 2, 1]).gw.imshow(robust=True, ax=ax)
plt.tight_layout(pad=1)
# %%
from geowombat.data import l8_224077_20200518_B2, l8_224078_20200518_B2
fig, ax = plt.subplots(dpi=200)
with gw.open([l8_224077_20200518_B2, l8_224078_20200518_B2],
              mosaic=True) as src:
    print(src)
    src.where(src != 0).sel(band=1).gw.imshow(robust=True, ax=ax)
plt.tight_layout(pad=1)

# %%

# Import GeoWombat
import geowombat as gw

# Load image names
from geowombat.data import l8_224078_20200518, l8_224077_20200518_B2, l8_224078_20200518_B2
from geowombat.data import l8_224077_20200518_B4, l8_224078_20200518_B4

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

#%%
fig, ax = plt.subplots(dpi=200)
with gw.open(l8_224078_20200518) as src:
    src.where(src != 0).sel(band=[3, 2, 1]).plot.imshow(robust=True, ax=ax)
plt.tight_layout(pad=1)
plt.savefig("rgb_plot.png", dpi=150)


#%%
fig, ax = plt.subplots(dpi=200)
filenames = [l8_224077_20200518_B2, l8_224078_20200518_B2]
with gw.open(filenames,
                band_names=['blue'],
                mosaic=True,
                bounds_by='union') as src:
    src.where(src != 0).sel(band='blue').plot.imshow(robust=True, ax=ax)
plt.tight_layout(pad=1)

#%% Color Infrared (vegetation)
fig, ax = plt.subplots(dpi=200)

from geowombat.data import rgbn
with gw.open(rgbn,
            band_names=['red','green','blue','nir'],) as src:
    src.where(src != 0).sel(band=['nir','red', 'green']).plot.imshow(robust=True, ax=ax)
plt.tight_layout(pad=1)
plt.savefig("rgb_plot.png", dpi=150)


#%%
fig, ax = plt.subplots(dpi=200)
filenames = [l8_224077_20200518_B2, l8_224078_20200518_B2]
with gw.open(filenames,
                band_names=['blue'],
                mosaic=True,
                bounds_by='intersection') as src:
    src.where(src != 0).sel(band='blue').plot.imshow(robust=True, ax=ax)
plt.tight_layout(pad=1)


#%%
def plot(bounds_by, ref_image=None, cmap='viridis'):
    fig, ax = plt.subplots(dpi=200)
    with gw.config.update(ref_image=ref_image):
        with gw.open([l8_224077_20200518_B4, l8_224078_20200518_B4],
                        band_names=['nir'],
                        chunks=256,
                        mosaic=True,
                        bounds_by=bounds_by) as srca:
            # Plot the NIR band
            srca.where(srca != 0).sel(band='nir').plot.imshow(robust=True, cbar_kwargs={'label': 'DN'}, ax=ax)
            # Plot the image chunks
            srca.gw.chunk_grid.plot(color='none', edgecolor='k', ls='-', lw=0.5, ax=ax)
            # Plot the image footprints
            srca.gw.footprint_grid.plot(color='none', edgecolor='orange', lw=2, ax=ax)
            # Label the image footprints
            for row in srca.gw.footprint_grid.itertuples(index=False):
                ax.scatter(row.geometry.centroid.x, row.geometry.centroid.y,
                            s=50, color='red', edgecolor='white', lw=1)
                ax.annotate(row.footprint.replace('.TIF', ''),
                            (row.geometry.centroid.x, row.geometry.centroid.y),
                            color='black',
                            size=8,
                            ha='center',
                            va='center',
                            path_effects=[pe.withStroke(linewidth=1, foreground='white')])
            # Set the display bounds
            ax.set_ylim(srca.gw.footprint_grid.total_bounds[1]-10, srca.gw.footprint_grid.total_bounds[3]+10)
            ax.set_xlim(srca.gw.footprint_grid.total_bounds[0]-10, srca.gw.footprint_grid.total_bounds[2]+10)
    title = f'Image {bounds_by}' if bounds_by else str(Path(ref_image).name.split('.')[0]) + ' as reference'
    size = 12 if bounds_by else 8
    ax.set_title(title, size=size)
    plt.tight_layout(pad=1)

#%%
The two plots below illustrate how two images can be mosaicked. The orange grids highlight the image
footprints while the black grids illustrate the ``DataArray`` chunks.


#@savefig union_example.png
#plot('union')
#%%
# @savefig intersection_example.png
plot('union')

#%%
#@savefig ref1_example.png
# plot(None, l8_224077_20200518_B4)
plot(None, l8_224077_20200518_B4)


# %%
import geowombat as gw
from geowombat.data import rgbn

with gw.open(rgbn) as src:
    print(src.transform)
    print(src.gw.transform)
    print(src.crs)
    print(src.resampling)
    print(src.res)
    print(src.gw.cellx, src.gw.celly)
# %%
import matplotlib.pyplot as plt
fig, ax = plt.subplots(dpi=200)

proj4 = "+proj=aea +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96 +x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs"

with gw.config.update(ref_crs=proj4):
    with gw.open(rgbn) as src:
        print(src.transform)
        print(src.crs)
        print(src.resampling)
        print(src.res)
        src.where(src != 0).sel(band=[3,2,1]).plot.imshow(robust=True, ax=ax)

plt.tight_layout(pad=1)

#%%

#from rasterio.crs import CRS

with gw.config.update(ref_crs=31972   ):
    with gw.open(rgbn, resampling='cubic') as src:
        print(src.transform)
        print(src.crs)
        print(src.resampling)
        print(src.res)
# %%
import matplotlib.pyplot as plt
fig, ax = plt.subplots(dpi=200)

proj4 = "+proj=aea +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96 +x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs"

with gw.config.update(ref_crs=proj4):
    with gw.open(rgbn) as src:
        print(src.transform)
        print(src.crs)
        print(src.resampling)
        print(src.res)
        src.where(src != 0).sel(band=[3,2,1]).plot.imshow(robust=True, ax=ax)

plt.tight_layout(pad=1)
# %%

import geowombat as gw
from geowombat.data import rgbn
import matplotlib.pyplot as plt
fig, ax = plt.subplots(dpi=200)

with gw.open(rgbn) as ds:
    print(ds)
    evi = ds.gw.evi(sensor='rgbn', scale_factor=0.0001)
    print(evi)
    evi.plot(robust=True, ax=ax)
plt.tight_layout(pad=1)


# %%
fig, ax = plt.subplots(dpi=150)

with gw.config.update(sensor='qb', scale_factor=0.0001):
    with gw.open(rgbn) as ds:
        tcap = ds.gw.tasseled_cap()
        tcap.sel(band='wetness').plot(robust=True, ax=ax)
plt.tight_layout(pad=1)
# %%
fig, ax = plt.subplots(dpi=150)

with gw.config.update(sensor='rgbn', scale_factor=0.0001):
    with gw.open(rgbn) as ds:
        evi2 = ds.gw.evi2()
        evi2.plot(robust=True, ax=ax)
plt.tight_layout(pad=1)

# %%
with gw.config.update(sensor='rgbn'):
    with gw.open(rgbn) as ds:
        d = ds.gw.norm_diff('red', 'nir')
        print(d)
# %%
import geowombat as gw
from geowombat.data import l8_224077_20200518_B4

# Transform the data to lat/lon
with gw.config.update(ref_crs=32621):

    with gw.open(l8_224077_20200518_B4) as src:

        # Write the data to a VRT
        gw.to_vrt(src, 'lat_lon_file.vrt')

# %%

import geowombat as gw
from geowombat.data import l8_224078_20200518
from geowombat import to_vrt

# Transform a CRS and save to VRT

# with gw.config.update(ref_crs=102033):

with gw.open([l8_224078_20200518,l8_224078_20200518]) as src:
        print(src)
        attrs = src.attrs.copy()
        src.attrs = attrs

        to_vrt(src,  'output.vrt')
                  
                  
# %%
# %%
import geowombat as gw

with gw.open(l8_224077_20200518_B4, chunks=1024) as src:

    # Xarray drops attributes
    # attrs = src.attrs.copy()

    # Apply operations on the DataArray
    src = src * 10.0

    # src.attrs = attrs

    # Write the data to a GeoTiff
    src.gw.to_raster('output.tif',
                        verbose=1,
                        n_workers=4,    # number of process workers sent to ``concurrent.futures``
                        n_threads=2,    # number of thread workers sent to ``dask.compute``
                        n_chunks=200)   # number of window chunks to send as concurrent futures
# %%
import geowombat as gw
from geowombat.data import rgbn

from rasterio.windows import Window
w = Window(row_off=0, col_off=0, height=100, width=100)

with gw.open(rgbn,
                band_names=['blue', 'green', 'red'],
                num_workers=8,
                indexes=[1, 2, 3],
                window=w,
                ) as src:
    print(src)
# %% 
bounds = (793475.76, 2049033.03, 794222.03, 2049527.24)

with gw.open(rgbn,
                band_names=['green', 'red', 'nir'],
                num_workers=8,
                indexes=[2, 3, 4],
                bounds=bounds,
                out_dtype='float32') as src:
    print(src)


# %%
with gw.config.update(ref_bounds=bounds):

    with gw.open(rgbn) as src:
        print(src)
# %%
with gw.config.update(ref_bounds=bounds, ref_tar=rgbn):

    with gw.open(rgbn) as src:
        print(src)
# %%
from geowombat.data import l8_224078_20200518, l8_224078_20200518_points

with gw.open([l8_224078_20200518, l8_224078_20200518],
            band_names=['blue', 'green', 'red'],
            time_names=['1/4/2020', '1/5/2020'],
            stack_dim='time') as src:

    # Extract and by point geometry
    df = src.gw.extract(l8_224078_20200518_points)

print(df)
 

# %%
from geowombat.data import l8_224078_20200518, l8_224078_20200518_polygons

with gw.config.update(sensor='bgr'):
    with gw.open(l8_224078_20200518) as src:
        print(src.values)
        dat  = src.sel(band='red')-src.sel(band='blue')
        print(dat.values)
# %%


# Import modules
import geopandas as gpd
import geoplot as gplt
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from rasterio.transform import Affine
from scipy import stats
from shapely.geometry import Polygon, box
from sklearn.datasets import fetch_species_distributions
from sklearn.neighbors import KernelDensity
# %%
