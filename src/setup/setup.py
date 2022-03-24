from cx_Freeze import setup, Executable

base = None
executables = [Executable("Main.py", base=base)]
packages = ["idna", "PyQt5", "XlsxWriter"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Pattern Builder",
    options=options,
    version="1.0",
    description='Build any pattern you want!',
    executables=executables
)
