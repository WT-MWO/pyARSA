import clr
from src import PyARSA

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll"
)
from RobotOM import *

app = RobotApplication()
str = PyARSA(app)


# create panel 1
free_num = str.objects.FreeNumber
panel_1 = str.objects.Create(free_num)

# create contour for object

geocontour = RobotGeoContour
# geocontour.Initialize

# creating segment

segment = RobotGeoSegmentLine

print(segment)
