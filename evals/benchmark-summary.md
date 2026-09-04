# 精简协议评测记录

## 目标

验证协议 2.0 同时保留答案相关的数学防错能力，并缩短默认验证链路。此次不运行完整多智能体基线或可视化评测。

## 定向场景

| 场景 | 预期决策 |
|---|---|
| 定义歧义 | A，阻塞并构造区分反例 |
| 多对象量词错误 | A，修复量词或结论 |
| 隐藏真值直接或间接进入策略 | A，`SOLVE_PASS = false` |
| 合法信息相同但策略动作不同 | A，`INFORMATION_PASS = false` |
| 跨问复用但信息前提失效 | 只复用仍成立的数学关系 |
| 静态完全信息问题 | `INFO_RISK = OFF`，不增加审计表 |
| 敏感性/容差 | 结果不变时为 B，有限验证并披露 |
| JSON/指纹/monkeypatch/attestation | C，不阻塞、不派生工作 |
| 验证者递归委派 | 拒绝，保持星型总控 |
| DONE 后继续审计 | 停止；第三轮需用户重新打开 |
| Objective replaced by a different aggregation | A under `MODEL == PROBLEM` |
| Continuous constraint checked only on a coarse grid | fail `SOLVER == MODEL` until evidence matches the quantifier |
| Restricted heuristic called a global optimum | lower the claim to `HIGH-QUALITY FEASIBLE` or `HEURISTIC / APPROXIMATE` |

## 结构性验收

- 保留阶段 00–70 和既有路径。
- 协议 2.0 使用 `VERIFY_REQUEST` / `VERIFY_REPORT`。
- 旧审计文件可保留和读取，但新版恢复不继承逐阶段双门。
- 状态包含 A/B/C、影响、证据、处理决定、轮次 0/1/2 和四种状态。
- 一次验证、一次修复回归、DONE 强制停止。
- 信息风险只触发一个契约和三道条件门禁，不增加阶段。
- `ANSWER_VALIDITY_PASS` requires all three consistency gates and a recorded claim label.

## 结论

新版把定义、量词、合法信息依赖、决策空间、约束回代、独立证据和结论等级保留为答案级不变量；具体泄漏方式只放进 eval。元审计、软件防篡改与无限返修不进入默认范围，静态完全信息题也不会承担额外信息审计。

The three consistency gates consolidate existing answer-changing safeguards; the new evals hold objective fidelity, continuous quantifiers, restricted search spaces, and claim strength as regression cases without adding audit stages.
