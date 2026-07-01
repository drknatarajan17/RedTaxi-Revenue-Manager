import streamlit as st
import pandas as pd
import os


def daily_register():

    st.title("📒 Daily Business Register")

    filename = "data/business_register.csv"

    if not os.path.exists(filename):
        st.warning("No business register found.")
        return

    df = pd.read_csv(filename)

    if df.empty:
        st.warning("Business Register is Empty.")
        return

    st.subheader("📋 Complete Business Register")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🔍 Search Records")

    taxi_list = ["All"] + sorted(df["Taxi_Number"].astype(str).unique().tolist())

    taxi = st.selectbox(
        "Select Taxi",
        taxi_list
    )

    if taxi != "All":
        filtered = df[df["Taxi_Number"] == taxi]
    else:
        filtered = df

    st.dataframe(
        filtered,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📊 Business Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Working Days",
        len(filtered)
    )

    c2.metric(
        "Total Revenue",
        f"₹{filtered['Revenue'].sum():,.0f}"
    )

    c3.metric(
        "Total Profit",
        f"₹{filtered['Profit'].sum():,.0f}"
    )

    c4.metric(
        "Total Trips",
        int(filtered["Trips"].sum())
    )

    st.markdown("---")

    st.subheader("🏆 Best Business Day")

    best = filtered.loc[filtered["Profit"].idxmax()]

    st.success(f"""
📅 Date : {best['Date']}

🚖 Taxi : {best['Taxi_Number']}

👨 Driver : {best['Driver_Name']}

💰 Revenue : ₹{best['Revenue']:,.0f}

🎉 Profit : ₹{best['Profit']:,.0f}
""")

    st.markdown("---")

    st.subheader("📉 Lowest Profit Day")

    worst = filtered.loc[filtered["Profit"].idxmin()]

    st.error(f"""
📅 Date : {worst['Date']}

🚖 Taxi : {worst['Taxi_Number']}

👨 Driver : {worst['Driver_Name']}

💰 Revenue : ₹{worst['Revenue']:,.0f}

🎉 Profit : ₹{worst['Profit']:,.0f}
""")

    st.markdown("---")

    st.subheader("📈 Daily Revenue")

    chart = filtered.set_index("Date")[["Revenue", "Profit"]]

    st.line_chart(chart)

    st.markdown("---")

    st.subheader("📥 Download Register")

    csv = filtered.to_csv(index=False)

    st.download_button(
        "Download CSV",
        csv,
        file_name="business_register.csv",
        mime="text/csv"
    )

    st.markdown("---")

    st.subheader("🗑 Delete Record")

    row = st.number_input(
        "Row Number",
        min_value=0,
        max_value=len(df)-1,
        step=1
    )

    if st.button("Delete Selected Record"):

        df = df.drop(index=row).reset_index(drop=True)

        df.to_csv(
            filename,
            index=False
        )

        st.success("Record deleted successfully.")

        st.rerun()
