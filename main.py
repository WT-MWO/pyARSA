
import clr
from src import Structure

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll")
from RobotOM import *

app = RobotApplication()
str = Structure(app)

nodes = str.get_all_nodes()
node = str.get_node_from_collection(1)

print(nodes.Count)
print(node.X)