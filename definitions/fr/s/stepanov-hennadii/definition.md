Développeur de Bitcoin Core, connu sous le pseudonyme hebasto sur GitHub, et l'un de ses mainteneurs. Sa première contribution dans l'historique du logiciel date du 2 août 2018 : une correction de l'aide de l'option `-prune`.

Le 19 avril 2021, la PR 21615 ajoute sa clé de signature à la liste des clés de confiance de Bitcoin Core, utilisée pour vérifier les commits fusionnés. Dans la description de la PR, il écrit que sa responsabilité devrait se limiter au dépôt de l'interface graphique, bitcoin-core/gui. Il y fusionne des PR, encore en août 2026, mais fusionne aussi des PR du dépôt principal (compilation, intégration continue). Le dictionnaire le compte parmi les cinq mainteneurs de Bitcoin Core en mars 2026.

Le 16 juillet 2024, il ouvre la PR 30454, « Introduce CMake-based build system », qui ajoute à Bitcoin Core un système de compilation fondé sur CMake. Elle est fusionnée le 28 août 2024, après 68 commits. Les notes de version de Bitcoin Core 29.0, publié le 14 avril 2025, indiquent que le système de compilation est passé d'Autotools à CMake. Cette migration change la façon dont chacun compile le logiciel, y compris pour les compilations reproductibles de Guix, qu'il a adaptées dans la même PR.

Son travail touche aussi Bitcoin-Qt, l'interface graphique de Bitcoin Core, et l'infrastructure d'intégration continue du dépôt.
