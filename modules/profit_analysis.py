import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt


def profit_analysis():

    st.title("📈 Profit Analysis Dashboard")

    if not os.path.exists("data/business_register.csv"):

        st.warning("No business records available.")

        return

    df = pd.read_csv("data/business_register.csv")

    if len(df) == 0:

        st.warning("Business register is empty.")

        return

    latest = df.iloc[-1]

    revenue = latest["Revenue"]
    profit = latest["Profit"]
    owner_share = latest["Owner_Share"]

    expense = (
        latest["Fuel"] +
        latest["EMI"] +
        latest["Maintenance"] +
        latest["Insurance"] +
        latest["Road_Tax"] +
        latest["Miscellaneous"]
    )

    trips = latest["Trips"]

    profit_margin = (profit / revenue) * 100

    revenue_trip = revenue / trips

    fuel_trip = latest["Fuel"] / trips

    st.subheader("Today's Business")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Revenue",
        f"₹{revenue:,.0f}"
    )

    c2.metric(
        "Owner Share",
        f"₹{owner_share:,.0f}"
    )

    c3.metric(
        "Expenses",
        f"₹{expense:,.0f}"
    )

    c4.metric(
        "Profit",
        f"₹{profit:,.0f}"
    )

    st.markdown("---")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Trips",
        int(trips)
    )

    c2.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )

    c3.metric(
        "Revenue / Trip",
        f"₹{revenue_trip:.0f}"
    )

    c4.metric(
        "Fuel / Trip",
        f"₹{fuel_trip:.0f}"
    )

    st.markdown("---")

    st.subheader("Revenue Trend")

    fig, ax = plt.subplots(figsize=(10,4))

    ax.plot(
        df["Revenue"],
        marker="o",
        linewidth=2
    )

    ax.set_xlabel("Business Day")

    ax.set_ylabel("Revenue (₹)")

    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Profit Trend")

    fig, ax = plt.subplots(figsize=(10,4))

    ax.plot(
        df["Profit"],
        marker="o",
        linewidth=2
    )

    ax.set_xlabel("Business Day")

    ax.set_ylabel("Profit (₹)")

    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Expense Distribution")

    expense_df = pd.DataFrame({

        "Expense":[
            "Fuel",
            "EMI",
            "Maintenance",
            "Insurance",
            "Road Tax",
            "Miscellaneous"
        ],

        "Amount":[
            latest["Fuel"],
            latest["EMI"],
            latest["Maintenance"],
            latest["Insurance"],
            latest["Road_Tax"],
            latest["Miscellaneous"]
        ]

    })

    fig, ax = plt.subplots(figsize=(7,7))

    ax.pie(

        expense_df["Amount"],

        labels=expense_df["Expense"],

        autopct="%1.1f%%"

    )

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Business Health")

    if profit_margin >= 20:

        st.success("🟢 Excellent Business Performance")

    elif profit_margin >= 10:

        st.info("🟡 Good Business Performance")

    else:

        st.error("🔴 Business Needs Improvement")

    st.markdown("---")

    st.subheader("Monthly Projection")

    monthly_profit = profit * 30

    yearly_profit = profit * 365

    c1,c2 = st.columns(2)

    c1.metric(
        "Expected Monthly Profit",
        f"₹{monthly_profit:,.0f}"
    )

    c2.metric(
        "Expected Yearly Profit",
        f"₹{yearly_profit:,.0f}"
    )

    st.markdown("---")

    st.subheader("Top Business Statistics")

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Highest Revenue",
        f"₹{df['Revenue'].max():,.0f}"
    )

    c2.metric(
        "Highest Profit",
        f"₹{df['Profit'].max():,.0f}"
    )

    c3.metric(
        "Average Profit",
        f"₹{df['Profit'].mean():,.0f}"
    )

    st.markdown("---")

    st.subheader("AI Business Advisor")

    if profit_margin < 10:

        st.error(
            "Increase revenue or reduce operating expenses."
        )

    elif latest["Fuel"] > owner_share * 0.40:

        st.warning(
            "Fuel cost is consuming a major portion of owner income."
        )

    elif profit_margin >= 20:

        st.success(
            "Business is performing well. Consider expanding your fleet."
        )

    else:

        st.info(
            "Business is stable. Continue monitoring daily performance."
        )
