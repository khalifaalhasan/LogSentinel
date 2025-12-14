# 🛡️ LogSentinel-ELK: Web Traffic Anomaly Detection

![ELK Stack](https://img.shields.io/badge/ELK_Stack-7.17.9-005571?style=for-the-badge&logo=elastic&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**LogSentinel-ELK** is a Big Data project designed to process, analyze, and detect anomalies in massive web server logs (>1.3 GB). By leveraging the power of **ELK Stack (Elasticsearch, Logstash, Kibana)** for data engineering and **Unsupervised Machine Learning (Isolation Forest)** for security analysis, this system can identify potential cyber threats such as DDoS attacks, brute force attempts, and data exfiltration.

---

## 📊 Project Architecture

The pipeline consists of three main stages:
1.  **Ingestion & ETL:** Parsing raw TSV logs using **Logstash** (Grok/CSV filters) and normalizing timestamps.
2.  **Storage & Visualization:** Indexing 13M+ records in **Elasticsearch** and visualizing traffic patterns in **Kibana**.
3.  **Advanced Analysis:** Extracting features using Python and applying **Isolation Forest** to detect outliers.

[Image of ELK Stack Architecture] 
*(You can upload your architecture diagram here)*

---

## 🛠️ Tech Stack

* **Infrastructure:** Docker & Docker Compose
* **ETL Pipeline:** Logstash 7.17
* **Database:** Elasticsearch 7.17 (Single Node Cluster)
* **Visualization:** Kibana 7.17
* **Machine Learning:** Python (Pandas, Scikit-Learn, Matplotlib)
* **Dataset:** NASA HTTP Server Log (Augmented to 1.3 GB / ~13 Million Hits)

---

## 🚀 Getting Started

### Prerequisites
* Docker Desktop (Engine running)
* Python 3.x
* Git

### 1. Clone the Repository
```bash
git clone [https://github.com/khalifaalhasan/LogSentinel-ELK.git](https://github.com/khalifaalhasan/LogSentinel-ELK.git)
cd LogSentinel-ELK
