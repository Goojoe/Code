chcp 65001
netsh interface ip set dns name="WLAN" source=static addr=8.8.8.8 register=primary
netsh interface ip add dns name="WLAN" addr=8.8.4.4 index=2
echo Google-DNS was suessful
pause