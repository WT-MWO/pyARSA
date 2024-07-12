class pyLoad:
    def __init__(self):
        self.Name = " "  # Load type IRobotLoadType
        self.LCName = " "  # Loadcase name
        self.objects = " "  # Objects node numbers, members, panels
        self.FX = 0  # Force value in X
        self.FY = 0  # Force value in Y
        self.FZ = 0  # Force value in Z
        self.Mx = 0  # Moment value in X
        self.My = 0  # Moment value in Y
        self.Mz = 0  # Moment value in Z
        self.PX = 0  # pressure X
        self.PY = 0  # pressure in Y
        self.PZ = 0  # pressure in Z
        self.alfa = 0  # angle for the load from X axis in degrees
        self.beta = 0  # angle for the load from Y axis in degrees
        self.gamma = 0  # angle for the load from Z axis in degrees
        self.disX = 0  # distance x for load on eccentricity - NOT USED??
        self.disY = 0  # distance y for load on eccentricity
        self.disZ = 0  # distance z for load on eccentricity
        self.calcnode = 0  # numer of calculation node
        self.cosystem = "-"  # coord system local or global
        self.absrel = "-"  # absolute or relative
        self.projected = "-"  # projected or not
        self.contourX = ""  # contour coordinates X
        self.contourY = ""  # contour coordinates Y
        self.contourZ = ""  # contour coordinates Z
        self.entirestruc = 0  # self-weight entrire structure

    def __repr__(self) -> dict:
        return str(
            {
                "Load type": self.Name,
                "Loadcase name": self.LCName,
                "Objects": self.objects,
                "Force value in X": self.FX,
                "Force value in Y": self.FY,
                "Force value in Z": self.FZ,
                "Moment value in X": self.Mx,
                "Moment value in Y": self.My,
                "Moment value in Z": self.Mz,
                "Pressure X": self.PX,
                "Pressure Y": self.PY,
                "Pressure Z": self.PZ,
                "Angle alfa": self.alfa,
                "Angle beta": self.beta,
                "Angle gamma": self.gamma,
                "Ecc. dist x": self.disX,
                "Ecc. dist y": self.disY,
                "Ecc. dist z": self.disZ,
                "Calc node": self.calcnode,
                "Coord system": self.cosystem,
                "Measure type": self.absrel,
                "Projected or not": self.projected,
                "Contour coord X": self.contourX,
                "Contour coord Y": self.contourY,
                "Contour coord Z": self.contourZ,
                "SW entire stucture": self.entirestruc,
            }
        )
