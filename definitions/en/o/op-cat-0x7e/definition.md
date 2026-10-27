Concatenates the top two items of the stack (that is, joins them end to end). This opcode is disabled in Bitcoin: a script that contains it is invalid, so it cannot be used. However, BIP-0347 proposes adding it to Tapscript to allow items on the stack to be combined, which would improve the expressiveness of the language. This one additional tool could enable:
* The use of Lamport signatures, which are in principle resistant to quantum attacks;
* The creation of vaults;
* The use of covenants;
* Or the use of non-equivocation contracts.
