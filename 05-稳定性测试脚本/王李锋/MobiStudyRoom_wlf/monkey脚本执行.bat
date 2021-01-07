adb uninstall com.offcn.yidongzixishi
adb install C:\mk\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk
adb push C:\mk\mk_for_MobiStudyRoom_wlf.txt /sdcard/
adb shell monkey -f /sdcard/mk_for_MobiStudyRoom_wlf.txt 1
pause
adb shell monkey -p com.offcn.yidongzixishi -vvv -s 1 --throttle 100 10000 1>C:\mk\nor.log 2>C:\mk\/error.log
adb shell screencap /sdcard/zixishi.png
adb pull /sdcard/zixishi.png C:\mk\