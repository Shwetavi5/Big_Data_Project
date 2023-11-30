# Big_Data_Project
Covid_Vaccination_Anaalysis using Dataflow
# COVID-19 Vaccination Progress Analysis using Google Dataflow

## Project Group 6
- Shwetarani
- Samhitha Upadhyaya
- Vamshi Krushna  

## Introduction
The COVID-19 pandemic has led countries worldwide to embark on extensive vaccination programs to curb the spread of the disease. This project focuses on analyzing the ongoing vaccination progress across different countries by creating a data analytics pipeline utilizing Google Dataflow. Our aim is to provide insights into various aspects of global vaccination efforts, such as the most widely used vaccines and countries with the highest vaccination rates.

## Dataset Description
The dataset "COVID 19 World Vaccination Progress" sourced from "Our World in Data" contains country-wise data on COVID-19 vaccinations. It encompasses daily vaccination information from December 12, 2020, to the present and is continually updated. Key data points include total vaccinations, people vaccinated, people fully vaccinated, daily vaccinations, and vaccination percentages.

## GCP Services Used
### Data Ingestion
- Google Cloud Storage
- Google Cloud PubSub
- Google Cloud Functions
### Data Preparation and Processing
- Google Cloud DataFlow
### Processed Data Storage
- Google Cloud BigQuery
### Data Visualization
- Google Data Studio

## Installation
- Install pip
- Set up a Python environment
- `pip install apache-beam`
- `pip install google-cloud-storage`
- `pip install google-cloud-bigquery`
- `pip install google-cloud-Pub/Sub`

## Visualizing Vaccination Progress Analytics Pipeline
- Streaming data is published to the PubSub topic.
- Batch data is read by publishing metadata to the PubSub topic using Cloud Functions.
- DataFlow reads batch and streaming data from the PubSub topics and transforms it.
- Transformed data is appended to BigQuery for storage.
- BigQuery data is connected to Data Studio for visualization.

## Objectives
- Identify popular vaccines globally and in various countries.
- Compare trends between partially vaccinated and fully vaccinated individuals.
- Determine the most utilized vaccine categories worldwide.
- Identify countries with the highest vaccination rates.

## Data Ingestion
### Batch Data Ingestion
Cloud Functions trigger PubSub when a new CSV file is added to the Google Storage Bucket.
### Streaming Data Ingestion
Continuously generated data is published to the PubSub topic.

## Data Preparation
- Cleaned data by handling missing values and removing unnecessary columns.

## Data Processing/Analyzing
- Analyzed vaccination trends and identified top countries and vaccines.

## Transforms used in the pipeline
- `beam.io.ReadFromPubSub`
- `beam.Map`
- `beam.window.FixedWindows`
- `beam.GroupByKey`
- `beam.CoGroupByKey`
- `beam.FlatMap`
- `beam.Flatten`
- `beam.io.WriteToBigQuery`

## Data Storage after Processing
- BigQuery was chosen for its scalability and ability to process vast amounts of data efficiently.

## Data Visualization
- Google Data Studio was used to visualize the processed data.

## Conclusion
- The project aims to provide meaningful insights into global vaccination programs.
- Continuous updates are available through our Data Studio Dashboard.
- Our analysis can aid the general public and governments in monitoring and assessing vaccination efforts.

## Future Work
- Explore correlations between total deaths and vaccinations.
- Implement machine learning models for vaccination trend forecasting.

For more detailed information and code implementation, refer to the project's source code and documentation.
