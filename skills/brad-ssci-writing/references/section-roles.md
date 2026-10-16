# Section argument contracts

Follow these as Brad's default section-writing logic, unless the latest explicit instruction or accepted outline overrides them. They specify argument order and paragraph jobs, not fixed sentence counts or a universal SSCI template. Do not restore outdated subsection numbers or paragraph counts from older project cards.

## Whole-paper alignment

Keep one substantive research problem as the spine. Constructs, indices, models, data pipelines, and scenario experiments serve that problem instead of becoming separate stories.

Privately map **question → literature gap → objective → analysis/result → discussion claim**. Keep this order recognizable across chapters. The Introduction motivates the question; the review establishes its foundations; Methods explains how it is answered; Results supplies the evidence; Discussion interprets the answer. A planning extension can enrich an objective without requiring an invented new gap.

Apply the relevant contract even when editing one paragraph, but do not rewrite unaffected chapters or show an internal planning worksheet when only prose was requested. Verify current venue rules when asked about journal compliance.

## 1. Abstract

**Ordered moves:** problem and tension/gap → objective and useful setting → compact data/design/measure → decisive findings in objective order → one supported implication.

Develop one connected summary: the context establishes the question, design explains the approach, findings answer the question, and the last sentence states why that answer matters. Keep methodological inventories subordinate to the problem. Explain a central measure's scope before presenting its results.

Choose a few principal findings rather than a results catalog. Use First/Second/Third when that is the accepted organization, and retain “Several findings emerged” if the author chooses it. Do not remove an accepted short transition merely for maximal compression.

**Keep out:** every processing step or robustness test, unexplained “qualifying options,” repeated criteria, unsupported policy effects, and findings not established in the paper.

**Exit check:** the reader can connect each finding to what was assessed. Verify population, comparison, year, units, denominator, and whether the result is observed or simulated.

## 2. Introduction

**Chapter sequence:** substantive relevance and tension → established progress and its boundary → specific gaps and their consequences → study response, linked objectives, and contributions.

### Opening and context

Define the central phenomenon when necessary, explain its social or practical importance, then narrow to the activity and setting in which the problem arises. A setting-specific study needs a substantive rationale: explain why the phenomenon takes a distinctive form there or why the setting reveals the question. Data availability alone is not the rationale.

Do not jump directly from a broad definition to a new index. Connect the broader phenomenon to the choices and conditions people encounter in that setting. Support claims of global prominence, changing behavior, and the causes of a trend rather than treating opening rhetoric as exempt from evidence.

### Gap paragraphs

**Each gap:** what previous work established → the specific perspective/relationship/comparison left incomplete → why that omission changes what can be understood → the evidence or question needed next.

Recognize real prior progress before describing its boundary. Limited integration is not complete absence of research. Use a concrete example when an abstract omission is otherwise hard to understand, without repeating several versions of it.

When supported by the actual paper, distinguish:

- **Conceptual gap:** why a provision-only account misses choices, expectations, or experiences. Explain the meaning that is missing, not merely the need for another score.
- **Distributional/integrative gap:** what separate quality, cost, and travel comparisons cannot establish about the same usable opportunities and groups. Explain the joint constraint; do not abruptly announce “three criteria.”
- **Temporal gap:** what changing provision, services, or preferences makes invisible in a snapshot, such as persistence or uneven development.

These are relevant gap types, not a required agenda for every new paper. Do not manufacture a gap or force three gaps when the author has accepted another structure.

### Study response and ending

State the actual design and objectives in the same order as the motivated gaps. Explain briefly which analysis answers which question. End with the supported conceptual, empirical, or practical contribution, rather than a full processing workflow.

**Keep out:** detailed equations, processing settings, a mini Results section, and theoretical novelty claims based only on having more data or a new model.

**Exit check:** each objective answers a previously motivated question and each promised contribution is traceable to work actually performed.

## 3. Literature review

**Chapter sequence:** definitions/theoretical development → measurement approaches → comparative evidence and explanations → precise remaining issue; the conceptual framework can close the review.

### Definitions and conceptual development

Explain how the phenomenon is defined, which dimensions different definitions include, and why the represented perspectives matter. Compare substantive ideas rather than listing author–year summaries. Distinguish a theoretical concept from the data available to measure it.

### Measurement and units

Compare what approaches measure, at which unit and scale, from which evidence, and with what interpretive boundary. If moving from individual-level assessment to an establishment or neighborhood setting, explain why that unit matters: an aggregate personal score and the range of options available in a local environment answer different questions.

Derive a bounded measurement issue from that comparison. Keep proposed prompts, weights, API calls, and calculations out of the review. A compact comparison table should support, not replace, the narrative argument.

### Inequality and explanations

Start with the social or spatial differences identified in prior studies, then explain the relevant reasons those differences may arise using verified evidence. Link the access dimensions to differences in socioeconomic resources, location, needs, provision, cost, or mobility where applicable.

A taxonomy of availability, accessibility, or affordability is not by itself an explanation of social inequality. Explain why those conditions differ between people or places and what consequences follow. Include preferences or awareness only when they serve that argument; do not introduce an unrelated awareness claim in a paragraph about price and walking access.

End by identifying the integrated comparison, distributional question, or temporal relationship that prior approaches leave unresolved. Do not repeat the entire Introduction gap list or append a separate research-aim section by default; aims stay in the Introduction, while a short synthesis can bridge into the framework.

**Paragraph sequence:** topic/theoretical proposition → comparison or synthesis of sources → interpretation of their common ground or difference → bounded implication for the issue under review.

**Keep out:** one paragraph per citation, recurring “this study will…” announcements, absolute novelty claims, and operational details.

**Exit check:** the review establishes the framework's foundations and shows exactly what remains unobserved, not merely that more research would be useful.

## 4. Conceptual framework

**Placement:** the last literature-review subsection when it synthesizes those foundations, unless the accepted outline specifies otherwise. Derive the number from the actual outline and synchronize downstream references; do not hard-code a number.

**Opening sequence:** what an existing perspective represents → why an additional perspective matters → what the integrated framework represents → its dimensions and relationships.

**Construct paragraph:** definition → relevant theoretical foundation → meaning in the study setting → link between provision and users' choices/expectations/experiences → a conceptual implication when it adds something.

Explain the bridge. Naming a physical attribute and then naming consumer perceptions does not establish why both should be considered. For instance, provision can shape available options while choices determine which enter users' experiences. Explain the applicable relationship without claiming a proxy measures verified behavior.

Consumption frequency may belong to the concept when repeated choices matter; the review-based count and frequency-weighting rule remain operational details. Likewise, cultural suitability, a classification of service types, and a computed diversity score are different levels of explanation.

Do not pretend each dimension directly measures both sides. Explain its actual role and the integration achieved by the framework. Vary paragraph development and endings instead of repeatedly closing with “This dimension therefore considers…”.

**Keep out:** datasets and extraction prompts, score bounds, normalization, weighting, missing-data treatment, and equation-by-equation descriptions. Put them in Methods or supporting information.

**Exit check:** readers understand what the constructs mean and why the perspectives belong together before learning how they are computed. The figure and concept table should reinforce this explanation rather than silently replacing it with a pipeline.

A final framework subsection may briefly position this study's conceptual perspective. This does not license a second research-aim section or the operational pipeline inside the review. Conceptual frequency of use and a particular frequency-weighting algorithm must remain distinct.

## 5. Methods

**Chapter sequence:** setting and analytical value → research design/data sources → construct operationalization → empirical analyses → validation/sensitivity and, when relevant, planning-scenario design. Preserve an accepted arrangement that groups these functions differently.

### Setting, design, and data

Explain the setting's analytical relevance before an inventory of characteristics. Introduce the analytical stages and their purpose once; do not keep repeating the objectives throughout Methods.

**Data-source paragraph:** information needed → what was obtained from which source → why it enters the analysis → relevant coverage and time alignment.

Prefer “We obtained…” or “We collected…from…” when using the author's active research voice. Connect each source to its purpose, not with a succession of “Furthermore” clauses. Report sample and observation unit clearly: establishments versus establishment-year observations, annual versus cumulative records, retrospective application of current attributes, and reused population composition.

### Measures and equations

**Measure paragraph:** previously introduced construct → input evidence and unit → operational definition → equation/rule → symbol and unit definitions → aggregation and missing-data treatment.

Introduce an equation's purpose before the equation group and define its symbols immediately afterward or where first needed. Make denominators, direction, and valid zero versus unavailable evidence explicit. Keep parameter sources, transformations, and value selection reproducible, even if the detail is in supporting information.

### Analysis and scenarios

**Analysis paragraph:** question/comparison → outcome or estimand → unit/sample → method and applicable adjustment → uncertainty → relevant robustness check. Explain what the model answers before its implementation.

**Scenario design:** decision objective → candidate universe → resources and constraints → selection/allocation procedure → outcome and denominator → baseline or alternative objective. Specify what is common across competing priorities. Do not label hypothetical candidates confirmed premises or insert the estimated benefit into a design paragraph.

Separate repeatability, cross-model consistency, reference agreement, and external validity. Move secondary implementation and extensive configurations to the supplement without losing the information necessary to reproduce the work.

**Keep out:** a second conceptual-framework essay, results disguised as method justification, unsupported institutional feasibility, and technical steps with no explained analytical purpose.

**Exit check:** the reader can identify how each objective is tested, what each measure represents, and where the exact operational details are documented.

## 6. Results

**Chapter sequence:** primary substantive pattern → corresponding temporal/spatial/group contrasts → integrated or extended analyses → robustness and decision scenarios in the accepted design order. Match the questions rather than the order output files were generated.

**Paragraph sequence:** finding-led topic sentence → minimum decisive quantitative evidence → important contrast or heterogeneity → relevant figure/table support. The opening can incorporate the decisive number when natural.

Report direction, magnitude, year, population, units, comparison, and denominator where required. Distinguish local conditions from reachable opportunities, an area score from every establishment's quality, and recorded price bands from household-specific affordability. Keep the principal pattern ahead of secondary contrasts.

A figure/table citation should support a substantive answer, not substitute for it. Do not write a panel-by-panel tour without a finding. Robustness reporting should say which finding persists or changes and under what specification, not only that another test was conducted.

For scenarios, compare the benefits of different decision priorities under common resources and state whose opportunities or coverage change. Keep the result conditional, not an implemented intervention or a causal effect.

**Keep out:** an opening roadmap repeating research questions, “To answer RQ…” paragraph openers, literature comparisons, unsupported mechanisms, and policy recommendations. Prefer compact declarative subsection headings to question titles unless the author chose otherwise.

**Exit check:** each main objective has an evidence-based answer and readers can locate its decisive support without relying on interpretation found only in a caption.

## 7. Discussion

**Chapter sequence:** main findings and interpretation → theoretical implications → practical implications → limitations/future research. Retain explicitly accepted combined or differently named sections, while keeping these argumentative jobs distinct.

### 7.1 Main findings

Use one brief opening synthesis when needed. Then organize finding paragraphs in objective order. If the accepted paper has three objectives, First/Second/Third should make that correspondence visible; do not invent a fourth finding to fill a template.

**Each paragraph:** principal finding → comparison with prior research → evidence-based explanation of agreement/difference → substantive theoretical or planning meaning.

Use only the numbers needed to anchor interpretation. Do not copy Results, list every significant comparison, or jump from a number to a broad recommendation. Distinguish an evidenced mechanism from a plausible interpretation; do not invent an explanation just to make the paragraph flow.

### 7.2 Theoretical implications

**Each paragraph:** one specific contribution claim → prior achievements and their relevant boundary → what this study actually advances → what changes in understanding.

Align contributions with Introduction gaps but explain what has now been learned rather than repeating “little is known.” Conceptual enrichment, integration of constraints and distribution, temporal understanding, and methodological extension are possible contribution types, not a mandatory four-paragraph list.

A temporal contribution needs its rationale: changing provision, services, and preferences can accumulate or reverse; repeated observations distinguish persistence and uneven development that a snapshot cannot show. Do not simply announce extra years or repeat “long-term.”

An integrated-access contribution should explain why favorable conditions measured separately do not establish that the same usable options are available to a person or group. Once clear, use a short backward reference instead of listing every criterion again in the next sentence.

Keep the social-science question central. A new LLM, larger dataset, or more years is not automatically a theoretical advance. Explain methodological contributions through what becomes measurable or comparable and the knowledge it enables, without implying independent ground truth or causal identification.

### 7.3 Practical implications

**Each paragraph:** one principal stakeholder → a finding-linked decision → a short chain of feasible actions → appropriately bounded benefit or planning significance.

Use a small justified actor set. Do not expand each paragraph into a coalition of agencies, operators, institutions, residents, and researchers. Explain the actor's relationship to the decision. If asked only to reduce stakeholder scope, keep the accepted substantive content close to its original form.

When actually added, quantitative location optimization or scenario comparisons can strengthen practical implications by comparing decision priorities. Keep hypothetical candidate sites distinct from confirmed premises and simulated coverage distinct from an implemented benefit. Do not invent a mandate, subsidy, regulation, or implementation feasibility.

Avoid generic calls to “raise awareness,” “strengthen collaboration,” or “improve sustainability” without a particular finding, actor, and action. Use selective numerical support rather than repeating the full scenario table.

### 7.4 Limitations and future research

**Each limitation:** a specific data/design/measurement/scope boundary → consequence for interpretation → a feasible study that could address it.

First/Second/Third/Finally can organize accepted limitations, often in one compact paragraph. Do not force four items, invent generic weaknesses, or create a defensive inventory. Suggest a targeted dataset, comparison, or validation rather than repeatedly saying “more research is needed.”

State necessary distinctions once in the appropriate place and use consistent language afterward; do not repeat what the study does not claim throughout the manuscript.

**Discussion exit check:** readers can distinguish the empirical answer, its interpretation relative to literature, the contribution to understanding, a finding-linked decision, and the remaining inferential boundary.

## 8. Conclusion

**Sequence:** integrated answer to the research problem → concise supported contribution → one broader or practical significance statement at the scale of the evidence.

Synthesize rather than copy the abstract or list every result in sequence. Keep a quantitative anchor only when important. Do not reopen methods, introduce new results/references, or append another limitations inventory. Do not create a new conclusion during a local edit if the accepted structure has none.

**Exit check:** the ending answers the question raised in the Introduction and leaves a precise takeaway rather than an inflated promise.

## 9. Supporting information

**Each note:** the methodological/evidentiary question supported → exact definitions/rules/configuration → corresponding table/figure/result → concise interpretation when needed.

Organize notes by function and connect them to the main manuscript. Preserve counts, parameters, units, filtering, aggregation, denominators, and settings needed to reproduce the analysis. Do not bury a changed primary method or replace a missing source with an unsupported assertion.

Keep tables compact and terminology aligned with the main text. Distinguish primary analysis from alternatives and validation statistics by what they actually establish.

**Exit check:** readers can trace a main-text method or robustness statement to exact supporting details without contradictory versions or unexplained numbers.

## Section-level acceptance check

Before returning the requested passage, check privately:

1. Does the chapter follow its argument sequence and the latest accepted outline?
2. Does this paragraph perform one necessary move and connect to its neighbors?
3. Is a premise missing despite the presence of transition words?
4. Has content moved into the wrong section: calculation in concepts, aims in the review, literature interpretation in Results, or detailed results in a cover letter?
5. Do gap, objective, evidence, and contribution correspond without altered facts or invented support?
6. Can repeated material be removed without deleting the reason the next claim follows?

Do not show the worksheet for a text-only request or claim a whole-paper audit when only one passage was revised. For revision-letter and cover-letter argument sequences, read [Revision and submission](revision-submission.md).

For sentence-level repairs and concrete author complaints, use [Micro-editing decisions](micro-editing.md). For field, font, caption, numbering, and file-version execution, use [Submission detail checks](submission-detail-checks.md). A correct chapter outline does not establish that those local decisions have been handled correctly.
