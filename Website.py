import streamlit as st

# Custom CSS to shift the header to the top-left corner
st.markdown(
    """
    <style>
    .header {
        position: absolute;
        top: -60px;
        left: -200px;
        font-size: 40px;
        font-weight: bold;
        margin: 10px;
    }
    </style>
    <div class="header">Flight Dashboard</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .custom-image {
        position: absolute;
        top: -50px;
        left: -220px;
        width: 20px;
        height: 30px  
    }
    </style>
    <img class="custom-image" src="https://via.placeholder.com/300" alt="Custom Positioned Image">
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
.custom-header {
    position: absolute;       /* Use absolute positioning */
    top: -30px;               /* Distance from the top of the page */
    right: -40px;               /* Center horizontally */
    transform: translateX(-50%); /* Adjust for centering */
    font-size: 2em;          /* Font size */
    color: #4CAF50;          /* Text color */
    text-align: center;      /* Center align text */
}
</style>
""", unsafe_allow_html=True
)
# Add content below the header
st.markdown(
    """
    <footer style='
        background-color: #34495e;
        padding: 20px 0;
        color: #ecf0f1;
        text-align: center;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        border-top: 4px solid #2c3e50;
    '>
        <p style='margin: 0; font-size: 0.9em;'>
            <a href="#" style='color: #3498db; text-decoration: none;'>DJS S4DS</a> |
            <a href="#" style='color: #3498db; text-decoration: none;'>About Us</a> | 
            <a href="#" style='color: #3498db; text-decoration: none;'>Terms of Service</a>
        </p>
    </footer>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
.button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white; /* White text */
    padding: 15px 32px; /* Padding */
    text-align: center; /* Center text */
    text-decoration: none; /* No underline */
    display: inline-block; /* Inline-block */
    font-size: 16px; /* Font size */
    margin: 4px 2px; /* Margin */
    cursor: pointer; /* Pointer on hover */
    border-radius: 5px; /* Rounded corners */
}
</style>
""", unsafe_allow_html=True)


# Initialize session state for the selected page
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Flight Profile"  # Default page

# Sidebar header
st.sidebar.header("Navigation")

# Create buttons for navigation
if st.sidebar.button("Flight Profile"):
    st.session_state.selected_page = "Flight Profile"

if st.sidebar.button("Weather"):
    st.session_state.selected_page = "Weather"

if st.sidebar.button("Fuel Consumption"):
    st.session_state.selected_page = "Fuel Consumption"

if st.sidebar.button("ETA & Delay Analysis"):
    st.session_state.selected_page = "ETA & Delay Analysis"

if st.sidebar.button("Alert"):
    st.session_state.selected_page = "Alert"

# Display content based on the selected page
if st.session_state.selected_page == "Flight Profile":
    st.subheader("Welcome to the Home Page!")
    st.write("This is some initial content that will remain visible.")
elif st.session_state.selected_page == "Weather":
    st.subheader("Data Page")
    st.write("Here you can display your data.")
elif st.session_state.selected_page == "Fuel Consumption":
    st.subheader("About Page")
    st.write("Information about the app and its creators.")
elif st.session_state.selected_page == "ETA & Delay Analysis":
    st.subheader("About Page")
    st.write("Information about the app and its creators.")
elif st.session_state.selected_page == "Alert":
    st.subheader("About Page")
    st.write("Information about the app and its creators.")



# Optional: Display some text next to the sidebar toggle arrow
st.sidebar.write("Quick Info")  # Text displayed in the sidebar


