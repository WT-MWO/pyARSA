import clr
import os

clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll")
from RobotOM import *
import RobotOM as rbt


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
        self.results = self.structure.Results  # IRobotResultServer
        self.objects = self.structure.Objects
        self.rbt = rbt

        # Record load types available in Robot, list[enum, value, string name}
        self.load_record_type = [
            [rbt.IRobotLoadRecordType.I_LRT_NODE_FORCE, 0, "nodal force"],
            [rbt.IRobotLoadRecordType.I_LRT_NODE_DISPLACEMENT, 1, "displacement of support node"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_DILATATION, 2, "shortening/extension of bar"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_FORCE_CONCENTRATED, 3, "concentrated force on the bar length"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_MOMENT_DISTRIBUTED, 4, "distributed moment load on a bar"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_UNIFORM, 5, "uniform bar load"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_TRAPEZOIDALE, 6, "linear trapezoidal load on a bar"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_THERMAL, 8, "thermal load on a bar"],
            [rbt.IRobotLoadRecordType.I_LRT_LINEAR, 21, "linear load on FE-2D"],
            [rbt.IRobotLoadRecordType.I_LRT_LINEAR_3D, 19, "linear load on FE-3D"],
            [rbt.IRobotLoadRecordType.I_LRT_POINT_AUXILIARY, 23, "concentrated load at a point"],
            [rbt.IRobotLoadRecordType.I_LRT_IN_3_POINTS, 22, "planar load defined at three points"],
            [rbt.IRobotLoadRecordType.I_LRT_PRESSURE, 24, "hydrostatic pressure"],
            [rbt.IRobotLoadRecordType.I_LRT_THERMAL_IN_3_POINTS, 25, "planar thermal load at three points"],
            [rbt.IRobotLoadRecordType.I_LRT_IN_CONTOUR, 28, "planar load defined on contour"],
            [rbt.IRobotLoadRecordType.I_LRT_NODE_FORCE_MASS, 30, "concentrated nodal mass"],
            [
                rbt.IRobotLoadRecordType.I_LRT_BAR_FORCE_CONCENTRATED_MASS,
                33,
                "concentrated mass at point on bar length",
            ],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_UNIFORM_MASS, 35, "uniform linear mass on a bar"],
            [rbt.IRobotLoadRecordType.I_LRT_BAR_TRAPEZOIDALE_MASS, 36, "trapezoidal linear mass on a bar"],
            [rbt.IRobotLoadRecordType.I_LRT_MASS_ACTIVATION, 39, "activation of a record for masses"],
            [rbt.IRobotLoadRecordType.I_LRT_SPECTRUM_VALUE, 40, "spectrum value"],
            [rbt.IRobotLoadRecordType.I_LRT_UNIFORM, 26, "uniform surface load"],
            [rbt.IRobotLoadRecordType.I_LRT_THERMAL, 8, "planar thermal load"],
            [rbt.IRobotLoadRecordType.I_LRT_NODE_FORCE_IN_POINT, 23, "concentrated force in point"],
            [rbt.IRobotLoadRecordType.I_LRT_LINEAR_ON_EDGES, 69, "linear load on edges"],
            [rbt.IRobotLoadRecordType.I_LRT_DEAD, 7, "self-weight"],
            [rbt.IRobotLoadRecordType.I_LRT_SURFACE_ON_OBJECT, 70, "surface load on object"],
            [rbt.IRobotLoadRecordType.I_LRT_MOBILE_POINT_FORCE, 53, "moving load - point force"],
            [rbt.IRobotLoadRecordType.I_LRT_MOBILE_DISTRIBUTED, 55, "moving distributed load"],
            [rbt.IRobotLoadRecordType.I_LRT_NODE_VELOCITY, 10, "node velocity"],
            [rbt.IRobotLoadRecordType.I_LRT_NODE_ACCELERATION, 11, "node acceleration"],
        ]
        self.analize_types = {
            rbt.IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR: "static case",
            rbt.IRobotCaseAnalizeType.I_CAT_STATIC_NONLINEAR: "non-linear static case",
            rbt.IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR_AUXILIARY: "auxillary case",
        }
