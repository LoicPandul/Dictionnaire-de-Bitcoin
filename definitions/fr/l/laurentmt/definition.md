Développeur travaillant sur la confidentialité des transactions Bitcoin, connu sous le pseudonyme LaurentMT, auteur de la mesure d'entropie des transactions.

Le 21 septembre 2015, il publie sur GitHub, en trois gists, la série « Bitcoin Transactions & Privacy ». Il y définit l'entropie d'une transaction comme le logarithme en base 2 du nombre d'associations possibles entre ses entrées et ses sorties : une transaction simple, dont les liens sont certains, a une entropie nulle, et un *coinjoin* de base atteint environ 1,585. Plus l'entropie est élevée, plus il est difficile de dire quelle entrée a financé quelle sortie.

Le 17 septembre 2016, le dépôt Boltzmann est créé sous l'organisation GitHub de Samourai Wallet. Ce script Python calcule l'entropie d'une transaction et le degré de liaison entre ses entrées et ses sorties ; LaurentMT en est le premier contributeur, avec 37 commits, devant SamouraiDev. Le dépôt est ensuite déplacé sur le serveur de code de Samourai (code.samourai.io).
