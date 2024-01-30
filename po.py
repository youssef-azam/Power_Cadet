import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your App", page_icon=":rocket:", layout="wide")

# Define the Power BI dashboard URL
power_bi_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=035ca501-5ee6-40a6-bcd7-e07df21f67f2&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"

# HTML code for embedding Power BI dashboard
power_bi_html_code = f'<iframe title="تقرير المبيعات كاديت" width="1140" height="541.25" src="{power_bi_dashboard_url}" frameborder="0" allowFullScreen="true"></iframe>'

# Use Streamlit to display the Power BI dashboard using HTML
st.markdown(power_bi_html_code, unsafe_allow_html=True)

# Additional Streamlit app code can be added here

# Run the Streamlit app
if __name__ == "__main__":
    st.write('Hello in my report Powered by Eng:Youssef Azam , for Manger Eng:Salem')
