# April Fools' Day Prank - The Matrix
# Free to use, copy, modify, and distribute for any purpose.
# The author(s) provide this software "as is", without warranty of any kind,
# and shall not be held liable for any damages or issues arising from its use.
# Source code available at: https://github.com/RezGabBud/The-Matrix

import webview
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == "__main__":

    html_path = resource_path("index.html")

    window = webview.create_window(
        title="",
        url=html_path,
        fullscreen=True,
        frameless=True,
        on_top=True,
        easy_drag=False,
        draggable=False,
    )

    webview.start()