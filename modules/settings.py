import streamlit as st
import pandas as pd
import os


def business_settings():

    st.title("⚙ Business Settings")

    st.markdown(
        "Configure your default taxi business expenses. "
        "These settings will be used automatically during "
        "daily profit calculation."
    )

    st.markdown("---")

    # ----------------------------
    # Business Profile
    # ----------------------------

    profile = st.selectbox(

        "Business Profile",

        [

            "City Taxi",

            "Airport Taxi",

            "Outstation Taxi"

        ]

    )

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        driver_type = st.selectbox(

            "Driver Salary Type",

            [

                "Fixed Amount",

                "Percentage"

            ]

        )

        driver_value = st.number_input(

            "Driver Salary",

            value=300

        )

        agent_type = st.selectbox(

            "Taxi Agent Commission",

            [

                "Fixed Amount",

                "Percentage"

            ]

        )

        agent_value = st.number_input(

            "Agent Commission",

            value=200

        )

        fuel_cost = st.number_input(

            "Average Fuel Cost",

            value=180

        )

        daily_emi = st.number_input(

            "Daily EMI",

            value=100

        )

    with c2:

        maintenance = st.number_input(

            "Maintenance",

            value=40

        )

        insurance = st.number_input(

            "Insurance",

            value=20

        )

        road_tax = st.number_input(

            "Road Tax / Permit",

            value=15

        )

        miscellaneous = st.number_input(

            "Miscellaneous",

            value=25

        )

        daily_target = st.number_input(

            "Daily Revenue Target",

            value=1500

        )

    st.markdown("---")

    st.subheader("Sample Calculation")

    revenue = 1000

    if driver_type == "Fixed Amount":

        driver_salary = driver_value

    else:

        driver_salary = revenue * driver_value / 100

    if agent_type == "Fixed Amount":

        agent_commission = agent_value

    else:

        agent_commission = revenue * agent_value / 100

    owner_share = revenue - driver_salary - agent_commission

    owner_expense = (

        fuel_cost

        + daily_emi

        + maintenance

        + insurance

        + road_tax

        + miscellaneous

    )

    owner_profit = owner_share - owner_expense

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Owner Share",

        f"₹{owner_share:.0f}"

    )

    c2.metric(

        "Owner Expense",

        f"₹{owner_expense:.0f}"

    )

    c3.metric(

        "Expected Profit",

        f"₹{owner_profit:.0f}"

    )

    st.markdown("---")

    if st.button("💾 Save Business Settings"):

        settings = pd.DataFrame({

            "Profile":[profile],

            "Driver Type":[driver_type],

            "Driver Value":[driver_value],

            "Agent Type":[agent_type],

            "Agent Value":[agent_value],

            "Fuel Cost":[fuel_cost],

            "EMI":[daily_emi],

            "Maintenance":[maintenance],

            "Insurance":[insurance],

            "Road Tax":[road_tax],

            "Miscellaneous":[miscellaneous],

            "Daily Target":[daily_target]

        })

        if not os.path.exists("data"):

            os.makedirs("data")

        settings.to_csv(

            "data/business_settings.csv",

            index=False

        )

        st.success(

            "Business settings saved successfully."

        )
