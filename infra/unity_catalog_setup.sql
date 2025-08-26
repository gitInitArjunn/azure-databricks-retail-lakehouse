-- Create Catalog for the project
CREATE CATALOG IF NOT EXISTS retail_lakehouse
COMMENT 'Retail Demand Lakehouse project';

-- Create schemas for medallion architecture
CREATE SCHEMA IF NOT EXISTS retail_lakehouse.bronze
COMMENT 'Raw / landing data';
CREATE SCHEMA IF NOT EXISTS retail_lakehouse.silver
COMMENT 'Cleansed / enriched data';
CREATE SCHEMA IF NOT EXISTS retail_lakehouse.gold
COMMENT 'Business / analytics layer';
