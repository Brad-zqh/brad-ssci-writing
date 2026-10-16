# Brad SSCI Writing

**`brad-ssci-writing`：以作者意图为先的社会科学论文写作与修订 skill。**

重点不是套用固定句型，而是把概念、证据和论证关系写清楚：简洁但不省略必要逻辑，修改但不擅自改研究。

An author-led writing skill for empirical social-science manuscripts: clear paragraph logic, restrained English, concept-first frameworks, evidence-matched citations, and coordinated revision correspondence. It is not a universal SSCI or journal template.

## 主要要求

- **尊重作者改动**：以最新修订和批注为准，非必要不改；只检查时不擅自改文件。
- **句间有实质衔接**：解释前后句为什么相连，而不是机械添加 therefore、however、furthermore。
- **精简但不跳步**：删重复、空话和不必要细节，保留必要前提、机制和解释。
- **概念框架先讲理论**：解释概念含义、研究基础及视角之间的关系，把公式、权重、数据提取放到方法部分。
- **贡献具体、尺度准确**：说明研究相对已有工作增加了什么认识，不把更多数据、模型或案例自动包装成理论突破。
- **实践启示有责任主体**：通常一段一个主要利益相关者，围绕研究发现、决策和可行行动展开。
- **不写防御性正文**：不反复向假想审稿人辩解，但保留真实的限制、参数来源和解释边界。
- **文献与正文逐项对应**：区分文献真实、题录正确、论点受支持；不虚构、不靠隐藏参数回避核查，保留 Zotero 引用域。
- **投稿文件联动核对**：主要数值、图表、章节定位、作者信息、回复信和 highlights 保持一致。
- **图表辅助论证**：概念图、流程图、结果图分工清晰；保留可编辑 PPTX 和绘图代码，更新数值时尊重原图形设计。

## 使用

### 各章节的论证顺序

技能要求先确定章节的论证任务和推进顺序，再润色句子；它不只是一个通用语言检查器。

| 章节 | 默认写作逻辑 |
| --- | --- |
| 摘要 | 问题与缺口 → 目标 → 精简设计 → 按目标排序的关键发现 → 一项启示 |
| 引言 | 现实重要性与矛盾 → 已有研究进展 → 有边界的 gap 及其影响 → 研究回应、目标与贡献 |
| 文献综述 | 概念与理论发展 → 测量方法比较 → 差异证据及解释 → 精确的未解问题；框架可作为末节 |
| 概念框架 | 概念定义 → 理论依据 → 具体情境中的含义 → 不同视角为何需要结合；不写计算流程 |
| 方法 | 研究区的分析价值 → 设计与数据来源 → 操作化与公式 → 具体分析 → 验证、敏感性或情景设计 |
| 结果 | 发现 → 关键定量证据 → 时间、空间或群体对比 → 图表支持；不复述研究问题，不提前做文献讨论 |
| 主要发现讨论 | 发现 → 与已有研究比较 → 异同的解释 → 研究意义；与研究目标保持对应 |
| 理论贡献 | 一项贡献 → 既有认识的边界 → 本研究实际推进 → 新增了什么理解 |
| 实践启示 | 一段一个主要利益相关者 → 发现支持的决策 → 具体可行行动 → 适度的预期作用 |
| 局限与未来研究 | 具体边界 → 对解释的影响 → 可行的后续研究 |
| 结论 | 综合回答研究问题 → 凝练贡献 → 有证据支持的意义；不重开方法或新增结果 |
| SI | 要支撑的问题 → 精确规则与配置 → 对应图表证据 → 必要解释 |

这些是作者偏好的论证顺序，不是统一段数或强制句型。最新的明确要求和已接受结构优先；只有三个目标时，不为凑模板制造第四项发现。详见 [章节论证规则](skills/brad-ssci-writing/references/section-roles.md)。

### 细节如何落实

- [22 项微观编辑决策](skills/brad-ssci-writing/references/micro-editing.md)：针对句间跳跃、字数压缩、therefore 重复、while 悬空、条件反复罗列、术语不清、地方标签、引用重复、数据来源主语和作者已认可表达，分别规定怎样改、不能改成什么。
- [16 项投稿细节检查](skills/brad-ssci-writing/references/submission-detail-checks.md)：区分同类段落字体与数学字体、英文弯引号与字体回退、真实重复与嵌套引用域、作者顺序与 CRediT、旧稿定位与新稿定位、实际上传文件与版本文件。
- 引文指南补充网页作者与年份、同 DOI 的作者标签、APA/CSL 元数据修复、结果版本选择及 LLM 图的矩阵和配置追溯。
- 图表指南补充长图注内容分流、符号与区间核对、PPTX 真正可编辑、保留原代码和图形设计更新数值。
- [情境校准案例](skills/brad-ssci-writing/references/examples.md) 说明在具体请求下应保留什么、应修改什么、何时不能自行发挥；工具测试不等同于写作质量认证。

### 调用示例

```text
用 $brad-ssci-writing 润色这段英文，只返回修改后的文字，保留我的意思，补齐句间逻辑，不要加入计算细节。
```

```text
用 $brad-ssci-writing 按我的批注修改概念框架，未批注的内容非必要不改；发现证据或数值问题先告诉我。
```

```text
用 $brad-ssci-writing 核对 manuscript、SI、response letter 和 cover letter，只检查对应关系，不改文件。
```

```text
Use $brad-ssci-writing to revise this discussion paragraph with clearer links, concise wording, and no change to the claims or citations.
```

## 安装到 Codex

让 Codex 使用系统自带的 `skill-installer`，从本仓库安装：

```text
Install the skill from Brad-zqh/brad-ssci-writing at skills/brad-ssci-writing using skill-installer.
```

也可将 `skills/brad-ssci-writing` 整个文件夹复制到你实际使用的 Codex `skills` 目录。安装后在下一轮对话调用 `$brad-ssci-writing`。临时文件和安装位置应遵守自己的存储设置。

## 可选检查工具

`review_prose.py` 只读检查 UTF-8 的 TXT/Markdown，不改文件，不评价文献真假，也不给“可以投稿”的自动结论：

```bash
python skills/brad-ssci-writing/scripts/review_prose.py draft.txt --json
python -B -m unittest discover -s tests -v
```

它只提示重复句、反复出现的因果连接词、防御性套话、含混标签和过长句。所有提示都需要结合上下文判断，不应为了消除提示而删掉作者认可的表达。

## 内容与边界

- 入口和按任务读取的指南见 [SKILL.md](skills/brad-ssci-writing/SKILL.md)。
- [示例](skills/brad-ssci-writing/references/examples.md) 全部为专门编写的说明性例句，不是论文摘录或真实实验结果。
- 本仓库不包含投稿稿件、研究数据、审稿人信息、个人联系方式或账号凭据。
- 语言润色不等于事实核查；文件一致不等于所有科学依据问题已经解决；skill 不能保证接收或替代作者判断。
