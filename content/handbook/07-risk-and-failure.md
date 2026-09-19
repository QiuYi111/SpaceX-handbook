---
title: "07 · 风险与失败"
weight: 12
status: "v0.3"
source_ids: ["SX-002","SX-004","SX-006","SX-020","SX-021","SX-023","SX-028"]
summary: "失败是否可接受，取决于后果是否被提前包住。"
---

“SpaceX 接受失败”是最容易学歪的一句话。

更准确的是：

> **失败是否可接受，要看失败发生在哪一层、伤害谁、损失什么、能拿回多少信息，以及下一轮能否快速修改。**

## 1. SpaceX 自己就不是一套风险标准

Musk 在 Starbase 访谈里明确区分：

- **Dragon**：载人，必须大量测试和保留 margin；
- **Falcon**：上升段正式任务不能失败，但早期回收试验可以承担更多风险；
- **Starship 早期原型**：无人、快速迭代，因此允许更高的 prototype loss。{{< source "SX-004" >}}

所以 SpaceX 的方法不是：

> “风险高一点也没事。”

而是：

> **让低后果开发环境承担更多学习，把正式任务中的未知降下来。**

## 2. 失败的价值来自信息，不来自爆炸

一次实验值得不值得，可以问：

- 失败前关键数据拿到了吗？
- 能定位 root cause 吗？
- 能排除哪些假设？
- 下一版会因此改变吗？
- 失败是否落在预先划定的安全范围内？

如果答案都是否，那么硬件炸掉没有任何“创新光环”。

## 3. 软件里的 blast radius

SpaceX 软件团队公开描述过 Starlink 的小范围 rollout：先把版本部署到有限范围，观察真实遥测，再逐步扩大。{{< source "SX-006" >}}

这是非常好的风险设计：

> **不要只降低 failure probability，也降低一次失败影响的范围。**

同一个原则可以出现在硬件：

- coupon 而不是整机；
- 单通道而不是全系统；
- bench test 而不是现场；
- dummy load 而不是患者；
- 少量 pilot build 而不是全量量产。

## 4. 风险管理不等于 risk register

前 SpaceX/Crew Dragon 工程师 Lauren Lyons 后来提出的 lean risk 方法很值得迁移，但必须标清：这是她给 startup 的推荐框架，不是 SpaceX 官方原样流程。{{< source "SX-020" >}}{{< source "SX-021" >}}

它的核心观点是：

> 风险是帮助组织做决定的工具，不是“所有可能坏事”的仓库。

一个有效 risk 至少要清楚：

- baseline 是什么；
- 偏离在哪里；
- 可能造成什么后果；
- 谁 owner；
- mitigation 是什么；
- residual risk 为什么可接受；
- 谁最终接受。

## 5. Risk owner 应该接近工作

如果风险完全由独立“风险部门”维护，很容易出现：

> 工程师做工程，风险经理更新表格。

这会把风险从工程决策里剥离。

更合理的状态是：

- RE owner 技术风险与 mitigation；
- 独立人员维护 process 和 company-wide consistency；
- chief engineer / senior authority 接受高后果 residual risk。

这是 SX-020 的 startup 迁移框架，适合作为我们的设计参考。

## 6. NASA 为什么看起来更谨慎

Garrett Reisman 的解释很重要：NASA 慢并不意味着人更差，而是**错误决定的代价、合同与组织可逆性不同**。SpaceX 高度垂直整合，错误后可以更快改方向；NASA 很多项目一旦方向错，返工链长得多。{{< source "SX-023" >}}

所以比较 risk tolerance 时，必须先比较：

- 一次错误要损失多少钱；
- 需要多少组织重新签字；
- 供应商能不能改；
- 下一件多久能造出来；
- 错误是否影响公众/乘员/患者。

## 7. Reentry 提供的反例价值

Eric Berger 的《Reentry》之所以重要，不只是写成功复用，也写严重事故、故障调查和高压决策。{{< source "SX-028" >}}

Handbook 必须记住：

> **快速组织依然会出严重事故。**

速度不是风险消失，只是风险管理方式不同。

## 8. 一个实用的“是否允许失败”检查

### 可以更激进

- 无人；
- 低成本；
- 可重复；
- 失败不会破坏关键设施；
- 能完整采集数据；
- 下一版很快能来。

### 必须保守

- 载人/患者；
- 不可逆；
- 唯一设备；
- 影响公众安全；
- 失败会摧毁长期基础设施；
- 无法拿到有效故障数据；
- 重造需要数月/数年。

## 9. 反模式

### Fail fast 变成 reckless fast

没有设计 instrumentation，没有 failure containment，只是快。

### Risk register burial

风险有 500 条，每周更新颜色，但没人改变工程决定。

### “已接受风险” = 不再想

真正 risk acceptance 必须有 rationale 和 authority。

### 为了零风险冻结开发

早期每件 prototype 都按正式产品验证，会把未知拖到更晚才暴露。

## 10. 医疗器械的翻译

医疗器械里不要说：

> “允许失败。”

应该说：

> **把失败尽量提前推到不会伤害患者、成本最低、数据最完整的工程环境中。**

这才是可迁移的核心。
