
from web3 import Web3
from tests.utils import run_test, load_contract

contract_compound_v3_mig_bundler_v2 = load_contract(
    "1f8076e2eb6f10b12e6886f30d4909a91969f7da"
)

def test_multicall_comp_v3_mig_v2(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xac9650d800000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000004470dc41fe0000000000000000000000006b175474e89094c44da98b954eedeac495271d0f00000000000000000000000000000000000000000000017b7883c069166000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001a44d5fcf680000000000000000000000006b175474e89094c44da98b954eedeac495271d0f0000000000000000000000004c9edd5852cd905f086c759e8383e09bff1e68b3000000000000000000000000ae4750d0813b5e37a51f7629beedd72af1f9ca35000000000000000000000000870ac11d48b15db9a138cf899d20f13f79ba00bc0000000000000000000000000000000000000000000000000bef55718ad6000000000000000000000000000000000000000000000000017b7883c0691660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000155067fcd3058fdd81233890000000000000000000000000aaf5feaa9e5694b2b293e67558e2da8ea4b1fb13000000000000000000000000000000000000000000000000000000000000014000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000669602b30000da44"
    run_test(
        contract_compound_v3_mig_bundler_v2, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

