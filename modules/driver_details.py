import streamlit as st
import pandas as pd
import os


def driver_details():

    st.title("👨 Driver Details")

    driver_name = st.text_input(
        "Driver Name",
        "Ravi"
    )

    phone = st.text_input(
        "Mobile Number"
    )

    license_number = st.text_input(
        "Driving License Number"
    )

    experience = st.slider(
        "Experience (Years)",
        0,
        30,
        5
    )

    salary = st.number_input(
        "Monthly Salary (₹)",
        value=18000
    )

    rating = st.slider(
        "Driver Rating",
        1.0,
        5.0,
        4.5
    )

    attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        95
    )

    joining_date = st.date_input(
        "Joining Date"
    )

    if st.button("💾 Save Driver"):

        driver = pd.DataFrame({

            "Driver":[driver_name],
            "Phone":[phone],
            "License":[license_number],
            "Experience":[experience],
            "Salary":[salary],
            "Rating":[rating],
            "Attendance":[attendance],
            "Joining Date":[joining_date]

        })

        driver.to_csv(
            "data/driver_details.csv",
            index=False
        )

        st.success("Driver details saved successfully.")

    if os.path.exists("data/driver_details.csv"):

        st.markdown("---")

        st.subheader("Saved Driver Information")

        st.dataframe(
            pd.read_csv("data/driver_details.csv"),
            use_container_width=True
        )
