
# jmid2name-hoshino
 禁漫数字ID转换为书名的Hoshino Bot插件

#  ‼️重要‼️
本插件需要部署Hoshino的服务器与禁漫天堂网站保持稳定的链接，所以本插件也提供了配置文件用来自定义代理，尽量选择较稳定的节点如香港等。具体的配置在下文部署方式中有提及。
# 简介

> 还在因为英雄们只发JM数字ID而无从下手吗？  
> 还在因为想去粉色APP或其他软件浏览却还需要去一趟JM拿到本子原名而苦恼吗？

jmid2name来啦！只需要发送jm或JM接数字id，即可轻松获取本子原名 、作者与标签。
API功能来自[hect0x7](https://github.com/hect0x7)的[JMComic-Crawler-Python](https://github.com/hect0x7/JMComic-Crawler-Python)，欢迎多多支持API作者。

#  效果
![07374b2e141ea1bb6377047be4792c46](https://github.com/Fatfish588/jmid2name-hoshino/assets/59791439/d48250d2-5b04-43fd-9154-6c9432bdc1d4)


#  部署方式

1.下载或git clone本插件：    

在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目：    

```bash
git clone https://github.com/Fatfish588/jmid2name-hoshino.git
```

2.安装依赖  

```bash
pip install jmcomic -i https://pypi.org/project --upgrade
```
3.编写配置文件  
在jmid2name-hoshino目录中有一个config.yml,在此可以编辑代理，仓库中已经默认打开了127.0.0.1:7890，有需要的可以自己修改。如果发生文件未找到错误请参考常见问题。
![image](https://github.com/Fatfish588/jmid2name-hoshino/assets/59791439/c650ffc8-b916-449b-a266-acad1ec38cc0)



4.检查与JM的链接状态  
这是一个单独的功能，默认会在每次重启hoshino时执行一次。
```bash
# 进入到jmid2name-hoshino目录后
python testDomain.py 
# 运行比较慢，耐心等待，看到输出后即为完成
# 如果想关闭这个功能，参考常见问题
```
正常情况：
![image](https://github.com/Fatfish588/jmid2name-hoshino/assets/59791439/3a7a808a-cf73-4b81-92d9-db01c6b4b542)
异常情况：
![image](https://github.com/Fatfish588/jmid2name-hoshino/assets/59791439/2dc1d2d7-3b2f-4e04-80d6-ff95dfa7e2fc)

5.启用：    
在 HoshinoBot\hoshino\config\bot.py 文件的 MODULES_ON 加入 'jmid2name-hoshino'。    

6.重启 HoshinoBot。    
#  指令
 发送【JM】+ 数字id，或者【jm】+数字ID即可，中间不要有空格，开头必须是jm或JM，结尾必须是数字（是的暂不支持批量查找）
 例如：jm114514、JM114514  
 注意！不要通过艾特bot再加id的方式触发！因为艾特和bot名字也会被接受，这将会导致id不存在的返回。  
 请不要通过艾特bot的方式触发！
#  常见问题
 - Q：为什么加了插件后每次开hoshino都很慢会卡住？
 - A：因为加载到本插件时会去执行一次测试与JM服务器连接到脚本，详情请看部署步骤中的第4条检查与JM的链接状态 ，如果想关闭这个功能或者能确保服务器与JM能保持稳定链接，可以直接把testDomain.py直接删除或者全文注释。
- Q：我执行testDomain.py一直在报错“全部请求失败”怎么回事？
- A：八成是没有开代理或者代理未生效，具体参考部署步骤中的第3条编写配置文件。
- Q：为什么我在网站里可以搜到这个本子但是bot返回未找到？
- A：因为在JM有些本子是必须登录才能看的，本插件目前没有登录功能。
- Q：为什么bot半天不回话？
- A：因为与JM链接不稳定，运行testDomain.py检查当前网络能链接上多少域名。
- Q：明明配置文件写好了但是开启hoshino的报错说找不到config.yml怎么回事？
- A：在不同的系统上文件目录的读取是不一样的，所以如果开启hoshino的报错说找不到config.yml的话，那就手动把config.yml的绝对路径复制粘贴到jmid2name.py和testDomain.py中对应的path参数位置，如下图。
![image](https://github.com/Fatfish588/jmid2name-hoshino/assets/59791439/3e3dcf69-aaa5-45f6-a96a-68933e2ca7a3)
![image](https://github.com/Fatfish588/jmid2name-hoshino/assets/59791439/c48ab7bd-f2f4-44ac-9aba-2f1b49acd011)


- Q：都有api了为啥不做到bot看本那种程度啊？
- A：疯掉啦这么玩bot能活过三天吗。
# 碎碎念
1. 本插件的编写目的是为了服务于只想在固定APP浏览本子的用户，现在英雄们为了不被河蟹都在发JM号，这样在只能搜索本子名的APP中浏览还是挺麻烦的，所以做了这个。
2. 关于那个隐藏本，这个机制我是在api的仓库里看到的，我也不清楚这个隐藏的范围有多广，目前常见xp们应该都没问题，如果被隐藏的很多，可以在这里提issue告诉我，范围很广的话，我后续加上登录功能。
3. 很简单的一个小东西，但对我帮助很大，发布成Hoshino插件形式分享给大家。

