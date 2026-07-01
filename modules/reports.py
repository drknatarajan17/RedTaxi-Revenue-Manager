import streamlit as st
import pandas as pd
import os


def reports():

    st.title("📑 Business Reports")

    if not os.path.exists("data/business_register.csv"):

        st.warning("No business records available.")

        return

    df = pd.read_csv("data/business_register.csv")

    if df.empty:

        st.warning("Business Register is Empty")

        return

    st.subheader("Business Register")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    # ===============================
    # SUMMARY
    # ===============================

    st.subheader("Business Summary")

    total_revenue = df["Revenue"].sum()

    total_profit = df["Profit"].sum()

    total_trips = df["Trips"].sum()

    avg_profit = df["Profit"].mean()

    working_days = len(df)

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "Revenue",
        f"₹{total_revenue:,.0f}"
    )

    c2.metric(
        "Profit",
        f"₹{total_profit:,.0f}"
    )

    c3.metric(
        "Trips",
        int(total_trips)
    )

    c4.metric(
        "Working Days",
        working_days
    )

    c5.metric(
        "Average Profit",
        f"₹{avg_profit:,.0f}"
    )

    st.markdown("---")

    # ===============================
    # FILTER REPORT
    # ===============================

    st.subheader("Filter Report")

    date_list = sorted(df["Date"].unique())

    selected_date = st.selectbox(

        "Select Date",

        ["All"] + list(date_list)

    )

    if selected_date != "All":

        filtered = df[
            df["Date"] == selected_date
        ]

    else:

        filtered = df

    st.dataframe(
        filtered,
        use_container_width=True
    )

    st.markdown("---")

    # ===============================
    # BEST PERFORMANCE
    # ===============================

    st.subheader("Performance Highlights")

    best = df.loc[df["Profit"].idxmax()]

    worst = df.loc[df["Profit"].idxmin()]

    c1,c2 = st.columns(2)

    with c1:

        st.success(

            f"""
Best Profit Day

📅 {best['Date']}

💰 Revenue : ₹{best['Revenue']}

🎉 Profit : ₹{best['Profit']}
"""

        )

    with c2:

        st.error(

            f"""
Lowest Profit Day

📅 {worst['Date']}

💰 Revenue : ₹{worst['Revenue']}

🎉 Profit : ₹{worst['Profit']}
"""

        )

    st.markdown("---")

    # ===============================
    # DOWNLOAD
    # ===============================

    st.subheader("Download Reports")

    csv = filtered.to_csv(index=False)

    st.download_button(

        "📥 Download CSV",

        data=csv,

        file_name="Business_Report.csv",

        mime="text/csv"

    )

    st.markdown("---")

    # ===============================
    # DAILY PROFIT STATEMENT
    # ===============================

    st.subheader("Daily Profit Statement")

    statement = pd.DataFrame({

        "Revenue":[total_revenue],

        "Total Profit":[total_profit],

        "Trips":[total_trips],

        "Working Days":[working_days],

        "Average Profit":[round(avg_profit,2)]

    })

    st.dataframe(
        statement,
        use_container_width=True
    )

    st.success(
        "Report generated successfully."
    )
