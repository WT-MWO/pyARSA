
import clr
from src import Structure

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll")
from RobotOM import *

app = RobotApplication()
str = Structure(app)

bars = str.results.Bars # IRobotBarResultServer

forces = bars.Forces # IRobotBarForceServer
bar_data = forces.Value(1,1,0) # IRobotBarForceData


print(bar_data.FX)

