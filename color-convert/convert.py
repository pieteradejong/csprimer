"""
Dev notes:
- potentially useful Python functions: hex() and bin()
- TODO rename class to e.g. "VarintEncoder"
"""
class Util:
    hex_to_bin = {
        '0': b'0000',
        '1': b'0001',
        '2': b'0010',
        '3': b'0011',
        '4': b'0100',
        '5': b'0101',
        '6': b'0110',
        '7': b'0111',
        '8': b'1000',
        '9': b'1001',
        'A': b'1010',
        'B': b'1011',
        'C': b'1100',
        'D': b'1101',
        'E': b'1110',
        'F': b'1111'  
    }
    
    # uncomment if if needed:
    # bin_to_hex = { v: k for k, v in hex_to_bin.items()}

from string import hexdigits

class Solution:
    def __init__(self):
        pass

    def is_valid_hex(self, colorAsHexCandidate: str) -> bool:
        """Valid formats: '#ABCDEF' or '0xABCDEF' or 'ABCDEF'."""
        if not 6 <= len(colorAsHexCandidate) <= 8: 
            return False
        if len(colorAsHexCandidate) == 7 and colorAsHexCandidate[0] != '#':
            return False
        if len(colorAsHexCandidate) == 8 and colorAsHexCandidate[:2] != '0x':
            return False
        if len(colorAsHexCandidate) == 6 and any(c not in hexdigits for c in colorAsHexCandidate):
            return False
        
        return True

    def hex_to_rgb(self, colorAsHex: str) -> str:
        # v1: support only '#nnnnnn' as input. Add input validaiton later.
        if not self.is_valid_hex(colorAsHex):
            raise ValueError(f"Invalid hex color: [{colorAsHex}]")


        red_as_hex, green_as_hex, blue_as_hex = colorAsHex[1:3], colorAsHex[3:5], colorAsHex[5:7]
        
        red_as_bin_str = Util.hex_to_bin[red_as_hex[0]] + Util.hex_to_bin[red_as_hex[1]]
        green_as_bin_str = Util.hex_to_bin[green_as_hex[0]] + Util.hex_to_bin[green_as_hex[1]]
        blue_as_bin_str = Util.hex_to_bin[blue_as_hex[0]] + Util.hex_to_bin[blue_as_hex[1]]
        
        _sum_red_as_decimal = 0
        for i in range(len(red_as_bin_str), 0, -1):
            _sum_red_as_decimal += pow(2, len(red_as_bin_str)-1-i)
        
        _sum_green_as_decimal = 0
        for i in range(len(green_as_bin_str), 0, -1):
            _sum_green_as_decimal += pow(2, len(green_as_bin_str)-1-i)

        _sum_blue_as_decimal = 0
        for i in range(len(blue_as_bin_str), 0, -1):
            _sum_blue_as_decimal += pow(2, len(blue_as_bin_str)-1-i)

        return f'rgb({_sum_red_as_decimal}, {_sum_green_as_decimal}, {_sum_blue_as_decimal})'



# assert hex_to_rgb('#00ff00') == 'rgb(0, 255, 0)'