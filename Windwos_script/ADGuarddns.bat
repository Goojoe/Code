chcp 65001
netsh interface ip set dns name="WLAN" source=static addr=127.0.0.1 register=primary
echo ADGuard-Home-DNS was suessful
pause