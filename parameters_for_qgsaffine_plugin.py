##[Josefs scripts]=group
##rotation_angle_in_degrees=number 0.0
##x0=number 0.0
##y0=number 0.0
##result=output string
#the following are not implemented
#xscale=number 1.0
#yscale=number 1.0

"""
This script will return a, b, c, d, tx, ty as needed by qgsaffine plugin (https://github.com/gingerik/qgsAffine) to perform rotation of vector layer
x' = a * x + b * y + tx 
y' = c * x + d * y + ty
"""
import math

def parameters_for_qgisaffine_plugin(theta,x0=0,y0=0):#,xscale=1,yscale=1):
    theta_radians = 2*math.pi*theta/360
    a = math.cos(theta_radians)#*xscale
    b = -math.sin(theta_radians)
    tx = (x0 - math.cos(theta_radians) * x0 + math.sin(theta_radians) * y0)#xtranslation
    c = math.sin(theta_radians)
    d = math.cos(theta_radians)#*yscale
    ty = (y0 - math.sin(theta_radians) * x0 - math.cos(theta_radians) * y0)#ytranslation
    result = a, b, tx, c, d, ty
    return result
    

result = parameters_for_qgisaffine_plugin(rotation_angle_in_degrees,x0,y0)#,xscale,yscale)
print(result)

