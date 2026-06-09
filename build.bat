@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo   数学知识图 构建（公开版 → index.html）
echo   目录: %cd%
echo ============================================

rem ── 选择 Python 启动器：优先 py -3，回退 python ──
set "PYCMD="
where py >nul 2>nul && set "PYCMD=py -3"
if not defined PYCMD where python >nul 2>nul && set "PYCMD=python"
if not defined PYCMD (
  echo [错误] 没找到 Python 启动器（py / python 都不在 PATH 上）。
  echo        请装 python.org 版本并勾选 "Add python.exe to PATH" 与 "py launcher"。
  echo.
  pause
  exit /b 1
)
echo 使用解释器: %PYCMD%
%PYCMD% --version
echo --------------------------------------------

%PYCMD% build.py
set "RC=%errorlevel%"
echo --------------------------------------------
if not "%RC%"=="0" (
  echo [构建失败] Python 退出码 = %RC% 。请把上面整段输出发给我。
  echo.
  pause
  exit /b 1
)

rem ── 显示产物时间戳，确认确实刚刚重建 ──
for %%F in (graph.json index.html) do (
  if exist "%%F" (echo 已更新 %%F   修改时间 %%~tF) else (echo [警告] 找不到 %%F)
)
echo.
echo 构建完成 ✓
echo 重要：浏览器里务必按 Ctrl+Shift+R 强制刷新，否则看到的还是缓存旧版！
echo.
echo 按任意键打开 index.html …
pause >nul
start "" "%~dp0index.html"
