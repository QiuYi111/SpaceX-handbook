---
title: "08 · 制造即工程"
weight: 13
status: "v0.3"
source_ids: ["SX-001","SX-003","SX-007","SX-014","SX-018","SX-019"]
summary: "Engineering 与 Manufacturing 不是前后两棒。"
---

SpaceX 最重要的一条硬件经验可能是：

> **能做出 prototype，不等于能生产产品。**

Starlink 前工程领导 Ramakrishna Akella 直接强调：rate manufacturing 不是产品开发结束后的 phase，而应从工程一开始就进入设计。{{< source "SX-014" >}}

## 1. 为什么“研发完成后转生产”很危险

传统流程：

**R&D → design freeze → transfer to manufacturing**

问题是很多东西直到工厂才暴露：

- 装不上；
- 工序太慢；
- 公差堆叠；
- 返工困难；
- 检验不可自动化；
- 供应商产能不够；
- 测试时间比装配时间还长。

于是所谓“设计完成”其实只是：

> **设计部门完成。**

系统还没完成。

## 2. SpaceX 的公开证据

Kellan O'Connor 回忆早期 Merlin 团队时，design、analysis、manufacturing、Texas testing 之间反馈非常短。{{< source "SX-019" >}}

NASA COTS 也观察到内部制造让 SpaceX 能更直接控制成本、进度和修改。{{< source "SX-003" >}}

2026 S-1 更进一步，把“tools that make the tools”和制造规模直接写进公司能力。{{< source "SX-001" >}}

## 3. Starlink：产品和工厂一起设计

Starlink 把问题推到了极端：

火箭可以低量、高价值；用户终端与卫星则需要完全不同的生产节拍。

Stack Overflow 对 SpaceX application software 团队的采访显示，为了 Starlink，他们不只是写新的制造软件，而是把软件工程师直接搬到 assembly line 旁，甚至轮班体验工位。{{< source "SX-007" >}}

这说明：

> **工厂不是 downstream customer，而是产品本身的一部分。**

## 4. 一个设计是否完成，要同时回答六个问题

1. 能不能工作？
2. 能不能做出来？
3. 能不能稳定重复做？
4. 能不能快速装？
5. 能不能快速测？
6. 失败后能不能定位和返工？

少任何一项，都可能只是 laboratory design。

## 5. 删除复杂度的制造收益

The Algorithm 的“删除”在制造上尤其强。

删一个零件，不只是 BOM -1。

还可能同时删掉：

- supplier；
- incoming inspection；
- stock location；
- drawing；
- work instruction；
- station；
- fastening；
- defect mode；
- test step；
- rework path。

Tim Berry 解释 Algorithm 时明确把 part/process deletion 与 labor、cycle time 联系起来。{{< source "SX-018" >}}

## 6. “更容易制造”本身就是性能

传统 engineer 容易把性能理解成：

- 功率；
- 重量；
- 精度；
- 强度。

但量产产品还应该把下面这些视为性能：

- cycle time；
- first-pass yield；
- operator touch time；
- station count；
- setup time；
- inspection time；
- supplier lead time。

否则“性能最好”的设计可能是公司整体最差的设计。

## 7. 软件为什么属于制造工程

SpaceX 内部 ERP/MES 类系统能跟踪：

- part 在哪；
- work order；
- defect；
- change；
- part relation。

{{< source "SX-007" >}}

这不是后台行政。

如果工人拿到错误 revision，或者 defect 无法沿装配层级追踪，制造系统就直接失效。

## 8. 反模式

### Prototype heroics

靠一个资深技师手工调到能工作，然后宣布设计成功。

### Throw over the wall

工程部说“图已经 release 了”，剩下问题都叫 manufacturing issue。

### 自动化不稳定工序

工艺自己都没稳定，就先上机器人。

### 只算材料成本

忽略装配时间、测试、返工、设备和供应商 lead time。

## 9. 适用边界

低量、高定制产品未必值得追求极致自动化。

但即使年产只有几十台，**可装、可测、可追踪、可返工**仍然应该是设计输入。

## 10. 一个简单的 design review 追加问题

每次 review 多问一句：

> **如果下个月要做 100 件，什么先崩？**

答案通常比再看一次 CAD 更有价值。
