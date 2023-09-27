
import clr
from src import RSAQuery

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll")
from RobotOM import *

app = RobotApplication()

str = RSAQuery(app)

nodes = str.get_all_nodes()
node = str.get_node_from_collection(1)

case_col = str.cases.GetAll()
case = IRobotCase(case_col.Get(1))

