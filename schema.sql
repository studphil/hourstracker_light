CREATE TABLE IF NOT EXISTS record_entry (
    id INTEGER PRIMARY KEY,
    date_of_record TEXT,
    client INTEGER,
    project TEXT,
    consultant TEXT,
    hours_worked TEXT,
    activity_description TEXT,
    billed BOOLEAN,
    date_time_of_creation TEXT
);

CREATE TABLE IF NOT EXISTS clients_companies (
    id INTEGER PRIMARY KEY,
    client TEXT,
    description TEXT,
    tax_id TEXT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS clients_people (
    id INTEGER PRIMARY KEY,
    id_client_company TEXT,
    project TEXT,
    hours_worked TEXT,
    date_time TEXT
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    client TEXT,
    project_sponsor TEXT,
    project_manager TEXT,
    project TEXT,
    projec_description TEXT,
    date_time TEXT,
    sap_project_number TEXT
);

CREATE TABLE IF NOT EXISTS consultants (
    id INTEGER PRIMARY KEY,
    client TEXT,
    project TEXT,
    hours_worked TEXT,
    date_time TEXT
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY,
    client TEXT,
    project TEXT,
    hours_worked TEXT,
    date_time TEXT
);

CREATE TABLE IF NOT EXISTS findocs (
    id INTEGER PRIMARY KEY,
    client TEXT,
    project TEXT,
    hours_worked TEXT,
    date_time TEXT
)