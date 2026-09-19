---
title: "99 · 医疗器械迁移边界"
weight: 99
status: "v0.1 · important"
source_ids: ["SX-020","SX-021","SX-002"]
summary: "速度原则必须放在患者安全、法规和设计控制之内。"
---

植入式医疗器械和火箭有很多相似结构：复杂硬件、软硬件耦合、长供应链、昂贵实物验证、强监管、最终产品高后果。但迁移 SpaceX 方法时，必须把**患者安全**放在顶层不可交易约束。

## 可以直接迁移

- outcome owner / Responsible Engineer；
- 缩短设计—制造—测试—数据闭环；
- 尽早做便宜、可控、可恢复的实验；
- 每条内部要求有来源、理由和 owner；
- 软件和数据系统进入工程、制造和质量主线；
- 简单 review 异步 ticket 化；
- 成本、周期、可制造性在设计早期共同 trade。

## 必须更严

- 风险管理和设计追溯；
- verification / validation；
- 变更控制；
- 供应商质量；
- 软件安全生命周期；
- 生物相容性、灭菌、包装和长期可靠性；
- 临床前与临床边界。

Lauren Lyons 同时有 Medtronic 与 SpaceX/Crew Dragon 背景，她后来提出的 lean risk 方法很适合作为**迁移参考**，但不能被描述成 SpaceX 官方原样流程。{{< source "SX-020" >}}{{< source "SX-021" >}}

## 推荐翻译

不要把 fail fast 翻成“允许失败”。

更准确的是：

> **让未知尽早在最低代价、最低后果、不会伤害患者的地方暴露。**

## 对 AI-native 医疗器械公司的额外原则

Agent 可以整理要求、追踪证据、生成测试草案、检查 traceability、驱动 issue 和分析数据；但安全责任和最终审批必须保持明确的人类 owner。AI 应该减少信息摩擦，不能制造责任真空。
