# 爬虫练习平台

![Deploy to Kubernetes](https://github.com/Germey/Scrape/workflows/Deploy%20to%20Kubernetes/badge.svg)

网络爬虫实验平台，包含多个样例，如纯静态网站、动态渲染网站、字体反爬网站、登录验证网站、验证码验证网站、反代理网站、JavaScript混淆及加密网站等，持续更新中。

## 案例介绍

本平台自爬数据、自建页面、自接反爬，案例稳定后永不过期，适合教学与练习。

### 登录验证网站

* [login1](http://login1.scrape.cuiqingcai.com/)：登录时用户名和密码经过加密处理，适合 JavaScript 逆向分析。

### 静态渲染网站

* [static1](http://static1.scrape.cuiqingcai.com/)：猫眼电影数据网站、数据通过服务端渲染，适合基本爬虫练习。

### 动态渲染网站

* [dynamic1](http://dynamic1.scrape.cuiqingcai.com/)：猫眼电影数据网站、数据通过 Ajax 加载、页面动态渲染，适合 Ajax 分析和动态页面渲染爬取。

## 自动部署

本平台采用 GitHub Actions + Kubernetes 自动化部署，详情见 [WorkFlow](https://github.com/Germey/Scrape/tree/master/.github/workflows)。
