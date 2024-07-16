import clr
import numpy as np
from src import PyARSA

doc = """This example creates simple 2D beam, applies loads, combinations and calculates the model"""

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll"
)
from RobotOM import *
app = RobotApplication()
pyrobot = PyARSA(app)


nodes_coords = np.array([[1,0,0,0],
                         [2,3,0,0],
                         [3,3.5,0,0],
                         [4,4,0,0]]
                         )
pyrobot.add_nodes(nodes_coords)

