# ⛓️ Blockchain API with FastAPI

A simple Python-based blockchain application that demonstrates how blocks are created, mined, linked using cryptographic hashes, and validated through a FastAPI web API.

## Features

* **Create Blockchain:** Initializes a blockchain with a Genesis Block.

* **Block Creation:** Creates blocks containing an index, timestamp, data, proof, and previous block hash.

* **Proof of Work:** Mines blocks by finding a proof that produces a SHA-256 hash beginning with four leading zeros.

* **SHA-256 Hashing:** Uses SHA-256 to generate a unique cryptographic hash for each block.

* **Chain Validation:** Verifies that each block is correctly linked to the previous block and that its Proof of Work is valid.

* **FastAPI Integration:** Provides API endpoints to mine blocks, view the blockchain, validate the chain, and retrieve the previous block.

## Requirements

* Python 3.x
* FastAPI
* Uvicorn

## Project Structure

```text
.

├── blockchain.py # Contains the Blockchain class and blockchain logic
├── main.py      # FastAPI application and API endpoints
└── README.md    # Project documentation
```

## How to Run

1. Clone the repository or download the source files.

2. Open your terminal in the project directory.

3. Install the required packages:

```bash
pip install fastapi uvicorn
```

4. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

5. Open the API documentation in your browser:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Mine a Block

```text
POST /mine_block
```

Used to mine a new block with the provided data.

### View Blockchain

```text
GET /blockchain
```

Returns the complete blockchain.

### Validate Blockchain

```text
GET /validate
```

Checks whether the blockchain is valid.

### Get Previous Block

```text
GET /previous_block
```

Returns the most recently added block.

## How It Works

1. **Genesis Block:** The blockchain starts with a Genesis Block.

2. **Add Data:** Data is provided when requesting a new block.

3. **Proof of Work:** The program searches for a proof that produces a SHA-256 hash beginning with `0000`.

4. **Create Block:** Once the proof is found, a new block is created with its previous block's hash.

5. **Add to Chain:** The new block is added to the blockchain.

6. **Validate:** The application checks the previous hash and Proof of Work of each block to verify the blockchain.

## Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **SHA-256**
* **JSON**
* **Proof of Work**


LinkedIn URL:https://www.linkedin.com/posts/josna-johnson-894a29392_python-pythonproject-blockchain-activity-7498680978857570304-2s7J?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGCdu7AB3McqJazzcJ3w2cmEvw-1JU5jJNc
