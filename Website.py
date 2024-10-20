import streamlit as st
import streamlit.components.v1 as components
import time
from Main import get_cost


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css(r'C:\Users\omnku\Desktop\Data hack 24hrs\Website\styles.css')

# components.html(
#     """
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
#     """,
#     height=0,  # Set height to 0 as we don't need to render anything visible
# )

# Custom CSS to shift the header to the top-left corner
st.markdown(
    """
    <style>
    body {
        background-color: #0682fc;
        font-family: Playfair;
    }

    header {
        background-color: #0682fc;
        color: #fff;
        padding: 20px;
        text-align: center;
        border-radius: 8px;
    }

    .header-title {
        font-size: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.markdown(
    """
    <header>
        <p class="header-title">Flight Dashboard</p> 
    </header>
    """,
    unsafe_allow_html=True,
)

# st.markdown(
#     """
#     <style>
#     .custom-image {
#         position: absolute;
#         top: -50px;
#         left: -250px;
#         width: 200px;
#         height: 300px  
#     }
#     </style>
#     <img class="custom-image" src="download.png" alt="Custom Positioned Image">
#     """,
#     unsafe_allow_html=True
# )


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
            <a href="https://www.djss4ds.in/" style='color: #3498db; text-decoration: none;'>DJS S4DS</a> |
            <a href="#" style='color: #3498db; text-decoration: none;'>About Us</a> | 
            <a href="https://youtube.com/shorts/SXHMnicI6Pg?si=BZG1mGML2S-q7-u" style='color: #3498db; text-decoration: none;'>Terms of Service</a>
        </p>
    </footer>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
.stButton button{
    border: none;
    background color: #007bff;
    color: white; /* White text */
    padding: 10px 20px; /* Padding */
    text-align: center; /* Center text */
    text-decoration: none; /* No underline */
    font-size: 100px; /* Font size */
    margin: 5px 10px; /* Margin */
    cursor: pointer; /* Pointer on hover */
    font-family: 'Helvetica', sans-serif;
}
</style>
""", unsafe_allow_html=True)


# Initialize session state for the selected page
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Flight Profile"  # Default page

# Create buttons for navigation
if st.sidebar.button("✈️ Flight Profile"):
    st.session_state.selected_page = "Flight Profile"

if st.sidebar.button("🌦️ Weather"):
    st.session_state.selected_page = "Weather"

if st.sidebar.button("⛽ Fuel Consumption"):
    st.session_state.selected_page = "Fuel Consumption"

if st.sidebar.button("⏰ ETA & Delay Analysis"):
    st.session_state.selected_page = "ETA & Delay Analysis"

if st.sidebar.button("🚨 Alert"):
    st.session_state.selected_page = "Alert"

# Display content based on the selected page
if st.session_state.selected_page == "Flight Profile":
    st.subheader("Flight Profile")
    
    st.markdown(
    """
    <style>
    .stTextInput > div > input {
        width: 100px;  /* Change this value to your desired width */
        height: 30px;  /* Adjust height if needed */
        margin-left: auto;        /* Auto margin on left */
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .stTextInput > div > input {
            font-size: 1000px;  
            padding: 10px;     
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Leave the first and third columns blank
    col1, col2, col3 = st.columns(3)

    with col1:
        pass  # First column is blank

    with col2:
        # Store input in session state for Flight Number
        st.session_state.flight_number = st.text_input("Enter Flight Number", value=st.session_state.get('flight_number', ''))
    with col3:
        pass  # Third column is blank

    if len(st.session_state.flight_number)>0:
        price=get_cost(st.session_state.flight_number)[0]
        progress_bar = st.progress(0)
    # Simulate a long-running process
        for i in range(1, 101):
            time.sleep(0.005)  # Simulate work being done (adjust the delay as needed)
            progress_bar.progress(i)  # Update the progress bar

        if isinstance(price,str):
            st.success("Loading complete!")

            col1, col2, col3 = st.columns(3)

            # Column 1 for Departure Airport
            with col1:
                st.write(f"Departure Airport: {get_cost(st.session_state.flight_number)[1]}", value=st.session_state.get('departure', ''))

            # Column 2 for Arrival Airport
            with col2:
                st.write(f"Arrival Airport: {get_cost(st.session_state.flight_number)[2]}", value=st.session_state.get('departure', ''))
                
            with col3:
                st.write(f"Distance: {get_cost(st.session_state.flight_number)[3]}", value=st.session_state.get('departure', ''))
        else:
            st.error("Flight not found")
    
    
    

elif st.session_state.selected_page == "Weather":
    st.subheader("Weather")
    st.write("Weather will be displayed here")
    
elif st.session_state.selected_page == "Fuel Consumption":
    st.subheader("Fuel Consumption")
    st.write(f"Cost of fuel: ${get_cost(st.session_state.flight_number)[0]}")
elif st.session_state.selected_page == "ETA & Delay Analysis":
    st.subheader("ETA & Delay Analysis")
    st.write("Information about the app and its creators.")
elif st.session_state.selected_page == "Alert":
    st.subheader("Alert")
    st.write("Information about the app and its creators.")



