import streamlit as st


def fuel_analysis():

    st.title("⛽ Fuel Analysis")

    distance = st.number_input(
        "Distance Travelled (km)",
        value=250.0
    )

    fuel_used = st.number_input(
        "Fuel Used (Litres)",
        value=20.0
    )

    fuel_price = st.number_input(
        "Fuel Price (₹/Litre)",
        value=110.0
    )

    if fuel_used == 0:
        st.warning("Fuel used cannot be zero.")
        return

    mileage = distance / fuel_used

    fuel_cost = fuel_used * fuel_price

    cost_per_km = fuel_cost / distance if distance > 0 else 0

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Mileage",
        f"{mileage:.2f} km/L"
    )

    c2.metric(
        "Fuel Cost",
        f"₹{fuel_cost:.0f}"
    )

    c3.metric(
        "Cost per km",
        f"₹{cost_per_km:.2f}"
    )

    st.markdown("---")

    if mileage >= 18:

        st.success("🟢 Excellent Fuel Efficiency")

    elif mileage >= 15:

        st.info("🟡 Good Fuel Efficiency")

    else:

        st.warning("🔴 Low Mileage - Vehicle service recommended")
