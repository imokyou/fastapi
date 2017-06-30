# 一个轻量、高性能的API服务
# http://falcon.readthedocs.io/en/stable/user/quickstart.html
##　使用到的框架及工具
cpython
falcon
gunicorn
meinheld
supervisor
mysql
redis
celery
virtualenv
httpie


gunicorn --workers=2  --worker-class="egg:meinheld#gunicorn_worker" things:app

## gunicorn things:app

## 模拟手游统计数据收集接口
1. GET发送
2. 整段参数base64
3. md5(key + timestamp)
4. 一次可发送多条记录，即一个list
5. nginx记录请求log
6. 队列形式写入，避免出现波峰
7. 记录业务日志及错误日志，出现错误时可恢复数据，日志只存最近3天，其他上传到别的地方保存，比如说亚马逊s3
8. 上线前有压力测试，大致的性能统计分析
9. 新旧版可同时使用，有流量切换开关，灰度测试，可按流量百分比切换，也就是要做负载均衡
10. 有测试脚本，保证一定的测试覆盖率，要有错误报告
11. 监控报警机制，5xx过多
12. 所有数据先存到一个大表，再利用数据库/脚本统计出数据分析报表，大表只存最近N天的数据
13. 自动化部署及更新程序 anssible


## 具体实现方案
* 数据分两层存
	* 第一层先存mongodb，3/7/14天原始数据，过期上传OR下载本地保留
	* 第二层存mysql，按一定指标聚合后的数据，用作报表、数据分析等
* 请求过来直接存第一层， 用写入队列
* 数据聚合脚本每3/5分钟查询第一层数库，聚合之后写入第二层数据库主表
* 第二层数据库(mysql)触发器再具体聚合出更多报表数据
* 为什么直接存mysql然后用触发器聚合出更多报表数据， 因为这样的话mysql库就会越来越大，大表只是存数据又不用来查，很浪费空间，都是钱啊。把大表拆出来好会好多
