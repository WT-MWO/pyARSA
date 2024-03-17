import clr
from src import PyARSA

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll"
)
from RobotOM import *

app = RobotApplication()
pyrobot = PyARSA(app)

bars = pyrobot.results.Bars  # IRobotBarResultServer

forces = bars.Forces  # IRobotBarForceServer
bar_data = forces.Value(1, 1, 0)  # IRobotBarForceData


print(bar_data.FX)
