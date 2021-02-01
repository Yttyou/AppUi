# testing-neptune
这个仓库是针对 SP Android QA 的自动化测试脚本的代码管理
* 1、分支信息
> master : 正式环境分支（发版分支）

> neptune_developer: 开发分支

* 2、master 分支和 neptune_developer 的区别
> 2.1 初始化功能（main_ini.py)
>> (1) 根据 ip 识别测试手机并强制安装测试包获取所有运行权限

>> (2) 读取手机配置和测试包信息写入`Caps/bc_app_config.yaml`

>> (3) 读取测试环境相关信息写入`Allure-Report/xml/environment.properties`

>> (4) 命令行方式启动 appium 服务（不同的脚本需要配置不同的服务端口，不冲突即可）

>> (5) 测试当前网速是否满足测试要求（网速>1mbps & 延迟<500ms)

>> (6) 其它：流量监控和内存监控（已经停用，暂时还未找到功能级监控方案，存在技术瓶颈）

> 2.2 后置数据处理功能（main_cal.py)
>> (1) 将结果数据存储至数据库

>> (2) 推送结果报告至 BC

>> (3) 发送测试结果邮件到指定邮箱

> 2.3 环境配置
>> (1) 通过 Common/mysql_config.py 来配置数据库环境和禅道账号

>> (2) 通过 Common/ZenTaoApiToMysql.py 来配置禅道指向的是正式还是测试环境

* 3、Jenkins 执行流程

```
graph TD
A(开发提交分支到 pre_live)-->B(提交分支触发打包:Android-SP-QA-Neptune-Build-Auto)
B-->|通过插件Changelog+gitinfo.csv传递分支提交信息|C{打包成功?}
C-->|成功|D(打包即触发自动化UI测试:Android-SP-QA-Neptune-Run-Auto)
C-->|失败|E(结束)
D-->F{脚本执行成功?}
F-->|成功|G(后置结果处理:Android-SP-QA-Neptune-AfterRun)
F-->|失败|H(结束)
G--> |结果推送: BC & 邮件+PDF文件|I(结束)
```
* 4、结果展示
> 4.1 涉及`前端`项目 https://github.com/cityfruit/Neptune-Emcharm

> 4.2 涉及`后端`项目 https://github.com/cityfruit/Neptune-Alluer

> 4.3 Web 页面 http://117.50.36.141/#/home/overall
