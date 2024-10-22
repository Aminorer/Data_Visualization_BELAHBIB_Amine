import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import plotly.graph_objs as go

# Page configuration
st.set_page_config(page_title="Amine BELAHBIB · CV", page_icon="📜", layout="wide")

# Custom CSS to style the app
st.markdown("""
    <style>
    /* General settings */
    body {
        background-color: #f0f2f6;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    /* Main content area */
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
    /* Sidebar settings */
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #007ACC;
    }
    /* Links */
    a {
        color: #007ACC;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    /* Buttons */
    .stButton>button {
        color: #ffffff;
        background-color: #007ACC;
    }
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background-color: #dddddd;
        margin: 25px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Portfolio", "Analyse French Museums"])

if page == "Portfolio":
    st.image('C:/Users/User/Documents/EFREI/Semestre_7/Data_Visualization/Projet/Images/EFREI.png', width=170)
    
    col1, col2 = st.columns([1,3])
    with col1:
        st.image('C:/Users/User/Documents/EFREI/Semestre_7/Data_Visualization/Projet/Images/photo_de_profil.png', width=250)
    with col2:
        st.title("Amine BELAHBIB")
        st.write("**Data Science Intern**")
        st.write("I am seeking to complete my M1 internship in data science from **November 6, 2024** to **April 7, 2025**.")
        st.markdown("""
        **Phone:** +33 6 20 20 08 81  
        **Email:** [amine.belahbib@efrei.net](mailto:amine.belahbib@efrei.net)  
        **Address:** Compiègne, 60200  
        [![LinkedIn](https://img.icons8.com/ios-filled/24/000000/linkedin.png)](https://www.linkedin.com/in/amine-belahbib-60baa8250/)
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.header("Education")
    st.subheader("EFREI Engineering School")
    st.write("""
    **Program:** Engineering Cycle - Data Engineering  
    **Year:** 2024 - Present  
    """)
    
    st.subheader("Preparatory Class PCSI/PC")
    st.write("""
    **School:** Lycée Pierre d'Ailly Compiègne  
    **Year:** 2020 - 2022  
    """)
    
    st.subheader("Scientific Baccalaureate")
    st.write("""
    **School:** Lycée Mireille Grenet Compiègne  
    **Year:** 2020  
    """)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.header("Skills")
    st.subheader("Programming Languages & Tools")
    st.write("""
    - **Programming Languages:** Python, Java, PHP, JavaScript, HTML/CSS  
    - **Web Development:** HTML, CSS, JavaScript, PHP  
    - **Databases:** SQL, SQL queries  
    - **Python Libraries:** pandas, matplotlib, numpy, scikit-learn, spaCy  
    - **Software:** Visual Studio Code, Jupyter, Replit, Regressi  
    """)
    
    st.subheader("Languages")
    st.write("""
    - **English:** Advanced Level B2  
    - **French:** Native  
    - **Spanish:** Intermediate Level B1  
    """)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.header("Projects")
    
    st.subheader("ITECH Feelings | Review Scanner (2023)")
    st.write("""
    **Objective:** Developed a review scanner to analyze customer sentiments regarding a specific product using a predefined dataset.  
    
    **Skills Acquired:**  
    - Utilized libraries: scikit-learn, spaCy  
    - Data processing: Efficiently managed large datasets  
    - Model evaluation: Assessed sentiment analysis model performance and identified improvement areas  
    - Report writing: Communicated project results coherently in a detailed report  
    """)
    
    st.subheader("DVF Analytics | Real Estate Transaction Analysis (2023)")
    st.write("""
    **Objective:** Conducted analysis on DVF (Real Estate Value Requests) data to deepen data analysis skills and familiarize with real estate transactions.  
    
    **Skills Acquired:**  
    - Data processing: Extracted relevant information from large datasets  
    - Model evaluation: Evaluated DVF data analysis model performance and identified improvement areas  
    - Unsupervised machine learning: Applied algorithms to discover hidden structures in unlabeled data  
    - Project management: Planned, organized, and managed the project effectively, meeting deadlines and milestones  
    """)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.header("Download CV")
    st.write("Click the button below to download the PDF version of my CV.")
    cv_file_path = "C:/Users/User/Documents/EFREI/Semestre_7/Data_Visualization/Projet/BELAHBIB Amine CV Stage Data Science.pdf"
    with open(cv_file_path, 'rb') as file:
        st.download_button(label="Download PDF", data=file, file_name='CV_Amine_Belahbib.pdf')

elif page == "Analyse French Museums":
    st.image('C:/Users/User/Documents/EFREI/Semestre_7/Data_Visualization/Projet/Images/EFREI.png', width=150)
    
    st.header("Analyze French Museums")
    
    csv_file = "C:/Users/User/Documents/EFREI/Semestre_7/Data_Visualization/Projet/frequentation-musees-fusionne-2001-2018.csv"
    df = pd.read_csv(csv_file)
    
    st.write("### Data Overview")
    st.dataframe(df.head())
    
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['stats_payantes'] = pd.to_numeric(df['stats_payantes'], errors='coerce')
    df['stats_gratuites'] = pd.to_numeric(df['stats_gratuites'], errors='coerce')
    
    df = df.dropna(subset=['year', 'stats_payantes', 'stats_gratuites'])
    st.sidebar.write("### Paid Attendance of Museums by Year")
    option = st.sidebar.selectbox("Choose an analysis", 
                                  ["Paid Attendance by Year", 
                                   "Free Attendance by Year", 
                                   "Top 10 Most Visited Museums (Paid + Free)"])
    
    if option == "Paid Attendance by Year":
        st.write("### Paid Attendance of Museums by Year")
        fig_payantes = px.bar(df.groupby('year')['stats_payantes'].sum().reset_index(),
                              x='year', y='stats_payantes',
                              title="Paid Attendance by Year",
                              labels={'stats_payantes': 'Paid Attendance', 'year': 'Year'})
        st.plotly_chart(fig_payantes)
    
    elif option == "Free Attendance by Year":
        st.write("### Free Attendance of Museums by Year")
        fig_gratuites = px.bar(df.groupby('year')['stats_gratuites'].sum().reset_index(),
                               x='year', y='stats_gratuites',
                               title="Free Attendance by Year",
                               labels={'stats_gratuites': 'Free Attendance', 'year': 'Year'})
        st.plotly_chart(fig_gratuites)
    
    elif option == "Top 10 Most Visited Museums (Paid + Free)":
        st.write("### Most Visited Museums (Paid + Free)")
        df['total_frequentation'] = df['stats_payantes'] + df['stats_gratuites']
        top_museums = df.groupby('name')['total_frequentation'].sum().sort_values(ascending=False).head(10).reset_index()
        fig_top_museums = px.bar(top_museums, x='name', y='total_frequentation',
                                 title="Top 10 Most Visited Museums (Paid + Free)",
                                 labels={'total_frequentation': 'Total Attendance', 'name': 'Museum Name'})
        st.plotly_chart(fig_top_museums)
    
    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')
    df['total_frequentation'] = df['stats_payantes'] + df['stats_gratuites']
    df = df.dropna(subset=['lat', 'lon'])

    st.sidebar.write("### Top 10 Cities by Total Attendance")
    selected_year = st.sidebar.selectbox('Choose the year', sorted(df['year'].unique()))
    st.write("### Top 10 Cities by Total Attendance")
    attendance_by_city = df[df['year'] == selected_year].groupby('city')['total_frequentation'].sum().reset_index()
    top_cities = attendance_by_city.sort_values('total_frequentation', ascending=False).head(10)
    fig_top_cities = px.bar(
        top_cities, 
        x='city', 
        y='total_frequentation',
        title=f'Top 10 Cities by Total Attendance in {selected_year}',
        labels={'total_frequentation': 'Total Attendance', 'city': 'City'}
    )
    st.plotly_chart(fig_top_cities)


    st.sidebar.write("### Treemap of Museum Attendance by City")
    selected_year_treemap = st.sidebar.selectbox('Choose the year for Treemap', sorted(df['year'].unique()))

    st.write(f"### Treemap of Museum Attendance by City in {selected_year_treemap}")
    treemap_data = df[df['year'] == selected_year_treemap].groupby(['city', 'name'])['total_frequentation'].sum().reset_index()

    fig_treemap = px.treemap(
        treemap_data, 
        path=['city', 'name'], 
        values='total_frequentation',
        title=f"Treemap of Museum Attendance by City in {selected_year_treemap}",
        labels={'total_frequentation': 'Total Attendance'}
    )
    st.plotly_chart(fig_treemap)

    st.sidebar.write("### Pie Chart of Paid vs Free Attendance")
    selected_year_pie = st.sidebar.selectbox('Choose the year for Pie Chart', sorted(df['year'].unique()))

    st.write(f"### Pie Chart of Paid vs Free Attendance in {selected_year_pie}")
    attendance_pie = df[df['year'] == selected_year_pie].groupby('year')[['stats_payantes', 'stats_gratuites']].sum().reset_index()

    attendance_pie_data = pd.DataFrame({
        'Type': ['Paid', 'Free'],
        'Attendance': [attendance_pie['stats_payantes'].values[0], attendance_pie['stats_gratuites'].values[0]]
    })

    fig_pie = px.pie(
        attendance_pie_data, 
        values='Attendance', 
        names='Type', 
        title=f"Pie Chart of Paid vs Free Attendance in {selected_year_pie}",
        labels={'Attendance': 'Attendance', 'Type': 'Attendance Type'}
    )
    st.plotly_chart(fig_pie)

    st.sidebar.write("### Violin Plot of Paid vs Free Attendance Distribution")
    selected_year_violin = st.sidebar.selectbox('Choose the year for Violin Plot', sorted(df['year'].unique()))

    st.write(f"### Violin Plot of Paid vs Free Attendance Distribution in {selected_year_violin}")
    attendance_violin = df[df['year'] == selected_year_violin][['city', 'stats_payantes', 'stats_gratuites']].melt(
        id_vars='city', value_vars=['stats_payantes', 'stats_gratuites'], var_name='Type', value_name='Attendance'
    )

    fig_violin = px.violin(
        attendance_violin, 
        x='Type', 
        y='Attendance', 
        color='Type', 
        box=True, 
        points='all',
        title=f'Violin Plot of Paid vs Free Attendance Distribution in {selected_year_violin}',
        labels={'Attendance': 'Attendance', 'Type': 'Attendance Type'}
    )
    st.plotly_chart(fig_violin)

    st.sidebar.write("### Horizontal Bar Chart of Paid vs Free Attendance for Selected Museum")
    selected_year_bar = st.sidebar.selectbox('Choose the year for Bar Chart', sorted(df['year'].unique()))
    selected_museum_bar = st.sidebar.selectbox('Choose a museum for Bar Chart', df['name'].unique())


    st.write(f"### Comparison of Paid vs Free Attendance for {selected_museum_bar} in {selected_year_bar}")
    museum_bar_data = df[(df['year'] == selected_year_bar) & (df['name'] == selected_museum_bar)][['stats_payantes', 'stats_gratuites']]

    bar_data = pd.DataFrame({
        'Attendance Type': ['Paid Attendance', 'Free Attendance'],
        'Attendance': [museum_bar_data['stats_payantes'].sum(), museum_bar_data['stats_gratuites'].sum()]
    })

    fig_bar = px.bar(
        bar_data, 
        x='Attendance', 
        y='Attendance Type', 
        orientation='h',
        title=f"Paid vs Free Attendance for {selected_museum_bar} in {selected_year_bar}",
        labels={'Attendance': 'Attendance', 'Attendance Type': 'Type of Attendance'}
    )
    st.plotly_chart(fig_bar)

    attendance_3d_data_updated = df  

    df['total_frequentation'] = df['stats_payantes'] + df['stats_gratuites']

    fig_3d_updated = px.scatter_3d(
        attendance_3d_data_updated,
        x='year',  
        y='total_frequentation',  
        z='city',  
        color='total_frequentation', 
        size='total_frequentation', 
        hover_name='name',  
        title="3D Scatter Plot of Museums Based on City, Year, and Attendance (All Years)",
        labels={'total_frequentation': 'Total Attendance', 'year': 'Year', 'city': 'City'}
    )

    st.plotly_chart(fig_3d_updated)


    st.sidebar.write("### Museum Attendance Over Years")
    entry_type = st.sidebar.selectbox("Choose entry type", ["Total Entries", "Paid Entries", "Free Entries"])
    
    if entry_type == "Paid Entries":
        df['entries'] = df['stats_payantes']
    elif entry_type == "Free Entries":
        df['entries'] = df['stats_gratuites']
    else:
        df['entries'] = df['stats_payantes'] + df['stats_gratuites']
    
    st.write("### Museum Attendance Over Years")
    df['entries'] = df['entries'].fillna(0)
    df = df[df['entries'] >= 0]
    df['scaled_entries'] = np.log1p(df['entries'])
    
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        size="scaled_entries",
        color="entries",
        animation_frame="year",
        hover_name="name",
        size_max=30,
        zoom=5,
        mapbox_style="open-street-map",
        title="Museum Attendance Over Years",
        center={"lat": 46.2276, "lon": 2.2137}  
    )
    
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    
    st.plotly_chart(fig, use_container_width=True)

