# FastAPI Blockchain API

A lightweight custom Blockchain implementation wrapped in a REST API built with Python and **FastAPI**.

---

## Features

* **Custom Blockchain Architecture**: Built-in support for genesis block creation, block hashing via SHA-256, and cryptographic validation.
* **Proof of Work (PoW)**: Mines new blocks using a custom Proof of Work algorithm requiring 4 leading zeros (`0000`).
* **Integrity Validation**: Verifies both block hash chains and Proof of Work algorithms to prevent chain tampering.
* **Interactive OpenAPI Docs**: Test mining and chain inspection directly via FastAPI's built-in Swagger UI.

---

## Project Structure

```text
├── blockchain.py   # Core Blockchain logic (PoW, hashing, validation)
├── main.py         # FastAPI REST API endpoints
└── README.md       # Project documentation


LinkedIn URL:https://lnkd.in/p/gb2bwiS2
