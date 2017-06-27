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