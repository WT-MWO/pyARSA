import clr
import os

clr.AddReference(
    r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll"
)
from RobotOM import *
import RobotOM as rbt
from Structure import Structure

class pyARSAReporting(Structure):
    """Query information from ARSA model.
    """
    def __init__(self, app):
        super().__init__(app)

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
        node = rbt.IRobotNode(node_collection.Get(index))
        return node

    def get_compatible_nodes(self):
        """
        Gets all nodes in the Robot Model
        Returns: IRobotCollection of nodes
        """
        return self.nodes.CompatibleNodes

    def get_model_path(self):
        """Get Autodesk Robot model path
        Parameters:
            project: RobotApplicationClass.Project
        Returns:
            path(string): path of current (active) model
        """
        filename = self.project.FileName
        dir = os.path.dirname(filename)
        return dir

    def get_used_supports(self):
        """This code does not work needs to be investigated"""
        labels = self.labels.GetAvailableNames(rbt.IRobotLabelType.I_LT_SUPPORT)
        supports_count = labels.Count
        for i in range(1, supports_count + 1):
            label = labels.Get(i)
            available_supports.append(label)

        for i in range(1, count + 1):
            node = self.get_node_from_collection(i)
            node_number = node.Number
            # print(type(node_number)
            # print(node_number)
            # print(node.HasCalcSupport)
            if node.HasLabel(rbt.IRobotLabelType.I_LT_SUPPORT):
                node_sup = node.GetLabel(rbt.IRobotLabelType.I_LT_SUPPORT)
                num = node.Number
                suport_data = rbt.IRobotNodeSupportData(self.nodes.GetCalcSupport(num))

                # problems.append([node_sup.Name, num, suport_data.KZ])
                problems.append(
                    [
                        suport_data.KZ,
                        suport_data.ElasticLinear,
                        suport_data.NonlinearModel.IsDefined(
                            rbt.IRobotDegreeOfFreedom(2)
                        ),
                    ]
                )

    def get_current_view(self):
        return rbt.IRobotView3(self.project.ViewMngr.GetView(1))

    def get_combinations(self):
        pass

    def get_all_load_cases(self):
        return self.structure.Cases.GetAll()
