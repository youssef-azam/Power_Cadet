import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your App", page_icon=":rocket:", layout="wide")

# Define the Power BI dashboard URLs
daily_sales_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=03558a93-ea7b-47b7-ae02-be32bc09bd07&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"
overall_sales_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=035ca501-5ee6-40a6-bcd7-e07df21f67f2&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"

# HTML code for embedding Power BI dashboards
daily_sales_html_code = f'<iframe title="تقرير المبيعات كاديت - اليومي" width="1140" height="541.25" src="{daily_sales_dashboard_url}" frameborder="0" allowFullScreen="true"></iframe>'
overall_sales_html_code = f'<iframe title="تقرير المبيعات كاديت" width="1140" height="541.25" src="{overall_sales_dashboard_url}" frameborder="0" allowFullScreen="true"></iframe>'

# Use Streamlit to display the Power BI dashboards using HTML in two columns
col1, col2 = st.columns(2)
col1.markdown(daily_sales_html_code, unsafe_allow_html=True)
col2.markdown(overall_sales_html_code, unsafe_allow_html=True)

# Additional Streamlit app code can be added here

# Run the Streamlit app
if __name__ == "__main__":
    st.write('Hello in my report Powered by Eng: Youssef Azam 👨‍💻, for Manager Eng: Salem 🚀')
