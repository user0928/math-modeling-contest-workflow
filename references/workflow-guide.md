# 精简工作流说明

## 默认路径

`00 题目简化与风险路由 → 10 答案相关定义 → 20 最低充分模型 → 30 求解与回代 → 40 每问一次封闭验证 → 50 跨问一致性 → 60 交付与 DONE`

阶段编号和文件路径保留以兼容旧项目，但 00/10/20/30 不再分别建立独立监督双门。旧审计文件原样保留为历史证据；重新打开的小问从当前事实与协议 2.0 状态开始。

## 决策原则

1. 先把整题压缩成输入、输出、依赖、风险和交付。
2. 只展开能改变数学答案、结论可信度或明确交付的工作。
3. 用 A/B/C 记录影响，分类取决于实际后果而非问题名称。
4. 每小问把最高风险压缩为 1–3 个可判真的验证命题。
5. 初次验证后最多一次 A 类修复和一次直接依赖回归。
6. DONE 后停止；第三轮由用户重新授权。

`INFO_RISK = ON` 只加载一个信息可用性插件并把 `INFORMATION_PASS` 并入 DONE，不新增阶段或逐阶段审计表。

All risks converge on three consistency gates: `MODEL == PROBLEM`, `SOLVER == MODEL`, and `EVIDENCE == CLAIM`. Risk tags only identify the weakest gate and required evidence; they add no stage. Record `ANSWER_VALIDITY_PASS = true` only after all relevant checks pass.

## 代理结构

采用星型结构：总控默认自行分析、建模和求解；每小问至多一个验证者。验证者没有流程决定权、写权限或再委派权。

## 行动价值

行动准入不仅包括改变答案的工作，也包括用户明确要求和交付所需的复现工作。普通数模默认排除软件安全、可信计算、防篡改和审计链自证。

## 降级

独立线程不可用时，用不同推导或算法做同线程交叉检查并降低证据等级。只有未解决 A 才阻塞，不为等待监督无限暂停。
