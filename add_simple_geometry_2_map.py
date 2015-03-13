##[Josefs scripts]=group
#geometry type
##geometrytype=string
#coordinates x and y separated by space and coordinate pairs separated by comma, polygon defined by first and last pair being exactly the same
##pointstring=string

from qgis.core import *
from PyQt4.QtCore import QSettings

def dothejob():
    if geometrytype == "point":
        the_geometry = QgsGeometry.fromWkt("POINT (" + pointstring + ")") 
        #MLayer = QgsVectorLayer("Point?crs=epsg:4326", "MemoryPointlayer", "memory") 
        MLayer = QgsVectorLayer("Point", "MemoryPointlayer", "memory")
    elif geometrytype== "line":
        the_geometry = QgsGeometry.fromWkt("LINESTRING (" + pointstring + ")")
        MLayer = QgsVectorLayer("LineString", "MemoryLineLayer", "memory")
    else: #elif geometrytype== "polygon":
        the_geometry = QgsGeometry.fromWkt("POLYGON ((" + pointstring + "))")
        MLayer = QgsVectorLayer("Polygon", "MemoryPolygonLayer", "memory")
    fet = QgsFeature() 
    fet.setGeometry(the_geometry) 
    MLayer.dataProvider().addFeatures( [fet] ) 
    MLayer.updateExtents() 
    QgsMapLayerRegistry.instance().addMapLayer(MLayer)
 
def enableUseOfGlobalCrs(s):  # 'set new Layers to use the Project-CRS' 
    oldValidation = s.value("/Projections/defaultBehaviour")#.toString()
    s.setValue( "/Projections/defaultBehaviour", "useProject" )
    return s, oldValidation 
    
def disableUseOfGlobalCrs(s, oldValidation):  #' enable old settings again' 
    s.setValue( "/Projections/defaultBehaviour", oldValidation ) 
    
s = QSettings()  
s, oldValidation = enableUseOfGlobalCrs(s)
dothejob()
disableUseOfGlobalCrs(s, oldValidation)