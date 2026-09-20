---
title: "10 · 内部软件与数字主线"
weight: 15
status: "v0.5"
source_ids: ["SX-005","SX-007","SX-003"]
summary: "软件不是 IT 支持层，而是制造系统本身。"
---

SpaceX 公开材料里一个容易被忽略的部分，是**围绕物理产品建立的内部软件**。

2013 年 SpaceX 软件工程师在 AMA 的 **OP / Edit 2** 中，把 Enterprise Information Systems 描述为一套“几乎全公司都使用”的内部 web application；公开举例已经覆盖 purchase order、part inventory、工程设计、work order，以及现场技术员根据设计查看当天工作。{{< source "SX-005" >}}

到 2021 年，SpaceX Application Software 管理者又公开描述了更具体的制造对象：原材料采购与收货、work order、inventory、quality escape、change management、零件位置和零件关系。文章还明确写到，defect 或 design change 的影响需要沿零件关系被追踪。{{< source "SX-007" >}}

NASA 的 COTS 复盘提供了另一条更早的证据：2013 年 deck 的 slide 16 记录 SpaceX 用 SharePoint / Confluence 承载团队流程和一般信息，用 TRAC ticket 管 issue、change、risk；在部分场景还以 FEM model + summary 代替大型结构分析报告。{{< source "SX-003" >}}

这三份材料来自不同团队、不同年份。它们能共同支持“SpaceX 长期把内部软件放进工程和制造主流程”，但不能证明 2026 年仍使用同一套工具，也不能把 COTS 期 TRAC、2013 年 EIS 和后来的 Warp Drive 当成同一个系统。

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

SpaceX 公开案例更值得学的，不是某个软件名字，而是内部系统直接进入采购、设计、制造、质量、测试和现场执行。

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

系统应该能回答，而不是靠某个资深工程师记忆。

注意：上面这张完整“数字主线”清单是**本手册的迁移目标**。公开来源直接支持的是其中一部分，例如采购、库存、设计/工单、零件位置、零件关系、质量问题和变更；不能反过来声称 SpaceX 某一时期已经把清单里的全部对象接进一个系统。{{< source "SX-005" >}} {{< source "SX-007" >}}

## 3. 最小数字主线不是“一个大数据库”，而是一组稳定工程对象

基于公开材料里已经能看到的 purchase order、part inventory、engineering design、work order、part location、part relationship、quality escape 和 change management，本手册建议至少把下面这些对象定义清楚。{{< source "SX-005" >}}{{< source "SX-007" >}}

下面是**迁移 schema**，不是 SpaceX 官方数据模型：

| 对象 | 最低要求 | 典型关系 |
|---|---|---|
| Requirement | 稳定 ID、版本、rationale、owner | 被 design / test 满足 |
| Part / Revision | part ID + revision | 属于 BOM，被 serial 实例化 |
| Supplier / Lot | supplier、lot/batch、证书 | 供给 part / serial |
| Work Order | 当前 revision、步骤、执行状态 | 生成具体 assembly |
| Serial / Assembly | 唯一 serial、as-built 配置 | 连接 lot、work order、test |
| Test Artifact | test ID、配置、结果、原始数据位置 | 验证 requirement / serial |
| Quality Event | defect / escape、影响范围、disposition | 指向 serial / lot / revision |
| Change / Decision | before/after、rationale、approver | 改动 requirement / part / process |

真正关键的是三件事：

1. **每种事实有 authoritative source**；
2. **跨系统对象有稳定 ID**；
3. **关系能沿 change 向前、向后追。**

这比“所有东西必须进同一个 PLM”更重要。

## 4. 软件工程师应该靠近真实工作

2021 年采访里一个非常具体的细节，是 Starlink 软件工程师被搬到装配线旁，并轮班去不同工位实际工作，以理解生产问题。{{< source "SX-007" >}}

这比传统 IT 模式更直接：

传统：

> 业务写需求 → IT 排期 → 开发 → 上线 → 发现不适用。

更直接：

> 能改系统的人，直接观察工作，再与现场一起修改系统。

这让内部软件本身也进入快速反馈环。

这里也要收住边界：公开采访证明的是 **Application Software / Starlink 场景中的做法**，不是“所有 SpaceX 软件工程师都长期轮岗产线”的公司制度。

## 5. Ticket 是工程对象，不只是待办

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

## 6. 一个好的工程 issue 应该自带上下文

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

这是本手册的迁移规则，不是公开来源里 SpaceX 的固定 issue 模板。

## 7. 一个 change 应该怎样沿数字主线传播

假设一个连接器或结构件从 revision A 改成 revision B。一个成熟系统不应该只做“上传新 CAD”。

至少要能回答：

1. 哪些 BOM / assembly 使用了 revision A？
2. 哪些 serial number 已经装了 A？
3. 哪些尚未执行的 work order 应切到 B？
4. 已完成的 test evidence 对 B 是否仍有效？
5. 哪些 quality event / failure 可能与 A 有关？
6. supplier 是否仍按旧 drawing / process 在生产？
7. 哪些 requirement 或 interface 需要重新验证？

这里的具体字段是本手册的迁移设计；公开采访直接能支持的是 SpaceX 当时已经重视 part relationship、defect、design change 与制造对象之间的影响传播。{{< source "SX-007" >}}

所以数字主线真正的价值不是“资料更整齐”，而是：

> **变更发生时，系统能自动告诉你哪里已经不再可信。**

## 8. 数字系统真正优化的是“上下文搬运”

硬件组织里大量时间并不是设计，而是在做：

- “最新图纸在哪？”
- “这个版本测过没有？”
- “谁批准的？”
- “供应商用的是哪个 revision？”
- “这个 failure 和上次是不是同一个？”
- “为什么当时这么设计？”

当信息已经结构化连接，这些问题不再需要人肉搜索。

这可能比把 CAD 建模加速 2 倍更重要。

## 9. 对 AI-native 公司的真正意义

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

## 10. Agent 应该能读什么

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

## 11. Agent 应该写什么

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

## 12. Single source of truth 不等于 single tool

一个常见误区是：

> “我们要把所有东西塞进一个平台。”

SpaceX 自己公开过一个很好的反例。2021 年采访把 **Warp Drive** 描述为长期使用的 monolithic ERP；但 Starlink 在 2019 年进入新的制造阶段后，团队认为卫星终端制造与火箭制造不同，于是在 Warp Drive 之外另建新的 manufacturing execution system。{{< source "SX-007" >}}

因此更合理的目标不是“全公司只有一个软件”，而是：

- 每种事实有明确 authoritative source；
- 系统之间有稳定 ID；
- 能通过接口找到相关对象；
- 版本和变更能追踪。

其中“稳定 ID、接口、版本规则”是本手册从公开案例抽象出的迁移要求；采访并没有公开 SpaceX 的完整跨系统 schema。

**统一语义比统一软件更重要。**

## 13. 内部软件的 ROI

内部工具最值得做的场景通常具备：

- 高频；
- 多人重复；
- 上下文搬运多；
- 容易出版本错误；
- 与物理吞吐直接相关。

下面是本手册的迁移例，不是 SpaceX 已公开确认的工具清单：

- 自动生成 traveler；
- 测试结果自动挂到 serial number；
- CAD release 自动触发 BOM diff；
- quality issue 自动找到受影响批次。

这类工具不是只在“提高办公体验”，而是在减少重复搬运、版本错误和人工追踪成本。

## 14. 反模式

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

## 15. 最终目标

真正好的数字系统应该让一句话成立：

> **任何一个工程问题，都能从当前状态一路追到它为什么存在、谁负责、有哪些证据、改过什么、下一步是什么。**

到了 AI 时代，这条链又多了一层价值：

> **Agent 终于可以持续工作，而不是每次从零听人讲故事。**
