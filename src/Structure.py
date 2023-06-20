import clr

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll")
from RobotOM import *


class Structure:
    def __init__(self, app):
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

    def get_all_nodes(self):
        """
        Gets all nodes in the Roboit Model
        Returns: IRobotCollection of nodes
        """
        return self.nodes.GetAll()
    
    def get_node_from_collection(self, index):
        """
        Returns the node of given index.
        Parameters:
        index(int): index of node
        Returns: IRobotNode object
        """
        node_collection = self.get_all_nodes()
        node = IRobotNode(node_collection.Get(index))
        return node
