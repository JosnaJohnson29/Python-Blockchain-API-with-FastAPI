import datetime as _dt
import hashlib as _hashlib
import json as _json


class Blockchain:

    def __init__(self):
        self.chain = list()
        # Create the Genesis Block
        genesis_block = self.create_block(
            data="I am the genesis block", proof=1, previous_hash="0", index=1
        )
        self.chain.append(genesis_block)

    def create_block(
        self, data: str, proof: int, previous_hash: str, index: int
    ) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash,
        }
        return block

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _to_digest(
        self,
        new_proof: int,
        previous_proof: int,
        index: str,
        data: str,
    ) -> bytes:
        to_digest = (
            str(new_proof**2 - previous_proof**2 + int(index)) + data
        )
        return to_digest.encode("utf-8")

    def _proof_of_work(self, previous_proof: int, index: int, data: str) -> int:
        new_proof = 1
        check_proof = False

        while not check_proof:
            to_digest = self._to_digest(
                new_proof=new_proof,
                previous_proof=previous_proof,
                index=str(index),
                data=data,
            )
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            # Target criteria: hash must start with 4 leading zeros
            if hash_value[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def _hash(self, block: dict) -> str:
        """Hashes a block and returns its hexadecimal SHA-256 value."""
        encoded_block = _json.dumps(block, sort_keys=True).encode()
        return _hashlib.sha256(encoded_block).hexdigest()

    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1

        proof = self._proof_of_work(
            previous_proof=previous_proof, index=index, data=data
        )
        previous_hash = self._hash(block=previous_block)

        block = self.create_block(
            data=data, proof=proof, previous_hash=previous_hash, index=index
        )
        self.chain.append(block)
        return block

    def is_chain_valid(self) -> bool:
        current_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            # 1. Check if previous hash matches the actual hash of current block
            if next_block["previous_hash"] != self._hash(current_block):
                return False

            # 2. Re-evaluate Proof of Work criteria
            current_proof = current_block["proof"]
            next_proof = next_block["proof"]
            next_index = next_block["index"]
            next_data = next_block["data"]

            to_digest = self._to_digest(
                new_proof=next_proof,
                previous_proof=current_proof,
                index=str(next_index),
                data=next_data,
            )
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            if hash_value[:4] != "0000":
                return False

            current_block = next_block
            block_index += 1

        return True