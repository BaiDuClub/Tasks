# 前言
git英语俚语意思是蠢货，自以为是且好辩的人，但是据说这只是随便的三个字母组合，并且没有被unix系统占用而且它发音跟get接近。
> I'm an egotistical bastard, and I name all my projects after myself. First 'Linux', now 'Git'.<br>我是个任性的杂种，我把所有我做的项目以我自己命名。先是'Linux'，这次是'Git'.     --Linus Torvalds

它的诞生就是为了版本控制，所谓版本控制就是指：你需要管理代码的新增，删除，合并和更改，如果只是一个文件，那或许创建副本或者只是 ctrl z \ctrl shift z就可以查看前后版本，但是一旦文件数量很多或者备份出现意外，那你的代码就真的丢失了。同时代码数量一旦增加，管理代码也就变得十分困难。

同样大佬Linus也面对了这样的问题，他创建了开源Linux后，全世界的人向他发送代码（~~这谁受得了~~）起初它使用的是使用BitKeeper作为Linux内核管理工具，可是那玩意不是开源的，造成一些纠纷之后，大佬一怒之下10天写了第一个版本的git，和linux一样，这位大佬无私地将他开源（~~respect!!~~）[git的前生今世](https://www.liaoxuefeng.com/wiki/896043488029600/896202815778784)

<br>

---

# 学习git

这里我们先快速上手，请参考[视频教程](https://www.bilibili.com/video/BV1HM411377j/?spm_id_from=333.337.search-card.all.click&vd_source=e25316b6f912bb2563d59c6c99d49d77)，如果你有不懂的地方，请参考下面那个更详细的教程

[廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/896043488029600)

如果你还不太理解：
结合这个可视化小游戏来理解分支管理的具体内容
[learngitBranch](https://learngitbranching.js.org/?locale=zh_CN)

<br>

---

# 使用github

>GitHub上性别严重失衡，男性群体高达95%以上，所以GitHub经常被大家戏称为GayHub，也是全球最大同性交友网站。

git通过引入代码分支管理使得代码库的维护和管理变得无比容易，比如我们的一个项目，大家只需要将代码用git在一台仓库服务器上进行管理就可以了,每个人的修改记录和代码的历史版本都记录在上面。

那么如果我们遇到解决不了的问题，想要和别的项目联系、合作、共享代码，我们还是得通过点对点的网络连接或者邮件传播代码（~~像我们用QQ\微信版本管理一样~~），如果很多人都想看我们的项目，那我们还是要浪费时间和每个人进行联系！因此为了帮助程序员找到开源项目,也方便组织和公司公开自己的代码，github就诞生了[github的前生今世](https://36kr.com/p/1722666106881)

相信刚才的git教程中你已经接触了github，下面我们将重点说明git和github的几个重要知识点：

## 本地仓库：  
- git init 后创建 .git文件夹(window中避免删除会自动隐藏),存储有git工具的代码，它为当前这一层的文件简历索引和管理工具，同时存储有所有文件的历史版本，因此如果你删除.git文件夹你将丢失所有的版本！
- 工作区：也就是这一层的文件，你对.git统同一目录下的文件进行更改时，这些更改只存在于工作区中，还没有被git 管理
- 暂存区：git add xxx 将文件添加到暂存区，相当于把这些文件的当前版本复制一份交给git管理（好像拍照片定格现在状态一样，所以有时这种版本复制也叫快照），此时commit提交的是暂存区内复制的文件

      比如你git init后，创建了 a.md 里面写了hello ，然后 git add 到缓冲区，git status查看状态，然后你又修改a.md 为hello world ，然后才git commit -m “” ，其实这个时候本地仓库内a.md: hello，你的修改仍然留在工作区

- 本地仓库：终于到了本地仓库，缓冲区中的文件通过git commit就被提交到了本地仓库，这是对外的窗口，外部能看到的都是这里面的文件，我们用push命令，pull命令都是对这里进行改变

## 远程仓库：
- 我们在github上创建的 Repository 就是远程仓库，远程仓库存储在github公司的服务器上，相当于云备份，如果设置为公开，别人就可以通过链接访问到我们的远程仓库中的内容
- github\git为了防止云端的仓库被随意改变，规定：远程仓库和本地仓库中 **相同的分支上** ，必须确保本地仓库领先远程仓库（就像数学中的包含于∈关系，远程仓库∈本地仓库），这样就确保总是提交新东西进去，远程仓库原有的不会改变。
- 当然如果你提交了错误的东西到远程仓库，那么肯定还是需要删除、覆盖、修剪远程仓库代码的，你需要学习[冲突处理](https://www.liaoxuefeng.com/wiki/896043488029600/900004111093344)的知识，用手动方式合并每一个冲突，确保程序员自己对代码修改负责任,同样本地仓库的commit中也会面临冲突处理的可能，思路是一样的
- 一切机制的核心目的：确保远程仓库、本地仓库代码不会被随意修改。


延申阅读：[图解git操作](https://zhuanlan.zhihu.com/p/263050507)

<br>

---

# HomeWork

### 1:在github创建公共仓库BaiDuClub
使用git将你前几次写的md文件，C语言实验的代码，latex编译后生成的pdf文件 放在一个文件夹中，git init,add,commit后，想办法把该文件夹push 到你创建的仓库，今后的HomeWork都push到这个仓库的这个文件夹中。
- 如果你不能正确push \ clone ，请搜索***github ssh*** 尝试解决，[参考](https://www.cnblogs.com/zhoulujun/p/15141608.html)  [参考2](https://zhuanlan.zhihu.com/p/108972475)  [参考3](https://zhuanlan.zhihu.com/p/114068278)
>github在2021年后不再支持密码登陆的方式，要么使用非常难记忆的token，要么配置ssh免密登录，注意clone时不再使用https的链接，而是选择ssh

如果要你输用户名和密码，出现这种错误一般就需要用ssh处理，不懂的地方请多问gpt，一般的错误用搜索引擎得到的结果不是很适合初学者

```agsl
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/leo59123/git.git/'
```

设置好后重新关联远程仓库：
  
    git remote set-url origin（这个指的是远程仓库名） git@github.com:leo59123/git.git（这个指的是ssh方式的仓库链接） 


### 2：完成以下任务
- 新建一个文件夹,取名为learn_git 进去,本地git init 创建一个新的git 仓库
- 添加一个新的文件,取名为a.md,在文件里面添加：***I love BaiduClub***.
  然后尝试把这个文件git add到暂存区,然后commit，（注意参考延伸资料提到的commit message书写方式）
- 添加一个新的文件,取名为b.md,在文件里面添加 ***I love AI***.
  然后尝试把这个文件add 到暂存区,然后 git status 查看状态,但是不commit
- 对于a.md我们对其进行修改,修改成 ***I don't love BaiduClub*** ，同样commit -m “< xxx > : < xxx >”
- 你又发现这样子写大家看到会很伤心的,所以说你想复原,请用 [版本回退](https://www.liaoxuefeng.com/wiki/896043488029600/897013573512192)的方式进行复原
- 请参考[分支管理](https://www.liaoxuefeng.com/wiki/896043488029600/896954848507552)，接着创建一个新的分支：new_branch ,（git branch ）查看当前所有的分支，然后切换到新分支，修改a.md 为***I really really love BaiDuClub !*** 提交你的修改,看看是否已经提交成功了 ， 然后切换回main分支，看看a.md的内容
- 现在我们把new_branch分支的内容合并到原先的分支main分支，发生错误了吗？尝试解决：[如何处理冲突](https://www.liaoxuefeng.com/wiki/896043488029600/900004111093344)

### 3:尝试从github 上clone 一个项目
> 我敢发誓这绝对是你大学中用的最多的github功能：），再次提醒 [独立自主&学术诚信](https://zhuanlan.zhihu.com/p/40568346)
- https://github.com/recolic/awesome-hust.git
- https://github.com/AlexFanw/HUSTER-CS.git
- 如果还是有ssh登录的问题，请参考 1 中

>## 预计完成时间：2 h

<br>

---

# 延伸阅读
[全面了解git\github的一切](https://zhuanlan.zhihu.com/p/369486197)

[如何写出清晰的Git commit message](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)

    速览，重点是按照格式 <feat\bugfix\chore\test\docs>:<精准的描述>

[HelloGithub](https://hellogithub.com/?sort_by=last&tid=juBLV86qa5)

    一个发现和分享有趣开源项目的平台，有同名公众号，每周一会推荐一些好玩、有用的项目和工具，最近重点聚焦于AI前沿的工具，可以多逛一逛


<br>

---
by hgj <br>最后修改于2023.10.15