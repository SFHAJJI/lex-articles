---
lex_id: 'eu-eurlex:32024r2977:2024-11-28'
title: 'Commission Implementing Regulation (EU) 2024/2977 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014'
valid_from: '2024-11-28'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2977'
source_sha256: 'e6823fd65f11dc56c803daac4e5e5fde5c6404b0fad6924f80bd54264bcb3e94'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

This Regulation lays down rules for the issuance of person identification data and electronic attestations of attributes to wallet units, to be updated on a regular basis to keep in line with technology and standards developments and with the work carried out on the basis of Recommendation (EU) 2021/946, and in particular the architecture and reference framework.

<a id="art_2"></a>

### art_2

Article 2

For the purpose of this Regulation, the following definitions apply:

| (1) | ‘wallet user’ means a user who is in control of the wallet unit; |
| --- | --- |

| (2) | ‘wallet unit’ means a unique configuration of a wallet solution that includes wallet instances, wallet secure cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual wallet user; |
| --- | --- |

| (3) | ‘wallet solution’ means a combination of software, hardware, services, settings, and configurations, including wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic devices; |
| --- | --- |

| (4) | ‘provider of person identification data’ means a natural or legal person responsible for issuing and revoking the person identification data and ensuring that the person identification data of a user is cryptographically bound to a wallet unit; |
| --- | --- |

| (5) | ‘wallet unit attestation’ means a data object that describes the components of the wallet unit or allows authentication and validation of those components; |
| --- | --- |

| (6) | ‘wallet instance’ means the application installed and configured on a wallet user’s device or environment, which is part of a wallet unit, and that the wallet user uses to interact with the wallet unit; |
| --- | --- |

| (7) | ‘wallet secure cryptographic application’ means an application that manages critical assets by being linked to and using the cryptographic and non-cryptographic functions provided by the wallet secure cryptographic device; |
| --- | --- |

| (8) | ‘wallet secure cryptographic device’ means a tamper-resistant device that provides an environment that is linked to and used by the wallet secure cryptographic application to protect critical assets and provide cryptographic functions for the secure execution of critical operations; |
| --- | --- |

| (9) | ‘wallet provider’ means a natural or legal person who provides wallet solutions; |
| --- | --- |

| (10) | ‘critical assets’ means assets within or in relation to a wallet unit of such extraordinary importance that where their availability, confidentiality or integrity are compromised, this would have a very serious, debilitating effect on the ability to rely on the wallet unit; |
| --- | --- |

| (11) | ‘wallet-relying party’ means a relying party that intends to rely upon wallet units for the provision of public or private services by means of digital interaction; |
| --- | --- |

| (12) | ‘wallet-relying party access certificate’ means a certificate for electronic seals or signatures authenticating and validating the wallet-relying party issued by a provider of wallet-relying party access certificates; |
| --- | --- |

| (13) | ‘provider of wallet-relying party access certificates’ means a natural or legal person mandated by a Member State to issue relying party access certificates to wallet-relying parties registered in that Member State. |
| --- | --- |

<a id="art_3"></a>

### art_3

Article 3

1. Providers of person identification data shall issue person identification data to wallet units in accordance with the electronic identification schemes under which wallet solutions are provided.

2. Providers of person identification data shall ensure that person identification data issued to wallet units contains the information necessary for authentication and validation of the person identification data.

3. Providers of person identification data shall ensure that person identification data issued to wallet units comply with the technical specifications set out in the Annex.

4. Member States shall ensure that the person identification data issued to a given wallet user is unique for the Member State.

5. Providers of person identification data shall ensure that person identification data that they issue is cryptographically bound to the wallet unit to which it is issued.

6. Member States shall make publicly available a list of wallet solutions that are supported by providers of person identification data that is part of electronic identification schemes of that Member State.

7. Member States shall enroll wallet users in accordance with the requirements relating to enrolment at assurance level high, as set out in Commission Implementing Regulation (EU) 2015/1502 (11). In the context of the enrolment process, providers of person identification data shall perform identity verification of the wallet user in accordance with the requirements related to identity proofing and verification before issuing the person identification data to the wallet unit of the corresponding wallet user.

8. When issuing person identification data to wallet units, providers of person identification data shall identify themselves to wallet units using their wallet-relying party access certificate or by using another authentication mechanism in accordance with an electronic identity scheme notified at assurance level high.

9. Before issuing person identification data to a wallet unit, providers of person identification data shall authenticate and validate the wallet unit attestation of the wallet unit and verify that the wallet unit belongs to a wallet solution the provider of person identification data accepts or use another authentication mechanism in accordance with an electronic identity scheme notified at assurance level high.

<a id="art_4"></a>

### art_4

Article 4

1. Electronic attestations of attributes issued to wallet units shall comply with at least one of the standards in the list set out in Annex I of Implementing Regulation (EU) 2024/2979.

2. Providers of electronic attestations of attributes shall identify themselves to wallet units using their wallet-relying party access certificate.

3. Providers of electronic attestations of attributes shall ensure that electronic attestations of attributes issued to wallet units contain the information necessary for authentication and validation of those electronic attestations of attributes.

<a id="art_5"></a>

### art_5

Article 5

1. Providers of person identification data issued to a wallet unit shall have written and publicly accessible policies relating to validity status management, including, where applicable, the conditions under which such person identification data can be revoked without delay.

2. Only providers of person identification data or electronic attestation of attributes can revoke the person identification data or electronic attestations of attributes issued by them.

3. Where providers of person identification data have revoked person identification data, they shall, through dedicated and secure channels, inform wallet users subject of those person identification data within 24 hours of the revocation and of the reasons for the revocation. This shall be done in a manner that is concise, easily accessible and using clear and plain language.

4. Where providers of person identification data revoke person identification data issued to wallet units, they shall do so in each of the following circumstances:

| (a) | upon the explicit request of the wallet user to whose wallet unit the person identification data or electronic attestation of attributes were issued to; |
| --- | --- |

| (b) | where the wallet unit attestation to which the person identification data was issued to has been revoked; |
| --- | --- |

| (c) | in other situations determined by the providers of person identification data or electronic attestations of attributes in their policies referred to in paragraph 1. |
| --- | --- |

5. Providers of person identification data issued to a wallet unit shall ensure that revocations cannot be reverted.

6. The revoked person identification data shall remain accessible for as long as required by Union law or national law.

7. Where providers of person identification data revoke person identification data issued to wallet units, they shall make publicly available the validity status of person identification data they issue, in a privacy preserving manner, and indicate the location of that information in the person identification data.

8. Providers of person identification data shall enable privacy preserving techniques which ensure unlinkability where the electronic attestations of attributes do not require the identification of the user.

<a id="art_6"></a>

### art_6

Article 6

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
