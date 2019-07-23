## *我们正处于互联网最好的时代*

本博客的Github地址是：https://github.com/Masterpaopao/Master-Blog

转载请标明原Github出处，觉得不错请点个star支持！

* [一\.环境安装](#%E4%B8%80%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85)
    * [1\.特点](#1%E7%89%B9%E7%82%B9)
    * [2\.版本](#2%E7%89%88%E6%9C%AC)
* [二\.文档学习](#%E4%BA%8C%E6%96%87%E6%A1%A3%E5%AD%A6%E4%B9%A0)
    * [1\.学习链接](#1%E5%AD%A6%E4%B9%A0%E9%93%BE%E6%8E%A5)
    * [2\.创建项目](#2%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE)
    * [3\.生成数据库](#3%E7%94%9F%E6%88%90%E6%95%B0%E6%8D%AE%E5%BA%93)
* [三\.投票应用](#%E4%B8%89%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8)
    * [1\.添加应用](#1%E6%B7%BB%E5%8A%A0%E5%BA%94%E7%94%A8)
    * [2\.创建模型](#2%E5%88%9B%E5%BB%BA%E6%A8%A1%E5%9E%8B)
    * [3\.激活模型](#3%E6%BF%80%E6%B4%BB%E6%A8%A1%E5%9E%8B)
    * [4\.命令交互](#4%E5%91%BD%E4%BB%A4%E4%BA%A4%E4%BA%92)
    * [5\.管理页面](#5%E7%AE%A1%E7%90%86%E9%A1%B5%E9%9D%A2)
    * [6\.更多视图](#6%E6%9B%B4%E5%A4%9A%E8%A7%86%E5%9B%BE)
    * [7\.修改URL](#7%E4%BF%AE%E6%94%B9url)
    * [8\.完善表单](#8%E5%AE%8C%E5%96%84%E8%A1%A8%E5%8D%95)
* [四\.BBS应用](#%E5%9B%9Bbbs%E5%BA%94%E7%94%A8)
    * [1\.学习须知](#1%E5%AD%A6%E4%B9%A0%E9%A1%BB%E7%9F%A5)
    * [2\.模型原理](#2%E6%A8%A1%E5%9E%8B%E5%8E%9F%E7%90%86)
    * [3\.模型设计](#3%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1)
    * [4\.settings\.py](#4settingspy)
    * [5\.激活模块](#5%E6%BF%80%E6%B4%BB%E6%A8%A1%E5%9D%97)
    * [6\.认识MTV](#6%E8%AE%A4%E8%AF%86mtv)
    * [7\.API交互](#7api%E4%BA%A4%E4%BA%92)

&nbsp;

## 一.环境安装

#### 1.特点

1）满足快速开发与后台开发人员的严格要求

2）集中精力编写应用程序，无需重复造轮子

3）处理常见的开发任务如用户身份验证和内容管理等

4）重视安全性，防止SQL注入、恶意脚本与请求等

5）丰富的拓展性满足频繁变更要求

6）全能模板特性，能够做各种各样的网站

&nbsp;

#### 2.版本

Python3.7 + Django2.1

我们会在ConEmu+Miniconda上进行配置Django的环境。:

（不懂的同学请移步到我的Relearn-Python博客学习第一篇的搭建环境教程）

在ConEmu中输入这条命令（BBS是项目的架构）：cc up2u-bbs python=3.7 django=2.1

![1563775877874](assets/1563775877874.png)

然后安装完毕以后，你就可以coa up2u-bbs进入这个环境，开始你的Django学习之旅。

![1563776494929](assets/1563776494929.png)

&nbsp;

## 二.文档学习

#### 1.学习链接

学习的地方必须是官网，官网里面就含有汉化的教程。

https://docs.djangoproject.com/zh-hans/2.1/

![1563776223358](assets/1563776223358.png)

我们这篇博客会在这个快速入门的文档上面进行学习，搭建属于我们的Django项目!

&nbsp;

#### 2.创建项目

在创建项目之前我们可以看看当前cmu的路径是C:\Users\hp

难道我们的Django项目就放在这个地方吗，毫无疑问肯定不是，所以我们需要切换路径

```
D:
cd D:\Program Files\PythonCode\django
```

![1563776677150](assets/1563776677150.png)

当我们切换好路径以后，我们就可以照着官方文档去创建一个项目了

![1563776736603](assets/1563776736603.png)

注意，这个命名的时候千万不要用Django或者Python关键字来命令，那样会引起错误。

输入```django-admin startproject mysite```自动创建一个文件夹与py配置文件。

创建成功以后，输入```cd mysite```，进入这个文件夹：

![1563776861869](assets/1563776861869.png)

如果你刚好安装了个vscode，不妨就继续输入```code .```这条命令，打开这个项目工程吧!

（打开vscode的时候，千万别忘记先切换Python环境到up2u-bbs哦！）

打开以后，你会发现左侧栏有一个mysite文件夹与manage.py在项目里。

![1563777047420](assets/1563777047420.png)

&nbsp;

这些玩意到底是什么，我们可以回到官方文档继续阅读，它会告诉我们答案：

![1563777146822](assets/1563777146822.png)

请你好好仔细阅读文档，或者你懒得打开网站，就读一下这张图片。

这些py文件非常的重要，它们是Django项目的依赖设置。

当你读完以后，你可以回到ConEmu，测试一下你的Django项目是否启动成功：

输入```python manage.py runserver```来启动Django项目，不出意外你会看到这样的玩意

![1563777343150](assets/1563777343150.png)

请忽略红色的报错，这只是有关未应用最新数据库迁移的警告，稍后我们处理数据库。

然后打开http://127.0.0.1:8000/

![1563777425416](assets/1563777425416.png)

如果你看到这样的网页，这代表你的Django简易项目成功启动了，我们正式进入开发之旅。

&nbsp;

#### 3.生成数据库

我们启动项目以后，可以发现vscode项目里生成了一个文件叫做db.sqlite3

这个db一看就是database的缩写，是数据库的意思，正好可以解决一下上面的报错

我们按ctrl+c退出正在运行的Django报错，按照上面红色报错的指引，

输入```python manage.py migrate```配置数据库：

![1563778064986](assets/1563778064986.png)

然后再输入```python manage.py runserver```重新启动Django项目即可。

&nbsp;

事实上我们可以仔细探讨一下这个数据库，在vscode中查找一下py文件

发现在settings.py中找到了相关的配置信息，发现这是一个引擎文件：

![1563778296190](assets/1563778296190.png)

这个时候我们自然需要一个可视化管理数据库的工具DB Browser for SQLite。

https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.11.2-win64.msi

请将这个链接复制到迅雷下载，有会员的话就更nice了。

下载成功以后，启动一下这个软件，点击打开数据库，找到Django项目的db.sqlite3文件启动：

![1563779718021](assets/1563779718021.png)

我们的生成数据库与控制数据库的目的就完成了，这些暂时搁浅，后面会用。

&nbsp;

## 三.投票应用

#### 1.添加应用

mysite项目只是我们的入门启动项目，我们可以再复习一遍上面的操作，重新创建一个项目

因为我们是up2u-bbs环境，所以我们真正的项目文件应该命名为up2u_bbs（文件命名不允许横杠）

因此，我们输入```cd ..```回到上一级目录，然后输入```django-admin startproject up2u_bbs```创建新的工程。

再然后输入```cd up2u_bbs```进入我们新创建的Django工程文件，```code .```用vscode启动此项目

&nbsp;

现在，我们根据官方文档的指引，去做一个投票应用网站：

![1563780206715](assets/1563780206715.png)

就根据它所描述的，输入```python manage.py startapp polls```，完成以后你应当在vscode看见这样：

![1563780305127](assets/1563780305127.png)

这个polls目录就包括了投票应用的全部内容。

然后往下浏览，开始编写我们的第一个Django视图，打开polls/views.py，编写以下的Python代码:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("大家好啊，我们正在学习Django呢！")
```

然后想要看见上面代码显示的视图，需要将一个url映射到这个视图去展示：

所以我们在polls文件夹下面，新建一个urls.py文件，然后编写Python代码如下：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

这个文件是什么意思呢，就是通过urls.py的代码连接到views视图的index函数视图。

然后这个还需要被送往到总urls.py文件，也就是up2u_bbs下的urls.py，将代码补全：

```python
path('polls/', include('polls.urls')),
```

![1563781169178](assets/1563781169178.png)

这些准备工作就绪以后，回到ConEmu去启动```python manage.py runserver```

（这个时候还没生成数据库，所以要先弄出db.sqlite3文件）

打开我们的网站，在url后面加进去/polls/，我们就可以看到我们创造了新的网页：

![1563781270758](assets/1563781270758.png)

&nbsp;

看明白了吗，我们所做的操作就是添加了一个新的网页站点，那么这个过程到底是怎么样的呢?

```
python manage.py startapp polls（创建一个应用） -->

polls/views.py（在当前应用创建一个视图）--> 

polls/urls.py（将视图映射当前应用的URLS）--> 

up2u_bbs/urls.py（将这个应用的URLS映射到总项目的URLS）-->

python manage.py runserver（启动这个总项目去查看应用的内容）
```

&nbsp;

#### 2.创建模型

先按ctrl+c退出Django项目，输入```python manage.py migrate```生成数据库，然后用SQLite软件控制

![1563782197586](assets/1563782197586.png)

在这个简单的投票应用中，需要创建两个模型：问题 Question和选项 Choice。Question 模型包括问题描述和发布时间。Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。

![1563782389420](assets/1563782389420.png)

模型是一切的起源，是一个非常重要的概念，取决了你要做什么。

&nbsp;

模型在python中就是一个类，我们在polls/models.py中拷贝以下代码进去：

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

我们可以发现这两个模型一共有5个变量，换句话说是字段，这些字段全是Field类的实例。

括号参数里面是告诉了Django每个字段要处理的数据类型。

然而最值得我们注意的是Choice模型下的question变量，使用了ForeignKey定义：

![1563782784562](assets/1563782784562.png)

这就是外键的意思，这将告诉 Django，每个Choice对象都关联到一个Question对象。这不就好比一道题目有四个选项嘛，就是这个意思。Django 支持所有常用的数据库关系：多对一、多对多和一对一。

&nbsp;

#### 3.激活模型

创建了模型之后应该干嘛？当然是激活模型啊！

激活模型成功之后，Django就可以根据这个模型去为这个应用创建数据库，这样就可以使用投票应用，但是在此之前，我们需要将polls应用安装到我们的Django项目。

（这句话暗示了Django的应用是可插拔的，可以将一个应用安装到不同的项目之中，类似于Vue的组件开发）

在up2u_bbs/settings.py中将```'polls.apps.PollsConfig'```加入进去：

![1563783247825](assets/1563783247825.png)

然后你的Django项目就会包含polls应用，回到ConEmu让配置生效

输入```python manage.py makemigrations polls```，不出意外你会看到这个：

![1563783764451](assets/1563783764451.png)

这是成功创建两个模型的意思，但是你发现没，这些被存储在0001_initial.py的py文件里。

我们可以看看这个文件的芳容：

![1563783932919](assets/1563783932919.png)

这就是一个活生生的数据库配置文件。

但是这个时候，你会突然发现，这只是polls应用的数据库配置文件，我们还没有将其应用迁移到总项目数据库。

输入```python manage.py migrate```，你可以看到这个：

![1563784101121](assets/1563784101121.png)

至于为什么要这样做，我觉得官方文档解释的非常漂亮，直接截图过来吧

![1563784149958](assets/1563784149958.png)

这个时候，我们就可以打开SQLite软件，目前我还没研究出来笔记本怎么刷新这个数据库，我选择的是重新打开数据库文件来进行刷新；有机械键盘的直接按F5刷新，我们可以发现新产生了两个表和一个索引

![1563784364443](assets/1563784364443.png)

当然，这两个表肯定是空的，还需要我们的后续进一步操作。

&nbsp;

所以我们回顾一下上面的操作，我们是怎么样创建模型并激活的？

```
如果还没有db.sqlite3文件，先输入python manage.py migrate生成数据库 -->
polls/models.py（创建模型，编写Python代码） -->
up2u_bbs/settings.py（将polls应用加入配置文件） -->
python manage.py makemigrations polls（产生polls应用的数据库配置文件） -->
python manage.py migrate（将配置文件进行迁移应用到全局） -->
使用SQLite软件验证是否创表成功
```

&nbsp;

#### 4.命令交互

模型激活之后，我们需要进入交互式Python命令行，尝试一下 Django 为你创建的各种 API。

如果你是我Relearn-Python博客系列的读者，你肯定第一时间会想到ipython，更为优秀的命令行存在。

所以我们直接```pip install ipython```吧！

安装完之后输入```python manage.py shell```进入命令行交互模式，你会看到这样：

![1563785450028](assets/1563785450028.png)

然后依次输入以下的交互命令：

```python
from polls.models import Question, Choice
from django.utils import timezone
q = Question(question_text = "最好的编程语言是什么？",pub_date = timezone.now())
q.save()
```

![1563785794478](assets/1563785794478.png)

这四条命令到底是什么意思呢，其实你也能直接看得出来，这是创造了一个提问，还引入了时间模块，标注了这个题目被创建的时间点，你在软件中点击查看polls_question表也能看到：

![1563786150717](assets/1563786150717.png)

q变量就相当于你所创建的提问题目的变量，你可以去访问它的id与时间点：

![1563785966228](assets/1563785966228.png)

你甚至还能修改它的提问题目，但是你别忘记了要save()一下，你还能在软件里查到这个q的改动：

![1563786086145](assets/1563786086145.png)

最后，你可以输入```Question.objects.all()```查看当前所有的提问题目对象：

![1563786233551](assets/1563786233551.png)

但是官方文档说，这个对象的结果没有什么帮助，我们需要修改下polls/model.py，这样能够帮助我们更为直观地感受到提问的问题是什么：

![1563786420329](assets/1563786420329.png)

所以根据它的说法，我们回到vscode将这两段def函数加进去：

![1563786488496](assets/1563786488496.png)

保存改动以后，在ipython输入exit()，再重新```python manage.py shell```启动进入，再输入

```python
from polls.models import Question, Choice
Question.objects.all()
```

可以发现，返回的结果更为直观：

![1563787089029](assets/1563787089029.png)

这就是一个小小的技巧，使用```__str__```函数来完成，将返回的结果从数量修改成text文本。

当然了，还有另外一个小技巧，也是官方文档提供的，你可以直接更新这些代码进去，然后重启shell：

![1563787379943](assets/1563787379943.png)

这个小技巧的目的就是给Question对象创造一个自定义的方法，将在后面中进行使用，从代码的意思看得明白，这是判断是否是被发布时间在一天时间内的自定义方法。

&nbsp;

我们现在可以接触一些简单的筛选问题的方法，目的是为了抓取指定对象：

```python
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='世界')
```

值得一提的是第二个筛选方法，它的原型其实是question_text.startswith('世界')，在django中成了双下划线和等于号的形式，这个也是一个需要大家的一个记忆点。

![1563787800680](assets/1563787800680.png)

也可以通过timezone模块，来筛选创建时间是今年的问题：

```python
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
```

![1563788141524](assets/1563788141524.png)

注意，我们这个不再是filter()方法，因为你要弄清楚filter()返回的结果是一个列表，还需要索引操作抓取，而get()却能将找到的结果作为返回值，进行使用。

所以，可以再输入一条命令```q = Question.objects.get(pub_date__year=current_year)```获取到这个对象：

![1563788123267](assets/1563788123267.png)

当然了，获取到这个对象的方法还可以是```q = Question.objects.get(pk=1)```

这个方法是官方推荐的，等价于Question.objects.get(id=1)，我们还可以验证一下刚才弄的自定义方法：

![1563788380418](assets/1563788380418.png)

好了，现在我们已经学会了如何从现有Question对象里面获取到想要的具体变量对象，接下来该配置选项上去了，也就是说，给这个q提问对象配置上几个选择选项。

&nbsp;

输入```q.choice_set.all()```查询此提问对象的选项，肯定是空的，因为我们还没配置：

![1563788601130](assets/1563788601130.png)

如何添加选项呢，根据官方文档的描述，应当使用的方法是```q.choice_set.create()```

所以我们可以一口气配置四个选项进去：

```python
q.choice_set.create(choice_text='C++', votes=0)
q.choice_set.create(choice_text='PHP', votes=0)
q.choice_set.create(choice_text='Java', votes=0)
q.choice_set.create(choice_text='Python', votes=0)
```

然后再输入``q.choice_set.all()``查看当前的选项：

![1563788833020](assets/1563788833020.png)

（这个votes=0是默认票数的意思，自然是设置为0）

当然了，我们的选项是可以作为对象进行操作的,再创建一个选项，等下会进行删除

输入```c = q.choice_set.create(choice_text='Master', votes=0)```

我们就拿到了c变量，可以进行一系列的操作：

![1563796746321](assets/1563796746321.png)

当然了，Master并不是语言，我们可以删掉这个选项，输入```c.delete()```就可以删除

![1563796797803](assets/1563796797803.png)

当然了，也可以通过filter()方法去找到选项对象

![1563797604047](assets/1563797604047.png)

最后的最后，请灵活使用```q.choice_set.all()```与```q.choice_set.count()```查看选项的情况。

![1563796871343](assets/1563796871343.png)

&nbsp;

看明白了吗，我们使用命令交互的方式去创建提问的题目与提问的选项，这个过程可以在SQLite看到

![1563796991397](assets/1563796991397.png)

question_id都是1，说明这些选项都属于第一道提问。我们在这儿做一个小节总结：

```
1 - from polls.models import Question, Choice（引入题目与选项的两个模型）
2 - q = Question(question_text = "最好的编程语言是什么？",pub_date = timezone.now())
3 - q.save()（创建好题目以后肯定要保存生效一下）
4 - Question.objects.filter(question_text__startswith='世界')（注意startswith的转化）
5 - q = Question.objects.get(pk=1)（官方推荐的获取对象方式）
6 - q.choice_set.create(choice_text='C++', votes=0)（根据字段创建一个选项）
7 - c.delete()（选项变量可以作为对象，进行自删操作）
8 - c = q.choice_set.filter(choice_text__startswith='Master')[0]（抓取到某个选项作为对象）
9 - q.choice_set.all()（查询这个题目所有选项的信息）
10 - q.choice_set.count()（查询这个题目的选项数量）
```

&nbsp;

#### 5.管理页面

当我们搞定模型，题目与选项之后，我们该来搞一搞页面了

（页面上面同样也能进行后台设置，比命令交互便捷许多，但前者依旧是必学技能）

搞页面必然有后台管理页面，需要配置一个管理员帐号，这个时候我们并不需要关掉ipython

可以选择新增一个cmu窗口，进行配置管理员

输入```python manage.py createsuperuser```进行配置

输入名字，邮箱可以不填直接回车，密码不能太过于简单：

![1563798968667](assets/1563798968667.png)

然后你就可以```python manage.py runserver ```，进入这个网址

然后url的后面输入/admin/站点，会来到一个登陆界面，输入账号密码登陆上去是这样的界面

![1563799076129](assets/1563799076129.png)

成功了以后，我们能干啥？当然是将投票应用加入进去，也就是告诉管理页面，问题 Question`对象需要被管理。所以我们得编辑一下polls/admin.py：

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

这段代码的意思就是，向管理员注册问题Question类，保存修改以后，我们回到管理页面，刷新一下

![1563800330282](assets/1563800330282.png)

发现Questions类成功被注册，当然了，Choice类也不能忘记

在polls/admin.py补上这两句```from .models import Choice```和```admin.site.register(Choice)```

![1563802005997](assets/1563802005997.png)

这个方法要比命令交互快很多，可以直接在网页端上面进行修改题目和选项。当然了，这是windows专属的，如果在真实开发环境，那是linux，肯定只能用命令交互的方式去修改题目与选项。

现在我们进行网页可视化操作，再给我们的题目添加一个选项：

进入Choice类页面，点击右上角的ADD CHOICE

![1563802184450](assets/1563802184450.png)

然后选择好题目，输入Ruby语言，Votes当然还设置为0，点击保存完成添加选项的步骤：

![1563802322601](assets/1563802322601.png)

这样一来，Ruby选项就成功添加进去了，我们可以回到ipython命令行，输入```q.choice_set.all()```检查下

可以发现，后台确实是同步成功了：

![1563802421570](assets/1563802421570.png)

当然了，命令交互依旧是优先使用，能熟练是最好的。

因为在真实的开发环境中，肯定还是linux上面，可没有网页让你便捷操作。

&nbsp;

#### 6.更多视图

视图在应用中是非常重要的组成部分，它能集成网页展示与功能实现于一身。

官方解释视图的重要性就很通俗易懂：

![1563802809918](assets/1563802809918.png)

好了，让我们给投票应用编写更多的视图吧！

在polls/views.py中，编写三个视图，实际上就是三个python函数，代码如下：

```python
def detail(request, question_id):
    return HttpResponse("你正在看这个投票：%s"%question_id)

def results(request, question_id):
    response = "你正在看投票的结果：%s"
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("你正在参与这个投票：%s"%question_id)
```

然后该干什么啊，把这些新试图添加进去polls/urls.py，形成一个映射：

```python
path('<int:question_id>/', views.detail, name='detail'),
path('<int:question_id>/results/', views.results, name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
```

![1563803352448](assets/1563803352448.png)

这个```<int:question_id>```是什么你不必疑惑，这个相当于一个转换器，可以转换到1，相当于第1个问题

![1563803898995](assets/1563803898995.png)

然后你就可以在url输入一下：http://127.0.0.1:8000/polls/1/vote/

能看到有一段你写的文字就说明映射成功！有人可能就问了，我是不是少了一步，映射到总urls.py？

大哥，那是应用的urls映射，我的polls应用早就被加入到总urls.py，无需下一步操作！

&nbsp;

当然了，以上的操作只是配置操作，完成了urls映射的配置，我们接下来编写一个真正有用的视图：

其实就是index()函数的视图，需要修改了，不再是简单的打招呼，将我们的投票问题展示上去

```python
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```

现在的话，新的问题就又来了，我如果这样写，就相当于页面的设计写死在视图函数的代码里的，如果你想修改网页，你得重新编辑修改python代码，这个做事效率无疑是巨慢的。

所以让我们使用 Django 的模板系统，只要创建一个视图，就可以将页面的设计从代码中分离出来。

在polls应用下，创建个templates/polls/index.html，为什么要这样的目录结构，官方给出了解释

![1563804844655](assets/1563804844655.png)

这是没办法的，Python就是怕遇到重名的文件夹玩意，所以我们要尽量地去避开：

![1563804946336](assets/1563804946336.png)

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

其实我也看不懂这段代码，反正直接拷贝进去index.html就行了，以后总会慢慢弄懂的！

这个时候，就可以再更新一下polls/views.py文件了

```python
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

这个时候，你的views.py文件就会是这个样子的：

![1563805148678](assets/1563805148678.png)

这个index()函数代码到底完成了一个怎么样的过程呢？

首先就是获取到Question对象的提问实例，提取出根据时间排序的前5个成为列表，然后加载polls/index.html模板文件，并且向它传递一个上下文(context)，将列表参数传递进去，这个上下文是一个字典，它将模板内的变量映射为 Python 对象。加载之后，再return返回来模板渲染加载后的结果显示在网页。

所以，打开http://127.0.0.1:8000/polls/

你会看到这个模板已经被渲染成功了！

![1563806820938](assets/1563806820938.png)

&nbsp;

接下来就轮到详情视图，还记得那个404吗，没错，我们也要给详情页整一个404

当你访问不存在的question_id的时候，自动抛出404的异常页面进行展示，我们可以把这个过程加入到detail视图

```python
from django.http import Http404

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("这个问题的id不存在！")
    return render(request, 'polls/detail.html', {'question': question})
```

你肯定也看得懂这段代码，使用了异常处理，存在就正常返回，不存在就抛出Http404异常。

下一步可别忘了，还是要再弄一个polls/templates/polls/detail.html，进行代码分离：

```python
{{ question }}
```

这样一来，我们就可以测试一下这个detail视图了

我们可以输入http://127.0.0.1:8000/polls/2/

不出意外的话，Http404异常应该是正常抛出的，效果如下:

![1563807825664](assets/1563807825664.png)

当然了，抛出404异常还有个更加简洁的函数来完成，了解一下或者去尝试一下都可以:

![1563807945128](assets/1563807945128.png)

我们虽然搞定了detail()视图的模板渲染与404异常抛出，但是我们的页面设计还需要完善

意思就是说，在进入详情页之后，应当展示出投票的标题与投票的选项，而不是干巴巴的如下:

![1563808077830](assets/1563808077830.png)

所以我们需要在detail.html完善代码，编写我们的前端设计：

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

这段代码是什么意思呢，就是将这个投票的标题以h1标签展示，投票的选项以无序列表的形式展示。

这个时候，我们的详情页就发生了变化：

![1563808190085](assets/1563808190085.png)

正是这个地方，我们正式接触到了全栈开发的雏形，我们会在后面一步步完善自身的能力。

&nbsp;

#### 7.修改URL

url的完善也是非常有必要的，我们来看看index.html里的这段代码:

![1563867015586](assets/1563867015586.png)

有没有觉得这儿直接写死了url地址？如果我在后面要修改url的时候，是不是修改起来很麻烦？

如果我想改成/polls/questions/1/，是不是得先改下polls/urls.py，然后再来改HTML里面的代码？

这样的写法肯定是不好，我们需要换个写法，让这个地方链接到urls.py里面的设置：

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

![1563867255265](assets/1563867255265.png)

![1563867451649](assets/1563867451649.png)

这样一来，你如果想修改url的时候，只需要在polls/urls.py任意修改即可，非常便捷。

&nbsp;

当然了，上面只考虑到了一个应用的情况，然而Django项目是可以有很多个应用的，那么这些应用如果都有detail视图，Python应该如何分辨重名的url呢？

也就是```{% url %}```标签，它到底对应哪个应用呢？所以我们还是需要继续操作：

![1563867633843](assets/1563867633843.png)

我们回到vscode将```app_name = 'polls'```加入到polls/urls.py中,然后回到index.html文件修改这个地方

![1563867775839](assets/1563867775839.png)

这样一来，Python就能准确地区分哪些视图属于哪些应用了。

&nbsp;

#### 8.完善表单

项目设计已经到了尾声，我们应该让这个应用变成真正的投票应用了，也就是设计出表单与按钮，表单肯定是radio单选框属性，然后按钮是submit提交属性。

这个修改过程，肯定还是在detail视图进行，毕竟你在首页点击标题进去之后，就可以开始投票了啊！

我们来看看detail.html的代码应该如何被更新：

```python
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

如果你没有html基础，那真是不好的消息，但事实上这段代码也没那么难看懂。

1）第二行代码就是如果投票报错，会返回error_message，网页显示报错信息

2）表单是用来POST提交数据的，也就是说，POST用来改变服务器端数据的手段，这是常识

3）{% csrf_token %}属于Django的安全特性，防止跨站点请求伪造的手段

4）forloop.counter是for标签循环多少次的当前值，所以选项的id会是choice1、choice2等

5）{% endfor %}类似于for循环的边界，如果不用的话，会把下面的代码一并带入循环

如果你看懂了我这5点，这说明你的理解天赋还是到位的，这段代码属于模板语言，我们会在后面进行一个系统地学习，直到我们能玩转模板语言，到那个时候我们就就拥有开发Django项目的能力了。

当你使用这段代码的时候，你会发现你的网页端已经发生了变化:

![1563868859513](assets/1563868859513.png)

已经很有意思了，我们继续下一步的操作，就是解决vote投票按钮，以及vote视图显示投票的结果。

我们的views.py中只剩下vote()视图函数没有进行编辑了:

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Choice

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "你还没选择一个选项呢！",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

这段代码又会是什么意思呢，可以发现，我们针对404采用了那个更为便捷的函数get_object_or_404()，函数名字本身就通俗易懂，找到就成对象，找不到就返回404异常，然后我们get()到detail.html那边传来的POST请求，这里面含有选项的具体信息，然后给它的votes参数加上1，最后还要进行保存结果。

except代码块那儿就很好懂了，就是你如果啥都不选直接投票，会抛出个error_message参数表示异常，正好打印在detail.html里面的```{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}```这儿，完成首尾呼应。

&nbsp;

vote视图函数搞定了，已经启动了后台的计数功能，现在我们应该修改results视图与results的html页面，让后台计数的结果打印在页面上。先来编辑下polls/views.py里面的results函数:

```python
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

你们可能就有疑问了，这个results该如何接收到参数呢，答案就在vote视图函数的最后一行：

![1563869553342](assets/1563869553342.png)

然后我们就编辑polls/templates/polls/results.html，将以下的代码传授进去：

```python
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">还需要继续投票吗？</a>
```

这段代码现在对你来说，已经变得非常通俗易懂了，我就不再过多解释了。

然后你就可以在网页端进行投票了，我投票了三次之后，最后的结果就是这样的：

![1563869751122](assets/1563869751122.png)

至此，我们已经根据官方文档，完成了投票应用的项目编写，也没必要深入下去了，后面无非是自动化测试，定义css，完善前端页面，打包应用等等，因为我们的目的是快速入门，快速上手感受一下，所以学到这个地步就可以了。我们接下来就是进入真正的实战，从0开发，锻炼自己的Django基础知识。

&nbsp;

## 四.BBS应用

#### 1.学习须知

在前面，我们按照官方文档过了一遍投票应用的学习，效果还是不错的。

至少我们能够感受到完整的一个Django开发流程，虽然真实开发环境只会更难。

现在，我们读一下投票应用的总结流程，再次过一遍Django的开发流程。

| 序   | 详细操作与命令                                               |
| ---- | ------------------------------------------------------------ |
| 1    | 创建Django环境：cc up2u-bbs python=3.7 django=2.1            |
| 2    | 创建Django项目：django-admin startproject up2u-bbs           |
| 3    | Vscode启动这个项目：code .                                   |
| 4    | 运行这个Django项目：python manage.py runserver               |
| 5    | 配置数据库文件：python manage.py migrate                     |
| 6    | 添加polls应用：python manage.py startapp polls               |
| 7    | 配置polls应用的urls： polls/urls.py --> up2u_bbs/urls.py     |
| 8    | 创建应用的模型：编辑polls/models.py                          |
| 9    | 激活模型的数据库：添加参数进up2u_bbs/settings.py             |
| 10   | 生成应用的数据库迁移文件：python manage.py makemigrations polls |
| 11   | 让应用的数据库迁移文件生效：python manage.py migrate         |
| 12   | 安装更好的Python命令交互shell： pip install ipython          |
| 13   | 进入Django的命令交互API： python manage.py shell             |
| 14   | 注册管理页面账户：python manage.py createsuperuser           |
| 15   | 向管理页面注册模型：编辑polls/admin.py                       |
| 16   | 完善更多视图：编辑polls/views.py                             |
| 17   | 将视图呈现到html：创建polls/templates/polls/xxx.html，避免python遇到重名问题 |
| 18   | 使用更灵活的url格式：{% url 'detail' question.id %}          |
| 19   | 多应用时的最终url格式：添加app_name到polls/urls.py，然后改成{% url 'polls:detail' question.id %} |
| 20   | 完善页面逻辑：灵活使用表单，使用GET从服务器端获取数据，使用POST发送数据到服务器端 |

&nbsp;

现在，我们来开发一个BBS网络论坛，这是一个实战的项目，从0开发，锻炼逻辑！

我们设计这个的项目的整个流程肯定还是跟官方文档差不多，无非还是遵循：

模型设计 --> 配置settings.py --> 创建数据库  --> 命令交互数据操作 --> 路由设计 --> 创建视图 --> 加载模板

我建议大家可以背下这条路线，虽然不同的项目有不同的详细路线，但基本都基于这个路线。

OK，话不多说，让我们开始启动新项目的编程！

&nbsp;

#### 2.模型原理

模型设计是个非常重要的部分，是一切的基石，我们先分析一下投票应用的两个模型吧：

首先```from django.db import models```是必须的，引入models模块进行模型设计

![1563878193181](assets/1563878193181.png)

我们可以看到，一共四个字段，它们都是怎么命名的，都是models.XXXField()这种形式，对吗？

我们正好也可以学习一下，有哪些字段：

- IntegerField，从-2147483648到2147483648的整数字段
- BigIntegerField，-9223372036854775808到9223372036854775807的整数字段
- FloatField，浮点数字段，含小数点的数字
- CharField，字符串字段，max_length是个很重要的参数，设置为最大长度
- TextField，可以理解为大型的字符串字段，或者说是文本字段，可含大量文本
- DateField，日期字段，原型是Python的datetime.date实例
- DatetimeField，日期和时间字段，原型是Python的datetime.datetime实例
- EmailField,，邮箱字段，检查该值是否为有效的电子邮件地址

事实上，字段是非常多的，我挑了几个比较常用的，都是值得记忆的字段，更多的字段请自行阅读:

https://docs.djangoproject.com/zh-hans/2.1/ref/models/fields/

当然了，Choice类里面的question变量，实际上也是一种字段，这个叫做关系字段。

我们就列出三种关系字段，一共有三种，同样是建议背诵的：

- ForeignKey，多对一的关系字段，需要两个位置参数，第一个参数指定哪个类一对多
- ManyToManyField，多对多的关系字段，需要一个类作为参数就可以多对多
- OneToOneField，一对一的关系字段，类似于主键关系

我觉得吧，模型设计其实就是个编写数据表的过程，反映出几对几的映射关系的过程！

所以拥有SQL基础的同学对于这块肯定上手地非常快！

总之不要害怕这部分的知识吃不透，这只是时间问题，做的项目多了，模型设计自然就会了！

&nbsp;

#### 3.模型设计

然后我们弄明白这个模型设计的原理之后，大概知道了怎么样去编写代码，我们现在就要准备创建应用了，没错，我们还是基于原来的up2u_bbs的项目基础上，再添加一个bbs应用，进行开发就行了！

在cmu输入```python manage.py startapp bbs```，将bbs应用添加进去

然后在vscode中打开bbs/models.py，开始设计bbs所需要用到的模型：

&nbsp;

先反思一下这个BBS是不是跟上面投票应用的模型很像？

BBS的帖子主题等同于投票应用的标题，帖子的评论等同于投票应用的选项？

然后我们需要再设计一个新的字段，就是作者字段，帖子主题的作者与评论的作者。

所以我们直接拷贝前面的models.py代码，然后进行加工一下，模型就成功设计出来了：

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text

```

我就简单地分析一下现在的代码吧！

![1563892684845](assets/1563892684845.png)

模型设计完以后应该干嘛啊？当然是激活模型了，激活模型要到up2u_bbs/settings.py去激活。

&nbsp;

#### 4.settings.py

说到激活模块，在settings.py，在激活之前，我觉得有必要讲解一下这个settings.py到底是什么作用

你要知道，这个settings.py实际上是个配置文件，它只是一个使用模块级变量的一个python模块

![1563889854020](assets/1563889854020.png)

你肯定会疑惑，这些配置的选项到底有什么用呢，它们分别是干什么的？

不要着急，我会拆分这个settings.py每一行代码，讲清楚这些配置项有啥用：

- SECRET_KEY： Django的加密key密钥，提供于加密签名，用来项目的启动认证
- DEBUG：默认是True，开启调试模式，显示详细的错误页面，但是请勿在生产环境开启，防止泄密！
- ALLOWED_HOSTS：表示Django站点可以提供的主机域名的字符串列表。
- INSTALLED_APPS：表示Django已安装并能启用的所有应用程序的字符串列表，添加应用时操作的地方。
- MIDDLEWARE：中间件，相当于类，在请求到来和结束后，django会根据规则在合适时机执行相应的方法。
- ROOT_URLCONF：表示根URLconf的完整Python导入路径的字符串。
- TEMPLATES：加载后端模板，包含与Django一起使用的所有模板引擎的设置的列表。
- WSGI_APPLICATION：内置服务器启动WSGI应用程序对象的完整Python路径。
- DATABASES：配置数据库的选项，是一个嵌套字典，将数据库别名映射到包含单个数据库选项的字典。
- AUTH_PASSWORD_VALIDATORS：用于检查用户密码强度的验证器列表。
- STATIC_URL： 引用位于的静态文件时使用的URL。

这些配置选项都是默认自带的选项，在生产环境中我们肯定要主动去添加一些配置进行项目上线。

这些都是要自己主动学习的，参考文档还是要认准官方文档，主要了解有哪些配置选项：

https://docs.djangoproject.com/zh-hans/2.1/ref/settings/

&nbsp;

#### 5.激活模块

当然了，激活模块的过程不就是生成数据库吗，我们要配置的数据库就是这儿：

![1563891463612](assets/1563891463612.png)

但是这个选项使用的是sqlite3数据库，一种轻量级数据库，难道就不能用别的数据库来充当后端角色?

我们上官方文档查询一下数据库引擎，得到了这样的结果：

![1563891562829](assets/1563891562829.png)

这说明Django后端还支持MySQL、Oracle和PostgreSQL数据库等，所以我们需要记住这一点，以后做大型Django项目的时候，就需要修改掉这儿的DATABASES配置。

我们这次的BBS项目依旧是小型项目，所以就继续使用sqlite3轻量级数据库了。

&nbsp;

言归正传，我们要激活模块了，自然是要往INSTALLED_APPS添加我们刚创建的BBS应用

添加进去```'bbs.apps.BbsConfig',```在第一行，进行保存，然后回到ConEmu

输入```python manage.py makemigrations```生成数据库迁移文件，发现如下：

![1563892225719](assets/1563892225719.png)

这就说明创建模型成功，然后再输入```python manage.py migrate```将数据库迁移文件应用到Django服务器

这个时候，就可以打开我们的SQLite软件看看新生成的表：

![1563892368040](assets/1563892368040.png)

这个时候，我们的数据库就成功部署起来了。

&nbsp;

#### 6.认识MTV

现在我们已经搞定了BBS项目的模型设计与数据库部署，继续往下就是通过API生成帖子和评论了。

在此之前，我们需要深入了解一下Django底层，搞清楚Django到底是一个怎么样的架构？

```
Django是一个MTV框架：即模型(Model)、模板(Template)和视图(View)三部分。
```

但是请你注意，并不是M到T再到V，而是M到T和V！

![1563899386985](assets/1563899386985.png)

这个M是ORM，大家应该没有了解，ORM就是通过使用描述对象和数据库之间映射的元数据，将编程语言创造的对象映射到数据库中的一种机制，在Python中数据库的内容表现为对象关系映射制定数据结构，如果你之前有过Python控制数据库的经历，应该对ORM不陌生。

粗暴的解释，ORM就是通过编程语言去对数据库增删改查的操作。

至于这个T和V，你可以理解为是同时进行的，也可以理解为双向绑定，因为页面的展示与逻辑的编写就是通过函数设计，然后return使用render()方法将得到的对象结果返回到html文件中进行渲染数据，这两者是互为关联的过程，所以整个过程就称为MTV架构。

除了MTV架构以外，我们应当还需要重视路由控制，也就是url的设计，在Django中是一个很重要的开发环节，这样的过程就很类似大名鼎鼎的MVC设计思想，MTV到MVC的过程其实也说得通。

&nbsp;

如果你还是看不懂上面的MTV架构原理的解释，我只好拿投票应用的例子，给你们一步步分析一下数据在Django项目中走通的流程。

1）首先我添加了polls应用，创建了两个模型，实际上就是两张数据库表

![1563900262042](assets/1563900262042.png)

2）然后我通过API交互操作，给我的两张数据表添加进去数据，此时已经有一个含有几个选项的投票了

![1563900462872](assets/1563900462872.png)

3）编辑views.py，注意，这儿有需要重点理解的地方，为何要引入两个模型进去

![1563900608981](assets/1563900608981.png)

4）编写各个视图的函数过后，从模型里面拿到数据返回，return返回的都是render()，这是为什么呢？

![1563900813456](assets/1563900813456.png)

render()其实非常好用，用来将数据载入html模板完全没任何问题，你可以看下面的图了解更多知识

![1563900882871](assets/1563900882871.png)

5）视图函数返回拿到的数据对象结果之后，传递到html文件进行渲染，将数据在网页展示

![1563901033997](assets/1563901033997.png)

6）最后的最后，我们的数据终于走完了所有的流程，完成了MTV架构，来到了网页上面

![1563901130025](assets/1563901130025.png)

所以，聪明的读者们，再问你们一遍，你们看懂MTV架构了吗？

&nbsp;

#### 7.API交互



