# SpaceX Engineering Handbook

一套基于公开可验证资料重建的 SpaceX 工程方法手册。

这不是 SpaceX 官方 Handbook，也不是对 Elon Musk 或 SpaceX 的宣传材料。项目目标是把公开材料中反复出现的工程方法拆成可追证据、可讨论、可迁移的知识库。

## 原则

- 事实、解释、公司规则分开写。
- 优先 P0/P1：官方、一手演讲、NASA 合作材料、前员工第一人称。
- 二手整理只用于导航，关键断言回到一手来源。
- “快速失败”不等于降低安全要求；真正目标是让未知尽早在最低代价、最低后果处暴露。
- 医疗器械迁移必须额外服从患者安全、法规、设计控制、验证确认和风险管理。

## 本地运行

安装 Hugo Extended 后：

    hugo server -D

站点入口：content/_index.md  
Handbook：content/handbook/  
来源库：data/sources.json  
引用组件：layouts/shortcodes/source.html

## 状态

v0.1：先建立内容结构、证据链和可运行站点。之后逐章扩写、翻译和审校。