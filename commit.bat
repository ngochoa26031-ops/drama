@echo off
cd /d %~dp0

echo =========================
echo   AUTO PUSH TO GITHUB
echo =========================

git add .
git commit -m "auto update"
git push origin main

echo.
echo DONE !!!
pause