# 阶段 00：整题简化

## 目标

先把题目压缩成可执行结构，避免在次要细节上提前展开。

## 最小产物

1. 每小问的一句话目标与正式输出。
2. 已知输入、缺失输入、单位、时间与空间范围。
3. 小问依赖图：哪些定义、参数或结果会被后问复用。
4. 交付边界：只求解、代码、结果文件，或用户明确要求的论文内容。
5. 可能改变答案的风险标签与对应插件。
6. 信息风险：命中部分观测、隐藏真值、多主体、通信/记忆、在线决策或跨问复用时记 `INFO_RISK = ON` 并加载信息可用性插件；否则记 `OFF` 及简短理由。
7. 初始状态：每问 `进行中`、验证轮次 `0`。

Risk tags only point to the weakest of `MODEL == PROBLEM`, `SOLVER == MODEL`, and `EVIDENCE == CLAIM`. Common tags are `INFO_RISK`, `CONTINUOUS_RISK`, `DISCRETIZATION_RISK`, `OPTIMALITY_RISK`, `REUSE_RISK`, and `OBJECTIVE_RISK`. Use only relevant tags; they do not create stages or long protocols.

只登记当前能说明影响的 A/B；C 不创建任务。旧审计文件仅登记为历史证据。

## 退出门 INTAKE_PASS

能用有限清单说明输入、输出、依赖、交付和主要风险，即进入阶段 10；不要求逐阶段监督或形式完备的审计包。
