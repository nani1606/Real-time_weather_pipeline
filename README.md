# Real-Time Weather Data Pipeline with AWS Kinesis and DynamoDB

A real-time data pipeline to collect, stream, process, store, and visualize weather data using AWS Kinesis, Lambda, DynamoDB, S3, and Tableau. Built to demonstrate Cloud Data Engineering skills in streaming, NoSQL storage, and data visualization.

## Overview
This project processes weather data for five cities (Chicago, New York, London, Mumbai, Sydney) from the [OpenWeatherMap API](https://openweathermap.org/). It:
- Collects real-time weather data using Python (~50 records).
- Streams data via AWS Kinesis Data Stream and Firehose to S3.
- Processes the stream with AWS Lambda and stores in AWS DynamoDB.
- Exports data to CSV and visualizes temperature trends in Tableau Public.

## Tableau dashboard
https://public.tableau.com/views/realtime_weather_data/Sheet2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Architecture
```mermaid
graph TD
    A[OpenWeatherMap<br>API] --> B[Python<br>fetch_weather.py]
    B --> C[Python<br>stream_weather.py]
    C --> D[AWS Kinesis<br>weather-stream]
    D --> E[AWS Firehose<br>weather-to-s3]
    E --> F[AWS S3<br>raw/]
    D --> G[AWS Lambda<br>weatherProcessor]
    G --> H[AWS DynamoDB<br>weather-table]
    H --> I[Python<br>export_dynamodb.py]
    I --> J[AWS S3<br>processed/]
    I --> K[Tableau Public<br>Dashboard]