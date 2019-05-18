#quick and dirth ELF entrypoint patcher
import sys
import binascii

# usage: ep_patcher.py -filename -new_entrypoint
patch_file_input = sys.argv[1]
new_ep = sys.argv[2]
new_ep = binascii.unhexlify(new_ep)

with open(patch_file_input, 'rb+') as f:
    f.seek(24)
    f.write(new_ep)
