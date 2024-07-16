import clr
from src import pyARSAReporting

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll"
)
from RobotOM import *

app = RobotApplication()

pyrobot = pyARSAReporting(app)

nodes = pyrobot.get_all_nodes()
node = pyrobot.get_node_from_collection(1)

case_col = pyrobot.cases.GetAll()
case = IRobotCase(case_col.Get(1))
print(case.Name)