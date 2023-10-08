from src import PyRobot
from src import save_clipboard_robot_view
from tkinter import Tk

pyrbt = PyRobot()
current_view = pyrbt.get_current_view()


path = r"C:\Users\mwo\OneDrive - WoodThilsted Partners\Professional\3_ROBOT Python\pyRobot\tests"

# result = current_view.ParamsFeMap.CurrentResult

rotation_point = current_view.GetRotationPoint()

# View settings
current_view.ParamsDisplay.Set(
    pyrbt.rbt.IRobotViewDisplayAttributes.I_VDA_OTHER_RULER, False
)
current_view.ParamsDisplay.Set(
    pyrbt.rbt.IRobotViewDisplayAttributes.I_VDA_OTHER_GRID, False
)
current_view.SetSize(800.0, 800.0)


# Reinforcement results
rc_res = {
    "ax_top": 577,
    "ax_bot": 579,
    "ay_top": 578,
    "ay_bot": 580,
    # "crack_ax": 1116,
    # "crack_ay": 1117,
    # "rc_deflection": 1118,
}


for key in rc_res:
    current_view.ParamsFeMap.CurrentResult = pyrbt.rbt.IRobotViewFeMapResultType(
        rc_res[key], True
    )
    current_view.Redraw(True)
    current_view.CopyToClipboard()
    save_clipboard_robot_view(path=path, filename=key)
