---
title: "04 · 分布式系统工程"
weight: 9
status: "v0.1"
source_ids: ["SX-002","SX-014"]
summary: "系统思维不是一个部门的专利。"
---

Muratore 2012 年描述的 SpaceX 系统工程并不是取消 Systems Engineering，而是把系统级工作分散到各工程团队，再用跨组织的 integrator 网络连接。{{< source "SX-002" >}}

Ramakrishna Akella 对 Starlink 的回顾也强调：设计、制造、测试、成本和系统风险不能由少数“系统工程师”写完再向下分发，参与设计的人需要理解整体系统。{{< source "SX-014" >}}

## 原则

- 每个工程师都要理解自己改变会怎样影响整体。
- 接口是共同问题，不是“另一个部门的接口文档”。
- integrator 的价值是连接和做系统 trade，不是替所有人思考。
- 技术信息尽量直接从 RE 到 RE，而不是沿管理链传话。

## 反模式

设立一个“系统工程部”，然后其他工程师只对自己的零件指标负责。这样组织图上有 Systems Engineering，实际却没有 systems thinking。
