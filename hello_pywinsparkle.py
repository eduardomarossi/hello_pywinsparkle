import sys
from PySide2.QtWidgets import *
import platform

if platform.system() == 'Windows':
    from pywinsparkle import pywinsparkle
else:
    pywinsparkle = None

VERSION = '1.1.0'
update_url = "http://localhost:8000/appcast.xml"
pywinsparkle.win_sparkle_set_appcast_url(update_url)
pywinsparkle.win_sparkle_set_app_details("eduardomarossi", "Hello PyWinSparkle", VERSION)
pywinsparkle.win_sparkle_init()
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
label = QLabel("Hello World v" + VERSION)
label.show()
pywinsparkle.win_sparkle_check_update_with_ui_and_install()
# Enter Qt application main loop
app.exec_()
sys.exit()