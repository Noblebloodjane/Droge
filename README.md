# Drug Data Extraction Project

## Description

This project extracts data of medications x, y and z from various sources.

## Getting Started

### Dependencies

Before you begin, ensure you have the following prerequisites:

- **Operating System**: Windows 10, macOS, or Linux
- **Docker**: Ensure Docker is installed on your system.
- **cURL**: Required for downloading the `docker-compose.yaml` file.

### Installing

1. **Download Docker Compose File**:
   - Use cURL to fetch the Docker Compose configuration:
     ```bash
     curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.0/docker-compose.yaml'
     ```

2. **Set Up Python Environment**:
   - Ensure Python is installed on your system.
   - Navigate to your project directory and install the required Python libraries using `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

### Executing Program

1. **Start Apache Airflow**:
   - Use Docker Compose to start the Airflow services:
     ```bash
     docker-compose up
     ```

2. **Run Data Extraction**:
   - After starting the Airflow services, configure and trigger your data extraction workflows through the Airflow web interface.

3. **Access Airflow Web Interface**:
   - Open your web browser and go to `http://localhost:8080` to access the Airflow dashboard.
