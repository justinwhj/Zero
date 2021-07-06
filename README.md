# Zero
a python web template

# 使用说明
程序入口在 controller 文件夹下
python web_controller.py 即可

# 程序说明
本程序严格遵照MVC(模型-视图-控制器模式)
## 主程序
即web_controller.py 这里有全局的路由，负责整个web页面的跳转
## 前端部分
static 文件夹是一些页面的基本组件，即模板

templates 文件夹整个项目的所有页面
## 后端部分
model 文件夹是本PJ用到的一些实体类，如模型，口令类，这么封装的好处是一步到位，直接能够通过该类调用相应的数据表
service 是服务类，实现业务的高级逻辑
## 数据库部分
使用的mysql，一共有三张表
