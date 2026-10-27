Cryptographe, coautrice de FROST, un schéma de signature de Schnorr à seuil.

En 2020, elle est rattachée à l'université de Waterloo, au Canada, et à la Zcash Foundation. En octobre 2020, elle présente avec Ian Goldberg, à la conférence Selected Areas in Cryptography, « FROST: Flexible Round-Optimized Schnorr Threshold Signatures ». Une version étendue est publiée sur l'archive ePrint de l'IACR sous le numéro 2020/852, et les actes de la conférence paraissent chez Springer en 2021.

FROST répond à une question concrète : n participants se partagent une clé, et t d'entre eux, avec t inférieur ou égal à n, doivent suffire pour signer. Le schéma s'exécute en deux tours, ou en un seul tour grâce à une phase de précalcul. Le résultat est une signature de Schnorr ordinaire, que l'on vérifie avec la clé publique du groupe. Le `BIP-0340`, qui spécifie les signatures de Schnorr de Bitcoin, cite FROST parmi les schémas à seuil rendus possibles par ces signatures, sans que Komlo en soit autrice. Voir les entrées FROST, SCHNORR et TAPROOT.

En juin 2024, elle cosigne avec Deirdre Connolly, Ian Goldberg et Christopher A. Wood la RFC 9591, qui spécifie FROST dans sa version à deux tours pour plusieurs suites cryptographiques.
