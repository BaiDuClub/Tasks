# 前言
[Who is linus?](https://zhuanlan.zhihu.com/p/19796979)

[Wiki：什么是Linux](https://zh.wikipedia.org/wiki/Linux) 需要科学上网

请做好心理准备，这一章节是从配置开始就是很难的东西，需要花很长时间捣鼓，甚至可以说运气不好的话，你花一周都配置不出一个好用的环境。因此我们并不催着大家一定要在期限内完成，你可以挑一个心情很好，没有ddl，就是想“虚度”一下光阴的时候尝试搜索：***怎样拥有linux环境*** , 然后搜索一切你能找到的资源来实现目标。（即使一整天一事无成，也千万不要懊悔、恼怒(~~我只会觉得我好菜啊QAQ~~)，因为和机器打交道就是这样。~~干这行最重要的就是耐心~~）

注意几个重要的注意事项：
- 配置任何环境前都要搜索教程：多搜索一些，比对阅读,找到和自己电脑情况接近的；找到和自己目的最接近的一个，然后坚持到底。
- 知道你每一步的操作在干什么：一定严格按照教程或者详细的指导来操作，任何随意的配置都会后患无穷甚至把你的电脑弄得一团糟，最后只能被迫Remake。
- 注意安装路径：从今以后99%的开发环境、app都不许安装到C盘（极少数例外），一定要自定义安装到你指定的路径，路径名尽量不要出现中文

<br>

---

# 配置linux
空谈无用，我们学习linux必须一边看教程一边实践，因此一切学习的基础就是安装一个可以正常运行终端的linux

如果你是mac电脑，那么你几乎不需要配置linux， macOS是类Unix内核系统，可以在Shell上体验到和Linux几乎一样的操作逻辑，相反地，你需要想办法配置一个window虚拟机：）~~这就是金钱的力量吗QAQ~~

如果你是window电脑，你可以搜索 ***"Window 10/11 ，虚拟机，VMvare ,Ubuntu "*** 这几个关键词的组合，然后阅读相关的博客，捣鼓很久，你就可以拥有一个和你的电脑几乎一模一样，但是基本上共用一套硬件的虚拟电脑，它有虚拟网卡，虚拟内存，虚拟磁盘，虚拟图形界面....除了你需要在Window中手动打开而不是按电源键就可以自动进入外，其他都和你的电脑一致，唯一不同的就是：它是linux系统的。
> 当然这里还有另一种方式：双系统，和虚拟机不同
> - 虚拟机是在一个系统上通过相关工具调度来共享硬件资源，通过虚拟化技术达到好像有一台机器有一套单独的硬件的样子，因此虚拟机相当于是同时在跑两套系统，优势也是你可以同时使用两种系统做很多协作的事
> 
> 双系统：则在你电源上电进入引导流程、BIOS(基本输入输出系统)，还没有加载操作系统的时候就已经分支了，底层上相当于把你的机器的硬件划分出两个区域，一个给win系统服务，另一个给你安装的双系统。然后你可以选择进入哪一个系统，之后就和正常的电脑完全一样，只不过底层能利用的硬件减半了，你一个系统只能用自己区域的硬件资源。优点是从硬件层面实现隔离，缺点是不能同时运行两个系统，且有一定的硬件浪费，对你硬件资源的要求比较高。

> - 建议搜索：***”虚拟机原理“***
> [虚拟机和双系统哪个好？](https://www.zhihu.com/question/64937979) 
 
我们鼓励大家安装虚拟机，另外的情况我们没有使用需求。

## ***WSL2 (Windows Subsystem for Linux)***
wsl2一种非常适合window的虚拟机方案 [wsl2介绍](https://zhuanlan.zhihu.com/p/394776349#:~:text=WSL2%E6%98%AFWSL1%E7%9A%84%E5%8D%87%E7%BA%A7%E7%89%88%EF%BC%8C%E6%8F%90%E4%BE%9B%E4%BA%86%E6%9B%B4%E5%A5%BD%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E6%80%A7%E8%83%BD%E5%92%8C%E6%9B%B4%E5%AE%8C%E5%85%A8%E7%9A%84Linux%E7%B3%BB%E7%BB%9F%E5%86%85%E6%A0%B8%E6%94%AF%E6%8C%81%EF%BC%8CWSL2%20%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96%E6%8A%80%E6%9C%AF%E5%9C%A8%E8%BD%BB%E9%87%8F%E7%BA%A7%E8%99%9A%E6%8B%9F%E6%9C%BA%20%28VM%29,%E4%B8%AD%E8%BF%90%E8%A1%8C%20Linux%20%E5%86%85%E6%A0%B8%EF%BC%8C%E5%90%8C%E6%97%B6%E4%BF%9D%E7%95%99%E4%BA%86WSL1%E7%9A%84%E6%93%8D%E4%BD%9C%E4%BD%93%E9%AA%8C%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%8A%8A%E9%80%9A%E8%BF%87WSL2%E5%90%AF%E5%8A%A8%E7%9A%84Linux%E7%B3%BB%E7%BB%9F%E8%AE%A4%E4%B8%BA%E6%98%AF%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E7%9A%84%E4%B8%80%E4%B8%AALinux%E7%B3%BB%E7%BB%9F%EF%BC%8C%E5%9B%A0%E6%AD%A4%EF%BC%8C%E7%9B%B8%E5%AF%B9%E4%BA%8E%E9%80%9A%E8%BF%87%E7%94%A8%E6%88%B7%E6%A8%A1%E5%BC%8F%E5%92%8C%E5%86%85%E6%A0%B8%E6%A8%A1%E5%BC%8F%E7%BB%84%E4%BB%B6%E6%9E%84%E6%88%90%E5%85%BC%E5%AE%B9%E6%80%A7%E5%BA%95%E5%B1%82%E6%9D%A5%E8%BF%90%E8%A1%8CLinux%E7%9A%84WSL1%E6%9D%A5%E8%AF%B4%EF%BC%8CWSL2%E7%9A%84Linux%E7%B3%BB%E7%BB%9F%E6%9B%B4%E5%AE%8C%E6%95%B4%EF%BC%8C%E5%8A%9F%E8%83%BD%E6%9B%B4%E5%AE%8C%E5%96%84%E3%80%82)

这是微软为windows原生适配的linux虚拟机，相比wsl1体验好了不少，你可以搜索 "***Win10/11 wsl2 ubuntu***"等关键词来查找教程，安装好后启动非常简单：我们只需要win + s搜索wsl启动，然后就完了，由于是windows自家的应用，整体安装非常简单，而且运行很丝滑。[参考教程](https://zhuanlan.zhihu.com/p/394776349#:~:text=WSL2%E6%98%AFWSL1%E7%9A%84%E5%8D%87%E7%BA%A7%E7%89%88%EF%BC%8C%E6%8F%90%E4%BE%9B%E4%BA%86%E6%9B%B4%E5%A5%BD%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E6%80%A7%E8%83%BD%E5%92%8C%E6%9B%B4%E5%AE%8C%E5%85%A8%E7%9A%84Linux%E7%B3%BB%E7%BB%9F%E5%86%85%E6%A0%B8%E6%94%AF%E6%8C%81%EF%BC%8CWSL2%20%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96%E6%8A%80%E6%9C%AF%E5%9C%A8%E8%BD%BB%E9%87%8F%E7%BA%A7%E8%99%9A%E6%8B%9F%E6%9C%BA%20%28VM%29,%E4%B8%AD%E8%BF%90%E8%A1%8C%20Linux%20%E5%86%85%E6%A0%B8%EF%BC%8C%E5%90%8C%E6%97%B6%E4%BF%9D%E7%95%99%E4%BA%86WSL1%E7%9A%84%E6%93%8D%E4%BD%9C%E4%BD%93%E9%AA%8C%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%8A%8A%E9%80%9A%E8%BF%87WSL2%E5%90%AF%E5%8A%A8%E7%9A%84Linux%E7%B3%BB%E7%BB%9F%E8%AE%A4%E4%B8%BA%E6%98%AF%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E7%9A%84%E4%B8%80%E4%B8%AALinux%E7%B3%BB%E7%BB%9F%EF%BC%8C%E5%9B%A0%E6%AD%A4%EF%BC%8C%E7%9B%B8%E5%AF%B9%E4%BA%8E%E9%80%9A%E8%BF%87%E7%94%A8%E6%88%B7%E6%A8%A1%E5%BC%8F%E5%92%8C%E5%86%85%E6%A0%B8%E6%A8%A1%E5%BC%8F%E7%BB%84%E4%BB%B6%E6%9E%84%E6%88%90%E5%85%BC%E5%AE%B9%E6%80%A7%E5%BA%95%E5%B1%82%E6%9D%A5%E8%BF%90%E8%A1%8CLinux%E7%9A%84WSL1%E6%9D%A5%E8%AF%B4%EF%BC%8CWSL2%E7%9A%84Linux%E7%B3%BB%E7%BB%9F%E6%9B%B4%E5%AE%8C%E6%95%B4%EF%BC%8C%E5%8A%9F%E8%83%BD%E6%9B%B4%E5%AE%8C%E5%96%84%E3%80%82)   [ 其他参考文档](https://zhuanlan.zhihu.com/p/337104547) 

缺点是：不像虚拟机那样具有一个完整的图形界面，只能在Windows Terminal中运行虚拟机，你也可以安装图形化界面，但是不如虚拟机效果好。不过对我们来讲这样一个玩具虚拟机只有终端或许更方便进行linux命令的学习。

安装后注意，默认是装在C盘的，这样伴随我们的使用会越来越卡，我们可以使用powerShell命令转移到别的盘[如何将wsl2移动到别的盘](https://blog.csdn.net/yihuajack/article/details/119915303)

同时注意wsl关闭终端窗口并没有停止，彻底关闭需要在powerShell中输入 wsl --shutdown ，再查看 wsl -l -v看看是否是 stopped

利用wsl+vscode 进行[远程开发](https://zhuanlan.zhihu.com/p/394623634)：[wsl+vscode远程开发](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-vscode)

远程开发简单讲就是我们的代码存储、运行在别的机器上，我们连接服务器后，可以在本地实时查看和修改远程服务器上的代码。这里因为之前讲的虚拟机经过虚拟化后具有可看作是于独立的物理硬件，所以此时wsl相当于是linux服务器，我们用vscode连接服务器进行开发。

这样你就具有了一个可以进行开发的linux环境了。

<br>

---

# linux简介

我们的讲解主要分为以下部分：
- 一个是linux操作系统的整体思想，和我们常用的window到底有什么不同
- 另一个是linux系统结构
- 最后是linux操作

这部分网上教程很多，所以我在这里不会多讲。有一个专门的工种就是linux运维，我们不需要那么精通，但是熟练掌握这种原始的命令行交互的操作系统是有好处的：
- 该使用怎样的指令：

        和所见即所得的有图形化界面GUI相比，命令行是很落后的，我们生活中一些很容易的操作在这里都没那么容易。这使得我们更接近底层，你会发现你用鼠标点点点的过程原来实际这么复杂。

- 对指令产生的结果需要了如指掌: [rm -rf /*的恐怖](https://www.zhihu.com/question/29438735/answer/101838852)

        因为自由度很高，如果你处于很高的权限上，简单的一行指令可以控制电脑中的任何模块，你可以用指令控制显示器亮度，控制电源的开断，理论上windos的 所有简单操作都是操作系统为你封装好后的接口，linux下这些都交给你用命令来控制。

- 整个操作系统对我们而言是透明的(~~这就是真正的自由~~)

<br>

---

# linux系统结构
[操作系统速成课](https://www.bilibili.com/video/BV1EW411u7th?p=18&vd_source=e25316b6f912bb2563d59c6c99d49d77)
我们必须了解一部分操作系统的发展史，虽然这是大三的课程，但是我觉得提前了解一部分简单内容是很有益的，详情请看参考资料，我总结出以下部分：
- 随着计算机加快处理程序的方式变化：

        单程序->批处理单程序->分时多任务多用户Multics -> 分时单用户系统UNIX  -> UNIX大家族分出主要的两派：闭源且庞大的Windows\Macos ，开源而简单的Linux ,开源的linux后来造就了绝大多数的服务器系统的选择，还有工业界的各种嵌入式系统，以及移动端的Android，以及近年来的HarmonyOS
- 随着文件存储的变化：[12分钟速成](https://www.bilibili.com/video/BV1EW411u7th?p=19)

        穿孔卡片-> 延迟线（像抛球把戏一样把100个球抛在空中循环，每次取一个，整体来看就好像存储了100个） ->磁介质（磁芯\磁带\磁鼓\磁盘）-> 软盘-> 光盘-> 半导体固态硬盘 

- 还有一些文件系统的变化，这个就太过繁琐了，等待大家后续进行学习 [文件系统速成](https://www.bilibili.com/video/BV1EW411u7th?p=20&vd_source=e25316b6f912bb2563d59c6c99d49d77)

此外，后续linux的详细系统设计很难在这里讲清楚，大家需要对计算机系统逐渐学习，有了更深地认识之后再深入理解操作系统。因此我们仅仅科普一下操作系统的发展和简单结构。

<br>

---

# linux设计思想：
也就是UNIX哲学，对于程序设计还有解决问题都有意义。

[自由和分享](https://www.zhihu.com/question/21424364)

[一切皆文件](https://zhuanlan.zhihu.com/p/349354666)

[linux中管道的思想](https://zhuanlan.zhihu.com/p/58489873)

      简单但正确的程序 连接起来就会变得不一样
[用简单的方法解决问题](https://ruanyifeng.com/blog/2009/06/unix_philosophy.html)

<br>

---

# linux操作

基本的操作，请参照[菜鸟教程](https://www.runoob.com/linux/linux-tutorial.html)

查找一个命令：别忘了直接向gpt询问

实践才是学习的唯一方法：光背会所有的指令你不能说学会linux，但是能做到日常生活中一直使用linux那你肯定是学会了。

<br>

---

# HomeWork

## 1：完成菜鸟教程:
从[linux简介](https://www.runoob.com/linux/linux-intro.html)  到  [linux vi/vim](https://www.runoob.com/linux/linux-vim.html),所有的例子请在虚拟机终端中尝试一遍，观察文件结构，执行相关命令操作
> 如果一个命令的写法总是忘记，学会使用man xxx 或 xxx --help ，不要忘记 ***1-提问的智慧*** 中讲到的 RTFM！
## 2:完成[一个简单的linux练习](\Reference\Linux A.pdf)
不需要记笔记，动手敲过就可以了。

## 3：速览[linux命令为什么要这么写？](https://www.runoob.com/w3cnote/linux-command-full-fight.html)
了解一些常用命令的名字来源，有利于我们记忆指令。

>### 预计完成时间2h 

<br>

---

# 延伸阅读

鸟叔的linux私房菜

[UNIX指南](https://www.harley.com/unix-book/book/chapters/01.html#A)

[命令行的艺术](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)

<br>

---
by hgj <br>最后修改于2023.10.15

