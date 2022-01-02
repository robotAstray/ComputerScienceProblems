import argparse

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleaotide in gene.upper():
            self.bit_string <<=2
            if nucleaotide == "A":
                self.bit_string |= 0b00
            elif nucleaotide == "C":
                self.bit_string |= 0b01
            elif nucleaotide == "G":
                self.bit_string |= 0b10
            elif nucleaotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotise:{}".format(nucleaotide))
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits: int = self.bit_string >> i & 0b11 
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()

def main():
    from sys import getsizeof
    import argparse
    parser = argparse.ArgumentParser(description="Command Line Gene Compression and Decompression")
    parser.add_argument('--c', type=str,
				help='Combination of A C G T ')
    args = parser.parse_args()
    compressGene = args.c
    if args.c != "":
        compressGene = args.c
        original: str = compressGene
        print("original is {} ytes".format(getsizeof(original)))
        compressed: CompressedGene = CompressedGene(original)
        print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
        print(compressed)
        print("original and decompressed are the same:{}".format(original) == compressed.decompress())

if __name__ == "__main__":
        main()



