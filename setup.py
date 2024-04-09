from cx_Freeze import setup, Executable

script_path = "main.py"

exe = Executable(
    script=script_path,
    base=None,
    target_name="color-model-converter.exe"
)

options = {
    "build_exe": {
        "includes": [],
        "excludes": [],
        "packages": [],
        "include_files": []
    }
}

setup(
    name="color-model-converter",
    version="1.0.0",
    description="Conversor de modos de cores",
    options=options,
    executables=[exe]
)
