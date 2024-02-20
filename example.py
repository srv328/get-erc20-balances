from eth_gen import ethereum_addresses
from eth_balance import get_eth, get_erc20tokens

# set your mnemo phrase

mnemonic = "abadon abadon abadon abadon abadon abadon abadon abadon abadon abadon abadon abadon"

depth = 1  # set the depth of the generating address. min value is 1, max value is 20

# addresses = ethereum_addresses(mnemonic, depth)

# for eth_address in addresses:
#     print(eth_address)

    # print 3*depth addresses for one mnemonic phrases.
    # dirivations paths is ["m/44'/60'/0'/0", "m/44'/60'/0'", "m/44'/60'"]
    # exodus trust wallet metamask , ledger, ledger live

    # addresses[0] exodus, trust wallet, matamask addresses
    # addresses[1] ledger address
    # addresses[2] ledger live addresses

# your Web3 provider (you can find free eth nodes at https://chainlist.org/chain/1)
url = "https://rpc.notadegen.com/eth"

# return a list of dictionary which include ETH balance of address

ethAddress = "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"

ethBalance = get_eth(url, ethAddress)
print(ethBalance)

# you can use it like this
#print(get_eth(url, "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"))

# or like this
#print(get_eth("https://rpc.notadegen.com/eth", "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"))

# get erc20tokens from address
# return a list of dictionaries which includes info about erc20 tokens from file erc20Tokens.json (you can edit it for your needs)
# this command can take a 1 minute (depends on your ping/connection to web3 provider)
print(get_erc20tokens(url, ethAddress))

# if you want to get combined result you also can use
# print(get_eth(url, ethAddress) + get_erc20tokens(url, ethAddress))
