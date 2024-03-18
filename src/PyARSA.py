import clr
import os

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll"
)
from RobotOM import *
import RobotOM as rbt


class Structure:
    def __init__(app):
        """
        This is Python wrapper for Autodesk Robot API.
        Parameters:
            app(RobotApplication): Robot application
        """
        self.app = app
        self.project = self.app.Project
        self.structure = self.project.Structure
        self.labels = self.structure.Labels
        self.cases = self.structure.Cases
        self.nodes = self.structure.Nodes
        self.results = self.structure.Results  # IRobotResultServer
        self.objects = self.structure.Objects
        self.rbt = rbt


class PyARSA(Structure):
    """Create and modify ARSA model."""

    def __init__(self):
        super().__init__()

    def add_nodes(self, coord_array):
        """Adds nodes in the model space.
        Parameters:
        coord_array(numpy.array): [node_number, X, Y, Z]"""
        self.structure.Nodes()
        pass