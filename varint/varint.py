"""
Dev notes:
- potentially useful Python functions: hex() and bin()
- TODO rename class to e.g. "VarintEncoder"
"""

from sys import byteorder
from typing import Tuple, Int
class Solution:
    
    BYTEORDER = byteorder
    NUM_BITS_IN_BYTE = 7
    
    def __init__(self):
        pass

    def encode(self, unsigned64bitInteger: int) -> int:
        """
        Encodes varint sequence from unsigned 64 bit integer.
        
        param: unsigned 64 bit integer
        return: sequence of bytes in the varint encoding used by Protocol Buffers
        """
        pass
        
        # steps:
        # - 150 -> binary using bin()
        # TODO rename to_bin_digits as e.g. 'bin_digits_as_str'
        to_bin_digits: str = bin(unsigned64bitInteger)[2:]
        leading_1_bit_index: int = to_bin_digits.find('1')
        to_bin_digits: str = to_bin_digits[leading_1_bit_index:]
        # - split into 7-bit parts
        (_7_bit_num_parts, residue): Tuple[Int, Int] = divmod(len(to_bin_digits), Solution.NUM_BITS_IN_BYTE)
        for k in range(len(to_bin_digits), residue, ):
            # TODO
        # [to_bin_digits[i:i+Solution.NUM_BITS_IN_BYTE] for i in range(len(to_bin_digits), 0, Solution.NUM_BITS_IN_BYTE)]
        
        

        # - put into little/big-endian order, depending system's byte order (local sys is 'little')


        # - add continuation bits
        # - convert to `bytes` 
        # - return

    def decode(self) -> int:
        """
        arg: sequence of bytes in the varint encoding used by Protocol Buffers
        returrns: unsigned 64 bit integer
        """
        pass

def main():
    pass
    # assert encode(150) == b'\x96\x01'
    # assert decode(b'\x96\x01') == 150

if __name__ == "__main__":
    main()
