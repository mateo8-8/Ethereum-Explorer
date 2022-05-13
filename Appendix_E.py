from eth_keys import keys
from eth_utils import decode_hex
from eth_typing import Address
from eth import constants
from eth.chains.base import MiningChain
from eth.consensus.pow import mine_pow_nonce
from eth.vm.forks.byzantium import ByzantiumVM
from eth.db.atomic import AtomicDB
 
 
 
GENESIS_PARAMS = {
   'difficulty': 100,
   'gas_limit': 3141592,
   # We set the timestamp, just to make this documented example reproducible.
   # In common usage, we remove the field to let py-evm choose a reasonable default.
   'timestamp': 1514764800,
}
 
SENDER_PRIVATE_KEY = keys.PrivateKey(
   decode_hex('0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8')
)
SENDER = Address(SENDER_PRIVATE_KEY.public_key.to_canonical_address())
 
RECEIVER = Address(b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x02')
 
klass = MiningChain.configure(
   __name__='TestChain',
   vm_configuration=(
       (constants.GENESIS_BLOCK_NUMBER, ByzantiumVM),
   ))
 
chain = klass.from_genesis(AtomicDB(), GENESIS_PARAMS)
genesis = chain.get_canonical_block_header_by_number(0)
vm = chain.get_vm()
 
 
#print("***************************************************************************************")
#print("*************************** Welcome to the py-evm logger ******************************")
#print("***************************************************************************************")
#print("Part 1")
#print("***************************************************************************************")
#print("We just created the chain, here it is: ", chain)
#print("We just created the mining chain object klass, here it is: ", klass)
#print("We just created the genesis block, here it is", genesis)
#print("We just created the VM, here it is: ", vm)
 
 
 
 
 
#this is the nonce from the sender, this if the nonce does not increase, then the transaction will be considered queued, if the nonce increases, then the transaction will be pending.  This is not the same nonce as the transaction nonce, this nonce is tied to the account to track transactions.
nonce = vm.state.get_nonce(SENDER)
 
 
tx = vm.create_unsigned_transaction(
   nonce=nonce,
   gas_price=0,
   gas=100000,
   to=RECEIVER,
   value=0,
   data=b'',
)
 
signed_tx = tx.as_signed_transaction(SENDER_PRIVATE_KEY)
 
#print("***************************************************************************************")
#print("***************************************************************************************")
#print("***************************************************************************************")
#print("Part 2")
#print("***************************************************************************************")
#print("This is the the SENDER variable", SENDER)
#print("This is the result of the Address object for the receiver: ", RECEIVER)
##print("This is the sender's private key, this is it decoded", SENDER_PRIVATE_KEY)
#print("this is the unsigned transaction", tx)
#print("This is the user's nonce:  ",nonce)
#print("this is the signed transaction", signed_tx)
 
 
 
 
chain.apply_transaction(signed_tx)
 
 
# Normally, we can let the timestamp be chosen automatically, but
# for the sake of reproducing exactly the same block every time,
# we will set it manually here:
chain.set_header_timestamp(genesis.timestamp + 1)
 
# We have to finalize the block first in order to be able read the
# attributes that are important for the PoW algorithm
block_result = chain.get_vm().finalize_block(chain.get_block())
block = block_result.block
 
 
q = type(block_result)
w = type(block)
 
 
# based on mining_hash, block number and difficulty we can perform
# the actual Proof of Work (PoW) mechanism to mine the correct
# nonce and mix_hash for this block
nonce, mix_hash = mine_pow_nonce(
   block.number,
   block.header.mining_hash,
   block.header.difficulty
)
#print("***************************************************************************************")
#print("***************************************************************************************")
#print("***************************************************************************************")
#print("Part 3")
#print("***************************************************************************************")
#print("This is the block type result we got: ", q)
#print("This is the block type we got", w)
#print("This is the nonce value from the mine_pow_nonce method: ", nonce)
#print("This is the mix_hash value from the mine_pow_nonce method: ", mix_hash)
 
chain.mine_block(mix_hash=mix_hash, nonce=nonce)
 
#print("***************************************************************************************")
#print("***************************************************************************************")
#print("***************************************************************************************")
#print("Part 4")
#print("***************************************************************************************")
#print("We are mining the block now")
#print(block.number)
