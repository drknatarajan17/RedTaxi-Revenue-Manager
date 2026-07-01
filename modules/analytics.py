import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt


def analytics():

    st.title("📊 Business Analytics")

    if not os.path.exists("data/business_register.csv"):

        st.warning("No business data available.")

        return

    df = pd.read_csv("data/business_register.csv")

    if len(df) == 0:

        st.warning("Business Register is Empty")

        return

    st.subheader("Overall Business Summary")

    total_revenue = df["Revenue"].sum()

    total_profit = df["Profit"].sum()

    total_trips = df["Trips"].sum()

    average_profit = df["Profit"].mean()

    c1,c2,c3,c4 = st.columns(4)

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
        "Average Profit",
        f"₹{average_profit:,.0f}"
    )

    st.markdown("---")

    st.subheader("Revenue Growth")

    growth = df["Revenue"].pct_change()*100

    fig, ax = plt.subplots(figsize=(10,4))

    ax.bar(
        range(len(growth)),
        growth.fillna(0)
    )

    ax.set_ylabel("Growth %")

    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Revenue vs Profit")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        df["Revenue"],
        marker="o",
        linewidth=2,
        label="Revenue"
    )

    ax.plot(
        df["Profit"],
        marker="o",
        linewidth=2,
        label="Profit"
    )

    ax.legend()

    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Profit Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(
        df["Profit"],
        bins=10
    )

    ax.set_xlabel("Profit")

    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Top Revenue Day")

    best = df.loc[df["Revenue"].idxmax()]

    st.success(

        f"""

📅 Date : {best['Date']}

💰 Revenue : ₹{best['Revenue']}

🎉 Profit : ₹{best['Profit']}

"""

    )

    st.markdown("---")

    st.subheader("Lowest Revenue Day")

    low = df.loc[df["Revenue"].idxmin()]

    st.error(

        f"""

📅 Date : {low['Date']}

💰 Revenue : ₹{low['Revenue']}

🎉 Profit : ₹{low['Profit']}

"""

    )

    st.markdown("---")

    st.subheader("Highest Profit Day")

    hp = df.loc[df["Profit"].idxmax()]

    st.success(

        f"""

📅 Date : {hp['Date']}

💰 Revenue : ₹{hp['Revenue']}

🎉 Profit : ₹{hp['Profit']}

"""

    )

    st.markdown("---")

    st.subheader("Lowest Profit Day")

    lp = df.loc[df["Profit"].idxmin()]

    st.error(

        f"""

📅 Date : {lp['Date']}

💰 Revenue : ₹{lp['Revenue']}

🎉 Profit : ₹{lp['Profit']}

"""

    )

    st.markdown("---")

    st.subheader("Business Score")

    score = (total_profit/total_revenue)*100

    st.metric(

        "Business Score",

        f"{score:.2f}%"

    )

    if score >= 20:

        st.success("🟢 Excellent Business")

    elif score >= 10:

        st.info("🟡 Good Business")

    else:

        st.error("🔴 Needs Improvement")

    st.markdown("---")

    st.subheader("🤖 AI Suggestions")

    if score >= 20:

        st.success(
            "Business is growing steadily."
        )

    if average_profit < 100:

        st.warning(
            "Average profit is low. Increase daily revenue."
        )

    if total_trips < len(df)*8:

        st.warning(
            "Average trips per day are low."
        )

    if df["Fuel"].mean() > 200:

        st.warning(
            "Fuel expenses are increasing."
        )

    if score < 10:

        st.error(
            "Review business expenses immediately."
        )
