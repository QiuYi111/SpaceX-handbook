---
title: "10 · 内部软件与数字主线"
weight: 15
status: "v0.1"
source_ids: ["SX-005","SX-007","SX-003"]
summary: "软件不是 IT 支持层，而是制造系统本身。"
---

2013 年 SpaceX 软件团队已经公开描述一套覆盖采购、库存、设计、工单和现场任务的企业信息系统。{{< source "SX-005" >}}

后来对内部软件团队的采访进一步展示了 Warp Drive 一类系统：原材料、采购、库存、work order、制造、质量问题、变更和零件关系被放进同一条数字链。软件工程师甚至直接到产线工位工作，以理解制造现场真正的摩擦。{{< source "SX-007" >}}

NASA 的 COTS 观察则补上了另一半：Confluence、SharePoint、TRAC ticket 等工具可以承载信息、问题、变更、风险和异步 review，减少一些传统 control board。{{< source "SX-003" >}}

## 对 AI-native 硬件公司的启发

不要把 Agent 当一个独立聊天入口。更合理的目标是：

**需求、CAD/EDA、BOM、供应商、工单、测试数据、质量事件、变更和 issue 处在同一个可追踪工作图里，Agent 在图上工作。**

这样 AI 才是在缩短工程反馈环，而不是另造一层聊天记录。
