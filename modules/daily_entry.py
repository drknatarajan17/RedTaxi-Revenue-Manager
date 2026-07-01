import streamlit as st
import pandas as pd
import os


def daily_entry():

    st.title("💰 Daily Revenue Entry")

    # ---------------------------------------
    # Check Business Settings
    # ---------------------------------------

    if not os.path.exists("data/business_settings.csv"):

        st.error("Please configure Business Settings first.")

        return

    settings = pd.read_csv("data/business_settings.csv")

    profile = settings.loc[0, "Profile"]

    driver_type = settings.loc[0, "Driver Type"]
    driver_value = settings.loc[0, "Driver Value"]

    agent_type = settings.loc[0, "Agent Type"]
    agent_value = settings.loc[0, "Agent Value"]

    fuel = settings.loc[0, "Fuel Cost"]
    emi = settings.loc[0, "EMI"]
    maintenance = settings.loc[0, "Maintenance"]
    insurance = settings.loc[0, "Insurance"]
    road_tax = settings.loc[0, "Road Tax"]
    misc = settings.loc[0, "Miscellaneous"]

    st.success(f"Business Profile : {profile}")

    st.markdown("---")

    # ---------------------------------------
    # Daily Entry
    # ---------------------------------------

    date = st.date_input("Business Date")

    taxi = st.text_input(
        "Taxi Number",
        "TS09AB1234"
    )

    driver = st.text_input(
        "Driver Name",
        "Ravi"
    )

    trips = st.number_input(
        "Trips",
        min_value=1,
        value=8
    )

    revenue = st.number_input(
        "Today's Revenue (₹)",
        min_value=0,
        value=1000
    )

    remarks = st.text_area(
        "Remarks",
        ""
    )

    st.markdown("---")

    if st.button("💾 Save Today's Business"):

        # -----------------------------
        # Driver Salary
        # -----------------------------

        if driver_type == "Fixed Amount":

            driver_salary = driver_value

        else:

            driver_salary = revenue * driver_value / 100

        # -----------------------------
        # Agent Commission
        # -----------------------------

        if agent_type == "Fixed Amount":

            agent_commission = agent_value

        else:

            agent_commission = revenue * agent_value / 100

        # -----------------------------
        # Owner Share
        # -----------------------------

        owner_share = revenue - driver_salary - agent_commission

        owner_expense = (

            fuel +
            emi +
            maintenance +
            insurance +
            road_tax +
            misc

        )

        profit = owner_share - owner_expense

        # -----------------------------
        # New Record
        # -----------------------------

        new_record = pd.DataFrame({

            "Date":[str(date)],

            "Taxi_Number":[taxi],

            "Driver_Name":[driver],

            "Trips":[trips],

            "Revenue":[revenue],

            "Driver_Salary":[driver_salary],

            "Agent_Commission":[agent_commission],

            "Owner_Share":[owner_share],

            "Fuel":[fuel],

            "EMI":[emi],

            "Maintenance":[maintenance],

            "Insurance":[insurance],

            "Road_Tax":[road_tax],

            "Miscellaneous":[misc],

            "Profit":[profit],

            "Remarks":[remarks]

        })

        filename = "data/business_register.csv"

        if os.path.exists(filename):

            history = pd.read_csv(filename)

            duplicate = history[
                (history["Date"] == str(date)) &
                (history["Taxi_Number"] == taxi)
            ]

            if len(duplicate) > 0:

                st.error(
                    "Business already entered for this Taxi and Date."
                )

                return

            history = pd.concat(
                [history, new_record],
                ignore_index=True
            )

        else:

            history = new_record

        history.to_csv(
            filename,
            index=False
        )

        st.success(
            "Today's Business Saved Successfully."
        )

        st.markdown("---")

        st.subheader("Today's Business Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Revenue",
            f"₹{revenue:,.0f}"
        )

        c2.metric(
            "Owner Share",
            f"₹{owner_share:,.0f}"
        )

        c3.metric(
            "Net Profit",
            f"₹{profit:,.0f}"
        )

        st.markdown("---")

        st.subheader("Revenue Distribution")

        flow = pd.DataFrame({

            "Stage":[

                "Customer Revenue",

                "Driver Salary",

                "Agent Commission",

                "Owner Share",

                "Fuel",

                "EMI",

                "Maintenance",

                "Insurance",

                "Road Tax",

                "Miscellaneous",

                "Final Profit"

            ],

            "Amount":[

                revenue,

                driver_salary,

                agent_commission,

                owner_share,

                fuel,

                emi,

                maintenance,

                insurance,

                road_tax,

                misc,

                profit

            ]

        })

        st.dataframe(
            flow,
            use_container_width=True
        )
