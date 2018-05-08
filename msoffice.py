try:
    import winreg
except ImportError:
    import _winreg as winreg

handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\excel.exe")

num_values = winreg.QueryInfoKey(handle)[1]
for i in range(num_values):
    print(winreg.EnumValue(handle, i))
