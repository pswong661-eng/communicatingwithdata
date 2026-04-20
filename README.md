# Sounada Home Concept (Laos) — Retail Intelligence Dashboard

A Streamlit analytics dashboard for Sounada Home Concept, an AKEMI home textile retailer operating five stores in Vientiane, Laos. Built for the Quantic MSBA "Communicating with Data" capstone project.

## Business Case

**Stakeholder:** Eric Wong Poh Sang, Owner of Sounada Home Concept, Quantic MSBA School of Business and Technology

**Decision needed:** How to optimise inventory, pricing, and store strategy to grow profitability while reducing excess stock and shrinkage.

**Key questions this dashboard answers:**

1. Which stores are performing best and where are we losing margin?
2. What is our payment mix and how does it affect cash flow?
3. Which products drive the most profit and which are tying up cash?
4. Where are stock variances hurting us most?

## Dashboard Pages

| Page | What it covers |
|------|----------------|
| **Overview** | Top-line KPIs: net sales, retail value, weighted margin, inventory days on hand |
| **Store Performance** | Sales KPIs, discount rates, and customer productivity across 5 stores |
| **Payment Analysis** | Payment method mix — Cash, Bank Transfer, Card, WeChat/Alipay |
| **Inventory Intelligence** | Highest-margin and highest-profit-potential products |
| **Stock Alerts** | Stock shortages, surplus items, and high-profit items at stock-out risk |
| **Chat Assistant** | Natural-language Q&A powered by Anthropic Claude (with OpenAI fallback) |

## Key Insights

- **Weighted margin: 64.6%** — overall healthy, above the 60% green threshold
- **Inventory days on hand: ~480** — significant overstock, cash tied up in inventory
- **Primary payment method: Bank Transfer** — 61% of transactions
- **Top profit drivers:** Tencel Ardent and Lofty Microfil lines dominate profit potential
- **Stock shrinkage risk:** Multiple high-margin items in shortage — immediate restocking recommended

## Data Source

CSV exports from a PostgreSQL database built from Loyverse POS data for Sounada Home Concept. The underlying SQL queries cover 10 analytical areas: store KPIs, payment mix, product margins, inventory valuation, stock variances, turnover, and sales productivity.

## Tech Stack

- **Python 3.11+**
- **Streamlit** — web app framework
- **Plotly** — interactive charts
- **Pandas** — data wrangling
- **Anthropic Claude API** — chat assistant (optional)
- **OpenAI GPT API** — fallback LLM (optional)

## Setup

```bash
# Install dependencies
pip install -r app/requirements.txt

# Run the app
streamlit run app/app.py
```

The chat assistant requires one of these environment variables:

```bash
export ANTHROPIC_API_KEY="your-key-here"
# or
export OPENAI_API_KEY="your-key-here"
```

Without an API key, the dashboard pages still work fully — the chat assistant will show a fallback message.

## Currency & Conventions

- All amounts shown in LAK (Lao Kip) with USD equivalents
- Exchange rate: LAK 21,500 = USD 1
- Margin health: green ≥60%, amber 50–59%, red <50%

## Project Structure

```
├── README.md
├── LICENSE
└── app/
    ├── app.py                 # Main Streamlit application
    ├── requirements.txt       # Python dependencies
    └── data/
        ├── q1.csv             # Store sales KPIs
        ├── q2.csv             # Payment method breakdown
        ├── q3.csv             # Top 10 high-margin SKUs
        ├── q4.csv             # Top 10 high-value SKUs
        ├── q5.csv             # Stock surplus (over-counted)
        ├── q6.csv             # Stock shortages
        ├── q7.csv             # Inventory financial summary
        ├── q8.csv             # Inventory turnover
        ├── q9.csv             # Sales per customer signup
        └── q10.csv            # High-profit stock shortage items
```
