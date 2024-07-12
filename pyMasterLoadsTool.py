import clr
from src import pyARSAReporting
from pyLoad import pyLoad

clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2023\Exe\Interop.RobotOM.dll")
from RobotOM import *
import RobotOM as rbt

U = 1000  # divider to get kN

supported_analize_type = [
    rbt.IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR,
    rbt.IRobotCaseAnalizeType.I_CAT_STATIC_NONLINEAR,
    rbt.IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR_AUXILIARY,
]

rect = rbt.IRobotLoadRecordType
supported_load_types = {
    rect.I_LRT_NODE_FORCE: "nodal force",
    rect.I_LRT_BAR_UNIFORM: "uniform load",
    rect.I_LRT_UNIFORM: "(FE) uniform",
    rect.I_LRT_BAR_FORCE_CONCENTRATED: "member force",
    rect.I_LRT_DEAD: "self-weight",
    rect.I_LRT_BAR_TRAPEZOIDALE: 
}


app = RobotApplication()

pyrobot = pyARSAReporting(app)


def read_cosystem(cosys):
    if cosys == 0:
        return "global"
    else:
        return "local"


def read_calcnode(cnode):
    if cnode == 0:
        return "no"
    else:
        return "generated"


def read_relabs(rela):
    if rela == 0:
        return "absolute"
    else:
        return "relative"


def read_objects(rec):
    objects = []
    count = rec.Objects.Count
    if count == 0:
        return "MISSING!!!"
    else:
        for r in range(1, count + 1):
            objects.append(rec.Objects.Get(r))
    return objects


def store_load(lcase, rec):
    load = pyLoad()
    rec_type = rec.Type
    load.LCName = lcase.Name
    load.objects = read_objects(rec)
    if rec_type == rect.I_LRT_NODE_FORCE:
        load.Name = supported_load_types[rec_type]
        load.FX = rec.GetValue(0) / U  # I_NFIPRV_FX
        load.FY = rec.GetValue(1) / U  # I_NFIPRV_FY
        load.FZ = rec.GetValue(2) / U  # I_NFIPRV_FZ
        load.Mx = rec.GetValue(3) / U  # I_NFIPRV_MX
        load.My = rec.GetValue(4) / U  # I_NFIPRV_MY
        load.Mz = rec.GetValue(5) / U  # I_NFIPRV_MZ
        load.alfa = rec.GetValue(8)  # I_NFIPRV_ALPHA
        load.beta = rec.GetValue(9)  # I_NFIPRV_BETA
        load.gamma = rec.GetValue(10)  # I_NFIPRV_GAMMA
    elif rec_type == rect.I_LRT_BAR_UNIFORM:
        load.Name = supported_load_types[rec_type]
        load.PX = rec.GetValue(0) / U  # I_URV_PX
        load.PY = rec.GetValue(1) / U  # I_URV_PY
        load.PZ = rec.GetValue(2) / U  # I_URV_PZ
        load.cosystem = read_cosystem(rec.GetValue(11))  # I_URV_LOCAL_SYSTEM
        load.projected = rec.GetValue(12)  # I_URV_PROJECTION
    elif rec_type == rect.I_LRT_DEAD:
        load.Name = supported_load_types[rec_type]
        load.entirestruc = rec.GetValue(15)  # I_BDRV_ENTIRE_STRUCTURE
    elif rec_type == rect.I_LRT_BAR_FORCE_CONCENTRATED:
        load.Name = supported_load_types[rec_type]
        load.FX = rec.GetValue(0) / U  # I_BFCRV_FX
        load.FY = rec.GetValue(1) / U  # I_BFCRV_FY
        load.FZ = rec.GetValue(2) / U  # I_BFCRV_FZ
        load.Mx = rec.GetValue(3) / U  # I_BFCRV_CX
        load.My = rec.GetValue(4) / U  # I_BFCRV_CY
        load.Mz = rec.GetValue(5) / U  # I_BFCRV_CZ
        load.alfa = rec.GetValue(8)  # I_BFCRV_ALPHA
        load.beta = rec.GetValue(9)  # I_BFCRV_BETA
        load.gamma = rec.GetValue(10)  # I_BFCRV_GAMMA
        load.cosystem = read_cosystem(rec.GetValue(11))  # I_BFCRV_LOC
        load.calcnode = read_calcnode(rec.GetValue(12))  # I_BFCRV_GENERATE_CALC_NODE
        load.absrel = read_relabs(rec.GetValue(13))  # I_BFCRV_REL
        load.disX = rec.GetValue(6)  # I_BFCRV_X
        load.disY = rec.GetValue(21)  # I_BFCRV_OFFSET_Y
        load.disZ = rec.GetValue(22)  # I_BFCRV_OFFSET_Z
    return load


# Get all cases
cases = pyrobot.get_all_load_cases()
records = []

for i in range(1, cases.Count + 1):
    lcase = rbt.IRobotCase(cases.Get(i))
    # Make sure case is not a combination or not supported type
    if lcase.AnalizeType in supported_analize_type:
        # Recast case object as simple
        lcase = rbt.IRobotSimpleCase(cases.Get(i))
        # Loop through the load records in case
        print(lcase.Records.Count)
        for r in range(1, lcase.Records.Count + 1):
            # Get load record
            rec = lcase.Records.Get(r)
            records.append(store_load(lcase, rec))
            print(rec.Type)

for r in records:
    print(r)
