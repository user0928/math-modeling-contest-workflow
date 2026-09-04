# 阶段 40：每小问一次封闭验证

## 目标

验证具体命题，而不是寻找所有可能缺陷。

## 轮次

- 轮次 1：用 `VERIFY_REQUEST` 提交 1–3 个封闭命题。
- 若无 A：记录 B 限制并完成。
- 若有 A：总控只修复该问题及直接依赖。
- 轮次 2：仅回归修改内容和直接依赖。
- 轮次 2 后强制停止；第三轮必须由用户将状态设为 `用户重新打开`。

验证深度默认一层。只有验证结果互相矛盾且可能改变答案时，才检查验证程序本身。

## 证据

按风险选择证明、手算、不同推导、替代算法、数值复算、界、不变量或小规模穷举。独立线程不可用时，在当前线程采用不同方法并降低证据等级，不无限等待。

The 1-3 propositions must cover the highest answer-changing risk and decide the relevant parts of:

- `MODEL == PROBLEM`: the original definitions, objective, constraints, information boundary, and quantifiers were not rewritten;
- `SOLVER == MODEL`: the program search space, discretization, sampling, and computed objective match the model;
- `EVIDENCE == CLAIM`: the evidence supports the final claim's quantifiers and strength.

Reproducing solver output, checking file completeness, obtaining a small residual, or rerunning the same evaluator cannot alone validate the answer. Continuous, all-object, global, or optimal claims need evidence matching those quantifiers; otherwise lower the claim level.

## 退出门 VERIFY_PASS

不存在未解决 A；B 已有限检查并披露；验证轮次与证据等级已记录。
