import platform
if platform.system() == 'Linux':
 from linux import LinuxKeyboardHandler as GlobalKeyboardHandler
else:
 from wx_handler import WXKeyboardHandler as GlobalKeyboardHandler
