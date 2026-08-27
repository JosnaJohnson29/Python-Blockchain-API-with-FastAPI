import blockchain as _blockchain
import fastapi as _fastapi

app = _fastapi.FastAPI()
blockchain = _blockchain.Blockchain()


@app.post("/mine_block")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        raise _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid"
        )

    block = blockchain.mine_block(data=data)
    return block


@app.get("/blockchain")
def get_blockchain():
    if not blockchain.is_chain_valid():
        raise _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid"
        )

    return blockchain.chain


@app.get("/validate")
def is_blockchain_valid():
    return blockchain.is_chain_valid()


@app.get("/previous_block")
def get_previous_block():
    if not blockchain.is_chain_valid():
        raise _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid"
        )

    return blockchain.get_previous_block()