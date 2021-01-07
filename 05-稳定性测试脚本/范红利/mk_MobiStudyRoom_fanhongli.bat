adb uninstall com.offcn.yidongzixishi
adb install E:\tool\app自动化测试工具\apk\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk
adb push E:\temp\mk_m.txt /sdcard/
adb shell monkey -f /sdcard/mk_m.txt 1
adb shell monkey -p com.offcn.yidongzixishi --ignore-crashes --ignore-timeouts --ignore-native-crashes --pct-touch 70 --pct-motion 15  --pct-trackball 15 -s 1 -vvv --throttle 200 10000 1>E:\monkey.txt 2>E:\error.txt

