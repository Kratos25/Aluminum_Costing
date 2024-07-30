import streamlit as st
from weight_ranges import weight_ranges
from credentials import users

# Function to check if the username and password are correct
def check_credentials(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

# Main application
def main_app():

    # Sidebar for user inputs
    st.sidebar.header('Input Dimensions and Specifications')

    # Select brand
    brand = st.sidebar.selectbox('Select Brand', options=list(weight_ranges.keys()))

    # Select series based on selected brand
    series = st.sidebar.selectbox('Select Series', options=list(weight_ranges[brand].keys()))

    # Input other specifications
    length = st.sidebar.number_input('Length (L)', min_value=0.0, format="%.2f")
    height = st.sidebar.number_input('Height (H)', min_value=0.0, format="%.2f")
    num_glasses = st.sidebar.selectbox('Number of Glasses', options=[2, 3])
    num_tracks = st.sidebar.selectbox('Number of Tracks', options=[2, 3])
    gauge = st.sidebar.selectbox('Gauge', options=[18, 16])

    # Main section
    st.title('Aluminum Window Costing')

    # Second section: Weight Range Calculation
    with st.expander('Weight Range Calculation'):
        weight_key = f"{gauge}_{num_tracks}"
        if weight_key in weight_ranges[brand][series]:
            weight_range = weight_ranges[brand][series][weight_key]
        else:
            st.error("Invalid Gauge and Track combination.")
            st.stop()

        bottom_weight = length * weight_range['Bottom']
        top_side_weight = (length + 2 * height) * weight_range['Top/Side']
        handle_weight = 2 * height * weight_range['Handle']
        interlock_weight = 2 * height * weight_range['Interlock']
        top_bottom_weight = length * (2 if num_tracks == 2 else 3) * weight_range['Top/Bottom']

        total_weight = bottom_weight + top_side_weight + handle_weight + interlock_weight + top_bottom_weight

        st.write(f"**Bottom Weight:** {bottom_weight:.2f}")
        st.write(f"**Top/Side Weight:** {top_side_weight:.2f}")
        st.write(f"**Handle Weight:** {handle_weight:.2f}")
        st.write(f"**Interlock Weight:** {interlock_weight:.2f}")
        st.write(f"**Top/Bottom Weight:** {top_bottom_weight:.2f}")
        st.write(f"**Total Weight:** {total_weight:.2f}")

    # Third section: Costing
    with st.expander('Costing'):
        market_price = st.number_input('Current Market Price', min_value=0.0, format="%.2f")
        final_cost = total_weight * market_price

        st.write(f"**Final Cost:** {final_cost:.2f}")

    # Footer
    st.markdown("---")
    st.markdown("**Developed by:** Your Name")
    st.markdown("For more information, visit [your website](http://example.com)")

# Login page
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    main_app()
