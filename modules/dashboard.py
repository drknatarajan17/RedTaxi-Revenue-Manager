import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt


def dashboard():

    st.title("🚖 RedTaxi Revenue Manager")

    st.subheader("Business Dashboard")

    if not os.path.exists("data/business_register.csv"):

        st.info("No business records available.")

        return

    df = pd.read_csv("data/business_register.csv")

    if len(df) == 0:

        st.warning("Business register is empty.")

        return

    latest = df.iloc[-1]

    today_revenue = latest["Revenue"]

    today_profit = latest["Profit"]

    owner_share = latest["Owner_Share"]

    today_expense = (
        latest["Fuel"]
        + latest["EMI"]
        + latest["Maintenance"]
        + latest["Insurance"]
        + latest["Road_Tax"]
        + latest["Miscellaneous"]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Today's Revenue",
        f"₹{today_revenue:,.0f}"
    )

    c2.metric(
        "Owner Share",
        f"₹{owner_share:,.0f}"
    )

    c3.metric(
        "Today's Expense",
        f"₹{today_expense:,.0f}"
    )

    c4.metric(
        "Today's Profit",
        f"₹{today_profit:,.0f}"
    )

    st.markdown("---")

    total_revenue = df["Revenue"].sum()

    total_profit = df["Profit"].sum()

    total_trips = df["Trips"].sum()

    working_days = len(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Revenue",
        f"₹{total_revenue:,.0f}"
    )

    c2.metric(
        "Total Profit",
        f"₹{total_profit:,.0f}"
    )

    c3.metric(
        "Total Trips",
        int(total_trips)
    )

    c4.metric(
        "Working Days",
        working_days
    )

    st.markdown("---")

    st.subheader("Revenue Trend")

    fig, ax = plt.subplots(figsize=(10,4))

    ax.plot(
        df["Revenue"],
        marker="o",
        linewidth=2
    )

    ax.set_xlabel("Business Days")

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

    ax.set_xlabel("Business Days")

    ax.set_ylabel("Profit (₹)")

    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Business Health")

    profit_margin = (today_profit / today_revenue) * 100

    st.metric(
        "Today's Profit Margin",
        f"{profit_margin:.2f}%"
    )

    if profit_margin >= 20:

        st.success("🟢 Excellent Business Performance")

    elif profit_margin >= 10:

        st.info("🟡 Good Business Performance")

    else:

        st.error("🔴 Business Needs Improvement")

    st.markdown("---")

    st.subheader("Latest Business Entry")

    st.dataframe(
        latest.to_frame().T,
        use_container_width=True
    )
