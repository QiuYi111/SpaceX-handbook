---
title: "08 · 制造即工程"
weight: 13
status: "v0.4"
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

## 2. 三个时期，制造都不是末端部门

### COTS：内制购买的是改动速度

NASA 在 COTS 复盘 slide 15 记录：SpaceX 在设计早期就追问零件为什么贵；当某些外购件成本过高时会转为内部制造。NASA 同时强调的好处不只有单价，还包括 **schedule control** 和更直接的 change / update。{{< source "SX-003" >}}

所以“自己做”真正购买的可能是：

- 下一版不用重新排供应商；
- 设计问题能直接回到制造；
- 一个改动不必跨多层合同边界。

但这不能推出“内制永远更便宜”。NASA 这页是项目经验总结，不是对所有 make/buy 决策的成本审计。

### 早期 Merlin：设计、制造、测试在一个物理闭环里

O'Connor 回顾的推进团队约 20–30 名工程师。design、analysis、development 紧密合作；数字分析之后进入制造和装配，再去 Texas test facility。{{< source "SX-019" >}}

这说明制造的价值不只是把图纸变成零件，而是：

> **让设计假设尽快遇到现实。**

同一采访还有一个反例：早期 Engineering Change Order 仍然要打印纸张、线下找多人签字，后来数字 PLM 才改善。也就是说，SpaceX 并不是从第一天起就拥有“完美数字工厂”；制造系统本身也在持续迭代。{{< source "SX-019" >}}

### 2026：制造工具本身也被当成核心能力

到 2026 年 S-1/A，SpaceX 已经把内部能力写到 engines、avionics、structures、software，甚至 **tools that make the tools**。{{< source "SX-001" >}}

这里可以可靠得到的结论是：制造能力长期处在公司核心工程能力之内；不能仅凭这句话推断具体工厂自动化率、设备自制比例或每条产线的组织方式。

## 3. Starlink：产品和工厂一起设计

Starlink 把问题推到了极端：

火箭可以低量、高价值；用户终端与卫星则需要完全不同的生产节拍。

Stack Overflow 对 SpaceX application software 团队的采访显示，为了 Starlink，他们不只是写新的制造软件，而是把软件工程师直接搬到 assembly line 旁，甚至轮班体验工位。{{< source "SX-007" >}}

这说明：

> **工厂不是 downstream customer，而是产品本身的一部分。**

而且这个案例还有第二层：2021 采访把 Warp Drive 描述成长期使用的 monolithic ERP；Starlink 从 2019 年开始，因为制造模式不同，又在它之外建设新的 MES。{{< source "SX-007" >}}

这给了一个很重要的反例：

> **“数字主线”不等于“所有产品永远用同一个系统”。**

当产品形态、生产节拍和现场需求变了，制造软件本身也需要跟着重新设计。

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

## 10. 一个制造 review 不该只看 CAD

每次 review 至少再问：

- 如果下个月要做 100 件，什么先崩？
- 哪一步最依赖某个熟练工的手感？
- 哪个公差最容易变成返工？
- 哪个 test station 会先排队？
- 哪个 defect 现在还无法沿零件关系追踪？
- 哪个 design change 会让现场拿到错误 revision？

其中最后两类问题正是 SpaceX application software 公开描述过的制造信息系统能力：追踪零件位置、零件关系、quality escape 和 change impact。{{< source "SX-007" >}}

所以制造设计至少同时包含两层：

> **物理工艺 + 信息流。**

只优化其中一层，规模上来都会出问题。
