The *Bitcoin Dictionary* defines the vocabulary of Bitcoin and its ecosystem. I wrote it so that a reader who runs into an unfamiliar term, in an article, in a BIP, or in the interface of a piece of software, can find an accurate explanation that requires no prior knowledge, and can then follow it from definition to definition until everything makes sense.

This edition is the English translation of the *Dictionnaire de Bitcoin*, which I wrote in French. The content and the structure are the same.

# WHY THIS DICTIONARY

Bitcoin has its own vocabulary, and it grows with every improvement proposal, every piece of software, and every protocol built on top of it. Technical documents use these words without explaining them, while a beginner does not know them yet. This book gathers these terms in one place and gives each of them a complete definition that can be read without opening ten other pages first.

# CONTENTS OF THE BOOK

The book is made up of the following parts, in this order:
* The technical dictionary: the terms of Bitcoin and of the protocols built on it, in alphabetical order, each with a full definition;
* Companies, applications, and software: the companies, associations, software, wallets, hardware, and services that make up the ecosystem. The mechanisms they implement are defined in the technical dictionary;
* People: the historical figures of Bitcoin and of the cypherpunk movement, along with the main personalities of the ecosystem;
* Timeline: the major events of Bitcoin, of the cypherpunk movement, and of the cryptography that matters to Bitcoin, in the order in which they happened. Each date is cross-checked against at least 2 sources;
* BIPs, then BOLTs and bLIPs: the Bitcoin Improvement Proposals (BIPs) and the documents of the Lightning Network (BOLTs and bLIPs). Each entry gives a summary and a status, and the full definition follows the summary when there is one.

# READING GUIDE

Each entry of the technical dictionary follows the same format:
* Title: the term being defined;
* Category: the field it belongs to (Cryptography, Network, Wallet, etc.), with its pictogram;
* Definition: the explanation of the concept;
* See also: the terms related to this definition.

The first sentence of the definition says what the term is. The following paragraphs explain how it works, what it implies, and where it comes from, each one building on the previous. When needed, an italic note at the end of the entry points out synonyms or common confusions.

The entries of the other parts are read the same way. The entry for a person or a company begins with the role of the person or company it describes. The entry for a BIP, a BOLT, or a bLIP gives its identifier, its status, its original title, and its summary. A timeline event has a date, a short title, and a short text.

To read efficiently, follow the “See also” terms: they link the concepts to one another, and you move from definition to definition.

# WRITING PRINCIPLES

Publishing a dictionary means choosing the terms it contains. I include a term as soon as it has a link with Bitcoin or its ecosystem, because the ambition of this book is to cover the vocabulary of Bitcoin as exhaustively as possible, in the spirit of the professional dictionaries of other disciplines. In practice, the question is this: “*Could a beginner studying Bitcoin come across this term during their research and want to understand what it means?*”

If the answer is yes, the term goes in, whether it is a technical notion, a piece of software, an algorithm, or a protocol related to Bitcoin, directly or not, including the protocols built on top of it (Lightning, RGB, Liquid, Ark, etc.). More general terms from computer science or cryptography go in only if a reader can come across them and Bitcoin cannot be understood without them. The Nostr specifications (the NIPs) are not in the book, but the notions of Nostr are defined in the technical dictionary.

I set no length limit for the definitions. I prefer a long and accurate definition to a short and vague one. I check the facts at the source (BIPs, Bitcoin Core code, project documentation), and I date those that may change. The dictionary describes: it does not recommend any product.

For proper names, the line is the following:
* A person has their own entry when they are among the historical figures of Bitcoin or of the cypherpunk movement (Satoshi Nakamoto, Hal Finney, or Wei Dai, for example), or among the main personalities of the ecosystem. The others are mentioned, when useful, in the definition of their contribution;
* An organization (company, brand, project, association) has its own entry when I consider it major, and the same rule applies to software and hardware. The ecosystem is hard to carve up, since concepts are carried by software, which is itself tied to entities, and knowing these entities helps in understanding the whole;
* The timeline is limited to major events. An event whose date could not be cross-checked against 2 sources is left out.

# CONTRIBUTING

The *Bitcoin Dictionary* is an open project. You can suggest:
* a new term, with or without a definition;
* the correction of a definition that seems wrong or imprecise to you;
* the correction of a spelling mistake or a typo;
* any other change.

To do so, open a pull request or an issue on the project's GitHub repository (https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/). The repository's README file details the procedure, and the editorial charter sets the writing conventions. Contributors are credited in the book under their GitHub username unless they ask otherwise.

The text is published under the CC BY-NC-SA 4.0 license. The repository holds the most recent version of the work.

# DISCLAIMER

This dictionary is purely informative and educational. The information it contains is in no way financial, legal, or investment advice, and I accept no responsibility for how it might be used.

Bitcoin moves fast, and despite the care taken in writing, some information may become outdated. Check it against official sources and technical documentation, and consult the most recent online version.
