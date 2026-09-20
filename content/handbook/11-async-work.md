---
title: "11 · Ticket、异步 Review 与会议"
weight: 16
status: "v0.4"
source_ids: ["SX-003","SX-019","SX-020"]
summary: "简单、可记录的问题异步化；真正有歧义的事情再同步。"
---

SpaceX 很早就把一部分工程协作从“大家同时开会”搬到了共享信息系统里。

NASA COTS 2013 年复盘的 slide 16 尤其具体：SpaceX 用 TRAC tickets 管 issue、change、risk；参与者异步提问、评论，保留完整讨论，最终由经理和 responsible engineer 收敛与签核。NASA 把这种方式描述成类似 **virtual board/review**。{{< source "SX-003" >}}

这里有一个重要边界：这证明的是 **COTS 合作期内 NASA 实际观察到的做法**，不是证据表明 SpaceX 全公司有一套统一的“异步优先”制度，更不能直接外推到今天仍使用同一套工具。

## 1. 异步真正节省的是什么

不是会议时长本身。

而是：

> **不再为了一个简单问题，等十个人日历同时空出来。**

如果一个 issue 已经定义清楚：

- 问题是什么；
- 数据在哪；
- 谁 owner；
- 需要什么决定；

大多数 review 可以按各自时间处理。

这里的关键不是“少开会”，而是把**等待大家同时出现**从流程里拿掉。

## 2. NASA 给出的边界非常好

同一张 slide 16 最后一条不是 SpaceX 的正式政策，而是 **NASA 自己的使用建议**：

- simple issue/change/risk → 适合 ticket；
- 如果迟迟不能 closure；
- 或问题本身不清；

就应该迅速切换到同步讨论。{{< source "SX-003" >}}

所以本手册把它迁移成一条规则：

> **异步用于传播和收敛已定义问题；同步用于快速消除高带宽歧义。**

注意：这是我们的迁移规则，不应写成“SpaceX 规定如此”。

## 3. 一个好的 ticket 是一个微型工程包

应该至少包含：

- Context：为什么现在出现；
- Problem：具体哪里不对；
- Evidence：log、图、测试、照片；
- Impact：影响谁；
- Owner：谁收口；
- Options：有哪些解；
- Decision needed：现在到底要决定什么；
- Done：什么状态算关闭。

这样 reviewer 不需要重新开会采访作者。

NASA 的原始材料还能再支持一步：TRAC ticket 在被观察到的场景里不仅是“任务卡”，还承载了问题、评论、closure 和签核。{{< source "SX-003" >}}

## 4. Change 为什么特别适合异步

Kellan O'Connor 回忆早期 SpaceX engineering change 曾需要纸张线下找多人签字；后续数字 PLM 显著改善了这一流程。{{< source "SX-019" >}}

这说明异步工具的价值并不神秘：

**把等待人出现，变成等待判断本身。**

前者是纯浪费。

## 5. Risk ticket 的同构性

Lauren Lyons 的 startup risk framework 也采用 database/ticket，理由是：

- single source of truth；
- workflow；
- 可以排序；
- 可以 review；
- owner 清楚。

{{< source "SX-020" >}}

这和 NASA 早年观察到的 TRAC 模式高度同构。

但“结构相似”不等于“同一套 SpaceX 制度”。这里是跨来源的模式归纳。

## 6. 会议应该用在哪里

适合开会：

- problem statement 还不一致；
- 两个 RE 都认为对方应 owner；
- 系统 trade 需要快速来回；
- 风险高到必须实时 challenge；
- 文字已经往返三轮还不收敛。

不适合开会：

- status readout；
- 逐条念 ticket；
- 让 15 个人听两个人讨论；
- 展示本来可以提前看的 PPT。

“三轮”只是本手册的实用触发器，不是 SpaceX/NASA 的原文要求。

## 7. 一个实用规则：会前先写

真正需要同步的讨论，也应该先有 ticket。

至少提前写清：

- 问题；
- 关键证据；
- 争议点；
- 要做的 decision。

这样会议结束后，decision 也回写 ticket。

于是：

> **会议是 ticket 生命周期中的一个工具，不是信息最终存放地。**

## 8. 反例：工具不会自动消灭延期

不要从“异步协作能节省等待”跳到“采用 ticket 就不会延期”。

GAO 2011 年对 COTS 的审计记录，SpaceX 当时仍出现过明显的演示任务延期，原因包括设计、软件、生产、供应商和安全批准等。{{< source "SX-003" >}}

这说明数字协作工具能压缩的是一部分沟通与变更成本；它不能消除真实技术风险、生产问题和外部审批。

## 9. AI 为什么会进一步推高异步价值

Agent 很擅长：

- 汇总长 thread；
- 检查遗漏 reviewer；
- 找相关历史 issue；
- 把 test data 附上；
- 生成决策摘要；
- 检查 close criteria。

于是人类真正需要花同步时间的部分会进一步收缩到：

> **价值判断、冲突和高风险 trade。**

前提是 Agent 写回真实工程对象，而不是另建一个聊天孤岛。

## 10. 反模式

### Slack/微信决策

讨论很快，但组织几个月后完全不知道为什么这样做。

### Ticket theater

所有东西都进 ticket，但描述只有一句“fix this”。

### Meeting avoidance

明明文字已经完全失效，还坚持异步两周。

### AI 自动评论洪水

Agent 每个 issue 都生成长文，反而降低 signal-to-noise。

## 11. 最终目标

不是“少开会”。

而是：

> **让正确的信息，以最低等待时间，到达能做决定的人；并把决定留下来。**
