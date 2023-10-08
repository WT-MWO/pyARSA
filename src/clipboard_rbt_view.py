import clr

clr.AddReference(
    r"C:\Users\mwo\OneDrive - WoodThilsted Partners\Professional\3_ROBOT Python\pyRobot\dll\ClipboardEMF.dll"
)
from ClipboardEMF import Class1

scetp = Class1()


def save_clipboard_robot_view(path, filename):
    """
    path(string) - path to the directory where .png image will be stored
    filename(string) - name of the image, without extension, which is always .png
    """
    format = ".png"
    dash = "\\"
    full_path = path + dash + filename + format
    # print(full_path)
    scetp.SavePNG(full_path)


if __name__ == "__main__":
    path = r"C:\Users\mwo\OneDrive - WoodThilsted Partners\Professional\3_ROBOT Python\pyRobot\tests"
    name = "screenshot"
    save_clipboard_robot_view(path=path, filename=name)
