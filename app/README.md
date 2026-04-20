# Sounada Home Concept — Retail Intelligence Dashboard

A Streamlit analytics dashboard for Sounada Home Concept, an AKEMI home textile retailer operating five stores in Vientiane, Laos.

## Business Case

Sounada Home Concept needs to optimise inventory, pricing, and store strategy to grow profitability while reducing excess stock and shrinkage. This dashboard answers:

1. Which stores perform best and where are we losing margin?
2. What is our payment mix and how does it affect cash flow?
3. Which products drive the most profit and which tie up cash?
4. Where are stock variances hurting us most?

## Dashboard Pages

| Page | What it covers |
|------|----------------|
| **Overview** | Top-line KPIs: net sales, retail value, weighted margin, inventory days |
| **Store Performance** | Sales KPIs, discount rates, and customer productivity across 5 stores |
| **Payment Analysis** | Payment method mix (Cash, Bank Transfer, Card, WeChat/Alipay) |
| **Inventory Intelligence** | Highest-margin and highest-profit products |
| **Stock Alerts** | Stock shortages, surplus items, and high-profit items at stock-out risk |
| **Chat Assistant** | Natural-language Q&A powered by Claude / GPT |

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data Source

CSV exports from a PostgreSQL database built from Loyverse POS data for Sounada Home Concept.

## Tech Stack

- Python 3.11+
- Streamlit
- Plotly
- Pandas
- Anthropic Claude API (optional, for chat assistant)
