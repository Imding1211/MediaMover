# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata

block_cipher = None

# 收集 Streamlit 的所有資料
streamlit_datas = collect_data_files('streamlit', include_py_files=True)
streamlit_hiddenimports = collect_submodules('streamlit')

# 🔥 關鍵：複製 metadata
streamlit_metadata = copy_metadata('streamlit')
altair_metadata = copy_metadata('altair')
pandas_metadata = copy_metadata('pandas')
numpy_metadata = copy_metadata('numpy')
pillow_metadata = copy_metadata('pillow')

# 🔥 加入 python-dotenv 的 metadata
try:
    dotenv_metadata = copy_metadata('python-dotenv')
except:
    dotenv_metadata = []

a = Analysis(
    ['run_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('main.py', '.'),
        ('.env', '.'),
    ] + streamlit_datas + streamlit_metadata + altair_metadata + pandas_metadata + numpy_metadata + pillow_metadata + dotenv_metadata,
    hiddenimports=[
        'streamlit',
        'streamlit.web',
        'streamlit.web.cli',
        'streamlit.web.server',
        'streamlit.web.server.server',
        'streamlit.runtime',
        'streamlit.runtime.scriptrunner',
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit.components.v1',
        'streamlit.elements',
        'streamlit.logger',
        'dotenv',  # 🔥 改成 'dotenv' 而不是 'python-dotenv'
        'PIL',
        'PIL.Image',
        'altair',
        'pandas',
        'numpy',
        'pyarrow',
        'tornado',
        'tornado.web',
        'tornado.websocket',
        'click',
        'toml',
        'blinker',
        'cachetools',
        'packaging',
        'importlib_metadata',
        'importlib.metadata',
    ] + streamlit_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PhotoSorter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'
)
