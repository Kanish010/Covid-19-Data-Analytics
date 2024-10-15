CREATE TABLE country_wise_latest (
    id SERIAL PRIMARY KEY,
    country_region VARCHAR(100),
    confirmed INT,
    deaths INT,
    recovered INT,
    active INT,
    new_cases INT,
    new_deaths INT,
    new_recovered INT,
    deaths_per_100_cases NUMERIC(5, 2),
    recovered_per_100_cases NUMERIC(5, 2),
    deaths_per_100_recovered NUMERIC(7, 2),  
    confirmed_last_week INT,
    one_week_change INT,
    one_week_percent_increase NUMERIC(7, 2),
    who_region VARCHAR(50)
);

CREATE TABLE covid_19_clean_complete (
    id SERIAL PRIMARY KEY,
    province_state VARCHAR(100),    
    country_region VARCHAR(100) NOT NULL,
    lat DECIMAL(10, 6) NOT NULL,
    long DECIMAL(10, 6) NOT NULL,
    date DATE NOT NULL,
    confirmed INT NOT NULL,
    deaths INT NOT NULL,
    recovered INT NOT NULL,
    active INT NOT NULL,
    who_region VARCHAR(100) NOT NULL
);

CREATE TABLE day_wise (
    date DATE,
    confirmed INT,
    deaths INT,
    recovered INT,
    active INT,
    new_cases INT,
    new_deaths INT,
    new_recovered INT,
    deaths_per_100_cases DECIMAL(5, 2),
    recovered_per_100_cases DECIMAL(5, 2),
    deaths_per_100_recovered DECIMAL(5, 2),
    no_of_countries INT
);

CREATE TABLE worldometer_data (
    country VARCHAR(100),
    continent VARCHAR(50),
    population NUMERIC,
    total_cases NUMERIC,
    new_cases NUMERIC,
    total_deaths NUMERIC,
    new_deaths NUMERIC,
    total_recovered NUMERIC,
    new_recovered NUMERIC,
    active_cases NUMERIC,
    serious_critical NUMERIC,
    total_cases_per_million DECIMAL(15, 8),
    deaths_per_million DECIMAL(15, 8),
    total_tests NUMERIC,
    tests_per_million DECIMAL(15, 8),
    who_region VARCHAR(50)
);

DROP TABLE IF EXISTS country_wise_latest;
DROP TABLE IF EXISTS covid_19_clean_complete CASCADE;
DROP TABLE IF EXISTS day_wise CASCADE;
DROP TABLE IF EXISTS worldometer_data CASCADE;