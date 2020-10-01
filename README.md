![banner](https://user-images.githubusercontent.com/64412954/94649344-6f43e980-032f-11eb-871c-77359141f6d9.png)
# Project Keyboard - Key Viewer with Python 3
PyKeyViewer by Steve28 <br>
Version : 1.0 <br><br>

Version 1.0 : 2020.9/29 ~ 2020.10/1 [Download](https://github.com/pl-Steve28-lq/Project-Keyboard/files/5309937/PKV_1.0.zip) <br><br>

Inspired from : [RoanH/KeysPerSecond](https://github.com/RoanH/KeysPerSecond), Key Viewer made with Java <br>
Overlay Technologies : [davidmaamoaix/Overlay](https://github.com/davidmaamoaix/Overlay), Extend of tkinter with Overlay Method<br>

## 다운로드 Download
> **최신 버전 Newest Version : 1.0 ([Download](https://github.com/pl-Steve28-lq/Project-Keyboard/files/5309937/PKV_1.0.zip))**<br>
1. 다운로드를 한 뒤 압축을 해제 합니다. Download the file, and unzip it.<br>
2. 안에 있는 Project_Keyboard.exe의 바로가기를 만듭니다.<br>
바로가기를 만드는 이유는 exe 파일이 Utils 파일을 상대적으로 읽기 때문에 두 파일의 위치가 다르면 실행이 불가하기 때문입니다.<br>
Make Shortcut of Project_Keyboard.exe, inside unzipped folder.<br>
Because the exe reads Utils folder relatively, So you can't execute exe file if you change the directory.<br>
3. 바로가기를 실행시킵니다. Execute the Shortcut.<br><br>

실행 화면 Run Screen<br>
<img width="400" src="https://user-images.githubusercontent.com/64412954/94761773-d66da680-03e0-11eb-9e9b-5a957b9fb595.PNG">

## 기능 Features
> **키 입력 감지 Key Input Detection : Default**<br>
전역 후킹을 통해 어디서든 키보드 입력을 감지합니다.<br>
Detect Keyboard Input Anywhere by using Global Hook.

> **오버레이 기능 Overlay Screen : Default**<br>
오버레이를 지원합니다. 다른 창을 열어도, 항상 모든 창 위에 있어 가려지지 않습니다.<br>
Support Overlay. Even if you open new window, it always not obscured by any window.

> **키 정보 세이브 로드 Save and Load of Key Info : Ctrl+C (Load), Ctrl+S (Save)**<br>
어느 키를 치면 그 키의 스탯이 1 증가합니다. 키 배치, 종료를 바꿀 수도 있습니다. \*.pkvstat 형식으로 저장하고 불러올 수 있습니다. <br>
If you press a key, Stat of the key increased by 1. You can rearrange or change keys. Save and load Stats, using \*.pkvstat format.

> **합산 기능 Total Function : Default** <br>
스탯을 모두 합산한 토탈 값을 보여줍니다.<br>
Visualize sum of your stats.

> **키 바꾸기 Change Key : Button Click**<br>
최초 프로그램 실행 시 키 정보는 SDFJKL 입니다. 키 종류를 바꿀 수 있습니다.<br>
If you install and execute the Program first, Key info is SDFJKL. You can change the Key infos.

> **구석에 고정하기 Move to Corner : Right Click** <br>
스크린의 가장 가까운 코너로 화면을 이동시킵니다. <br>
Move to nearest corner of Screen.

> **종료 Exit : Double Click** <br>
프로그램을 종료합니다.<br>
Exit the Program.

============================================================================

## 추가할 기능 Features to Add
> ~~**키 정보 세이브 로드 Save and Load Key info** : <br>
설정한 키 정보를 저장하고 불러올 수 있습니다.<br>
You can save and load your key infos.~~
(Merged with **Save and Load of Key Info**)
