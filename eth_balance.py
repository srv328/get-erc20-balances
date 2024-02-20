from json import loads
from web3 import Web3

def get_erc20tokens(url, address):
    w3 = Web3(Web3.HTTPProvider(url))

    if not w3.is_connected():
        print("Unable to connect to the Ethereum node.")
        return []

    with open("abiERC-20.json", "r") as fp:
        token_abi = loads(fp.read())

    with open("erc20Tokens.json", "r") as fp:
        erc20_data = loads(fp.read())

    token_balances = []

    decimals = 18

    for contract_info in erc20_data.get("erc20Tokens", []):
        token_address = contract_info.get("address")
        coin_name = contract_info.get("coin_name")

        checksum_address = w3.to_checksum_address(token_address)

        token_contract = w3.eth.contract(checksum_address, abi=token_abi)

        decimals = token_contract.functions.decimals().call()

        balance_wei = token_contract.functions.balanceOf(w3.to_checksum_address(address)).call()
        balance_token_units = balance_wei / 10 ** decimals

        token_balances.append({
            "coin_name": coin_name,
            "balance": balance_token_units
        })

    return token_balances


def get_eth(url, address):
    w3 = Web3(Web3.HTTPProvider(url))

    if not w3.is_connected():
        print("Unable to connect to the Ethereum node.")
        return []

    checksum_address = w3.to_checksum_address(address)
    balance_wei = w3.eth.get_balance(checksum_address)
    balance = w3.from_wei(balance_wei, 'ether')

    return [{
        "coin_name": "ETH",
        "balance": float(balance)
    }]


if __name__ == "__main__":
    print(get_eth("https://rpc.notadegen.com/eth", "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5") +
          get_erc20tokens("https://rpc.notadegen.com/eth", "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"))
