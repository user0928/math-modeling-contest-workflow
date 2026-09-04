# 阶段 60：交付与 DONE

## 每问交付

1. 目标与采用定义。
2. 核心模型、假设、约束和算法。
3. 最终结果、单位、精度和版本。
4. 验证命题、结论与证据等级。
5. 未解决的 B 限制及其适用边界。
6. 数据、代码、命令、随机种子或手算等复现入口。
7. Verdicts for `MODEL == PROBLEM`, `SOLVER == MODEL`, and `EVIDENCE == CLAIM`.
8. Core-claim label: `PROVED / EXACT`, `NUMERICALLY VERIFIED`, `HIGH-QUALITY FEASIBLE`, or `HEURISTIC / APPROXIMATE`.

## DONE 检查

- 定义、变量、单位和方向明确；
- 模型匹配目标、决策空间和硬约束；
- `ANSWER_VALIDITY_PASS = true`;
- 已生成正式解并完成回代；
- 有一种风险比例适当的独立证据；
- 若 `INFO_RISK = ON`，`INFORMATION_PASS = true`；
- 无未解决 A；B 已披露。

满足后立即标记 `DONE`。禁止继续优化、扩展审计或启动第三轮，除非用户明确重新打开。

## 退出门 DELIVERY_PASS

结果可追溯、结论等级诚实、限制已披露，且未越过用户授权进入论文写作。

`DELIVERY_PASS` requires the claim label to match the evidence. A restricted search, sample-only check, or heuristic result cannot be promoted to an unconditional global claim.
