import streamlit as st

from modules.dashboard import dashboard
from modules.settings import business_settings
from modules.daily_entry import daily_entry
from modules.profit_analysis import profit_analysis
from modules.daily_register import daily_register
from modules.analytics import analytics
from modules.reports import reports
from modules.taxi_details import taxi_details
from modules.driver_details import driver_details
from modules.fuel_analysis import fuel_analysis

st.set_page_config(
    page_title="RedTaxi Revenue Manager",
    page_icon="🚖",
    layout="wide"
)

st.sidebar.title("🚖 RedTaxi Revenue Manager")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "⚙ Business Settings",
        "💰 Daily Revenue Entry",
        "📈 Profit Analysis",
        "📒 Daily Register",
        "📊 Analytics",
        "📑 Reports",
        "🚕 Taxi Details",
        "👨 Driver Details",
        "⛽ Fuel Analysis"
    ]
)

if menu == "🏠 Dashboard":
    dashboard()

elif menu == "⚙ Business Settings":
    business_settings()

elif menu == "💰 Daily Revenue Entry":
    daily_entry()

elif menu == "📈 Profit Analysis":
    profit_analysis()

elif menu == "📒 Daily Register":
    daily_register()

elif menu == "📊 Analytics":
    analytics()

elif menu == "📑 Reports":
    reports()

elif menu == "🚕 Taxi Details":
    taxi_details()

elif menu == "👨 Driver Details":
    driver_details()

elif menu == "⛽ Fuel Analysis":
    fuel_analysis()
