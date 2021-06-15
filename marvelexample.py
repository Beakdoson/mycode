import time
import hashlib
import argparse

parseitup= argparse.ArgumentParser(description="Demo argparse and time")

names= ["Chad", "Chadwick", "Chadford", "Chadicus Maximus"]
# teach parseitup what args there are!

parseitup.add_argument("coolguy", choices=names, help="A real cool guy.")

demargstho= parseitup.parse_args()

x= f"{demargstho.coolguy}, the current epoch time in seconds is {time.time()}"

hashlib.md5((x).encode('utf-8')).hexigest())
