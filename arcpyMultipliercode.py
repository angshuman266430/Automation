import arcpy
import os
from arcpy.sa import *
for name in os.listdir(r"Z:\test"):
    if name.endswith(".nc"):
        file = os.path.join(r"Z:\test",name)
        arcpy.MakeNetCDFRasterLayer_md(file,"PRCP",
                         "lon","lat","PRCP"+name)
        out_rc_multi_raster = RasterCalculator(["PRCP"+name],
                                               ["PRCP"], "PRCP*0.9")
        arcpy.md.RasterToNetCDF(out_rc_multi_raster,os.path.join(r"Z:\test","CAL_"+name),"PRCP",
                        "","x","y", "", "")