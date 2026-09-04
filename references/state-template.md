# 状态账本

## 整题

- 题目：
- 交付范围：
- 输入与数据版本：
- 小问依赖：
- 信息风险：`INFO_RISK = ON/OFF`；理由：
- Other risk tags: list only relevant items from `CONTINUOUS / DISCRETIZATION / OPTIMALITY / REUSE / OBJECTIVE`, with a reason.
- 历史审计文件：保留，仅供追溯，不作为协议 2.0 门控

`INFO_RISK = ON` 时补充四项信息契约：世界真值、各决策者可观测信息、允许共享/记忆的信息、策略禁用的信息。

## 小问状态

| 小问 | 状态 | 阶段 | 验证轮次 | 当前结果版本 | 未解决 A | B 限制 | 下一有限动作 |
|---|---|---:|---:|---|---|---|---|
| Q1 | 进行中 | 00 | 0 | — | — | — | 简化题目 |

状态只能为：`进行中 / 验证中 / DONE / 用户重新打开`。
验证轮次只能为：`0 / 1 / 2`。从轮次 2 再进入验证，必须记录用户重新打开的原话或明确授权。

## 问题记录

| ID | 小问 | A/B/C | 具体影响说明 | 证据 | 处理决定 | 状态 |
|---|---|---|---|---|---|---|

- A 阻塞 DONE。
- B 有限验证并在交付中披露。
- C 只记录，不阻塞、不派生任务、不触发验证或重开。

## 封闭验证

| 小问 | 轮次 | 命题 1–3 | 方法与独立性 | 结论 | 直接修复范围 |
|---|---:|---|---|---|---|

## DONE 证书

- [ ] `MODEL == PROBLEM`: definitions, objective, constraints, information assumptions, and quantifiers match the problem
- [ ] `SOLVER == MODEL`: implementation, search space, discretization, and computed objective match the model; restrictions are proved lossless or disclosed
- [ ] `EVIDENCE == CLAIM`: validation targets the actual conclusion and the claim is no stronger than its evidence
- [ ] Core claim is labeled `PROVED / EXACT`, `NUMERICALLY VERIFIED`, `HIGH-QUALITY FEASIBLE`, or `HEURISTIC / APPROXIMATE`
- [ ] 定义、变量、单位、方向明确
- [ ] 模型匹配目标、决策空间和硬约束
- [ ] 正式解已生成
- [ ] 回代或直接约束检查通过
- [ ] 一种风险比例适当的独立证据支持核心结果
- [ ] 若 `INFO_RISK = ON`，`INFORMATION_PASS = true`
- [ ] 无未解决 A
- [ ] B 已披露

全部满足后标记 DONE 并停止主动优化。

When the three consistency checks pass, record `ANSWER_VALIDITY_PASS = true`.
