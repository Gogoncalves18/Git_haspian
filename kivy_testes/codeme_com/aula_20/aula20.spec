from kivy_deps import sld2, glew

#Linha acima é necessario inserir manualmente
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

#Necessário preencher o caminho de pathex=[]
a = Analysis(
    ['aula20.py'],
    pathex=['/home/gog/Documentos/Python/Git_haspian/kivy_testes/codeme_com/aula_20'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

#Linha abaixo necessario inserir para achar os kv
a.datas += [('Code/aula20.kv', '/home/gog/Documentos/Python/Git_haspian/kivy_testes/codeme_com/aula_20/aula20.kv', 'DATA')]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='aula20',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
#Necessario inserir as duas linhas nas posicoes corretas:
# Tree('/home/gog/Documentos/Python/Git_haspian/kivy_testes/codeme_com/aula_20/'),
# *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
coll = COLLECT(
    exe,
    Tree('/home/gog/Documentos/Python/Git_haspian/kivy_testes/codeme_com/aula_20/'),
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='aula20',
)
