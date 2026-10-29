Bitcoin Improvement Proposal that defines a DNS-based resolution system for human-readable payment addresses. BIP-0353 associates an identifier in the format `user@domain.com` with Bitcoin payment instructions, storing this information in DNS TXT records secured by DNSSEC.

In practice, when a wallet receives an address such as `satoshi@example.com`, it performs a DNS query to:

```
satoshi.user._bitcoin-payment.example.com
```

This lets it retrieve a payment URI in BIP-0021 format. The URI can contain an on-chain address, a BOLT-12 offer, or instructions for Silent Payments, which makes the mechanism compatible with different payment protocols.

The main advantage is user experience: addresses become memorable and reusable, without sacrificing privacy, since the underlying protocols (BOLT-12, Silent Payments, etc.) generate unique addresses or invoices for each payment. BIP-0353 was proposed by Matt Corallo and Bastien Teinturier in 2024.
