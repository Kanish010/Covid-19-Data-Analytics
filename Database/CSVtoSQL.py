import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection details from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Load the CSV files
global_csv_file = 'Dataset/Global/GlobalDecember23.csv'
usa_csv_file = 'Dataset/USA/USADecember23.csv'
vaccination_csv_file = 'Dataset/Global/VaccinationGlobal.csv'
usa_vaccination_csv_file = 'Dataset/USA/VaccinationUSA.csv'

global_df = pd.read_csv(global_csv_file)
usa_df = pd.read_csv(usa_csv_file)
vaccination_df = pd.read_csv(vaccination_csv_file)
usa_vaccination_df = pd.read_csv(usa_vaccination_csv_file)

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    print("Connected to the database successfully!")

    # Insert data into the global_covid_data table
    for index, row in global_df.iterrows():
        cursor.execute(
            """
            INSERT INTO global_covid_data (fips, admin2, province_state, country_region, last_update, latitude, longitude,
                                           confirmed, deaths, recovered, active, combined_key, incident_rate, case_fatality_ratio)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                row['FIPS'], row['Admin2'], row['Province_State'], row['Country_Region'], row['Last_Update'], row['Lat'],
                row['Long_'], row['Confirmed'], row['Deaths'], row['Recovered'], row['Active'], row['Combined_Key'],
                row['Incident_Rate'], row['Case_Fatality_Ratio']
            )
        )

    # Insert data into the usa_covid_data table
    for index, row in usa_df.iterrows():
        cursor.execute(
            """
            INSERT INTO usa_covid_data (province_state, country_region, last_update, latitude, longitude, confirmed,
                                        deaths, recovered, active, fips, incident_rate, total_test_results, 
                                        people_hospitalized, case_fatality_ratio, uid, iso3, testing_rate, 
                                        hospitalization_rate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                row['Province_State'], row['Country_Region'], row['Last_Update'], row['Lat'], row['Long_'],
                row['Confirmed'], row['Deaths'], row['Recovered'], row['Active'], row['FIPS'], row['Incident_Rate'],
                row['Total_Test_Results'], row['People_Hospitalized'], row['Case_Fatality_Ratio'], row['UID'],
                row['ISO3'], row['Testing_Rate'], row['Hospitalization_Rate']
            )
        )

    # Insert data into the vaccination_global table
    for index, row in vaccination_df.iterrows():
        cursor.execute(
            """
            INSERT INTO vaccination_global (province_state, country_region, date, doses_admin, 
                                            people_partially_vaccinated, people_fully_vaccinated, 
                                            report_date_string, uid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                row['Province_State'], row['Country_Region'], row['Date'], row['Doses_admin'],
                row['People_partially_vaccinated'], row['People_fully_vaccinated'], row['Report_Date_String'],
                row['UID']
            )
        )

    # Insert data into the usa_vaccination_data table
    for index, row in usa_vaccination_df.iterrows():
        cursor.execute(
            """
            INSERT INTO usa_vaccination_data (fips, province_state, country_region, date, latitude, longitude, 
                                              combined_key, people_fully_vaccinated, people_partially_vaccinated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                row['FIPS'], row['Province_State'], row['Country_Region'], row['Date'], row['Lat'], row['Long_'],
                row['Combined_Key'], row['People_Fully_Vaccinated'], row['People_Partially_Vaccinated']
            )
        )

    # Commit the changes
    conn.commit()
    print("Data uploaded successfully to all tables!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")