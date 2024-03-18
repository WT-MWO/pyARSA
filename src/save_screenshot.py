import win32clipboard
from io import BytesIO
from PIL import Image


def _get_image_from_clipboard():
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_ENHMETAFILE):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_ENHMETAFILE)
            im = Image.open(BytesIO(data))
            return im
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_METAFILEPICT):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_METAFILEPICT)
            metafile_picture = data[
                14:
            ]  # Skip the first 14 bytes which are header data
            return BytesIO(metafile_picture)
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            im = Image.open(BytesIO(data))
            return im
        else:
            print("No compatible image format found in Clipboard.")
            return None
    finally:
        win32clipboard.CloseClipboard()


def _save_image(image, filename):
    if isinstance(image, Image.Image):
        image.save(filename)
        print(f"Image saved as {filename}")
    else:
        print("Not a valid image.")



def save_screenshot(path, name):
    """Saves the ARSA model screenshot from clipboars as png.
    Parameters:
    path(string): path to directory where you want to save
    filename(string): filename of your screenshot"""
    image = _get_image_from_clipboard()
    full_name = path+ '\\'+name+'.png'
    _save_image(image, full_name)



if __name__ == "__main__":
    path = "C:\\Users\\mwo\\OneDrive - WoodThilsted Partners\\Professional\\5_PYTHON\\pyARSA\\tests\\"
    name = "test"
    save_screenshot(path=path, name=name)

