# ga.dayu

## 简介

`ga.dayu` 基于阿里云的短信服务

## 使用

### 开发

启动服务：

```
python3 src/server.py
```

运行管理工具：

```
# 查看工具帮助
python3 src/manage.py
# 同步数据库
python3 src/manage.py syncdb -d
# 清空数据库
python3 src/manage.py dropdb -d --ignore-env-check
```

### Docker

可以运行 docker-compose 启动开发环境：

```
docker-compose up -d --build
docker-compose exec api bash
```

进入容器内部，操作同上
