from cx_Freeze import setup, Executable

setup(name = "Pandas",
      version ="1.0",
      description = " Pandas example",
      executables = [Executable(r"C:\Users\Documents\***.py")]
      )

# Run the below command to build and generate Exe
# python python_to_exe.py build