adb uninstall com.offcn.yidongzixishi
adb install E:\appzaxiang\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk
adb push E:\appzaxiang\mk.txt /sdcard/
adb shell monkey -f /sdcard/mk.txt 1  