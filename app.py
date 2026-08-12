
import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming the data file is in the same directory or a known path
DATA_FILE = 'hotel_bookings_data.csv'

@st.cache_data
def load_data():
    if DATA_FILE.endswith('.csv'):
        df = pd.read_csv(DATA_FILE)
    elif DATA_FILE.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(DATA_FILE)
    else:
        st.error("Unsupported file format. Please provide a CSV or Excel file.")
        return pd.DataFrame()
    return df

st.set_page_config(layout="wide")
st.title("🏨 Hotel Bookings Dashboard")

data = load_data()

if not data.empty:
    st.subheader("Raw Data Preview")
    st.write(data.head())

    st.subheader("Data Statistics")
    st.write(data.describe())

    st.markdown("--- ")
    st.subheader("Future Development Notes:")
    st.markdown("- **Demographics**: Analyze guest origins, age groups (if available).")
    st.markdown("- **Charts**: Implement bar charts (e.g., bookings by month, country), pie charts (e.g., market segment distribution).")
    st.markdown("- **Interactive 3D Plots**: Explore using Plotly for 3D visualizations, e.g., 3D scatter plots if suitable dimensions are available (e.g., price, stay duration, lead time).")
    st.markdown("- **Bubble Charts**: Visualize high to low numbers for key metrics like cancellation rates, average daily rate by segment.")
    st.markdown("- **KPIs**: Display key performance indicators such as average daily rate (ADR), occupancy rate, cancellation rate, total revenue.")
    st.markdown("- **Filter Cards**: Add Streamlit sidebar widgets (selectboxes, sliders, multiselects) for filtering data by date, hotel type, customer type, etc.")
    st.markdown("- **Listings/Tables**: Create interactive tables to display filtered booking details.")
    st.markdown("- **Business Insights & Recommendations**: Generate textual insights based on data analysis, highlighting trends and offering recommendations.")
else:
    st.warning("No data loaded or data is empty. Please check the data file.")
