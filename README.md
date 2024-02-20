# get-erc20-balances
this Python package provides functionality to generate Ethereum addresses from a mnemonic phrase and check the ETH balance as well as ERC-20 token balances associated with a given Ethereum address.

## Installation

To use this package, you need to install the required libraries using pip. Open a terminal and run the following command:

```bash
pip install web3 hdwallet
```
eth\_gen Module
---------------

### Functions

#### `generate_ethereum_address_from_mnemonic(mnemonic, path)`

Generates an Ethereum address from a given mnemonic and derivation path.

*   `mnemonic`: The mnemonic phrase.
*   `path`: The derivation path.

#### `ethereum_addresses(mnemonic, depth=1)`

Generates a list of Ethereum addresses for different derivation paths.

*   `mnemonic`: The mnemonic phrase.
*   `depth`: The depth of address generation (default is 1, max is 20).

eth\_balance Module
-------------------

### Functions

#### `get_eth(url, address)`

Retrieves the ETH balance of a given Ethereum address.

*   `url`: The Web3 provider URL.
*   `address`: The Ethereum address.

#### `get_erc20tokens(url, address)`

Retrieves the balances of ERC-20 tokens associated with a given Ethereum address.

*   `url`: The Web3 provider URL.
*   `address`: The Ethereum address.

Example Usage (example.py)
--------------------------

Set your mnemonic phrase and Web3 provider URL, then call the functions to get ETH and ERC-20 token balances.

```python
# Set your mnemonic phrase and Web3 provider URL
mnemonic = "abadon abadon abadon abadon abadon abadon abadon abadon abadon abadon abadon abadon"
url = "https://rpc.notadegen.com/eth"
ethAddress = "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"

# Get ETH balance
ethBalance = get_eth(url, ethAddress)
print(ethBalance)

# Get ERC-20 token balances
erc20TokenBalances = get_erc20tokens(url, ethAddress)
print(erc20TokenBalances)

# Combined result (ETH balance + ERC-20 token balances)
combinedResult = ethBalance + erc20TokenBalances
print(combinedResult)
```
Note: Ensure you have a reliable Web3 provider. You can find free Ethereum nodes at Chainlist.

# Output
```python
[    {"coin_name": "ETH", "balance": 0.12345}]
[    {"coin_name": "USDT", "balance": 100.0},    {"coin_name": "DAI", "balance": 50.0}]
[    {"coin_name": "ETH", "balance": 0.12345},    {"coin_name": "USDT", "balance": 100.0},    {"coin_name": "DAI", "balance": 50.0}]
```
