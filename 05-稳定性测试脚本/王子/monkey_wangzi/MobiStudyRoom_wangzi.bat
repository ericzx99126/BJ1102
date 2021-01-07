adb uninstall com.offcn.yidongzixishi
adb install E:\apk\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk
adb push E:\mk.txt /sdcard/
adb shell monkey -f /sdcard/mk.txt 1
adb shell monkey -p com.offcn.yidongzixishi -s 1 -vvv --throttle 100 5000 1>E:\nomarl.log 2>E:\error.log