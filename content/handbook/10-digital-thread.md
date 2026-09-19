---
title: "10 · 内部软件与数字主线"
weight: 15
status: "v0.3"
source_ids: ["SX-005","SX-007","SX-003"]
summary: "软件不是 IT 支持层，而是制造系统本身。"
---

SpaceX 一个常被忽略的优势，不是火箭本身，而是**围绕物理产品建立的软件系统**。

2013 年 SpaceX 软件团队已经公开描述一套覆盖采购、库存、设计、工单和现场任务的企业信息系统。{{< source "SX-005" >}}

后来对 SpaceX 内部软件团队的采访进一步展示了 Warp Drive 一类系统：原材料、采购、库存、work order、制造、质量问题、变更和零件关系被放进同一条数字链。{{< source "SX-007" >}}

NASA 的 COTS 复盘提供了更早、也更具体的一块证据：2013 年 deck 的 slide 16 记录 SpaceX 用 SharePoint / Confluence 承载团队流程和一般信息，用 TRAC ticket 管 issue、change、risk；在部分场景还以 FEM model + summary 代替大型结构分析报告。{{< source "SX-003" >}}

这三份材料来自不同时期。它们能共同支持“SpaceX 长期重视内部数字系统和结构化工程对象”，但不能证明 2026 年仍使用同一套工具，也不能把 COTS 期 TRAC 直接等同于后来的 Warp Drive。

## 1. 软件不是“办公辅助”

传统硬件公司经常把软件系统理解成：

- ERP 是财务的；
- PLM 是工程的；
- MES 是生产的；
- Jira 是软件的；
- 文档在网盘；
- 测试数据在仪器电脑；
- 供应商记录在微信和邮件。

结果是：

> **产品是一件东西，产品的信息散成十几个世界。**

SpaceX 式内部软件的价值，在于让物理产品和它的数字信息尽量保持连接。

## 2. 什么叫数字主线

理想情况下，一件硬件能从当前版本一路追到：

- 顶层需求；
- 设计文件；
- BOM；
- 零件版本；
- 供应商批次；
- 工单；
- 装配记录；
- 测试结果；
- quality escape；
- change；
- 当前飞行/使用配置。

于是团队问：

> “这个改动会影响哪些已生产件？”

系统应该能回答。

而不是靠某个资深工程师记忆。

注意：上面这张完整“数字主线”清单是本手册的迁移目标，不是来源声称 SpaceX 在某个时期已经把全部对象放进一个系统。

## 3. 软件工程师应该靠近真实工作

Warp Drive 相关访谈里一个很值得学的细节，是软件工程师直接接近生产现场、理解工人真正怎样造卫星。{{< source "SX-007" >}}

这比传统 IT 模式强很多：

传统：

> 业务写需求 → IT 排期 → 开发 → 上线 → 发现不适用。

更直接：

> 能改系统的人，直接观察工作，再与现场一起修改系统。

这让内部软件本身也进入快速反馈环。

## 4. Ticket 是工程对象，不只是待办

NASA slide 16 观察到 SpaceX 用 TRAC ticket 支撑 issue、change、risk 和 virtual review：参与者能异步提问、评论，追踪讨论，最后收敛并签核。{{< source "SX-003" >}}

ticket 的价值不是“任务管理”，而是把：

- 问题；
- 证据；
- 决策；
- owner；
- review；
- 状态；

放到同一个可追踪对象里。

其中“证据、owner、decision”等完整字段是本手册建议的工程对象结构；原始 NASA slide 直接支持的是 issue/change/risk、讨论、closure、签核这些功能，不应混成 SpaceX 官方 schema。

## 5. 一个好的工程 issue 应该自带上下文

至少包括：

- 为什么这个问题重要；
- 当前配置；
- 失败证据；
- 相关需求；
- 相关 CAD / code / test；
- owner；
- 什么状态算完成；
- 最终 decision。

这样新的工程师、reviewer 或 Agent 能直接进入问题，而不需要重新采访原作者。

## 6. 数字系统真正优化的是“上下文搬运”

硬件组织里大量时间并不是设计，而是在做：

- “最新图纸在哪？”
- “这个版本测过没有？”
- “谁批准的？”
- “供应商用的是哪个 revision？”
- “这个 failure 和上次是不是同一个？”
- “为什么当时这么设计？”

当信息已经结构化连接，这些问题不再需要人肉搜索。

这可能比把 CAD 建模加速 2 倍更重要。

## 7. 对 AI-native 公司的真正意义

Agent 最怕的是**上下文断裂**。

如果：

- Linear 只有任务；
- GitHub 只有代码；
- CAD 在本地；
- BOM 在 Excel；
- 测试数据在 NAS；
- 决策在聊天记录；

那么再聪明的 Agent 都要不断重新拼上下文。

更好的结构是：

> **Agent 在工程图谱上工作，而不是在人类碎片信息之间猜。**

## 8. Agent 应该能读什么

一个硬件 Agent 至少应该逐步获得结构化访问：

- requirements；
- issues；
- CAD/EDA metadata；
- BOM；
- supplier；
- test artifacts；
- quality events；
- revisions；
- approvals；
- decision history。

这不意味着所有系统必须合成一个数据库。

关键是**可链接、可查询、版本明确、权限清楚**。

## 9. Agent 应该写什么

Agent 不应该只输出聊天文本。

更有价值的是直接产生可追踪对象：

- issue；
- review comment；
- test report；
- requirement link；
- change proposal；
- supplier comparison；
- root-cause hypothesis；
- next experiment。

于是 Agent 的工作会成为组织记忆的一部分，而不是消失在会话历史里。

## 10. Single source of truth 不等于 single tool

一个常见误区是：

> “我们要把所有东西塞进一个平台。”

不一定。

Git 可以继续管代码，CAD 系统管几何，ERP 管库存，Linear 管 issue。

真正要求是：

- 每种事实有明确 authoritative source；
- 系统之间有稳定 ID；
- 链接不会靠手工复制；
- 版本变化能追踪。

**统一语义比统一软件更重要。**

## 11. 内部软件的 ROI

内部工具最值得做的场景通常具备：

- 高频；
- 多人重复；
- 上下文搬运多；
- 容易出版本错误；
- 与物理吞吐直接相关。

例如：

- 自动生成 traveler；
- 测试结果自动挂到 serial number；
- CAD release 自动触发 BOM diff；
- quality issue 自动找到受影响批次。

这类工具不是“提高办公体验”，而是在直接提高工厂吞吐和降低错误率。

## 12. 反模式

### Chat-first organization

关键决策都在 Slack/微信/群聊，事后找不到。

### Dashboard without workflow

做了漂亮 dashboard，但实际决策和执行仍在另一个系统。

### AI as another silo

又加一个 Agent 平台，却不能读写真实工程系统。

### Duplicate truth

BOM 在三个 Excel 里分别维护，没有明确哪个是真的。

### Tool worship

不断换软件，但没有定义信息对象、owner 和版本规则。

## 13. 最终目标

真正好的数字系统应该让一句话成立：

> **任何一个工程问题，都能从当前状态一路追到它为什么存在、谁负责、有哪些证据、改过什么、下一步是什么。**

到了 AI 时代，这条链又多了一层价值：

> **Agent 终于可以持续工作，而不是每次从零听人讲故事。**
