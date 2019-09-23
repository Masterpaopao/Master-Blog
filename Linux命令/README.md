## 一.生产实习心得

以CentOS 6为环境，以下的命令都是我认为值得复习的。

环境准备：VMware 15 pro + CentOS 6 + XShell6。

&nbsp;

#### 1）网络准备

编辑网络文件：vi /etc/sysconf ig/network-scripts/ifcfg-eth33

**vi语法的进入编辑模式：按i**

进入命令模式开始操作：按Esc

查找文件中的某些单词：Esc + / + 你要查找的单词

不想保存修改并退出：Esc + q!

**成功修改后保存退出：Esc + :wq**

网络文件内容改动参考：

```ONBOOT=yes
ONBOOT=yes

BOOTPROTO=static

IPADDR=192.168.111.140

NETMASK=255.255.255.0

GATEWAY=192.168.111.2

DNS1=192.168.111.2
```

&nbsp;

#### 2）防火墙设置

**永久关闭防火墙：chkconfig iptables off**

查看防火墙状态：service iptables status

启动防火墙：service iptables start

关闭防火墙：service iptables stop

**虚拟里联通本机：yum install samba + service nmb start + iptables -F**

&nbsp;

#### 3）JDK的安装

**解压tar.gz压缩包的方法：tar -zxvf jdk1.7.0_45.tar.gz**

删除默认安装java位置的文件：rm -rf /usr/bin/java

将解压后的jdk文件覆盖默认安装java的位置：sudo ln -s jdk1.7.0_45/bin/java /usr/bin/java

**修改环境变量文件：vi /etc/profile**

**加载修改后的环境变量文件：source /etc/profile**

检查此时的java环境是否成功变化：java -version

&nbsp;

#### 4）数据库设置

安装好数据库文件后启动：service mysql start

给数据库设置密码：/usr/bin/mysqladmin -u root password '123456'

进入数据库：mysql -u root -p 123456

输入SQL语句开放所有权限：grant all privileges on *.* to 'root' @'%' identified by '123456'; + flush privileges;

将数据库加入系统服务并开机自动启动：chkconfig --add mysql + chkconfig mysql on

打开3306端口：/sbin/iptables -I INPUT -p tcp --dport 3306 -j ACCEPT + /etc/rc.d/init.d/iptables save

&nbsp;

#### 5）进程问题

**查询xxx进程是否活跃：ps -ef | grep xxx**

查询redis进程是否活跃：ps -ef | grep redis

**杀掉某个进程：kill -9 id**

也可以通过shell编程写个脚本来关闭脚本：./startRedisAll.sh  + ./closeRedisAll.sh

&nbsp;

#### 6）虚拟机改名

查看当前虚拟机的名字：hostname

编辑虚拟机的名字：vi /etc/sysconf ig/network

输入你的新名字立即生效：hostname xxxxx

如果是克隆过来的想要改名：rm -rf 　/etc/udev/rules.d/70-persistent-net.rules + reboot

**重启虚拟机：reboot**

&nbsp;

#### 7）ssh免密登录

搞ssh免密是为了能够让我们的ssh脚本能够统一管理控制多台机器

多台机器同时输入以下的命令，暴力解决：

生成公钥+私钥，碰到提示直接回车：ssh-keygen -t rsa -f ~/.ssh/id_rsa

ssh-copy-id root@Hadoop_One

ssh-copy-id root@Hadoop_Two

ssh-copy-id root@Hadoop_Three

ssh-copy-id root@Hadoop_Four

ssh-copy-id root@Hadoop_Five

ssh-copy-id root@Hadoop_Six

测试是否免密成功：ssh Hadoop_XXX

&nbsp;

## 二.面试必问12条命令

##### 1.cd命令

`cd  /home` ：  进入/home目录 
`cd .. ` ： 返回上一级目录 
`cd ../..`  ：  返回上两级级目录 
`cd - `  ： 返回上次所在的目录 

&nbsp;

##### 2.pwd命令

`pwd` ：显示当前路径

&nbsp;

##### 3.ls命令

`ls` ：查看目录中的文件

`ll(ls -l) ` ：显示目录中的详细资料

`la(ls -a)` ：显示所有文件，包含隐藏文件

&nbsp;

##### 4.cp命令

`cp xxx yyy` ：将xxx复制拷贝到yyy

`cp -a` ：将文件的特性一起复制

`cp -r`  ：递归持续复制，用于目录的复制行为

&nbsp;

##### 5.mv命令

`mv` ：移动文件或者更改名字

`mv -f`  ：强制操作，不询问任何操作直接覆盖

`mv -i` ：如果目标文件已经存在，就会询问

&nbsp;

##### 6.rm命令

`rm`  ：普通的删除操作

`rm -f` ：强制删除文件

`rm -i`  ：删除文件前会询问你

`rm -r` ：递归删除，连同目录一起删除

`rm -rf` ：这是一个危险的命令，用于暴力删除，没任何提示

&nbsp;

##### 7.cat命令

`cat filename` ：正序查看文件的所有内容

`tac filename` ：反序查看文件的所有内容

`more filename` ：如果文件内容过长，使用more命令

`head -n 2 filename` ：查看文件的前两行内容

`tail -n 2 filename`  ：查看文件的最后两行内容

&nbsp;

##### 8.find命令

`find /home -name filename` ：从/home目录下开始搜索名字叫filename的文件

`find /home -user username` ：从/home目录下开始搜索属于名字叫username的文件和目录

&nbsp;

##### 9.chmod命令

`ls -lh` ：显示权限

`chmod ugo+rwx filename` ：设置此文件开放全部的所有权限

所有人(u)、群组(g)、其他人(o)

读(r)、写(w)、执行(x)

`chmod o-rwx filename` ：设置此文件的其他人删除读写执行的权限

&nbsp;

##### 10.chown命令

`chown username filename` ：将文件filename的拥有者设为username

&nbsp;

##### 11.grep命令

`grep love /home/master` ：在/home/master下所有的文件查找关键词love

`ps -ef | grep redis` ：在所有进程中查找有关redis的进程

&nbsp;

##### 12.系统命令

`shutdown -h now` ：关闭系统

`reboot` ：重启

`logout` ：注销

&nbsp;

## 三.进一步强化面试

##### 1.怎么查看当前进程？怎么执行退出？怎么查看当前路径？

查看当前进程：ps

执行退出：exit

查看当前路径：pwd

&nbsp;

##### 2.查看文件内容有哪些命令可以使用？

vi：编辑方式查看，可修改

cat：显示全部文件内容

more：分页显示文件内容，大文件专属

less：跟more 相似，更好的是可以往前翻页

head ：仅查看头部，还可以指定行数

tail：仅查看尾部，还可以指定行数
&nbsp;

##### 3.怎么向屏幕输出带空格的字符串，比如”hello world”?

向屏幕输出带空格的字符串：echo hello world

&nbsp;

##### 4.终端是哪个文件夹下的哪个文件？黑洞文件是哪个文件夹下的哪个命令？

终端：/dev/tty

黑洞文件：/dev/null

&nbsp;

##### 5.用什么命令对一个文件的内容进行统计？

wc命令 ： - c 统计字节数      - l 统计行数       - w 统计字数

&nbsp;

##### 6.利用 ps 怎么显示所有的进程? 怎么利用 ps 查看指定进程的信息？

查看所有进程：ps -aux 

查看xxx进程是否存在：ps -ef | grep xxx

&nbsp;

##### 7.如果一个linux新手想要知道当前系统支持的所有命令的列表，他需要怎么做？

使用命令compgen ­-c，可以打印出所有支持的命令列表。

&nbsp;

##### 8.你的系统目前有许多正在运行的任务，在不重启机器的条件下，有什么方法可以把所有正在运行的进程移除呢？

使用linux命令 ’disown -r ’可以将所有正在运行的进程移除。 

&nbsp;

##### 9.怎样一页一页地查看一个大文件的内容呢？

按理说一个more命令就够了，但是回答尽量全面一点，两个命令配合：

 cat filename | more

&nbsp;

##### 10.怎么对命令进行取别名？

这个方法建议慎用，但是如果有强烈的需求，还是没问题的：

alias la='ls -a'