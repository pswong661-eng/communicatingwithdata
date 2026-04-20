"""
Sounada Home Concept — Retail Intelligence Dashboard
Streamlit analytics app for the Communicating with Data.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sounada Retail Intelligence",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Data loading ─────────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent / "data"


@st.cache_data
def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / name)


q1 = load_csv("q1.csv")  # Store sales KPIs
q2 = load_csv("q2.csv")  # Payment method breakdown
q3 = load_csv("q3.csv")  # Top 10 high-margin SKUs
q4 = load_csv("q4.csv")  # Top 10 high-value SKUs
q5 = load_csv("q5.csv")  # Stock surplus (over-counted)
q6 = load_csv("q6.csv")  # Stock shortages
q7 = load_csv("q7.csv")  # Inventory financial summary
q8 = load_csv("q8.csv")  # Inventory turnover
q9 = load_csv("q9.csv")  # Sales per customer signup
q10 = load_csv("q10.csv")  # High-profit stock shortage items

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.title("🏠 Sounada Retail Intelligence")
st.sidebar.caption("AKEMI Store Analytics — Vientiane, Laos")

EXCHANGE_RATE = 21_500


def lak_to_usd(lak: float) -> float:
    return lak / EXCHANGE_RATE


def fmt_lak(v: float) -> str:
    """Format as LAK with commas."""
    return f"LAK {v:,.0f}"


def fmt_usd(v: float) -> str:
    """Format as USD."""
    return f"USD {lak_to_usd(v):,.2f}"


def margin_color(margin: float) -> str:
    if margin >= 60:
        return "🟢"
    elif margin >= 50:
        return "🟡"
    return "🔴"


page = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Store Performance",
        "Payment Analysis",
        "Inventory Intelligence",
        "Stock Alerts",
        "Chat Assistant",
    ],
)

# ── Overview ─────────────────────────────────────────────────────────────────
if page == "Overview":
    st.title("Sounada Home Concept — Retail Dashboard")
    st.markdown(
        """
        **Stakeholder:** Eric Wong, Owner of Sounada Home Concept (AKEMI retail, Vientiane, Laos), Quantic MSBA School of Business and Technology

        **Decision needed:** How to optimise inventory, pricing, and store strategy
        to grow profitability while reducing excess stock and shrinkage.

        **Key questions this dashboard answers:**
        1. Which stores are performing best and where are we losing margin?
        2. What is our payment mix and how does it affect cash flow?
        3. Which products drive the most profit and which are tying up cash?
        4. Where are stock variances hurting us most?
        """
    )

    # ── Top-line KPIs ────────────────────────────────────────────────────
    total_net = q1["net_sales"].sum()
    total_retail = float(q7["total_retail_value"].iloc[0])
    total_profit = float(q7["total_potential_profit"].iloc[0])
    weighted_margin = float(q7["weighted_margin_percent"].iloc[0])
    inv_days = float(q8["inventory_days"].iloc[0])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Net Sales (Period)", fmt_lak(total_net), help=fmt_usd(total_net))
    col2.metric(
        "Total Retail Value", fmt_lak(total_retail), help=fmt_usd(total_retail)
    )
    col3.metric(
        "Weighted Margin",
        f"{weighted_margin:.1f}%",
        delta=f"{margin_color(weighted_margin)}",
    )
    col4.metric(
        "Inventory Days on Hand",
        f"{inv_days:.0f} days",
        help="How many days current stock will last at recent sales pace",
    )

    st.divider()

    # ── Quick insights ───────────────────────────────────────────────────
    st.subheader("Quick Insights")

    # Best / worst stores
    best = q1.sort_values("net_sales", ascending=False).iloc[0]
    worst = q1.sort_values("net_sales").iloc[0]

    col_a, col_b = st.columns(2)
    with col_a:
        st.info(
            f"**Top Store:** {best['store_name']} — {fmt_lak(best['net_sales'])} net sales "
            f"({fmt_usd(best['net_sales'])})"
        )
    with col_b:
        st.warning(
            f"**Lowest Store:** {worst['store_name']} — {fmt_lak(worst['net_sales'])} net sales "
            f"({fmt_usd(worst['net_sales'])})"
        )

    # Stock issues
    surplus_count = len(q5)
    shortage_count = len(q6)
    col_c, col_d = st.columns(2)
    with col_c:
        st.error(f"**{shortage_count} items** in stock shortage — lost sales risk")
    with col_d:
        st.warning(f"**{surplus_count} items** overstocked — cash tied up")

    # Payment
    top_payment = q2.sort_values("net_amount", ascending=False).iloc[0]
    st.info(
        f"**Primary payment method:** {top_payment['payment_type']} — "
        f"{top_payment['net_amount_share']*100:.1f}% of net revenue"
    )

# ── Store Performance ────────────────────────────────────────────────────────
elif page == "Store Performance":
    st.title("Store Performance")
    st.markdown("Comparing sales KPIs across the five Sounada locations.")

    # ── Sales overview table ─────────────────────────────────────────────
    df = q1.copy()
    df["net_sales_usd"] = df["net_sales"].apply(lak_to_usd)
    df["gross_sales_usd"] = df["gross_sales"].apply(lak_to_usd)

    display_cols = [
        "store_name",
        "gross_sales",
        "refunds",
        "discounts",
        "net_sales",
        "receipts",
        "average_sale",
        "customers_signed_up",
        "discounts_ratio",
    ]
    st.dataframe(
        df[display_cols].style.format(
            {
                "gross_sales": "{:,.0f}",
                "refunds": "{:,.0f}",
                "discounts": "{:,.0f}",
                "net_sales": "{:,.0f}",
                "average_sale": "{:,.0f}",
                "discounts_ratio": "{:.1%}",
            }
        ),
        use_container_width=True,
    )

    st.divider()

    # ── Charts ───────────────────────────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            df,
            x="store_name",
            y="net_sales",
            color="store_name",
            title="Net Sales by Store (LAK)",
            labels={"net_sales": "Net Sales (LAK)", "store_name": "Store"},
            text_auto=",.0f",
        )
        fig.update_layout(showlegend=False, yaxis_tickformat=",")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(
            df,
            x="store_name",
            y="discounts_ratio",
            color="store_name",
            title="Discount Rate by Store",
            labels={
                "discounts_ratio": "Discount Rate",
                "store_name": "Store",
            },
            text_auto=".1%",
        )
        fig.update_layout(showlegend=False, yaxis_tickformat=".0%")
        st.plotly_chart(fig, use_container_width=True)

    # ── Sales per customer ───────────────────────────────────────────────
    st.subheader("Sales Productivity per Customer Signup")
    fig = px.bar(
        q9,
        x="store_name",
        y="net_sales_per_signup",
        color="store_name",
        title="Net Sales per Customer Signup (LAK)",
        labels={
            "net_sales_per_signup": "LAK per Signup",
            "store_name": "Store",
        },
        text_auto=",.0f",
    )
    fig.update_layout(showlegend=False, yaxis_tickformat=",")
    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Parkson has the most customer signups but the lowest sales per signup — "
        "potential opportunity to improve conversion or upselling."
    )

# ── Payment Analysis ─────────────────────────────────────────────────────────
elif page == "Payment Analysis":
    st.title("Payment Analysis")
    st.markdown("Understanding payment mix to optimise cash flow and reduce processing costs.")

    df = q2.copy()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(
            df,
            values="net_amount",
            names="payment_type",
            title="Revenue by Payment Method",
            hole=0.4,
        )
        fig.update_traces(textinfo="label+percent")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.pie(
            df,
            values="payment_transactions",
            names="payment_type",
            title="Transaction Count by Method",
            hole=0.4,
        )
        fig.update_traces(textinfo="label+percent")
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ── Detailed breakdown table ─────────────────────────────────────────
    st.subheader("Payment Method Detail")
    st.dataframe(
        df.style.format(
            {
                "payment_transactions": "{:,.0f}",
                "payments_amount": "{:,.0f}",
                "refund_transactions": "{:,.0f}",
                "refunds_amount": "{:,.0f}",
                "net_amount": "{:,.0f}",
                "txn_share": "{:.1%}",
                "net_amount_share": "{:.1%}",
                "avg_transaction_amount": "{:,.0f}",
            }
        ),
        use_container_width=True,
    )

    # ── Average transaction amount ───────────────────────────────────────
    st.subheader("Average Transaction Amount by Payment Type")
    fig = px.bar(
        df.sort_values("avg_transaction_amount", ascending=False),
        x="payment_type",
        y="avg_transaction_amount",
        color="payment_type",
        title="Average Transaction Value (LAK)",
        labels={
            "avg_transaction_amount": "Avg Amount (LAK)",
            "payment_type": "Payment Type",
        },
        text_auto=",.0f",
    )
    fig.update_layout(showlegend=False, yaxis_tickformat=",")
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Bank transfers (ໂອນຈ່າຍ)** account for 61% of transactions but the lowest "
        "average value. **WeChat/Alipay** has the highest average transaction — consider "
        "promoting it for high-ticket purchases."
    )

# ── Inventory Intelligence ───────────────────────────────────────────────────
elif page == "Inventory Intelligence":
    st.title("Inventory Intelligence")
    st.markdown("Which products drive profit, which tie up cash, and where our margin sits.")

    # ── Summary metrics ──────────────────────────────────────────────────
    total_profit = float(q7["total_potential_profit"].iloc[0])
    total_retail = float(q7["total_retail_value"].iloc[0])
    weighted_margin = float(q7["weighted_margin_percent"].iloc[0])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Potential Profit", fmt_lak(total_profit), help=fmt_usd(total_profit))
    col2.metric("Total Retail Value", fmt_lak(total_retail), help=fmt_usd(total_retail))
    col3.metric("Weighted Margin", f"{weighted_margin:.1f}%")

    st.divider()

    # ── Top 10 by margin ─────────────────────────────────────────────────
    st.subheader("Top 10 Highest-Margin Products")
    fig = px.bar(
        q3.head(10),
        x="margin",
        y="item",
        orientation="h",
        color="margin",
        title="Highest Margin Products (%)",
        labels={"margin": "Margin %", "item": "Product"},
        text="margin",
        color_continuous_scale="Greens",
    )
    fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # ── Top 10 by profit potential ───────────────────────────────────────
    st.subheader("Top 10 Highest-Profit-Potential Products")
    fig = px.bar(
        q4.head(10),
        x="potentialprofit",
        y="item",
        orientation="h",
        color="potentialprofit",
        title="Products with Highest Profit Potential (LAK)",
        labels={"potentialprofit": "Potential Profit (LAK)", "item": "Product"},
        text_auto=",.0f",
        color_continuous_scale="Blues",
    )
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        showlegend=False,
        xaxis_tickformat=",",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "The Tencel Ardent and Lofty Microfil lines dominate profit potential. "
        "Consider prioritising these for promotions and ensuring they are never out of stock."
    )

# ── Stock Alerts ─────────────────────────────────────────────────────────────
elif page == "Stock Alerts":
    st.title("Stock Alerts")
    st.markdown("Items where physical stock doesn't match system records — the biggest source of shrinkage risk.")

    tab1, tab2, tab3 = st.tabs(
        ["Stock Shortages", "Stock Surplus", "Profit at Risk"]
    )

    with tab1:
        st.subheader("Items in Stock Shortage (Counted < Expected)")
        st.warning(f"**{len(q6)} items** are short vs. expected stock.")

        fig = px.bar(
            q6.head(15),
            x="difference",
            y="item",
            orientation="h",
            color="difference",
            title="Largest Stock Shortages",
            labels={"difference": "Shortage (units)", "item": "Product"},
            color_continuous_scale="Reds",
        )
        fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(
            q6[
                ["sku", "item", "expectedstock", "counted", "difference", "costdifference"]
            ].style.format(
                {
                    "expectedstock": "{:.0f}",
                    "counted": "{:.0f}",
                    "difference": "{:+.0f}",
                    "costdifference": "{:,.0f}",
                }
            ),
            use_container_width=True,
        )

    with tab2:
        st.subheader("Overstocked Items (Counted > Expected)")
        st.info(f"**{len(q5)} items** have more stock than expected.")

        fig = px.bar(
            q5.head(15),
            x="difference",
            y="item",
            orientation="h",
            color="difference",
            title="Largest Stock Surpluses",
            labels={"difference": "Surplus (units)", "item": "Product"},
            color_continuous_scale="Greens",
        )
        fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(
            q5[
                ["sku", "item", "expectedstock", "counted", "difference", "costdifference"]
            ].style.format(
                {
                    "expectedstock": "{:.0f}",
                    "counted": "{:.0f}",
                    "difference": "{:+.0f}",
                    "costdifference": "{:,.0f}",
                }
            ),
            use_container_width=True,
        )

    with tab3:
        st.subheader("High-Profit Items at Risk of Stock-Out")
        st.error(
            "These items have negative stock difference AND high profit-per-unit — "
            "prioritise restocking immediately."
        )

        fig = px.bar(
            q10.head(10),
            x="profit_per_unit",
            y="item",
            orientation="h",
            color="profit_per_unit",
            title="Highest Profit-per-Unit Items with Shortages",
            labels={
                "profit_per_unit": "Profit per Unit (LAK)",
                "item": "Product",
            },
            text_auto=",.0f",
            color_continuous_scale="Oranges",
        )
        fig.update_layout(
            yaxis=dict(autorange="reversed"),
            showlegend=False,
            xaxis_tickformat=",",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(
            q10[
                [
                    "sku",
                    "item",
                    "expectedstock",
                    "counted",
                    "difference",
                    "profit_per_unit",
                ]
            ].style.format(
                {
                    "expectedstock": "{:.0f}",
                    "counted": "{:.0f}",
                    "difference": "{:+.0f}",
                    "profit_per_unit": "{:,.0f}",
                }
            ),
            use_container_width=True,
        )

# ── Chat Assistant ───────────────────────────────────────────────────────────
elif page == "Chat Assistant":
    st.title("💬 Data Chat Assistant")
    st.markdown(
        "Ask natural-language questions about the Sounada retail data. "
        "The assistant has access to all store, payment, inventory, and stock data."
    )

    # Build a plain-text data context for the LLM
    data_context = f"""
STORE SALES (LAK):
{q1.to_string(index=False)}

PAYMENT TYPES:
{q2.to_string(index=False)}

TOP HIGH-MARGIN PRODUCTS:
{q3.to_string(index=False)}

TOP PROFIT-POTENTIAL PRODUCTS:
{q4.to_string(index=False)}

STOCK SURPLUS (over-counted):
{q5.to_string(index=False)}

STOCK SHORTAGES:
{q6.to_string(index=False)}

INVENTORY SUMMARY:
{q7.to_string(index=False)}

INVENTORY DAYS: {q8.iloc[0]['inventory_days']:.0f} days

SALES PER CUSTOMER SIGNUP:
{q9.to_string(index=False)}

HIGH-PROFIT AT RISK OF STOCK-OUT:
{q10.to_string(index=False)}

Exchange rate: LAK 21,500 = USD 1
Margin health: green >=60%, amber 50-59%, red <50%
"""

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! I'm your Sounada retail data assistant. "
                    "Ask me anything about store performance, inventory, "
                    "payment mix, or stock issues. For example:\n\n"
                    "- Which store has the highest discount rate?\n"
                    "- What are the top 5 items we should restock urgently?\n"
                    "- How does our payment mix affect cash flow?"
                ),
            }
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask a question about your retail data..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Try Anthropic first, fall back to OpenAI
        response_text = None

        try:
            import anthropic

            client = anthropic.Anthropic()
            message = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system=(
                    "You are a retail business intelligence analyst for "
                    "Sounada Home Concept, an AKEMI bedding/towel retailer "
                    "in Vientiane, Laos. Answer questions using ONLY the data "
                    "provided. Always show LAK amounts with USD equivalents "
                    "(LAK 21,500 = USD 1). Be concise, actionable, and "
                    "business-focused. Use bullet points where helpful."
                    f"\n\nDATA:\n{data_context}"
                ),
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            )
            response_text = message.content[0].text
        except Exception:
            try:
                import openai

                client = openai.OpenAI()
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a retail business intelligence analyst for "
                                "Sounada Home Concept, an AKEMI bedding/towel retailer "
                                "in Vientiane, Laos. Answer questions using ONLY the data "
                                "provided. Always show LAK amounts with USD equivalents "
                                "(LAK 21,500 = USD 1). Be concise, actionable, and "
                                "business-focused. Use bullet points where helpful."
                                f"\n\nDATA:\n{data_context}"
                            ),
                        }
                    ]
                    + [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                )
                response_text = completion.choices[0].message.content
            except Exception:
                response_text = (
                    "No LLM API key configured. Set `ANTHROPIC_API_KEY` or "
                    "`OPENAI_API_KEY` as an environment variable, or use the "
                    "dashboard pages for pre-built insights."
                )

        with st.chat_message("assistant"):
            st.markdown(response_text)
        st.session_state.messages.append(
            {"role": "assistant", "content": response_text}
        )
