-- Master Data Records entry

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
CREATE TABLE IF NOT EXISTS consultants (
    id INTEGER PRIMARY KEY,
    client TEXT,
    project TEXT,
    hours_worked TEXT,
    date_time TEXT
);


----------------------------------------------------
-- Master Data Projects
----------------------------------------------------

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    client TEXT,
    project_sponsor TEXT,
    project_manager TEXT,
    project TEXT,
    projec_description TEXT,
    start_date TEXT,
    end_date TEXT,
    project_status TEXT,
    activity_profile INTEGER,
    sap_project_number TEXT
);

----------------------------------------------------
-- Master Data Clients
----------------------------------------------------
xs
CREATE TABLE IF NOT EXISTS activity_profile (
    id INTEGER PRIMARY KEY,
    activity_number TEXT,

);

----------------------------------------------------
-- Master Data Clients
----------------------------------------------------
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
----------------------------------------------------
-- Transaction Data 
----------------------------------------------------
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
);
----------------------------------------------------
-- Historization Data
----------------------------------------------------
CREATE TABLE IF NOT EXISTS changelog (
    audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT,
    old_data TEXT,
    new_data TEXT,
    change_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);