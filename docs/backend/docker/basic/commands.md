# 常用命令

> 首次学习记录 · 2026-07-08

## 镜像

```bash
# 拉取镜像
docker pull nginx:latest

# 查看本地镜像
docker images

# 删除镜像
docker rmi nginx:latest
```

## 容器

```bash
# 运行容器（前台）
docker run nginx:latest

# 后台运行并映射端口
docker run -d -p 8080:80 --name my-nginx nginx:latest

# 查看运行中的容器
docker ps

# 查看所有容器（含已停止）
docker ps -a

# 停止 / 启动 / 删除容器
docker stop my-nginx
docker start my-nginx
docker rm my-nginx
```

## 日志与调试

```bash
# 查看容器日志
docker logs my-nginx

# 实时跟踪日志
docker logs -f my-nginx

# 进入容器 shell
docker exec -it my-nginx /bin/bash
```

## 本次小结

- `docker pull` 拉镜像，`docker run` 起容器
- `-d` 后台运行，`-p 宿主机:容器` 映射端口，`--name` 指定容器名
- `docker ps` 看运行状态，`docker exec -it` 进容器排查问题
