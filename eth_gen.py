from hdwallet import HDWallet
from hdwallet.symbols import ETH


def generate_ethereum_address_from_mnemonic(mnemonic, path):
    return HDWallet(symbol=ETH, use_default_path=False).from_mnemonic(mnemonic).from_path(path).dumps()


def ethereum_addresses(mnemonic, depth=1):
    addresses_list = []

    try:
        eth_paths = ["m/44'/60'/0'/0", "m/44'/60'/0'", "m/44'/60'"]
        # exodus trust wallet metamask , ledger, ledger live
        
        depth = min(depth, 20)
        depth = max(depth, 1)
        addresses_list = [
            address
            for path in eth_paths
            for i in range(depth)
            for address_type, address in generate_ethereum_address_from_mnemonic(mnemonic,
                                                                                 f"{path}/{i}")["addresses"].items()
            if address_type == "p2pkh"
        ]

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return addresses_list
