from src import PyRobot


pyrbt = PyRobot()
current_view = pyrbt.get_current_view()

# result = current_view.ParamsFeMap.CurrentResult

# code = current_view.GetTypeCode()
view_type = current_view.GetType()
rotation_point = current_view.GetRotationPoint()

# Reinforcement results

rc_res = {
    "ax_top": 577,
    "ax_bot": 579,
    "ay_top": 578,
    "ay_bot": 580,
    "crack_ax": 1116,
    "crack_ay": 1117,
    "rc_deflection": 1118,
}


ax_bottom = IRobotViewFeMapResultType(579, True)
# ax_bottom = 579

current_view.ParamsFeMap.CurrentResult = ax_bottom


# set parameters to the view (rotation etc)
# apply results to the view
# apply rotation
# remove previous screenshot
# take a screenshot
# save screenshot 


pyrbt.project.ViewMngr.Refresh

robapp.Project.PrintEngine.ScreenCaptures.Remove ("My screen capture")
scpar = robapp.CmpntFactory.Create(I_CT_VIEW_SCREEN_CAPTURE_PARAMS)
scpar.name = "My screen capture"
scpar.Resolution = I_VSCR_4096
ScPar.UpdateType = I_SCUT_COPY_TO_CLIPBOARD
viewRobot.MakeScreenCapture ScPar
robapp.Project.PrintEngine.AddScToReport("My screen capture")
robapp.Project.PrintEngine.SaveReportToOrganizer
robApp.Project.PrintEngine.SaveReportToFile(path, I_OFF_RTF_JPEG)