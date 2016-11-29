@echo off

rem uiファイルをpyファイルに変換
set THISDIR=%~dp0
pushd %THISDIR%

set COMPILER=C:\Python27\Scripts\pyside-uic.exe
set RESOURCE=C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe

for %%A in (*.ui) do %COMPILER% %%A > %%~nA.py

for %%A in (*.qrc) do %RESOURCE% %%A > %%~nA_rc.py

popd

rem EOF
