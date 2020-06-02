from cx_Freeze import setup, Executable

buildOptions = dict(include_files=[])
setup(
     name="appname",
     version="1.0",
     description="OC Projet 5",
     author="Julia",
     options=dict(build_exe=buildOptions),
     executables=[Executable("main2.py")]
)