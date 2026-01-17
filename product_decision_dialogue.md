# Product Go/No-Go Decision Framework
**Version 1.0** | Optimized for AI Agent Evaluation

---

## Purpose & Overview

This framework evaluates product ideas using weighted multi-criteria analysis to generate structured go/no-go recommendations. It's designed to combat cognitive biases (especially sunk cost fallacy) and force evidence-based decision making.

**Core Principle**: Every score must be backed by specific, verifiable evidence. Intuition and conviction are measured separately but cannot substitute for concrete data.

---

## How to Use This Framework

### Evaluation Process

1. **Gather Evidence** - For each lever, collect specific data from defined sources
2. **Score Each Lever** - Rate 1-10 using the detailed rubrics below
3. **Document Reasoning** - Write why you assigned each score
4. **Calculate Total** - Multiply scores by weights and sum (max: 170 points)
5. **Generate Recommendation** - Apply decision thresholds
6. **Sensitivity Analysis** - Identify which factors could flip your decision
7. **Create Dissenting View** - Argue against your recommendation

### Decision Thresholds

| Score Range | Decision | Confidence Needed | Action |
|-------------|----------|-------------------|--------|
| 70-170 | **STRONG GO** | 2+ high-weight levers score 7+, no critical red flags, sunk cost <5 | Commit resources, set aggressive timeline, assemble team |
| 40-69 | **CAUTIOUS PROCEED** | 1+ high-weight lever scores 7+, clear hypothesis to test | Build minimum prototype, time-box to 4-8 weeks, set decision criteria |
| 0-39 | **STRONG NO-GO** | High-weight levers <6, multiple red flags, better alternatives exist | Document lessons, archive research, evaluate alternatives |

---

## The Nine Decision Levers

### High-Weight Levers (3x multiplier)

These three levers are the foundation of product success. If all three score poorly (<6), strongly reconsider regardless of other factors.

---

## Lever 1: Market Window (Timing)
**Weight: 3x** | **Strength: HIGH** | **Category: External Market**

### What This Measures
Is there a specific, time-bound reason this product needs to exist NOW? Does the window of opportunity have an expiration date?

### Evidence Sources
- Market trend reports with publication dates
- Competitor product launch timelines
- Regulatory change schedules
- Technology adoption curves
- Google Trends data
- Industry analyst predictions

### Scoring Rubric

#### Score 9-10: Critical Window Closing (3-6 months)
**Required Evidence:**
- Specific external catalyst with documented date (e.g., "GDPR-like regulation takes effect June 2026")
- Competitor intelligence showing imminent competitive launches within 6 months
- Technology platform announcing breaking changes or deprecation deadline
- Market inflection point verified by 3+ independent sources

**Examples:**
- "New EPA regulation requires compliance by Q2 2026, creating 6-month window before market saturates"
- "iOS 18 deprecates key API in September 2025, forcing app migration"
- "Major platform announced shutdown of competing service, creating 4-month land-grab opportunity"

**Red Flags to Avoid:**
- "Feels urgent" without external catalyst
- Urgency based on internal readiness, not market forces
- Vague "trend is growing" without specific inflection point

---

#### Score 6-8: Favorable Timing Window (6-18 months)
**Required Evidence:**
- Market data showing sustained growth trajectory (>20% YoY)
- Early adopter demand signals (social media mentions, search volume trends)
- Competitive landscape analysis showing clear gaps
- Industry reports predicting market expansion

**Examples:**
- "AI coding assistants market growing 45% YoY with fragmented competition"
- "3 major enterprise buyers mentioned this pain point unprompted in discovery calls"

---

#### Score 3-5: Neutral Timing (18+ months)
**Required Evidence:**
- Stable market conditions, no urgent catalysts
- Opportunity will exist for foreseeable future
- Competition can enter anytime

**Examples:**
- "Project management SaaS - mature market, no time pressure"
- "Consumer finance app - evergreen problem"

---

#### Score 1-2: Poor Timing or Window Closed
**Required Evidence:**
- Market oversaturated (10+ established competitors with >80% market coverage)
- Technology becoming obsolete (declining search trends for 12+ months)
- Peak hype already passed (Gartner "Trough of Disillusionment")

**Examples:**
- "Launching a Clubhouse clone in 2024"
- "Building on platform that announced sunsetting"

---

### Verification Checklist for Market Window
- [ ] Can you name the specific external event/catalyst creating urgency?
- [ ] Is the timing claim falsifiable? (Could evidence prove it wrong?)
- [ ] Have you searched for recent market reports (within 3 months)?
- [ ] Would an objective observer agree the window is time-bound?
- [ ] If there's no window, why not admit "score: 3" instead of inflating?

---

## Lever 2: Strategic Moat
**Weight: 3x** | **Strength: HIGH** | **Category: Competitive Advantage**

### What This Measures
Do you have a defensible competitive advantage that compounds over time and prevents competitors from easily replicating your product?

### Types of Moats (with examples)

1. **Legal/IP Moat**
   - Granted utility patents covering core functionality
   - Exclusive licenses or data rights
   - Trademarks in regulated industries

2. **Data Moat**
   - Proprietary dataset that improves product with scale
   - Data network effects (each user makes product better for others)
   - Exclusive data partnerships

3. **Network Effects Moat**
   - Same-side effects: More users → more value for each user
   - Cross-side effects: More supply → more demand → more supply
   - Must specify the growth mechanism

4. **Brand/Trust Moat**
   - Reputation in high-stakes domain (finance, healthcare, security)
   - Regulatory certifications difficult to obtain
   - Years of trust-building required

5. **Process/Trade Secret Moat**
   - Proprietary manufacturing process
   - Unique operational advantages
   - Non-replicable relationships or expertise

### Evidence Sources
- Patent databases (USPTO, EPO, WIPO)
- Proprietary data inventory with growth metrics
- Customer retention data showing switching costs
- Network effect metrics (k-factor, viral coefficient)
- Legal opinions on IP defensibility

### Scoring Rubric

#### Score 9-10: Defensible Moat That Compounds
**Required Evidence (need 2+ of these):**
- **Granted patents**: Utility patent(s) in major jurisdictions covering core value proposition, attorney confirms enforceability
- **Exclusive data**: Signed agreements for proprietary data access, or dataset that grows with usage
- **Strong network effects**: Documented growth loops with k-factor >1.5, or quantified cross-side effects
- **High switching costs**: Customer data showing >$50k cost to switch, or 6+ month migration time

**Examples:**
- "Granted patent on novel ML training method, validated by IP attorney, covers core algorithm"
- "Exclusive partnership with FDA for regulatory data, 10-year agreement"
- "Marketplace with 15k supply-side users and 50k demand-side, doubling every 6 months due to network effects"

**What Doesn't Count:**
- "We'll execute better than competitors" (not a moat)
- "Patent pending" without strong prior art analysis (weak)
- "Network effects" without specific growth mechanism (handwaving)
- "First-mover advantage" alone (not sustainable)

---

#### Score 6-8: Temporary Advantage (1-2 year lead)
**Required Evidence:**
- Patent pending with reasonable likelihood of approval
- Proprietary insights or relationships that take time to build
- Technical complexity requiring specialized expertise
- First-mover in emerging category with learning curve

**Examples:**
- "Patent pending on delivery algorithm, attorney says strong case"
- "Relationships with 20+ enterprise buyers built over 2 years"
- "Technical implementation requires PhD-level expertise in narrow field"

---

#### Score 3-5: Minimal Differentiation
**Required Evidence:**
- Advantage based primarily on execution speed
- Open source or commodity technology stack
- Low barriers to entry

**Examples:**
- "Better UX than competitors" (easily copied)
- "Using GPT-4 API" (everyone has access)

---

#### Score 1-2: No Moat, Entrenched Competition
**Required Evidence:**
- Competing against established players with superior resources
- No unique IP, data, or network effects
- Commodity offering

---

### Verification Checklist for Strategic Moat
- [ ] Have you consulted with IP attorney if claiming patent moat?
- [ ] Can you name the specific mechanism that prevents replication?
- [ ] What would it cost a well-funded competitor to replicate? (If <$500k and <6 months, weak moat)
- [ ] Steel-man test: Describe how competitor would try to replicate, then explain why they can't
- [ ] Are you confusing "unique approach" with "defensible advantage"?

---

## Lever 3: Distribution Edge
**Weight: 3x** | **Strength: HIGH** | **Category: Go-to-Market**

### What This Measures
Do you have direct access to your target audience at scale? Can you reach customers without expensive, unproven acquisition channels?

### Evidence Sources
- Email marketing platform metrics (subscribers, open rates, unsubscribe rates)
- Social media analytics (followers, engagement rate, reach)
- Existing customer database (size, NPS, purchase frequency)
- Partnership agreements (signed contracts for co-marketing)
- Platform access confirmations (API partnerships, featured placement)

### Scoring Rubric

#### Score 9-10: Direct Access at Scale
**Required Evidence (need 1+ of these):**
- **Email list**: 10,000+ subscribers, 20%+ open rate in last 90 days, <5% unsubscribe rate
- **Social following**: 50,000+ followers in target niche, 2%+ engagement rate on recent posts
- **Existing customers**: 1,000+ paying customers, <5% monthly churn, NPS >50
- **Platform partnership**: Confirmed featured placement or API integration with signed agreement
- **Community**: Owned forum/community with 5,000+ daily active users

**Quantitative Thresholds:**
| Channel | Minimum Scale | Minimum Engagement | Maximum Attrition |
|---------|--------------|-------------------|-------------------|
| Email | 10k subscribers | 20% open rate | 5% unsubscribe |
| Social | 50k followers | 2% post engagement | N/A |
| Customers | 1k paying | NPS >50 | 5% monthly churn |
| Community | 5k DAU | 30% weekly active | 10% monthly churn |

**Examples:**
- "Newsletter with 15k subscribers, 28% open rate, averaging 450 link clicks per send"
- "2,500 B2B customers, NPS 67, 94% would recommend us"
- "Partnership with Salesforce AppExchange, confirmed featured listing in Q2"

**What Doesn't Count:**
- Twitter followers without engagement data (bots/inactive accounts)
- Email list purchased or scraped (not opted-in)
- "Could partner with X" without signed agreement

---

#### Score 6-8: Moderate Audience or Indirect Access
**Required Evidence:**
- 2,000-10,000 engaged contacts
- Partner willing to co-market (email/letter of intent)
- Adjacent audience that overlaps with target

**Examples:**
- "5k email subscribers, 15% open rate, in adjacent space (HR tools, targeting finance)"
- "Advisor willing to introduce to their 50-person Slack community"

---

#### Score 3-5: Small Audience, Building from Scratch
**Required Evidence:**
- <2,000 contacts
- No warm introductions to target audience
- Relying on cold outreach or paid acquisition

**Examples:**
- "500 Twitter followers, mostly friends/family"
- "Will use Google Ads and SEO"

---

#### Score 1-2: No Distribution, Highly Competitive CAC
**Required Evidence:**
- Zero owned audience
- High customer acquisition cost in market (documented CAC >$500 for B2B or >$50 for B2C)
- Saturated paid channels

---

### Verification Checklist for Distribution Edge
- [ ] Have you pulled actual metrics from platforms (not estimates)?
- [ ] Is your audience genuinely relevant to this new product? (Don't assume transfer)
- [ ] Can you calculate expected conversion rate based on past campaigns?
- [ ] Are you counting "awareness" (followers) vs "distribution" (ability to reach)?
- [ ] If claiming partnership, do you have written confirmation?

---

### Medium-Weight Levers (2x multiplier)

These levers are important but not make-or-break. They can tip close decisions or highlight specific risks.

---

## Lever 4: Conviction Level
**Weight: 2x** | **Strength: MEDIUM** | **Category: Founder Psychology**

### What This Measures
How committed are you really? Not how excited you feel, but what you're willing to sacrifice. Conviction must be backed by action, not just words.

### ⚠️ Warning
This lever is highly susceptible to self-deception. Use objective proxies (actions taken) rather than subjective feelings.

### Evidence Sources
- Decision journal entries over time
- Actual money/time invested from personal resources
- Opportunities declined to pursue this
- Consistency of interest over 30+ days

### Scoring Rubric

#### Score 9-10: Deep Conviction Backed by Personal Commitment
**Required Evidence (need 3+ of these):**
- Would invest personal savings: >$10k or >10% of net worth
- Already building prototype in spare time without being asked
- Willing to work exclusively on this for 18+ months
- Turned down other job/opportunity to pursue this
- Can articulate specific contrarian insight others miss
- Have thought deeply about failure modes and remain committed
- Consistently return to this idea over 3+ months despite exploring alternatives

**Objective Proxies:**
- Spending own money on validation (customer interviews, prototypes)
- Working nights/weekends on this for 30+ days
- Can explain why smart people are wrong about this market

**Examples:**
- "Invested $15k of savings into customer research, quit job to pursue full-time"
- "Been exploring this space for 6 months, tried 3 other ideas, keep coming back to this"
- "Understand why incumbents won't solve this due to innovator's dilemma"

**What Doesn't Count:**
- "I'm really passionate about this" (words not actions)
- Recent enthusiasm spike from positive feedback
- Excitement without sacrifice

---

#### Score 6-8: Interested with Reservations
**Required Evidence:**
- Would work on this but keeping other options open
- Excited about some aspects, uncertain about others
- Need external validation before committing fully

**Examples:**
- "Would try this for 3-6 months while consulting on side"
- "Love the market, unsure about specific approach"

---

#### Score 3-5: Low Conviction, Exploring Opportunistically
**Required Evidence:**
- Several unresolved doubts
- Pursuing due to external factors (competition, trends, FOMO)
- Would abandon if faced with obstacles

**Examples:**
- "Seems like a hot space, might as well try"
- "People keep asking me to build this"

---

#### Score 1-2: Fundamental Doubts
**Required Evidence:**
- Cannot envision success scenario clearly
- Pursuing due to sunk cost or social pressure
- Actively looking for reasons to stop

---

### Special Conviction Test Questions

Ask yourself these. If you can't answer clearly, score is likely <6:

1. **The Money Test**: "Would I invest $10k of my own money today knowing what I know?"
2. **The Time Test**: "Would I work on this exclusively for 18 months even if it fails?"
3. **The Opportunity Cost Test**: "Am I pursuing this because it's the best option, or because I've already started?"
4. **The Contrarian Test**: "What do I understand about this market that smart people miss?"
5. **The Fear vs Evidence Test**: "Am I doubting this because I'm afraid, or because evidence says it won't work?"

### Verification Checklist for Conviction
- [ ] List specific doubts - categorize each as fear-based or evidence-based
- [ ] What would change your conviction to 9-10? (If answer is vague, conviction is low)
- [ ] Has conviction been stable for 30+ days or does it fluctuate with mood?
- [ ] What have you sacrificed to pursue this? (Time, money, other opportunities)
- [ ] Steel-man: What would a skeptic say about your conviction level?

---

## Lever 5: Option Value
**Weight: 2x** | **Strength: MEDIUM** | **Category: Strategic Learning**

### What This Measures
Even if this specific product fails, does building it create strategic value? Will it unlock capabilities, relationships, data, or insights that enable bigger opportunities later?

### ⚠️ Warning
"Option value" is often used to rationalize weak ideas. It's only valid if you can specify what options are unlocked and why they're valuable.

### Evidence Sources
- Map of related opportunities (documented, not imagined)
- Capability development plan (what skills/assets will be built)
- Market learning objectives (what uncertainties will be resolved)

### Scoring Rubric

#### Score 9-10: High-Value Platform for Future Opportunities
**Required Evidence (need 3+ of these):**
- Clear path to 2-3 adjacent opportunities (documented with customer validation)
- Develops rare, valuable capabilities (technical, relationships, insights)
- Worst-case scenario still yields asymmetric learning value
- Creates strategic positioning regardless of product success
- Unlocks access to distribution/data/relationships valuable for multiple use cases

**Examples:**
- "Building this generates proprietary healthcare data valuable for 5+ adjacent products we've validated"
- "Establishes FDA regulatory clearance that takes competitors 18 months to obtain"
- "Proves out novel computer vision approach applicable to $10B market we've researched"
- "First product builds relationships with hospital procurement teams, enabling medical device sales later"

**What Doesn't Count:**
- "We'll learn a lot" (vague, every project teaches something)
- "Might open doors" (no specific opportunities identified)
- Adjacent opportunities are purely speculative (not validated)

---

#### Score 6-8: Moderate Strategic Value
**Required Evidence:**
- Develops generalizable skills or insights
- Opens 1 clear adjacent opportunity (with some validation)
- Reduces risk for future product decisions

**Examples:**
- "Learning this vertical enables us to build 1 follow-on product we've scoped"
- "Develops ML infrastructure reusable for other projects"

---

#### Score 3-5: Limited Transferable Value
**Required Evidence:**
- Learning is context-specific to this product
- Doesn't unlock other opportunities
- Could learn same lessons more cheaply

**Examples:**
- "We'll understand this narrow customer segment better"
- "Might help us if we ever build something similar"

---

#### Score 1-2: Dead-End with No Strategic Value
**Required Evidence:**
- No adjacent opportunities identified
- Doesn't build valuable capabilities
- High opportunity cost of not pursuing alternatives

---

### Verification Checklist for Option Value
- [ ] Name 2-3 specific adjacent opportunities - are they real or wishful thinking?
- [ ] What capabilities will be developed that are valuable outside this product?
- [ ] Could you learn the same lessons via customer interviews, desk research, or consulting instead of building?
- [ ] Are you using "option value" to rationalize a weak idea you know won't work?
- [ ] What's the cost of acquiring this learning? Is it worth it?

---

## Lever 6: External Validation
**Weight: 2x** | **Strength: MEDIUM** | **Category: Social Proof**

### What This Measures
What do credible, unbiased experts think? Are potential customers expressing unprompted willingness to pay?

### ⚠️ Critical: Weight Validator Quality

Not all validation is equal. Domain expert with no financial interest >> friend who's being supportive.

### Evidence Sources
- Customer discovery interview notes (with dates)
- Expert consultation summaries (with names/credentials)
- Investor feedback (with firm names)
- Advisor input (with backgrounds)

### Validator Quality Criteria

| Criterion | Strong | Weak |
|-----------|--------|------|
| **Domain Expertise** | 10+ years in specific industry | General business knowledge |
| **Incentive Alignment** | No financial stake, no reason to flatter | Friend/employee, wants to be supportive |
| **Track Record** | Pattern recognition from past successes | No relevant experience |
| **Specificity** | References concrete details, pushes back | Vague encouragement, cheerleading |

### Scoring Rubric

#### Score 9-10: Strong Validation from Credible Sources
**Required Evidence (need 2+ of these):**
- 3+ domain experts independently confirm opportunity (with written feedback)
- Potential customers expressing unprompted willingness to pay (with specific budget/timeline)
- Experienced founders/operators in space validate approach (with documented advice)
- Validators have no financial interest in outcome
- Validators have track record of successful pattern recognition

**Examples:**
- "3 CTOs from target companies (Series B+ fintech) said they'd pay $50k/year, 2 offered to pilot"
- "Former VP of Product at [competitor] reviewed approach, said 'this is what we should have built'"
- "Domain expert with 15 years experience said this is the #1 pain point, introduced me to 10 prospects"

**What Doesn't Count:**
- Friends/family saying "great idea!"
- Advisor with equity stake being encouraging
- General interest without commitment ("yeah, we might use that")

---

#### Score 6-8: Mixed Signals
**Required Evidence:**
- Some experts positive, others cautious
- Customers interested but with conditions
- Validators have some conflicts of interest

**Examples:**
- "2 experts like it, 1 pointed out major concern we're addressing"
- "Customers interested if we add feature X"

---

#### Score 3-5: Limited or Low-Quality Validation
**Required Evidence:**
- Feedback mostly from non-experts
- Polite interest but no commitment
- Validators telling you what you want to hear

---

#### Score 1-2: Negative Validation or Red Flags
**Required Evidence:**
- Experts identify fundamental flaws
- Customers uninterested despite outreach
- Experienced operators warn against pursuing

---

### Verification Checklist for External Validation
- [ ] List validators with credibility score (expertise, incentives, track record)
- [ ] For each validator: What specific feedback did they give? (Not general sentiment)
- [ ] Have you sought out skeptical validators who would benefit from being wrong?
- [ ] Are you dismissing negative feedback as "they don't get it"?
- [ ] Would any validator invest their own money/time based on their feedback?

---

## Lever 7: Regulatory/Legal Ease
**Weight: 2x** | **Strength: MEDIUM** | **Category: Execution Risk**

### What This Measures
How much friction exists in the regulatory environment? Will compliance create massive delays or costs?

### Evidence Sources
- Legal counsel assessment (from specialized attorney, not general)
- Regulatory requirement checklist (specific to jurisdiction)
- Compliance cost estimate (from attorney or compliance consultant)
- Precedent case analysis (similar products' regulatory journey)

### Scoring Rubric

#### Score 9-10: Clear Regulatory Path, Minimal Friction
**Required Evidence:**
- No licenses or permits required (confirmed by attorney)
- Clear precedent from similar products operating successfully
- Legal review confirms low-risk profile
- Standard terms of service sufficient

**Examples:**
- "B2B SaaS analytics tool, no data regulations apply (attorney confirmed)"
- "Consumer marketplace, established legal frameworks, 100+ similar companies operating"

---

#### Score 6-8: Moderate Requirements, Manageable
**Required Evidence:**
- Standard licenses/permits with clear process
- 6-12 month timeline for approvals (verified by attorney)
- Compliance costs <20% of initial budget
- Precedent from competitors navigating successfully

**Examples:**
- "Food delivery requires business licenses and insurance, 3-month process, $15k cost"
- "Financial services requires state money transmitter licenses, 9-month timeline, precedent from 20+ companies"

---

#### Score 3-5: Significant Regulatory Burden
**Required Evidence:**
- Complex licensing with 12+ month timeline
- High compliance costs (>50% of budget)
- Regulatory uncertainty in category
- Requires specialized legal expertise

**Examples:**
- "Medical device requires FDA clearance, 18-24 month process, $500k cost"
- "Crypto product, unclear regulatory framework, SEC enforcement risk"

---

#### Score 1-2: Prohibitive Regulatory Barriers
**Required Evidence:**
- No clear path to compliance
- Multi-year approval processes
- Regulatory framework in flux
- Precedent of similar products being shut down

**Examples:**
- "Online pharmacy, requires 50-state licensing, unclear if business model is legal"
- "Drone delivery in urban area, FAA approval unclear, similar companies grounded"

---

### Verification Checklist for Regulatory Ease
- [ ] Have you consulted with specialized attorney (not just general counsel)?
- [ ] What specific regulations apply? (List them with citations)
- [ ] What's the timeline and cost for each regulatory milestone?
- [ ] What's the enforcement pattern in this jurisdiction? (Lax, moderate, aggressive?)
- [ ] Is the regulatory landscape stable or changing?

---

## Lever 8: Pipeline Alternatives
**Weight: 2x** | **Strength: MEDIUM** | **Category: Opportunity Cost**

### What This Measures
What else could you be working on? Is this your best option or are you settling?

### Evidence Sources
- Documented idea backlog (with initial scoring)
- Comparative analysis of top 3 alternatives
- Resource availability assessment

### Scoring Rubric

#### Score 9-10: Clearly the Best Option
**Required Evidence:**
- Scores higher than alternatives on multiple key levers (documented)
- Alternative ideas have been evaluated with same rigor (scored)
- No regrets about pausing other opportunities
- Team aligned that this is highest-impact use of time

**Examples:**
- "Scored 3 alternatives: Idea A=52, Idea B=48, this idea=78"
- "Compared to alternatives: stronger market timing, better distribution, similar moat"

---

#### Score 6-8: Competitive with Other Options
**Required Evidence:**
- Similar scoring to 1-2 alternative ideas
- Some advantages over alternatives, some disadvantages
- Could justify pursuing this or an alternative

**Examples:**
- "This idea: strong distribution but uncertain market, Alternative: weak distribution but proven market"

---

#### Score 3-5: Weaker Than Other Opportunities
**Required Evidence:**
- Alternative ideas score higher on key metrics
- Pursuing this means passing on better options
- Choosing this primarily due to recency bias or progress made

---

#### Score 1-2: Clearly Inferior to Alternatives
**Required Evidence:**
- Multiple better options available (scored higher)
- High opportunity cost
- Only advantage is being further along (sunk cost)

---

### Verification Checklist for Pipeline Alternatives
- [ ] Have you listed top 3 alternative ideas?
- [ ] Have you scored alternatives using this same framework?
- [ ] What would have to be true for an alternative to be better?
- [ ] Are you pursuing this because it's best, or because it's "ready"?
- [ ] What's the opportunity cost of not pursuing your second-best option?

---

## Lever 9: Sunk Cost Bias (PENALTY LEVER)
**Weight: -1x** | **Strength: LOW** | **Category: Cognitive Bias**

### ⚠️ CRITICAL: This is a Penalty Score

This is the ONLY reverse-scored lever. High scores REDUCE your total, serving as a warning flag.

### What This Measures
Are you continuing because of past investment rather than future potential? This is the most common reason people pursue bad ideas.

### Evidence Sources
- Decision rationale documentation
- Investment log (time, money spent)
- Counterfactual analysis ("Would I start this today?")

### Scoring Rubric

#### Score 9-10: Decision Heavily Influenced by Past Investment (SEVERE PENALTY)
**Warning Signs (3+ = score 9-10):**
- Primary argument for continuing is "we've already spent $X"
- Would NOT start this project if starting fresh today
- Repeatedly referencing past investment in decision rationale
- Team/stakeholders pressuring to not "waste" prior work
- Cannot articulate forward-looking value independent of sunk costs
- Defensive when questioned about abandoning prior work

**Common Phrases That Signal High Score:**
- "We've already invested 6 months..."
- "Can't let that $50k go to waste..."
- "We're so close, just need to finish..."
- "The team will be demoralized if we stop..."

**Examples:**
- "We've spent $100k on development, can't stop now" (even though market validation is weak)
- "Built prototype, would feel like failure to pivot" (even though customer feedback is negative)

---

#### Score 6-8: Moderate Sunk Cost Influence
**Warning Signs:**
- Past investment mentioned but not primary driver
- Some emotional attachment to prior work
- Difficulty imagining abandoning investment

---

#### Score 3-5: Minimal Sunk Cost Influence
**Evidence:**
- Aware of past investment but willing to walk away
- Decision rationale focused on forward-looking factors
- Can articulate value independent of sunk costs

---

#### Score 1-2: No Sunk Cost Bias Detected
**Evidence:**
- Would make same decision if starting fresh today
- Past investment not mentioned in decision rationale
- Clear separation between past and future value

---

### The Sunk Cost Test

**Ask yourself:**
1. "If I had $0 and 0 hours invested, would I start this today knowing what I know?"
2. "Am I continuing because the future is promising, or because the past is expensive?"
3. "What are my forward-looking reasons to proceed that don't reference past investment?"

If you struggle to answer #3, your sunk cost score is likely 7+.

### Verification Checklist for Sunk Cost Bias
- [ ] Conduct fresh-start counterfactual: Decide as if no prior investment exists
- [ ] List forward-looking reasons to proceed (without mentioning past investment)
- [ ] Ask: "If competitor offered this capability for free tomorrow, would I still build it?"
- [ ] Separate emotional attachment from strategic value
- [ ] Calculate: Is FUTURE investment justified by FUTURE returns alone?

---

## Decision Output Format

After scoring all levers, generate a structured recommendation:

### 1. Calculate Total Score
```
Total = (Market_Window × 3) + (Strategic_Moat × 3) + (Distribution_Edge × 3) + 
        (Conviction × 2) + (Option_Value × 2) + (External_Validation × 2) + 
        (Regulatory_Ease × 2) + (Pipeline_Alternatives × 2) + 
        (Sunk_Cost_Bias × -1)

Maximum Possible: 170 points
```

### 2. Decision Recommendation

**Format:**
```
DECISION: [GO | CAUTIOUS_GO | NO_GO]
CONFIDENCE: [HIGH | MEDIUM | LOW]
TOTAL SCORE: [X/170]

KEY STRENGTHS:
- [Lever name]: [Score] - [Specific evidence]
- [Lever name]: [Score] - [Specific evidence]

KEY WEAKNESSES:
- [Lever name]: [Score] - [Specific evidence]
- [Lever name]: [Score] - [Specific evidence]

CRITICAL ASSUMPTIONS:
1. [Assumption that if wrong, would invalidate decision]
2. [Assumption that if wrong, would invalidate decision]

RED FLAGS:
- [Unresolved concern with potential impact]
- [Unresolved concern with potential impact]

NEXT STEPS:
1. [Specific action with timeline]
2. [Specific action with timeline]

DECISION CRITERIA FOR NEXT EVALUATION:
- [Metric/milestone that would trigger re-evaluation]
- [Metric/milestone that would trigger re-evaluation]
```

### 3. Sensitivity Analysis

Identify which lever changes would flip your decision:

**Format:**
```
MOST IMPACTFUL LEVER: [Lever name]
- Current score: X
- If score were Y, decision would change to [GO/NO_GO]

DECISION FLIP SCENARIOS:
- If Market_Window dropped from 8 to 5, decision becomes NO_GO
- If Distribution_Edge improved from 4 to 7, decision becomes GO
```

### 4. Dissenting View (Required)

**Format:**
```
STEEL-MAN ARGUMENT AGAINST THIS RECOMMENDATION:

[Write the strongest possible case for the opposite decision. 
If recommending GO, argue for NO-GO. If recommending NO-GO, argue for GO.
Use specific evidence and address the weaknesses in your recommendation.
This should be a genuinely compelling counter-argument, not a strawman.]

Example:
"While the market timing appears strong (score 8), this could be FOMO rather than 
genuine opportunity. The lack of distribution (score 4) means even with perfect 
timing, we may not be able to capitalize. Historical precedent shows that timing 
without distribution leads to watching competitors win the market you identified. 
The high conviction (score 9) may be founder overconfidence rather than insight."
```

---

## AI Agent Execution Guidelines

### When Acting as Evaluator

**Core Principles:**
1. **Prioritize evidence over narrative** - Require concrete data for all scores
2. **Be skeptical of founder optimism** - Apply scoring rubric strictly
3. **Call out missing evidence** - Don't fill gaps with assumptions
4. **Weight source credibility** - Domain expert > friend/advisor
5. **Check internal consistency** - Do scores make sense together?
6. **Generate adversarial view** - Always challenge the recommendation

**Common Failure Modes to Watch For:**

| Pattern | What It Looks Like | Intervention |
|---------|-------------------|--------------|
| **Timing FOMO** | "Market window is closing!" but no specific catalyst | Challenge: "What external event creates urgency?" |
| **Fake Moat** | "Unique approach" claimed as defensible advantage | Challenge: "What prevents competitor from copying in 6 months?" |
| **Vanity Metrics** | Social media followers counted as distribution | Challenge: "Show me engagement rate and conversion data" |
| **Conviction ≠ Evidence** | "I really believe this" treated as high score | Challenge: "What have you sacrificed to pursue this?" |
| **Vague Option Value** | "We'll learn a lot" without specifics | Challenge: "Name 2 adjacent opportunities this unlocks" |
| **Sunk Cost Rationalization** | "Already invested $X" reframed as "strategic" | Flag: "Would you start this today with $0 invested?" |

### Intervention Triggers

**When to push back hard:**

- **If conviction_level > 7 but external_validation < 4**: Flag disconnect, recommend validation before proceeding
- **If all 3 high-weight levers < 6**: Recommend immediate pivot regardless of other scores
- **If sunk_cost_bias > 7**: Require fresh-start counterfactual analysis before accepting any other reasoning
- **If total_score in 40-69 range but founder wants "strong go"**: Identify exactly which levers need improvement and by how much
- **If regulatory_ease < 4 and market_window > 8**: Flag regulatory risk as potential showstopper that negates timing advantage

### Evidence Quality Requirements

Before accepting any score, verify:

- [ ] **Specificity**: Evidence includes numbers, dates, names (not vague generalities)
- [ ] **Recency**: Data from last 90 days for fast-moving levers (market, validation)
- [ ] **Source credibility**: Can trace back to original source, not hearsay
- [ ] **Falsifiability**: Evidence could potentially be proven wrong
- [ ] **Independence**: Multiple evidence sources that don't reference each other

### Confidence Calibration

Assign confidence levels to final recommendation:

- **HIGH confidence**: 8+ evidence points per high-weight lever, validators with strong track records, no major contradictions
- **MEDIUM confidence**: 4-7 evidence points, some validation gaps, minor contradictions that can be explained
- **LOW confidence**: <4 evidence points, poor quality evidence, significant contradictions, founder defensive about gaps

---

## Meta-Framework Guidance

### What This Framework Is

- **A structured thinking tool** to force evidence-based decisions
- **A bias detector** especially for sunk cost fallacy
- **A communication framework** to align teams on criteria
- **A learning system** to improve decision-making over time

### What This Framework Is Not

- **Not a formula** that guarantees success if you hit 70 points
- **Not a substitute for judgment** - edge cases require interpretation
- **Not comprehensive** - it doesn't capture everything that matters
- **Not stable over time** - revisit scores as evidence changes

### When to Override the Framework

The framework can be wrong. Override if:

1. **Black swan evidence emerges** - Something fundamental changes that the framework doesn't capture
2. **Extreme values on single lever** - Sometimes one 10/10 lever outweighs everything else
3. **Qualitative factors not captured** - Team dynamics, personal circumstances, strategic fit
4. **Framework gaming detected** - Scores being inflated to hit thresholds

**But**: If overriding, explicitly document why and what the framework missed.

### Iteration and Learning

After each decision:

1. **Document prediction**: What score did this idea get?
2. **Set review date**: When will we know if decision was correct?
3. **Track outcomes**: Did the high-scoring levers actually matter?
4. **Calibrate**: Were we too harsh/lenient on certain levers?
5. **Update rubrics**: Refine scoring criteria based on learnings

---

## Quick Reference: Decision Tree

```
Start → Gather evidence for all 9 levers
  ↓
Score each lever (1-10) with documented reasoning
  ↓
Calculate weighted total (max 170)
  ↓
Total ≥ 70? → STRONG GO (if 2+ high-weight levers score 7+)
  ↓
Total 40-69? → CAUTIOUS PROCEED (if 1+ high-weight lever scores 7+)
  ↓
Total < 40? → STRONG NO-GO
  ↓
Check: Sunk cost bias > 7? → Re-evaluate with fresh-start mindset
  ↓
Generate sensitivity analysis
  ↓
Write dissenting view (steel-man)
  ↓
Make decision with documented reasoning
```

---

## Example Evaluation (Abbreviated)

**Product Idea**: AI-powered code review tool for enterprise teams

**Scores**:
- Market Window: 7 (AI coding tools growing fast, but no specific catalyst) × 3 = 21
- Strategic Moat: 5 (Using GPT-4 API, no unique IP) × 3 = 15
- Distribution Edge: 8 (15k developer newsletter, 22% open rate) × 3 = 24
- Conviction: 9 (Quit job, working full-time for 3 months) × 2 = 18
- Option Value: 6 (Opens door to AI dev tools generally) × 2 = 12
- External Validation: 7 (3 CTOs interested, 1 committed to pilot) × 2 = 14
- Regulatory Ease: 10 (No regulatory concerns) × 2 = 20
- Pipeline Alternatives: 6 (Have 2 other ideas, this scores highest) × 2 = 12
- Sunk Cost Bias: 4 (Some attachment, but would start fresh) × -1 = -4

**Total: 132/170**

**Recommendation**: STRONG GO
- High conviction + strong distribution overcomes weak moat
- Proceed but with awareness that defensibility is key risk
- Set milestone: If no paying customers in 8 weeks, re-evaluate

**Dissenting View**: "High score driven by distribution and conviction, but weak moat (score 5) in competitive AI space is concerning. Large players (GitHub Copilot, Cursor) have superior resources. Distribution advantage may not matter if product is feature, not platform. Consider: is this business or feature?"

---

## End of Framework

**Version**: 1.0  
**Last Updated**: January 2026  
**Recommended Review Cycle**: Re-score every 4-8 weeks as new evidence emerges

**Questions or Issues**: This framework is designed to evolve. If you encounter edge cases or find rubrics unclear, document them for future refinement.