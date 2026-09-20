---
title: "14 · 流程随成熟度增长"
weight: 19
status: "v0.3"
source_ids: ["SX-002","SX-004","SX-008","SX-013","SX-023","SX-025"]
summary: "开发样机、资格验证、生产和载人任务不能用一套流程。"
---

SpaceX 最容易被复制错的一点是：

> 看见早期 Starship 原型快速飞、快速炸，就认为成熟产品也应该减少流程。

Muratore 2012 年原始材料已经明确：随着系统进入 later cycles、qualification、first flight、production，documentation 和 process 会变得更正式。{{< source "SX-002" >}}

## 1. Process 应该跟 failure consequence 和 knowledge maturity 一起变化

一个简单模型：

### Explore

问题：到底什么方案能工作？

重点：

- 快实验；
- 多设计空间；
- 小样；
- 低成本失败。

### Develop

问题：这个方案能稳定工作吗？

重点：

- 关闭主要未知；
- 重复测试；
- 建立 requirement / interface。

### Qualify

问题：设计是否有足够 margin 应对预期环境？

重点：

- 受控 configuration；
- 极限环境；
- qualification evidence。

### Produce

问题：每一件是不是同一个已验证设计？

重点：

- process control；
- supplier control；
- traceability；
- acceptance test。

### Operate / Human-rated

问题：如何把残余未知压到可接受水平？

重点：

- configuration discipline；
- independent check；
- hazard control；
- go/no-go。

## 2. Dragon vs Starship 是最直接案例

Musk 自己公开说 Dragon 与早期 Starship 风险哲学几乎相反：Dragon 载人，所以极端重测试和 margin；早期 Starship 无人，可以让 prototype 承担更多 learning risk。{{< source "SX-004" >}}

这不是双重标准。

而是：

> **不同 consequence 应有不同 process。**

## 3. 软件也一样

SpaceX Software Delivery Engineering 公开描述：

- 一般软件与 safety-critical flight software 质量门槛不同；
- safety-critical change merge 前有额外条件；
- merge 后继续 test；
- verification 独立存在；
- HITL 与任务模拟进入 pipeline。

{{< source "SX-008" >}}

所以“敏捷 = 不做 gate”是不成立的。

## 4. 过早成熟化的代价

startup 常见错误：

第一版 prototype 就建立：

- 20 页 change form；
- 8 人审批；
- 完整量产 traveler；
- 所有 supplier 都走成熟 PPAP 式流程。

结果设计每两天还在改，但 change system 已经比产品稳定。

这叫：

> **process ahead of knowledge。**

## 5. 过晚成熟化同样危险

另一极端：

产品已经要交付，却还靠：

- 口头改图；
- 本地 Excel BOM；
- 无 serial trace；
- test 数据散落；
- “这个 technician 知道怎么装”。

这叫：

> **knowledge ahead of process。**

当组织进入重复生产，隐性知识必须逐步变成显性控制。

## 6. regulated hardware 仍可迭代

Garrett Reisman 对 NASA–SpaceX 合作的回顾提供了另一个边界：他认为 NASA 的安全与复杂系统经验帮助 SpaceX 变得更成熟，而 SpaceX 的速度也反过来影响 NASA。也就是说，**成熟度增长不必等同于把反馈环拉长**。{{< source "SX-023" >}}

Chris Hansen 从 SpaceX 去 Radiant 后明确说，核系统仍需要 detailed analysis、rigorous testing、validation，只是他把快速学习、跨专业和 hands-on 方法迁移过去。{{< source "SX-013" >}}

这说明“regulated vs iterative”并不是二选一。

真正问题是：

> **在哪一层、哪个阶段允许什么程度的变化？**

Flow Volume II 对这一点有好的教学整理，但具体所谓 SpaceX stage-gate 细节不能当一手事实。{{< source "SX-025" >}}

## 7. 一条实用规则

每增加一个流程，问：

> 这个流程是在控制一个已经出现、且后果足够高的真实风险吗？

如果回答是：

> “因为以后可能需要。”

那它可能加得太早。

每删除一个流程，也问：

> 删除后谁在承担新增风险？

如果答案没人知道，就可能删得太快。

## 8. 反模式

### Prototype forever

永远用开发期自由度，到了客户/患者还没形成配置纪律。

### Certification theater

流程一大堆，但 evidence 质量很差。

### Copy mature company

20 人 startup 原样复制万人公司的 QMS/PLM 节奏。

### Process purge

把所有 review 都叫官僚主义。

## 9. AI 会让流程成熟更早还是更晚？

两者都可能。

AI 可以低成本生成：

- trace matrix；
- test report；
- change impact；
- risk summary；
- supplier record。

这意味着很多过去“太贵所以晚做”的基础记录，可以更早做。

但不要因此更早建立**审批层级**。

AI 应该让 evidence 更便宜，不应该让 bureaucracy 更便宜。
