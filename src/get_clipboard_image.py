import win32clipboard
from io import BytesIO
from PIL import Image

# This code to be fixed and tested - draft created by ChatGPT


def get_image_from_clipboard():
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_ENHMETAFILE):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_ENHMETAFILE)
            return BytesIO(data)
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


def save_image_as_emf(image, filename):
    if isinstance(image, Image.Image):
        image.save(filename, "EMF")
        print(f"Image saved as {filename}")
    else:
        print("Not a valid image.")


if __name__ == "__main__":
    image = get_image_from_clipboard()
    if image:
        save_image_as_emf(image, "clipboard_image.emf")
