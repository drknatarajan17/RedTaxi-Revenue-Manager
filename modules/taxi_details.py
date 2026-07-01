import streamlit as st
import pandas as pd
import os


def taxi_details():

    st.title("🚖 Taxi Details")

    st.subheader("Vehicle Information")

    taxi_number = st.text_input(
        "Taxi Number",
        "TS09AB1234"
    )

    vehicle_model = st.text_input(
        "Vehicle Model",
        "Maruti Dzire Tour S"
    )

    vehicle_brand = st.text_input(
        "Vehicle Brand",
        "Maruti Suzuki"
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        [
            "Petrol",
            "Diesel",
            "CNG",
            "Electric"
        ]
    )

    registration_date = st.date_input(
        "Registration Date"
    )

    purchase_cost = st.number_input(
        "Purchase Cost (₹)",
        value=900000
    )

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        value=700000
    )

    monthly_emi = st.number_input(
        "Monthly EMI (₹)",
        value=18000
    )

    insurance_expiry = st.date_input(
        "Insurance Expiry"
    )

    permit_expiry = st.date_input(
        "Permit Expiry"
    )

    fitness_expiry = st.date_input(
        "Fitness Certificate Expiry"
    )

    pollution_expiry = st.date_input(
        "Pollution Certificate Expiry"
    )

    odometer = st.number_input(
        "Current Odometer (km)",
        value=25000
    )

    if st.button("💾 Save Taxi Details"):

        data = pd.DataFrame({

            "Taxi Number":[taxi_number],
            "Model":[vehicle_model],
            "Brand":[vehicle_brand],
            "Fuel":[fuel_type],
            "Registration":[registration_date],
            "Purchase Cost":[purchase_cost],
            "Loan":[loan_amount],
            "Monthly EMI":[monthly_emi],
            "Insurance":[insurance_expiry],
            "Permit":[permit_expiry],
            "Fitness":[fitness_expiry],
            "Pollution":[pollution_expiry],
            "Odometer":[odometer]

        })

        if not os.path.exists("data"):
            os.makedirs("data")

        data.to_csv(
            "data/taxi_details.csv",
            index=False
        )

        st.success("Taxi details saved successfully.")

    if os.path.exists("data/taxi_details.csv"):

        st.markdown("---")

        st.subheader("Saved Taxi Information")

        st.dataframe(
            pd.read_csv("data/taxi_details.csv"),
            use_container_width=True
        )
