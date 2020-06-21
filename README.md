# AutoLoginNJUPT
## 南邮校园网辅助登陆
### 使用说明：
在config文件里有三行配置，正确填写后运行联网程序就可以代为完成学校的网络验证了。

运营商可以填`校园网` `移动` `电信`，不要多字少字多加空格。

在安装了Python3和requests库的电脑上，直接使用

    python autoConnect.py
来实现自动联网

考虑到可能大多数同学还是Windows系统，我打包了exe可执行文件，填写一次`config.txt`文件后，双击联网程序`autoConnecter`即可（不需要安装python）。

由于我~~懒得考虑程序的健壮性了~~只有一天测试时间无法考虑太多因素，秉着能用就行的原则，希望大家多多注意细节，比如不要用中文冒号、配置文件与程序要放在同一文件夹内等，相信大家学过C/JAVA也都懂的。
### 题外话：
代码思路受到了[NJUPT_Network_AutoLogin](https://github.com/pdxgf1208/NJUPT_Network_AutoLogin)的启发~~实际上原作者考虑到跨平台问题，找我写一个python版本的实现~~。

为什么想在离校前最后一天写这个脚本，用原作者的话说算是给学弟学妹们留下点有用的东西。之前每天联网的时候都想吐槽一下学校联网的页面做的不尽人意，每天联网验证大概率会遇到令人头疼的问题。比如会出现连上WIFI或网线后能直接弹出验证窗口，但是没有浏览器自动填写密码的功能；填写p.njupt.edu.cn进行联网，第一次总是失败，跳转后才能成功等等。总的来说每日单调的联网操作确实不太方便，不如交给程序来执行。

另外由于编码问题，window用户可能需要配置文件用记事本另存为`utf-8`编码(windows文本默认保存为GBK，而python使用utf-8编码），否则程序会报错。
### 进阶用法：
Windows计划任务定时联网

WIFI负载均衡（经过一次偶然的测试发现，使用CMCC或者CHINANET无线网也可以连校园网，也就是说没有必要去挤连的人超多的NJUPT无线网信道）
