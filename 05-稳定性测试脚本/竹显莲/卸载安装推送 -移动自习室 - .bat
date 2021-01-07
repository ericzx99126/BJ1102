adb uninstall com.offcn.yidongzixishi
adb install E:\tool\App²âÊÔ¹¤¾ß\apk\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk
adb push E:\temp\mk1.txt /sdcard/
adb shell monkey -f /sdcard/mk1.txt 1 
adb shell monkey -p com.offcn.yidongzixishi  --ignore-timeouts  --pct-touch 70 --pct-motion 15  --pct-trackball 15 -s 1 -vvv --throttle 200 10000 1>E:\monkey.txt 2>E:\error.txt

