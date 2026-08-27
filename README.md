# 🔗 Blockchain with Python and FastAPI

A simple educational **Blockchain system** developed using **Python and FastAPI**.

This project demonstrates the basic concepts of blockchain technology, including block creation, SHA-256 hashing, Proof of Work, mining, previous block hashes, and blockchain validation.

## 📌 Project Overview

The blockchain starts with a **Genesis Block** and allows new blocks to be mined and added to the chain.

Each block contains:

- Block index
- Timestamp
- Data
- Proof
- Previous block hash

The project uses **SHA-256 hashing** to generate hashes and **Proof of Work** to mine blocks.

## 🚀 Features

- Create a Genesis Block
- Mine new blocks
- Generate SHA-256 hashes
- Implement Proof of Work
- Link blocks using previous hashes
- Validate the blockchain
- Get the previous block
- Access the blockchain through FastAPI endpoints

## 🛠️ Technologies Used

- Python
- FastAPI
- SHA-256
- `hashlib`
- `datetime`
- `json`
- REST API
- Object-Oriented Programming

## 📂 Project Structure

```text
Blockchain/
│
├── blockchain.py
├── main.py
└── README.md

📄 File Description
blockchain.py

This file contains the main Blockchain class.

It is responsible for:

Creating the Genesis Block
Creating new blocks
Getting the previous block
Generating SHA-256 hashes
Performing Proof of Work
Mining new blocks
Validating the blockchain

The blockchain starts by creating a Genesis Block with initial data.

main.py

This file creates the FastAPI application and provides API endpoints for interacting with the blockchain.

The API includes endpoints for:

Mining a block
Viewing the blockchain
Validating the blockchain
Getting the previous block
🔐 SHA-256 Hashing

The project uses Python's hashlib module to generate SHA-256 hashes.

Each block is converted into JSON format and then hashed using SHA-256.

hash_value = hashlib.sha256(encoded_block).hexdigest()
⛏️ Proof of Work

The project implements a simple Proof of Work mechanism.

The program searches for a proof value where the resulting SHA-256 hash starts with four zeros:

0000

The proof is repeatedly changed until the required hash is found.

🔗 Blockchain Structure

The blocks are connected using the hash of the previous block.

Genesis Block
      ↓
   Block 2
      ↓
   Block 3
      ↓
   Block 4

Each new block stores the hash of the previous block.

If a previous block is changed, the blockchain validation can detect that the chain is no longer valid.

🌐 FastAPI Endpoints
1. Mine a Block
POST /mine_block

This endpoint accepts data and mines a new block.

Example:

/mine_block?data=Hello Blockchain
2. Get Blockchain
GET /blockchain

Returns the current blockchain.

3. Validate Blockchain
GET /validate

Checks whether the blockchain is valid.

Example response:

true
4. Get Previous Block
GET /previous_block

Returns the most recent block in the chain.

▶️ How to Run the Project
Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

python --version
Step 2: Install FastAPI

Run:

pip install fastapi

You may also need an ASGI server such as Uvicorn:

pip install uvicorn
Step 3: Run the FastAPI Application

Run:

uvicorn main:app --reload
Step 4: Open the API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

The FastAPI Swagger interface can be used to test the API endpoints.

🧪 Testing the Project

Using the FastAPI documentation, you can test:

/mine_block
/blockchain
/validate
/previous_block

Before returning blockchain information, the API checks whether the blockchain is valid. If the blockchain is invalid, the API returns an error.

📚 What I Learned

Through this project, I learned:

Basic blockchain concepts
How blocks are created
How blocks are connected
SHA-256 cryptographic hashing
Proof of Work
Blockchain validation
Python classes and objects
FastAPI
REST API endpoints
Working with JSON data
🚀 Future Improvements

Possible improvements include:

Add a transaction system
Add wallets and user accounts
Add a mining reward
Add a peer-to-peer network
Add a database for persistent blockchain storage
Add authentication
Create a frontend interface

LinkedIn URL:https://lnkd.in/p/gb2bwiS2
