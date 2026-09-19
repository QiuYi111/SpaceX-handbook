---
title: "15 · 成本、周期与吞吐"
weight: 20
status: "v0.3"
source_ids: ["SX-001","SX-003","SX-004","SX-014","SX-016","SX-018"]
summary: "成本与周期从一开始就是工程变量。"
---

SpaceX 的速度不是和成本无关。

恰恰相反：

> **成本越低、吞吐越高，组织越有能力多做真实试验。**

2026 S-1 明确把持续 drive cost down / throughput up 写成公司原则。{{< source "SX-001" >}}

## 1. Cost 不是 finance 的后处理

NASA COTS 观察到 SpaceX 很早就在设计阶段问：

> 为什么这个东西这么贵？

而不是等 design freeze 后再成立 cost-down team。{{< source "SX-003" >}}

因此工程 trade 应同时讨论：

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

## 2. 真正昂贵的常常不是材料

一件零件材料只要 30 美元，但如果：

- 要 12 周 lead time；
- 每改一次收 5000 美元 NRE；
- 必须人工 2 小时装配；
- 每件做 45 分钟检验；

它可能是系统非常昂贵的设计。

所以成本应该看：

> **lifecycle cost + iteration cost。**

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

## 4. Musk 对 manufacturing 的强调

Starbase 访谈里 Musk 直接说 manufacturing 被低估，而生产系统往往比单次产品设计难得多。{{< source "SX-004" >}}

这是因为产品设计只要“能工作一次”。

生产系统需要：

> **重复、便宜、稳定地让产品工作。**

## 5. Rate manufacturing 反过来塑造架构

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

## 6. 垂直整合与成本不是简单“自己做更便宜”

Tom Mueller 后来在 Impulse 仍强调 vertical integration 对 cost、schedule、quality 的综合控制。{{< source "SX-016" >}}

有些东西内部做单价可能更高，但：

- 没 NRE；
- 不排队；
- 可当天改；
- 失败可马上拆；

对 development 总成本反而更低。

## 7. Algorithm 里的 throughput

Tim Berry 对 The Algorithm 的解释里，第四步“go faster”直接包括：

- 加 station；
- ramp manufacturing；
- 减 cycle time。

{{< source "SX-018" >}}

所以“速度”不是只让个人工作更快。

很多时候要改的是系统产能。

## 8. 一套更有用的成本指标

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

## 9. 反模式

### Cheapest unit wins

选了单价最低但 lead time 最长的供应商。

### Performance at any cost

性能 +3%，制造成本 ×4。

### Faster people

所有提速动作都是加班，没有改设备、供应链和流程。

### Scale after design

架构根本不适合量产，却期待制造部门后面“优化”。

## 10. 对小公司尤其重要

资源少不意味着应该少算成本。

恰恰相反：

> **startup 最应该知道，钱到底花在 learning 上，还是花在 waiting 上。**
