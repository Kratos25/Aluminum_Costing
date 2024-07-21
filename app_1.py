import streamlit as st

# Updated dummy weight range data with Top/Bottom
weight_ranges = {
    '18_2': {'Bottom': 0.695, 'Top/Side': 0.547, 'Handle': 0.418, 'Interlock': 0.507, 'Top/Bottom': 0.418},
    '18_3': {'Bottom': 0.4, 'Top/Side': 0.6, 'Handle': 0.5, 'Interlock': 0.5, 'Top/Bottom': 0.4},
    '16_2': {'Bottom': 0.6, 'Top/Side': 0.8, 'Handle': 0.7, 'Interlock': 0.7, 'Top/Bottom': 0.6},
    '16_3': {'Bottom': 0.5, 'Top/Side': 0.7, 'Handle': 0.6, 'Interlock': 0.6, 'Top/Bottom': 0.5}
}   

# Sidebar for user inputs
st.sidebar.header('Input Dimensions and Specifications')
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
    if weight_key in weight_ranges:
        weight_range = weight_ranges[weight_key]
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
st.markdown("**Developed by:** Abhijeet Giri")
st.markdown("For more information, visit [your website](http://example.com)")
