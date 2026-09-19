---
title: "15 · 成本、周期与吞吐"
weight: 20
status: "v0.4"
source_ids: ["SX-001","SX-003","SX-004","SX-014","SX-016","SX-018"]
summary: "成本与周期从一开始就是工程变量。"
---

SpaceX 的速度不是和成本无关。

恰恰相反：

> **成本越低、吞吐越高，组织越有能力多做真实试验。**

2026 S-1 明确把持续 drive cost down / throughput up 写成公司原则。{{< source "SX-001" >}}

## 1. Cost 不是 finance 的后处理

NASA COTS 2013 年复盘的 slide 15 把 **Design with cost in mind** 单独列为 SpaceX 的经验：NASA 观察到 SpaceX 在初始设计阶段就持续追问零件和部件为什么这么贵，并在外购件被认为过贵时选择内部制造。{{< source "SX-003" >}}

所以成本不是 design freeze 之后才出现的“降本任务”。它本来就是工程 trade 的一部分：

- performance；
- reliability；
- material；
- labor；
- tooling；
- supplier；
- lead time；
- test time；
- rework；
- iteration cost。

这里也要守住证据边界：NASA 的 slide 15 是项目团队的经验总结，不是逐项成本审计；它能证明 SpaceX **早期把成本放进设计决策**，不能证明每次内制都比外购便宜。

## 2. 真正昂贵的常常不是材料

一件零件材料只要 30 美元，但如果：

- 要 12 周 lead time；
- 每改一次收 5000 美元 NRE；
- 必须人工 2 小时装配；
- 每件做 45 分钟检验；

它可能是系统非常昂贵的设计。

所以成本应该看：

> **lifecycle cost + iteration cost。**

这组指标是本手册的迁移框架，不是 SpaceX 官方术语。

## 3. Throughput 会改变研发策略

假设同样一年预算：

A 团队能造 2 台 prototype。  
B 团队能造 20 台。

B 团队：

- 能测更多假设；
- 单次失败压力更低；
- 更敢进入极限；
- 数据更多；
- 学习曲线更快。

所以 throughput 不是量产以后才重要。

它从第一天就在决定你**能怎样研发**。

## 4. NASA 对“周期成本”的一个直接解释

同一张 slide 15 还有一个很有价值的观察：如果因为 readily available parts / processes 把整个项目周期缩短 6–12 个月，省下的不只是某个零件的钱，而是整支团队那几个月的 burn rate。{{< source "SX-003" >}}

这比“单件采购价”更接近研发公司的真实成本：

> **时间本身就是系统成本。**

但这里仍然是 NASA 的经验判断，不应把“6–12 个月”当成 SpaceX 项目的普遍统计值。

## 5. Musk 对 manufacturing 的强调

Starbase 访谈里 Musk 直接说 manufacturing 被低估，而生产系统往往比单次产品设计难得多。{{< source "SX-004" >}}

这是因为产品设计只要“能工作一次”。

生产系统需要：

> **重复、便宜、稳定地让产品工作。**

## 6. Rate manufacturing 反过来塑造架构

Akella 对 Starlink 的回顾强调：

- 不是先造 perfect satellite；
- 而是尽快建立能 rate manufacture 的产品与 factory；
- 再持续迭代两者。

{{< source "SX-014" >}}

这是一种不同的最优化目标。

早期版本可能不是单件性能最强，但系统能更快产生：

- flight data；
- manufacturing data；
- cost curve。

## 7. 垂直整合与成本不是简单“自己做更便宜”

NASA slide 15 对内部生产给出的直接好处之一不是单价，而是 **更好的 schedule control 和更直接的 change/update**。{{< source "SX-003" >}}

Tom Mueller 后来在 Impulse 仍强调 vertical integration 对 cost、schedule、quality 的综合控制。{{< source "SX-016" >}}

所以有些东西内部做单价可能更高，但：

- 没 NRE；
- 不排队；
- 可当天改；
- 失败可马上拆；

对 development 总成本反而可能更低。

“可能”很重要：是否值得内制必须按具体零件、供应商和阶段计算，不能把 vertical integration 当信仰。

## 8. 速度方法也会失败

不能从 slide 15 的 design-test-repeat、COTS parts 和 cost-conscious design 推出“SpaceX 项目天然很快”。

GAO 在 2011 年记录，SpaceX COTS 首次演示任务比原计划晚约 18 个月，后续演示也有接近两年的推迟；原因涉及设计、软件、生产、供应商和安全批准。{{< source "SX-003" >}}

所以真正值得迁移的是：

> **降低一次学习的成本和等待时间。**

不是给项目贴一个“快公司”的标签。

## 9. Algorithm 里的 throughput

Tim Berry 对 The Algorithm 的解释里，第四步“go faster”直接包括：

- 加 station；
- ramp manufacturing；
- 减 cycle time。

{{< source "SX-018" >}}

所以“速度”不是只让个人工作更快。

很多时候要改的是系统产能。

## 10. 一套更有用的成本指标

### Part cost

一件多少钱。

### Iteration cost

改一版多少钱。

### Iteration latency

改一版多久。

### Touch time

人实际操作多久。

### Yield

一次通过多少。

### Test throughput

每天/每周能测多少。

### Cost of failure

失败一次损失多少。

这几个数字一起看，才会得到真实研发经济性。

## 11. 反模式

### Cheapest unit wins

选了单价最低但 lead time 最长的供应商。

### Performance at any cost

性能 +3%，制造成本 ×4。

### Faster people

所有提速动作都是加班，没有改设备、供应链和流程。

### Scale after design

架构根本不适合量产，却期待制造部门后面“优化”。

## 12. 对小公司尤其重要

资源少不意味着应该少算成本。

恰恰相反：

> **startup 最应该知道，钱到底花在 learning 上，还是花在 waiting 上。**
