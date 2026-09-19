---
title: "09 · 垂直整合与 Make / Buy"
weight: 14
status: "v0.3"
source_ids: ["SX-001","SX-002","SX-003","SX-016","SX-019","SX-023"]
summary: "内制的核心价值之一，是压缩物理反馈环。"
---

“SpaceX 什么都自己做”也是一种神话化表达。

真正值得学的是：

> **Make / Buy 是系统工程 trade，不只是采购价格比较。**

## 1. SpaceX 为什么高度内制

2026 S-1 明确把 extreme vertical integration 写成竞争优势，并说明内部制造范围覆盖 engines、avionics、structures、software，甚至制造工具本身。{{< source "SX-001" >}}

Muratore 2012 的材料则给出更早期的系统原因：有限的 contract/subcontract 边界，会让 key design parameter trade 更快。{{< source "SX-002" >}}

NASA COTS 观察补充了经济原因：有时供应商价格高，内部制造同时能改善进度控制和变更速度。{{< source "SX-003" >}}

## 2. Make / Buy 应该比较什么

不要只问：

> 外购单价 vs 自制单价？

还要问：

- 第一次样品多久？
- 改一次图多久？
- supplier queue 多长？
- MOQ/NRE 是多少？
- 供应商是否愿意做小批量快速迭代？
- 缺陷能否快速 root cause？
- 关键 know-how 会不会被锁在外面？
- 这个部件是否决定系统学习速度？
- 未来量产是否有战略供应风险？

## 3. Reisman：垂直整合让错误更可逆

Garrett Reisman 比较 NASA 与 SpaceX 时给了一个很关键的解释：

SpaceX 能够快速做决定、发现错了再改，很大程度因为它从 design 到 development 的链条更内部化，因此改变方向成本更低。{{< source "SX-023" >}}

这说明 vertical integration 不只是 cost-down。

它是在购买：

> **optionality。**

也就是：

> 我今天做错了，明天还有能力改。

## 4. Tom Mueller：控制 cost、schedule、quality

Tom Mueller 后来创办 Impulse Space 时仍然把 vertical integration 当作核心差异，理由很直接：更紧地控制 cost、schedule、service quality。{{< source "SX-016" >}}

这说明它不是 SpaceX 某一个年代的临时习惯，而是早期核心工程领导者认为值得迁移的方法。

## 5. 什么东西最值得内制

优先考虑：

### 高频迭代件

每周都要改，外包会把反馈环拉长。

### 系统核心 know-how

决定产品差异化。

### 市场供应差

供应商少、lead time 长、价格离谱。

### 质量定位关键

失败时必须拿到 process detail。

### 制造本身就是产品能力

例如独特焊接、测试、精密装配、自动化工装。

## 6. 什么不值得内制

- 成熟标准件；
- 不影响迭代速度；
- 市场供应非常充分；
- 内部做反而质量更差；
- 需要巨额 CAPEX，但不是核心能力；
- 量太小，学习曲线永远起不来。

垂直整合的目标不是“纯血”，而是系统最优。

## 7. 一个反例：自研成瘾

创业公司很容易说：

> “SpaceX 都自己做，我们也自己做。”

结果：

- 做连接器；
- 做 ERP；
- 做 CNC；
- 做电源；
- 做测试仪器；

最后核心产品没人推进。

正确问题不是“能不能自己做”，而是：

> **如果不自己做，我们最关键的反馈环会不会被卡住？**

## 8. 供应商也可以成为“半内部反馈环”

Make / Buy 不是二元。

优秀供应商合作可以做到：

- 小批量；
- 快速 DFM；
- 工程师直接沟通；
- 共享 process data；
- 快速 revision；
- 预留产能。

如果能做到这些，外部供应商一样可以进入快速 loop。

## 9. 医疗器械特别注意

医疗器械供应商往往同时承担：

- 特殊材料；
- 洁净；
- 灭菌；
- 植入级资质；
- process validation；
- traceability。

因此“自己做更快”可能在研发阶段成立，但到受控生产阶段反而增加验证负担。

Make / Buy 必须把**法规与供应商质量体系**一起算进去。
