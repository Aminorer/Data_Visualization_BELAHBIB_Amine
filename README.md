# Data_Visualization_BELAHBIB_Amine

This Streamlit application serves as both a personal portfolio for Amine Belahbib and an interactive analysis of French museum attendance data.

## **Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)
- [Dependencies](#dependencies)
- [License](#license)
- [Contact](#contact)

## **Introduction**

This application allows users to view Amine Belahbib's professional portfolio, including education, skills, projects, and a downloadable CV. Additionally, it provides an interactive analysis of French museum attendance from 2001 to 2018, featuring various data visualizations.

## **Features**

- **Portfolio Page:**
  - View personal information, education, skills, and projects.
  - Downloadable CV in PDF format.

- **French Museums Analysis:**
  - Interactive data visualizations using Plotly and Streamlit.
  - Analysis options include:
    - Paid and free attendance by year.
    - Top 10 most visited museums.
    - Top 10 cities by total attendance.
    - Treemap of museum attendance by city.
    - Pie chart and violin plot of attendance types.
    - 3D scatter plot of museums based on city, year, and attendance.
    - Map visualization of museum attendance over years.

## **Installation**

To run this application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Navigate through the application:**

   - Use the sidebar to switch between the "Portfolio" and "Analyse French Museums" pages.
   - Interact with the various visualizations and options available.

## **Data Source**

The museum attendance data is sourced from the CSV file `frequentation-musees-fusionne-2001-2018.csv`, which contains attendance statistics for French museums from 2001 to 2018.

## **Dependencies**

The application relies on the following Python libraries:

- streamlit
- pandas
- numpy
- plotly
- scikit-learn
- statsmodels

All dependencies are listed in the `requirements.txt` file.

## **Contact**

For any inquiries or feedback, please contact:

- **Email:** [amine.belahbib@efrei.net](mailto:amine.belahbib@efrei.net)
- **LinkedIn:** [Amine Belahbib](https://www.linkedin.com/in/amine-belahbib-60baa8250/)

---

