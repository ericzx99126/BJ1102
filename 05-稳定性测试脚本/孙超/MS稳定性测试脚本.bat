 adb push C:\Users\Administrator\Desktop\MS.txt /sdcard
adb uninstall com.offcn.yidongzixishi
adb install E:\apk\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk
adb shell monkey  -f /sdcard/MS.txt 1
adb shell monkey -p  com.offcn.yidongzixishi  --ignore-crashes --ignore-timeouts --ignore-native-crashes --pct-touch 20 --pct-syskeys 10 --pct-motion 40 --pct-anyevent 30 -s 100 -v -v -v --throttle 2000 2000 1 > C:\Users\Administrator\Desktop\MS_corr.log 2> C:\Users\Administrator\Desktop\MS_error.log  


