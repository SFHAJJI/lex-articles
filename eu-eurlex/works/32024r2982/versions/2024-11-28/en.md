---
lex_id: 'eu-eurlex:32024r2982:2024-11-28'
title: 'Commission Implementing Regulation (EU) 2024/2982 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014'
valid_from: '2024-11-28'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2982'
source_sha256: '6dcd6d801df70c72976faf396166d82990cd6b3b152a10828be5eda3e7b8c213'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

This Regulation lays down rules on the protocols and interfaces of wallet solutions for:

| (1) | the issuance of person identification data and electronic attestations of attributes to wallet units; |
| --- | --- |

| (2) | the presentation of attributes of person identification data and electronic attestations of attributes, to wallet-relying parties and other wallet units; |
| --- | --- |

| (3) | the communication of data erasure requests to wallet-relying parties; |
| --- | --- |

| (4) | the reporting of wallet-relying parties to supervisory authorities established under Article 51 of Regulation (EU) 2016/679;to be updated on a regular basis to keep in line with technology and standards developments and with the work carried out on the basis of Recommendation (EU) 2021/946, and in particular the Architecture and Reference Framework. |
| --- | --- |

<a id="art_2"></a>

### art_2

Article 2

For the purpose of this Regulation, the following definitions apply:

| (1) | ‘wallet-relying party’ means a relying party that intends to rely upon wallet units for the provision of public or private services by means of digital interaction; |
| --- | --- |

| (2) | ‘wallet user’ means a user who is in control of the wallet unit; |
| --- | --- |

| (3) | ‘wallet solution’ means a combination of software, hardware, services, settings, and configurations, including wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic devices; |
| --- | --- |

| (4) | ‘wallet unit’ means a unique configuration of a wallet solution that includes wallet instances, wallet secure cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual wallet user; |
| --- | --- |

| (5) | ‘wallet provider’ means a natural or legal person who provides wallet solutions; |
| --- | --- |

| (6) | ‘wallet instance’ means the application installed and configured on a wallet user’s device or environment, which is part of a wallet unit, and that the wallet user uses to interact with the wallet unit; |
| --- | --- |

| (7) | ‘wallet secure cryptographic application’ means an application that manages critical assets by being linked to and using the cryptographic and non-cryptographic functions provided by the wallet secure cryptographic device; |
| --- | --- |

| (8) | ‘wallet secure cryptographic device’ means a tamper-resistant device that provides an environment that is linked to and used by the wallet secure cryptographic application to protect critical assets and provide cryptographic functions for the secure execution of critical operations; |
| --- | --- |

| (9) | ‘critical assets’ means assets within or in relation to a wallet unit of such extraordinary importance that where their availability, confidentiality or integrity are compromised, this would have a very serious, debilitating effect on the ability to rely on the wallet unit; |
| --- | --- |

| (10) | ‘wallet-relying party access certificate’ means a certificate for electronic seals or signatures authenticating and validating the wallet-relying party issued by a provider of wallet-relying party access certificates; |
| --- | --- |

| (11) | ‘provider of wallet-relying party access certificates’ means a natural or legal person mandated by a Member State to issue relying party access certificates to wallet-relying parties registered in that Member State; |
| --- | --- |

| (12) | ‘wallet unit attestation’ means a data object that describes the components of the wallet unit or allows authentication and validation of those components; |
| --- | --- |

| (13) | ‘embedded disclosure policy’ means a set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes; |
| --- | --- |

| (14) | ‘wallet-relying party registration certificate’ means a data object that indicates the attributes the relying party has registered to intend to request from users; |
| --- | --- |

| (15) | ‘provider of person identification data’ means a natural or legal person responsible for issuing and revoking the person identification data and ensuring that the person identification data of a user is cryptographically bound to a wallet unit; |
| --- | --- |

| (16) | ‘cryptographic binding’ means the method to link person identification data or electronic attestations of attributes to wallet units through cryptographic means. |
| --- | --- |

<a id="art_3"></a>

### art_3

Article 3

Regarding the protocols and interfaces referred to in Articles 4 and 5, wallet providers shall ensure that wallet units:

| (1) | authenticate and validate the wallet-relying party access certificates where interacting with wallet-relying parties; |
| --- | --- |

| (2) | authenticate and validate the wallet unit attestations of other wallet units where interacting with other wallet units; |
| --- | --- |

| (3) | authenticate and validate requests made using wallet-relying party access certificates or wallet unit attestations from other wallet units, where applicable; |
| --- | --- |

| (4) | authenticate and validate the wallet-relying party registration certificate, where applicable; |
| --- | --- |

| (5) | display to wallet users information contained in the wallet-relying party access certificates or in the wallet unit attestations; |
| --- | --- |

| (6) | display to wallet users, where applicable, the attributes that wallet users are requested to present; |
| --- | --- |

| (7) | display to wallet users, where applicable, information contained in the wallet-relying party registration certificate; |
| --- | --- |

| (8) | present wallet unit attestations of the wallet unit to wallet-relying parties or wallet units that request it; |
| --- | --- |

| (9) | do not present any requested attributes to wallet-relying parties or wallet units until the following requirements are met:(a)verify the wallet secure cryptographic application has authenticated the identity of the wallet user;(b)verify embedded disclosure policies have been processed within the wallet unit in accordance with Article 11 of Implementing Regulation (EU) 2024/2979, where applicable;(c)verify wallet users have partially or in full approved the presentation. |
| --- | --- |
| (a) | verify the wallet secure cryptographic application has authenticated the identity of the wallet user; |
| (b) | verify embedded disclosure policies have been processed within the wallet unit in accordance with Article 11 of Implementing Regulation (EU) 2024/2979, where applicable; |
| (c) | verify wallet users have partially or in full approved the presentation. |

| (10) | enable privacy preserving techniques which ensure unlinkability where the electronic attestations of attributes do not require the identification of the wallet user, when presenting attestations or person identification data across different wallet-relying parties. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

1. Wallet providers shall ensure that wallet solutions support protocols and interfaces for the issuance of person identification data and electronic attestations of attributes to wallet units.

2. Wallet providers shall ensure that wallet units request issuance of person identification data and electronic attestations of attributes only from parties having an authentic and valid wallet-relying party access certificate attesting them as:

| (a) | a provider of person identification data; |
| --- | --- |

| (b) | a provider of a qualified electronic attestation of attributes; |
| --- | --- |

| (c) | a provider of an electronic attestation of attributes issued by or on behalf of a public sector body responsible for an authentic source; or |
| --- | --- |

| (d) | a provider of non-qualified electronic attestations of attributes. |
| --- | --- |

3. In relation to the issuance of person identification data and electronic attestations of attributes to a wallet unit, wallet providers shall ensure that the following requirements are complied with:

| (a) | where wallet users use their wallet unit to request the issuance of person identification data or of electronic attestations of attributes from providers of person identification data or providers of electronic attestations of attributes that enable issuance of person identification data or electronic attestations in more than one format, the wallet unit shall request it in all formats referred to in Article 8 of Implementing Regulation (EU) 2024/2979 laying down rules for the application of Regulation (EU) No 910/2014 as regards the integrity and core functionalities of European Digital Identity Wallets; |
| --- | --- |

| (b) | where wallet users use their wallet unit to interact with providers of person identification data or electronic attestations of attributes, wallet units shall enable authentication and validation of the wallet unit components by presenting the wallet unit attestations to those providers upon their request; |
| --- | --- |

| (c) | wallet solutions shall support mechanisms that enable providers of person identification data to verify issuance, delivery and activation in compliance with assurance level high requirements set out in Commission Implementing Regulation (EU) 2015/1502 (11); |
| --- | --- |

| (d) | wallet units shall verify the authenticity and validity of person identification data and electronic attestations of attributes. |
| --- | --- |

<a id="art_5"></a>

### art_5

Article 5

1. Wallet providers shall ensure that wallet solutions support protocols and interfaces for the presentation of attributes to wallet-relying parties, remotely, and where appropriate in proximity, in accordance with the standards set out in the Annex.

2. Wallet providers shall ensure that, at the request of users, wallet units respond to successfully authenticated and validated requests from wallet-relying parties referred to in Article 3, in accordance with the standards set out in the Annex.

3. Wallet providers shall ensure that wallet units support proving the possession of private keys corresponding to public keys used in cryptographic bindings.

4. Wallet providers shall ensure that wallet solutions support the selective disclosure of attributes of personal identification data and of electronic attestations of attributes.

5. Paragraphs 1 to 4 shall apply mutatis mutandis to interactions between two wallet units in proximity.

<a id="art_6"></a>

### art_6

Article 6

1. Wallet providers shall ensure that wallet units support protocols and interfaces allowing wallet users to request from wallet-relying parties, with whom they have interacted through those wallet units, the erasure of their personal data provided through those wallet units, in accordance with Article 17 of Regulation (EU) 2016/679.

2. The protocols and interfaces referred to in paragraph 1 shall allow wallet users to select the wallet-relying parties to which data erasure requests are to be submitted.

3. Wallet units shall display to the wallet user previously submitted data erasure requests made through those wallet units.

<a id="art_7"></a>

### art_7

Article 7

1. Wallet providers shall ensure that wallet units allow wallet users to easily report wallet-relying parties to supervisory authorities established under Article 51 of Regulation (EU) 2016/679.

2. Wallet providers shall implement the protocols and interfaces for reporting wallet-relying parties in compliance with national procedural laws of the Member States.

3. Wallet providers shall ensure that wallet units allow wallet users to substantiate the reports, including by attaching relevant information to identify the wallet-relying parties, and the wallet users’ claims in machine-readable format.

<a id="art_8"></a>

### art_8

Article 8

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
