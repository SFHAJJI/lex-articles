---
lex_id: 'eu-eurlex:32024r2979:2024-11-28'
title: 'Commission Implementing Regulation (EU) 2024/2979 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014'
valid_from: '2024-11-28'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2979'
source_sha256: 'ac7e5fff2a72a3bb4ad6fa442745e59ee59ad3e65dc578f6acdd6575040b8b5a'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

This Regulation lays down rules for the integrity and core functionalities of the wallets, to be updated on a regular basis to keep in line with technology and standards developments and with the work carried out on the basis of Recommendation (EU) 2021/946, and in particular the Architecture and Reference Framework.

<a id="art_2"></a>

### art_2

Article 2

For the purpose of this Regulation, the following definitions apply:

| (1) | ‘wallet secure cryptographic application’ means an application that manages critical assets by being linked to and using the cryptographic and non-cryptographic functions provided by the wallet secure cryptographic device; |
| --- | --- |

| (2) | ‘wallet unit’ means a unique configuration of a wallet solution that includes wallet instances, wallet secure cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual wallet user; |
| --- | --- |

| (3) | ‘critical assets’ means assets within or in relation to a wallet unit of such extraordinary importance that where their availability, confidentiality or integrity are compromised, this would have a very serious, debilitating effect on the ability to rely on the wallet unit; |
| --- | --- |

| (4) | ‘provider of person identification data’ means a natural or legal person responsible for issuing and revoking the person identification data and ensuring that the person identification data of a user is cryptographically bound to a wallet unit; |
| --- | --- |

| (5) | ‘wallet user’ means a user who is in control of the wallet unit; |
| --- | --- |

| (6) | ‘wallet-relying party’ means a relying party that intends to rely upon wallet units for the provision of public or private services by means of digital interaction; |
| --- | --- |

| (7) | ‘wallet provider’ means a natural or legal person who provides wallet solutions; |
| --- | --- |

| (8) | ‘wallet unit attestation’ means a data object that describes the components of the wallet unit or allows authentication and validation of those components; |
| --- | --- |

| (9) | ‘embedded disclosure policy’ means a set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes; |
| --- | --- |

| (10) | ‘wallet instance’ means the application installed and configured on a wallet user’s device or environment, which is part of a wallet unit, and that the wallet user uses to interact with the wallet unit; |
| --- | --- |

| (11) | ‘wallet solution’ means a combination of software, hardware, services, settings, and configurations, including wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic devices; |
| --- | --- |

| (12) | ‘wallet secure cryptographic device’ means a tamper-resistant device that provides an environment that is linked to and used by the wallet secure cryptographic application to protect critical assets and provide cryptographic functions for the secure execution of critical operations; |
| --- | --- |

| (13) | ‘wallet cryptographic operation’ means a cryptographic mechanism necessary in the context of authentication of the wallet user and the issuance or presentation of person identification data or electronic attestations of attributes; |
| --- | --- |

| (14) | ‘wallet-relying party access certificate’ means a certificate for electronic seals or signatures authenticating and validating the wallet-relying party issued by a provider of wallet-relying party access certificates; |
| --- | --- |

| (15) | ‘provider of wallet-relying party access certificates’ means a natural or legal person mandated by a Member State to issue relying party access certificates to wallet-relying parties registered in that Member State. |
| --- | --- |

<a id="art_3"></a>

### art_3

Article 3

1. Wallet units shall not perform any functionality listed in Article 5a(4) of Regulation (EU) No 910/2014, except wallet user authentication to access the wallet unit, until the wallet unit has successfully authenticated the wallet user.

2. Wallet providers shall, for each wallet unit, sign or seal, at least one wallet unit attestation compliant with the requirements laid down in Article 6. The certificate used to sign or seal the wallet unit attestation shall be issued under a certificate listed in the trusted list referred to in Implementing Regulation (EU) 2024/2980.

<a id="art_4"></a>

### art_4

Article 4

1. Wallet instances shall use at least one wallet secure cryptographic device to manage critical assets.

2. Wallet providers shall ensure integrity, authenticity and confidentiality of the communication between wallet instances and wallet secure cryptographic applications.

3. Where critical assets relate to performing electronic identification at assurance level high, the wallet cryptographic operations or other operations processing critical assets shall be performed in accordance with the requirements for the characteristics and design of electronic identification means at assurance level high, as set out in Commission Implementing Regulation (EU) 2015/1502 (11).

<a id="art_5"></a>

### art_5

Article 5

1. Wallet providers shall ensure that wallet secure cryptographic applications:

| (a) | perform wallet cryptographic operations involving critical assets other than those needed for the wallet unit to authenticate the wallet user only in cases where those applications have successfully authenticated wallet users; |
| --- | --- |

| (b) | where they authenticate wallet users in the context of performing electronic identification at assurance level high; perform authentication of wallet users, in accordance with, the requirements for the characteristics and design of electronic identification means at assurance level high, as set out in Implementing Regulation (EU) 2015/1502; |
| --- | --- |

| (c) | are able to securely generate new cryptographic keys; |
| --- | --- |

| (d) | are able to perform secure erasure of critical assets; |
| --- | --- |

| (e) | are able to generate a proof of possession of private keys; |
| --- | --- |

| (f) | protect the private keys generated by those wallet secure cryptographic applications during the existence of the keys; |
| --- | --- |

| (g) | comply with the requirements for the characteristics and design of electronic identification means at assurance level high, as set out in Implementing Regulation (EU) 2015/1502; |
| --- | --- |

| (h) | are the only components able to execute wallet cryptographic operations and any other operation with critical assets in the context of performing electronic identification at assurance level high. |
| --- | --- |

2. Where wallet providers decide to provide a wallet secure cryptographic application to an embedded secure element these wallet providers shall base their technical solution on the technical specifications listed in Annex I or on other equivalent technical specifications.

<a id="art_6"></a>

### art_6

Article 6

1. Wallet providers shall ensure that each wallet unit contains wallet unit attestations.

2. Wallet providers shall ensure that the wallet unit attestations referred to in paragraph 1 contain public keys and that the corresponding private keys are protected by a wallet secure cryptographic device.

3. Wallet providers shall:

| (a) | inform wallet users of their rights and obligations in relation to their wallet unit; |
| --- | --- |

| (b) | provide mechanisms, independent of wallet units, for the secure identification and authentication of wallet users; |
| --- | --- |

| (c) | ensure wallet users have the right to request revocation of their wallet unit attestations, using the authentication mechanisms referred to in point (b). |
| --- | --- |

<a id="art_7"></a>

### art_7

Article 7

1. Wallet providers shall be the only entities capable of revoking wallet unit attestations for wallet units that they have provided.

2. Wallet providers shall establish a publicly available policy specifying the conditions and the timeframe for the revocation of wallet unit attestations.

3. Where wallet providers have revoked wallet unit attestations, they shall inform affected wallet users within 24 hours of the revocation of their wallet units, including the reason for the revocation and the consequences for the wallet user. This information shall be provided in a manner that is concise, easily accessible and using clear and plain language.

4. Where wallet providers have revoked wallet unit attestations, they shall make publicly available the validity status of the wallet unit attestation in a privacy preserving manner and describe the location of that information in the wallet unit attestation.

<a id="art_8"></a>

### art_8

Article 8

Wallet providers shall ensure that wallet solutions support the usage of person identification data and electronic attestations of attributes issued in compliance with the list of standards set out in Annex II.

<a id="art_9"></a>

### art_9

Article 9

1. Irrespective of whether or not a transaction is successfully completed, wallet instances shall log all transactions with wallet-relying parties and other wallet units, including electronic signing and sealing.

2. The logged information shall at least contain:

| (a) | the time and date of the transaction; |
| --- | --- |

| (b) | the name, contact details, and the unique identifier of the corresponding wallet-relying party and the Member State in which that wallet-relying party is established, or in case of other wallet units, relevant information from the wallet unit attestation; |
| --- | --- |

| (c) | the type or types of data requested and presented in the transaction; |
| --- | --- |

| (d) | in the case of non-completed transactions, the reason for such non-completion. |
| --- | --- |

3. Wallet providers shall ensure integrity, authenticity and confidentiality of the logged information.

4. Wallet instances shall log reports sent by the wallet user to the data protection authorities via their wallet unit.

5. The logs referred to in paragraphs 1 and 2 shall be accessible to the wallet provider, where it is necessary for the provision of wallet services, on the basis of explicit prior consent by the wallet user.

6. The logs referred to in paragraphs 1 and 2 shall remain accessible for as long as they are required by Union law or national law.

7. Wallet providers shall enable wallet users to export the logged information referred to in paragraph 2.

<a id="art_10"></a>

### art_10

Article 10

1. Wallet providers shall ensure that electronic attestations of attributes with common embedded disclosure policies set out in Annex III can be processed by the wallet units that they provide.

2. Wallet instances shall be able to process and present such embedded disclosure policies referred to in paragraph 1 in conjunction with data received from the requesting wallet-relying party.

3. Wallet instances shall verify whether the wallet-relying party complies with the requirements of the embedded disclosure policy and inform the wallet user of the result.

<a id="art_11"></a>

### art_11

Article 11

1. Wallet providers shall ensure that wallet users are able to receive, qualified certificates for qualified electronic signatures or seals which are linked to qualified signature or seal creation devices that are either local, external, or remote in relation to the wallet instances.

2. Wallet providers shall ensure that wallet solutions are able to securely interface with one of the following types of qualified signature or seal creation devices: local, external, or remotely managed qualified signature or seal creation devices for the purposes of using the qualified certificates referred to in paragraph 1.

3. Wallet providers shall ensure that wallet users who are natural persons have, at least for non-professional purposes, free-of-charge access to signature creation applications which allow the creation of free-of-charge qualified electronic signatures using the certificates referred to in paragraph 1.

<a id="art_12"></a>

### art_12

Article 12

1. The signature creation applications used by wallet units may be provided either by wallet providers, by providers of trust services or by wallet-relying parties.

2. Signature creation applications shall have the following functions:

| (a) | signing or sealing wallet user-provided data; |
| --- | --- |

| (b) | signing or sealing relying party-provided data; |
| --- | --- |

| (c) | creating signatures or seals in accordance with at least the mandatory formats referred to in Annex IV; |
| --- | --- |

| (d) | informing wallet users about the result of the signature or seal creation process. |
| --- | --- |

3. The signature creation applications may either be integrated into or be external to wallet instances. Where signature creation applications rely on remote qualified signature creation devices and where they are integrated into wallet instances, they shall support the application programming interface referred to in Annex IV.

<a id="art_13"></a>

### art_13

Article 13

Wallet units shall, where technically feasible and excepting cases of critical assets, support secure export and portability of personal data of the wallet user, to allow the wallet user to migrate to a wallet unit of a different wallet solution in a way that ensures level of assurance high as set out in Implementing Regulation (EU) 2015/1502.

<a id="art_14"></a>

### art_14

Article 14

1. Wallet units shall support the generation of pseudonyms for wallet users in compliance with the technical specifications set out in Annex V.

2. Wallet units shall support the generation, upon the request of a wallet-relying party, of a pseudonym which is specific and unique to that wallet-relying party and provide this pseudonym to the wallet-relying party, either standalone or in combination with any person identification data or electronic attribute attestation requested by that wallet-relying party.

<a id="art_15"></a>

### art_15

Article 15

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
