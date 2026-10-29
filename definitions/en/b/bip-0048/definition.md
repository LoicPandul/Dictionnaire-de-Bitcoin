Proposal defining the derivation path for multisignature wallets that support several script types:

```
m/48'/coin_type'/account'/script_type'
```

The `script_type'` level distinguishes the address format used: `1'` for P2SH-P2WSH and `2'` for native P2WSH. This structure lets the same hardware wallet manage several multisig configurations with different script formats while keeping a clear separation between them. BIP-0048 is widely adopted across the software and hardware ecosystem. It is currently the de facto standard for key derivation in multisignature wallets.
