##[Josefs scripts]=group
#name for the group
##group_name=string
#transparency given as a number 0-100
##transparency_0_100=number 100.0

from qgis.core import *

def dothejob():
    root = QgsProject.instance().layerTreeRoot()
    mygroup = root.findGroup(group_name)
    for child in mygroup.children():
        if isinstance(child, QgsLayerTreeLayer):
            if child.layer().type() == 0: #QgsVectorLayer
                child.layer().setLayerTransparency(int(transparency_0_100))
            else:
                child.layer().renderer().setOpacity(transparency_0_100/100.0)
            child.layer().triggerRepaint()

dothejob()
