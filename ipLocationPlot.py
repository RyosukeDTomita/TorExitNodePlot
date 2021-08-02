##########################################################################
# Name: torExitLocation.py
#
# python3 torExitLocation.py <csv>
#
# Usage: Using cartopy, plot Tor exit node location info.
#
# Author: Ryosuke Tomita
# Date: 2021/06/19
##########################################################################
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfea
from cartopy.mpl.ticker import LatitudeFormatter,LongitudeFormatter

csvfile = sys.argv[1]
f = pd.read_csv(
        csvfile,
        header   = 0,)
lat  = f.loc[:,'latitude']
lon = f.loc[:,'longitude']
ip   = f.loc[:,'IPaddress']

# map
fig = plt.figure(figsize=(36,24),facecolor='w')
ax = fig.add_subplot(1,1,1,
        projection=ccrs.PlateCarree(central_longitude=0.0))
ax.set_global()
ax.coastlines()
dlon,dlat = 30,30 #punctuation
xticks = np.arange(-180,180.1,dlon)
yticks = np.arange(-90,90.1,dlat)
ax.set_xticks(xticks,crs=ccrs.PlateCarree())
ax.set_yticks(yticks,crs=ccrs.PlateCarree())
latfmt = LatitudeFormatter() #axis = degree
lonfmt = LongitudeFormatter(zero_direction_label=True) # No NS mark 0 degree
ax.xaxis.set_major_formatter(lonfmt)
ax.yaxis.set_major_formatter(latfmt)
ax.axes.tick_params(labelsize=12)
ax.plot(lon,lat,'bo',
        markersize      = 7,
        color           = '#ff1493',
        markeredgewidth = 1.,
        markeredgecolor = 'gray')
ax.add_feature(cfea.LAND,color='#2f4f4f')
ax.add_feature(cfea.OCEAN,color='#4682b4')

grid = ax.gridlines(crs       = ccrs.PlateCarree(),
                  draw_labels = False,
                  linewidth   = 1,
                  alpha       = 0.8,
                  color       = 'k')
#ax.set_xlim(120,150)
#ax.set_ylim(30,60)
grid.xlocator = mticker.FixedLocator(xticks)
grid.ylocator = mticker.FixedLocator(yticks)

fig.savefig("test",bbox_inches="tight",pad_inches=0.5)
