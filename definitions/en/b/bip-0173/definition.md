Introduces the bech32 address format for SegWit v0 addresses. This address format is characterized by the prefix `bc1q`. The bech32 format offers several advantages:
* It takes less space in QR codes;
* It is easier for humans to read;
* It has a checksum that detects any error affecting at most 4 characters (the BIP advises against automatically correcting typos and recommends at best indicating where the error is).
These characteristics make receiving addresses easier to use while minimizing the risk of errors.
