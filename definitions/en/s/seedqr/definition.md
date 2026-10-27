Format for representing a mnemonic phrase as a QR code. Developed by the SeedSigner project, SeedQR encodes each word of the BIP-0039 mnemonic phrase by its index in the word list (a four-digit position, padded with zeros), then concatenates these indexes into a single numeric string. The numeric mode of QR codes makes the result compact.

A variant called Compact SeedQR directly encodes the binary entropy of the phrase (128 bits for 12 words, 256 bits for 24 words), which reduces the size of the QR code by 35 to 40%. The format is adopted by several signing devices, such as SeedSigner, Coldcard Q, and Blockstream Jade.

SeedQR offers an alternative to the classic word-by-word transcription: the phrase can be backed up on a physical medium (metal, paper) as a QR code, then scanned directly by the signing device to import it without manual entry.
