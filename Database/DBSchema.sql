CREATE TABLE global_covid_data (
    fips FLOAT,
    admin2 VARCHAR(255),
    province_state VARCHAR(255),
    country_region VARCHAR(255) NOT NULL,
    last_update TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    confirmed INT,
    deaths INT,
    recovered FLOAT,
    active FLOAT,
    combined_key VARCHAR(255),
    incident_rate FLOAT,
    case_fatality_ratio FLOAT
);

CREATE TABLE usa_covid_data (
    province_state VARCHAR(255),
    country_region VARCHAR(255) NOT NULL,
    last_update TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    confirmed INT,
    deaths INT,
    recovered FLOAT,
    active FLOAT,
    fips FLOAT,
    incident_rate FLOAT,
    total_test_results FLOAT,
    people_hospitalized FLOAT,
    case_fatality_ratio FLOAT,
    uid FLOAT,
    iso3 VARCHAR(10),
    testing_rate FLOAT,
    hospitalization_rate FLOAT
);

CREATE TABLE vaccination_global (
    province_state VARCHAR(255),
    country_region VARCHAR(255) NOT NULL,
    date DATE,
    doses_admin FLOAT,
    people_partially_vaccinated FLOAT,
    people_fully_vaccinated FLOAT,
    report_date_string DATE,
    uid FLOAT
);

CREATE TABLE usa_vaccination_data (
    fips FLOAT,
    province_state VARCHAR(255),
    country_region VARCHAR(255) NOT NULL,
    date DATE,
    latitude FLOAT,
    longitude FLOAT,
    combined_key VARCHAR(255),
    people_fully_vaccinated INT,
    people_partially_vaccinated FLOAT
);

TRUNCATE TABLE global_covid_data;
TRUNCATE TABLE usa_covid_data;
TRUNCATE TABLE vaccination_global;
TRUNCATE TABLE usa_vaccination_data;