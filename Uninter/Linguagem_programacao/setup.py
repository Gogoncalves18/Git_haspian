from cx_Freeze import setup, Executable
import os

path = "C:/git/Git_haspian/Uninter/Linguagem_programacao/Trabalho/entities/asset/"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]

#print(asset_list_completa)


executables = [Executable("main_jogo.py")]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}
setup(name="PegaFantasma",
      version="1.0",
      description='Pega Fantasma app',
      options={"build_exe": files},
      executables=executables
      )

