# Presentation Script — Sounada Retail Intelligence Dashboard

**Total time: ~8 minutes**

---

## Slide 1: Title & Identity (30 sec)

> "Hi, my name is [YOUR NAME]. I'm presenting my Communicating with Data capstone for Quantic MSBA."
>
> [Hold up government-issued ID to camera]
>
> "Today I'll walk you through a retail intelligence dashboard I built for Sounada Home Concept, an AKEMI home textile retailer operating five stores in Vientiane, Laos."

---

## Slide 2: Business Case (45 sec)

> "The stakeholder is Eric Wong, owner of Sounada. His core challenge: how to optimise inventory, pricing, and store strategy to grow profitability while reducing excess stock and shrinkage."
>
> "He needs answers to four questions:
> 1. Which stores are performing best and where are we losing margin?
> 2. What does our payment mix look like and how does it affect cash flow?
> 3. Which products drive the most profit — and which are tying up cash?
> 4. Where are stock variances hurting us most?"
>
> "I chose the Analytics App path using Streamlit so Eric can explore the data interactively, not just look at static reports."

---

## Slide 3: Overview Page — Demo (90 sec)

> [Switch to live Streamlit app — Overview page]

> "The Overview page shows four headline KPIs. Net sales for the period, total retail value of current inventory at 16.9 billion LAK, a weighted margin of 64.6% — which is healthy, above our 60% green threshold — and inventory days on hand at approximately 480 days."
>
> "Right away, two stories jump out. First, Expo is the top-performing store with 1.2 billion LAK in net sales. Second, we have significant items in stock shortage — these are lost sales waiting to happen — and other items overstocked, which means cash is sitting on shelves instead of working for the business."

---

## Slide 4: Store Performance — Demo (90 sec)

> [Navigate to Store Performance page]

> "Looking at the five stores side by side, Expo leads in net sales. But discount rates vary — some stores are discounting heavily to move product, which erodes margin."
>
> "The sales-per-signup chart reveals something interesting: Parkson has the most customer signups but the lowest sales per signup. That's a conversion opportunity — we're bringing people in but not turning them into buyers. This is exactly the kind of actionable insight a non-technical stakeholder can act on."

---

## Slide 5: Payment Analysis — Demo (60 sec)

> [Navigate to Payment Analysis page]

> "Our payment mix tells a cash flow story. Bank transfers — in Laos we call this ໂອນຈ່າຍ — account for 61% of transactions. Cash is about 31%."
>
> "The key finding: bank transfers have the lowest average transaction value. WeChat and Alipay have the highest. That tells us our Chinese tourist customers spend more per visit. Eric could promote WeChat/Alipay for high-ticket purchases to increase average order value."

---

## Slide 6: Inventory Intelligence — Demo (60 sec)

> [Navigate to Inventory Intelligence page]

> "On the product side, the Colourlush Flannel Blanket line has the highest margins at 77%. But when we look at absolute profit potential, the Tencel Ardent and Lofty Microfil lines dominate — these are the cash cows."
>
> "The insight for Eric: prioritise these products for promotions and make sure they are never out of stock. A single day of stock-out on the Tencel Ardent King QuiltCover Set means losing millions of LAK in potential profit."

---

## Slide 7: Stock Alerts — Demo (60 sec)

> [Navigate to Stock Alerts page]

> "This is where shrinkage becomes visible. Over 60 items are in stock shortage — the physical count is less than what the system expects. The Ultra Absorbent Air-Loop Cotton towels show a gap of 17 units. That's a 2 million LAK cost difference, and we don't know if it's theft, damage, or data entry error."
>
> "The 'Profit at Risk' tab highlights the worst offenders — high-margin items where a stock-out directly costs us profit. These need immediate restocking."

---

## Slide 8: Chat Assistant — Demo (45 sec)

> [Navigate to Chat Assistant page]

> "Finally, I added a natural-language chat assistant powered by Claude. The idea: not every store manager wants to read charts. They want to ask 'which products should I restock?' and get a straight answer."
>
> [Type a sample question, e.g. "Which items should we restock urgently?"]
>
> "The assistant has access to all the data and responds in plain language with LAK and USD amounts. This lowers the barrier for non-technical users."

---

## Slide 9: Wrap-Up (30 sec)

> "To summarise: Sounada has a healthy 64.6% margin, but 480 inventory days means too much cash is locked in stock. The biggest levers are: reduce overstock, restock high-profit items that are short, and focus promotional energy on the Tencel and Lofty lines."
>
> "The dashboard gives Eric an interactive, always-current way to monitor these KPIs and act on them. Thank you."

---

## Timing Summary

| Section | Duration |
|---------|----------|
| Title & Identity | 0:30 |
| Business Case | 0:45 |
| Overview Demo | 1:30 |
| Store Performance Demo | 1:30 |
| Payment Analysis Demo | 1:00 |
| Inventory Intelligence Demo | 1:00 |
| Stock Alerts Demo | 1:00 |
| Chat Assistant Demo | 0:45 |
| Wrap-Up | 0:30 |
| **Total** | **~8:30** |
