#!/usr/bin/env python3

import math
import sys

# function: flip binary bits
def flip_bits(bits):
    output = []

    for c in bits:
        if c == '0':
            output.append('1')
        else:
            output.append('0')

    return ''.join(output)

# function: calculate binary sum
def sum_bits(bits_list):
    dec_output = 0

    for c in bits_list:
        dec_c = int('0b%s' %(c), base=2)
        dec_output += dec_c

    return str(bin(dec_output))[2:]

if __name__ == '__main__':
    input_digits = sys.argv[1]
    ceil = math.ceil(len(input_digits) / 16)

    if len(input_digits) <= 16:
        final_input_digits = input_digits.zfill(16)
        final_checksum = flip_bits(final_input_digits)

        print('Input Digits: %s' %(input_digits))
        print('Finalized Input Digits: %s' %(final_input_digits))
        print('Data Sum: %s' %(final_input_digits))
        print('Final Checksum: %s' %(final_checksum))
    else:
        final_full_length_input_digits = input_digits.zfill(ceil * 16)

        computes = []

        for i in range(ceil):
            computes.append(final_full_length_input_digits[i*16:(i+1)*16])

        data_sum = sum_bits(computes)
        initial_data_sum = data_sum

        # if the length of data sum is greater than 16, that means we need to wrap-around carry bits
        if len(data_sum) > 16:
            ceil_inner = math.ceil(len(data_sum) / 16)

            final_full_length_input_digits_inner = data_sum.zfill(ceil_inner * 16)
            computes_inner = []

            # assume we only need to do wrap-around once
            computes_inner.append(final_full_length_input_digits_inner[0:16])
            computes_inner.append(final_full_length_input_digits_inner[17:])

            data_sum = sum_bits(computes_inner).zfill(16)
        else:
            data_sum = data_sum.zfill(16)

        final_checksum = flip_bits(data_sum)

        print('Input Digits: %s' %(input_digits))
        print('Finalized Input Digits: %s' %(final_full_length_input_digits))
        print('Initial Data Sum: %s' %(initial_data_sum))
        print('Final Data Sum: %s' %(data_sum))
        print('Final Checksum: %s' %(final_checksum))
