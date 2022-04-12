from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract

connector = Connect("https://testnet.veblocks.net")
dict = {
  "address": "25281c4a22cf4bb93e079045b25e9a6a03eb3ae5",
  "crypto": {
    "cipher": "aes-128-ctr",
    "ciphertext": "ebedd5a51ed56ff6cf4654cd5f806c945c94db3349d5ffd2e54c4cb7d200a5d0",
    "cipherparams": {
      "iv": "b08fe00ba5cb5228db635f68b2c599b8"
    },
    "mac": "1c8497aa081db949d223c373a9bdd8c5ac269132ddef60e92c8aa2ed864f3d9b",
    "kdf": "scrypt",
    "kdfparams": {
      "dklen": 32,
      "n": 262144,
      "r": 8,
      "p": 1,
      "salt": "0c2ee5b0db26747e5fcaebf4e1ebf449f354be5afb9cdf55dc96976ab48d5a15"
    }
  },
  "id": "d0083404-0503-4357-8cde-2d141154e5ef",
  "version": 3
}

# wallet address: 0x7567d83b7b8d80addcb281a71d54fc7b3364ffed
wallet = Wallet.fromKeyStore(ks=dict, password='XXXXXXXX')
contract = Contract.fromFile("/home/osboxes/VendingMachine/build/contracts/VendingMachine.json")
_contract_addr = '0x040E299D822470d9A25dc1Bf96D510F14F0D7018'

connector.deploy(wallet, contract)

connector.transact(wallet, contract, "addDrink", [("Coca Cola"),("0.5 L"), ("2 EUR")],to=_contract_addr, value=0 * (10 ** 18))

connector.transact(wallet, contract, "getDrinkList", [0], to=_contract_addr, value=0 * (10 ** 18))
