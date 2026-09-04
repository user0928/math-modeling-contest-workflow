# 规则覆盖表

| 风险或行为 | 主要位置 | 默认处理 |
|---|---|---|
| 整题简化、输入输出、依赖 | stage 00 | 一次完成 |
| 定义、分母、方向、单位、边界 | stage 10 | 可能改答案则 A |
| 多对象量词与集合聚合 | stage 10 + plugin | 量词错误为 A |
| 信息可用性、隐藏真值、策略依赖 | information-admissibility plugin | 违规为 A；条件式门禁 |
| 目标、硬约束、决策空间 | stage 20 | 不一致为 A |
| 代码、参数、随机种子、回代 | stage 30 | 服务模型与复现 |
| 连续最优、几何可行性 | risk plugins | 按结论风险选择证据 |
| 敏感性、容差、稳定性 | stages 30/40 | 通常 B，有限验证并披露 |
| 每问 1–3 个封闭命题 | stage 40 + supervision | 一次验证 |
| A 修复后的回归 | stage 40 | 只允许轮次 2 |
| 第三轮 | SKILL + state | 用户明确重新打开 |
| 跨问传播 | stage 50 | 只处理实际依赖 |
| `MODEL == PROBLEM` | stages 10/20 + information plugin | Definition, objective, constraint, information, or quantifier mismatch is A |
| `SOLVER == MODEL` | stages 20/30 | Search-space, discretization, or computed-objective mismatch is A unless the conclusion is explicitly downgraded |
| `EVIDENCE == CLAIM` | stages 40/60 | Insufficient evidence lowers the claim; answer-changing overclaim is A |
| DONE | stage 60 | 满足即停止 |
| 通用软件安全、完整性与可信计算加固 | SKILL + stage 30 | C，默认不阻塞 |
| 递归委派、审查验证者 | supervision | 禁止 |
| 旧盲审计包 | workflow + state | 历史可读，不作新门控 |

保留的答案级不变量覆盖：定义与量词、合法信息依赖、原始决策空间、约束回代、独立证据和诚实结论等级。具体失败形态放在 eval，不继续堆入主流程。删除的默认目标是逐阶段盲审、元验证、形式完备性和无限返修。

These three gates index existing safeguards; they are not a new audit chain. Keep risk tags and concrete failure shapes out of the main workflow when an eval can cover them.
