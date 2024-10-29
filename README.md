# Covid-19 Data Analytics

## Project Overview

This project involves processing data, transforming it into a structured SQL database, and visualizing insights. The key components include:
1. **CSV to SQL Data Transformation**: Using Python scripts to convert CSV files into a structured SQL database.
2. **Database Schema**: SQL scripts to define the database structure and tables.
3. **Pivot Tables & Charts**: Excel sheets that showcase data analysis using pivot tables and charts.
4. **Covid-19 Dashboard**: A Tableau workbook for visualizing Covid-19 related data.
5.	Clustering Models: Notebooks for clustering analysis on global and U.S.-specific COVID-19 datasets.

## Files

- `CSVtoSQL.py`: A Python script that reads CSV data files and loads them into a SQL database.
- `DBSchema.sql`: SQL script that defines the schema for the database, including tables, relationships, and constraints.
- `Pivot Tables & Charts.xlsx`: An Excel file containing data analysis through pivot tables and visualizations.
- `Covid-19 Dashboard.twb`: A Tableau workbook file designed to provide visual insights into Covid-19 data.
- GlobalClustering.ipynb: A Jupyter notebook performing clustering on global COVID-19 data to analyze case and death trends.
- USAClusterin.ipynb: A Jupyter notebook for U.S.-specific clustering and correlation analysis of COVID-19 cases and vaccination impact.
- `requirements.txt`: A file listing all the Python dependencies required for the project.

## Prerequisites

- Python 3.11.10
- PostgreSQL database
- Excel (for viewing and editing the pivot tables and charts)
- Tableau Desktop (for accessing the dashboard)

## Setup Instructions

### 1. Setting Up the PostgreSQL Database
1. Install and configure PostgreSQL on your system. You can download it from [PostgreSQL Downloads](https://www.postgresql.org/download/).
2. Create a new database in PostgreSQL using the following command:
    ```sql
    CREATE DATABASE your_database_name;
    ```
3. Execute the `DBSchema.sql` file in your PostgreSQL database to create the necessary tables and structure. You can do this using a tool like `psql`:
    ```bash
    psql -U your_username -d your_database_name -f DBSchema.sql
    ```

### 2. Creating the Environment File
1. Create a `.env` file in the root directory of the project.
2. Add the following environment variables:
    ```plaintext
    DB_HOST=your_database_host
    DB_PORT=your_database_port
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_NAME=your_database_name
    ```
3. Replace the placeholders with your actual database connection details.

### 3. Installing Required Python Libraries
1. Make sure you have Python installed on your system.
2. Run the following command to install all necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

### 4. Running the CSV to SQL Script
1. Place your CSV data files in the specified directory.
2. Open and run `CSVtoSQL.py` to load data into your PostgreSQL database.

### 5. Analyzing Data with Excel
1. Open `Pivot Tables & Charts.xlsx` in Excel.
2. Modify or refresh the pivot tables to analyze data as needed.
3. Use the charts to visualize key insights.

### 6. Running Clustering Notebooks
1. Global Clustering: The GlobalClustering.ipynb notebook performs K-means clustering on global COVID-19 case and death data, highlighting clusters based on confirmed cases, deaths, incident rates, and fatality ratios.
2. USA Clustering: The USAClusterin.ipynb notebook merges U.S.-specific COVID-19 and vaccination data, and provides correlation analysis between COVID-19 impact metrics and vaccination levels, displaying results in a heatmap. 

### 7. Visualizing Data with Tableau
1. Open `Covid-19 Dashboard.twb` using Tableau Desktop.
2. Update the data source if required and explore the visual dashboards.

## Usage

### Python Script (`CSVtoSQL.py`)
This script reads CSV files from a predefined directory and loads them into a PostgreSQL database. Ensure that the CSV files match the expected format as per the database schema. The script uses environment variables from the `.env` file to connect to the database.

### PostgreSQL Database (`DBSchema.sql`)
Defines the tables and relationships for storing structured data. Run this script to set up your database before loading any data.

### Excel File (`Pivot Tables & Charts.xlsx`)
The Excel file contains pivot tables and charts. You can use these to perform exploratory data analysis, summarize data, and gain insights through visualizations.

### Tableau Dashboard (`Covid-19 Dashboard.twb`)
The Tableau workbook provides an interactive dashboard for visualizing trends and key metrics related to Covid-19 data. Adjust filters and parameters as needed to explore different views.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.