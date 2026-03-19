# Kafka Local Setup (Python + Docker)

## Overview

This project shows a minimal local setup of **Apache Kafka** using Docker and basic interaction (topic creation, message production and consumption)  via Python.
Kafka runs in Docker using Confluent’s cp-all-in-one (community) setup, which includes the Kafka broker and related components and Python uses the `confluent-kafka` client.

---

## Python Client Structure

```text
kafka-python-app/
│
├── create_topic.py
├── producer.py
├── consumer.py
└── README.md
```
---

## Prerequisites

* Docker
* Python 3.12 (or similar)
* VS Code (optional)

---

## Kafka Setup (Docker)

### 1. Clone repository

```bash
git clone https://github.com/confluentinc/cp-all-in-one.git
cd cp-all-in-one/cp-all-in-one-community 
```

### 2. Start Kafka

```bash
docker-compose up -d
```

### 3. Verify containers

```bash
docker ps
```

Kafka broker should be available at:

```text
localhost:9092
```

For full setup (containers, networks, volumes) follow:

https://docs.confluent.io/platform/current/get-started/platform-quickstart.html#step-4-uninstall-and-clean-up

---

## Python Setup

Create virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependency:

```bash
pip install confluent-kafka
```

---

## Usage

### 1. Create topic

```bash
python 1create_topic.py
```

---

### 2. Start consumer

```bash
python 2consumer.py
```

---

### 3. Send messages

```bash
python 3producer.py
```

---

## Notes

* `produce()` is asynchronous; delivery is confirmed via callback
* consumer uses polling (`poll()`) rather than push
* offsets are tracked per **consumer group**
* changing `group.id` allows re-reading messages from the beginning

---

## Scope

This is a minimal local setup focused on Kafka fundamentals.

Not included:

* schema management
* stream processing frameworks
* production deployment
  
  
**Dominik Mikulski**  
Expanding hands-on data engineering capabilities alongside 12 years of analytics leadership
[LinkedIn](https://www.linkedin.com/in/dominikmikulski/) | [dominik.mikulski@gmail.com](mailto:dominik.mikulski@gmail.com)
