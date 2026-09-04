# 封闭验证模板

## VERIFY_REQUEST

```yaml
protocol: 2.0
subproblem: Q?
round: 1 # 仅可为 1 或 2
problem_and_data: <原题与必要数据或路径>
propositions:
  - id: P1
    statement: <可判真命题>
    tolerance: <数值或精确标准>
    pass_criterion: <PASS 条件>
allowed_scope:
  - <允许的推导、数据、文件或计算>
forbidden_scope:
  - 修改正式文件
  - 决定返修、推进、DONE 或重新打开
  - 创建或委派智能体
  - 递归审计、验证者审查、通用安全加固
```

命题总数为 1–3。轮次 2 只能覆盖已修改内容及其直接依赖。

## VERIFY_REPORT

```yaml
protocol: 2.0
subproblem: Q?
round: 1
proposition_results:
  - id: P1
    verdict: PASS | FAIL | UNCERTAIN
    evidence: <证明、手算、替代算法、复算、界或小规模穷举>
    evidence_level: <独立线程或同线程替代>
issues:
  - class: A | B
    evidence: <具体证据>
    affected_result: <不修会改变哪个结果>
    change_mechanism: <如何改变>
    bounded_action: <有限建议>
additional_A_exists: false
```

报告最多列五项 A/B。C 仅可作为非阻塞附注。验证者返回报告后停止。
