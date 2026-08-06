---
lex_id: 'eu-eurlex:32024r2690:2024-10-17'
title: 'Commission Implementing Regulation (EU) 2024/2690 of 17 October 2024 laying down rules for…'
valid_from: '2024-10-17'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690'
source_sha256: '1d10f42c31a2b3c6b929b4696a04093ee1d84a298c0c0437a22f8718a9ffb3cd'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

This Regulation, with regard to DNS service providers, TLD name registries, cloud computing service providers, data centre service providers, content delivery network providers, managed service providers, managed security service providers, providers of online market places, of online search engines and of social networking services platforms, and trust service providers (the relevant entities) lays down the technical and the methodological requirements of the measures referred to in Article 21(2) of Directive (EU) 2022/2555 and further specifies the cases in which an incident shall be considered to be significant as referred to in Article 23(3) of Directive (EU) 2022/2555.

<a id="art_2"></a>

### art_2

Article 2

1. For the relevant entities the technical and methodological requirements of cybersecurity risk-management measures referred to in Article 21(2), points (a) to (j), of Directive (EU) 2022/2555 are set out in the Annex to this Regulation.

2. The relevant entities shall ensure a level of security of network and information systems appropriate to the risks posed when implementing and applying the technical and methodological requirements of cybersecurity risk-management measures set out in the Annex to this Regulation. For that purpose, they shall take due account of the degree of their exposure to risks, their size and the likelihood of occurrence of incidents and their severity, including their societal and economic impact, when complying with the technical and methodological requirements of cybersecurity risk-management measures set out in the Annex to this Regulation.

Where the Annex to this Regulation provides that a technical or methodological requirement of a cybersecurity risk-management measure shall be applied ‘where appropriate’, ‘where applicable’ or ‘to the extent feasible’, and where a relevant entity considers it not appropriate, not applicable or not feasible for the relevant entity to apply certain such technical and methodological requirements, the relevant entity shall in a comprehensible manner document its reasoning to that effect.

<a id="art_3"></a>

### art_3

Article 3

1. An incident shall be considered to be significant for the purposes of Article 23(3) of Directive (EU) 2022/2555 with regard to the relevant entities where one or more of the following criteria are fulfilled:

| (a) | the incident has caused or is capable of causing direct financial loss for the relevant entity that exceeds EUR 500 000 or 5 % of the relevant entity’s total annual turnover in the preceding financial year, whichever is lower; |
| --- | --- |

| (b) | the incident has caused or is capable of causing the exfiltration of trade secrets as set out in Article 2 point (1), of Directive (EU) 2016/943 of the relevant entity; |
| --- | --- |

| (c) | the incident has caused or is capable of causing the death of a natural person; |
| --- | --- |

| (d) | the incident has caused or is capable of causing considerable damage to a natural person’s health; |
| --- | --- |

| (e) | a successful, suspectedly malicious and unauthorised access to network and information systems occurred, which is capable of causing severe operational disruption; |
| --- | --- |

| (f) | the incident meets the criteria set out in Article 4; |
| --- | --- |

| (g) | the incident meets one or more of the criteria set out in Articles 5 to 14. |
| --- | --- |

2. Scheduled interruptions of service and planned consequences of scheduled maintenance operations carried out by or on behalf of the relevant entities shall not be considered to be significant incidents.

3. When calculating the number of users impacted by an incident for the purpose of Articles 7 and 9 to 14, the relevant entities shall consider all of the following:

| (a) | the number of customers that have a contract with the relevant entity which grants them access to the relevant entity’s network and information systems or services offered by, or accessible via, those network and information systems; |
| --- | --- |

| (b) | the number of natural and legal persons associated with business customers that use the entities’ network and information systems or services offered by, or accessible via, those network and information systems. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

Incidents that individually are not considered a significant incident within the meaning of Article 3, shall be considered collectively as one significant incident where they meet all of the following criteria:

| (a) | they have occurred at least twice within 6 months; |
| --- | --- |

| (b) | they have the same apparent root cause; |
| --- | --- |

| (c) | they collectively meet the criteria set out in Article 3(1)(a). |
| --- | --- |

<a id="art_5"></a>

### art_5

Article 5

With regard to DNS service providers, an incident shall be considered significant under Article 3(1)(g), where it fulfils one or more of the following criteria:

| (a) | a recursive or authoritative domain name resolution service is completely unavailable for more than 30 minutes; |
| --- | --- |

| (b) | for a period of more than one hour, the average response time of a recursive or authoritative domain name resolution service to DNS requests is more than 10 seconds; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of the authoritative domain name resolution service is compromised, except in cases where the data of fewer than 1 000 domain names managed by the DNS service provider, amounting to no more than 1 % of the domain names managed by the DNS service provider, are not correct because of misconfiguration. |
| --- | --- |

<a id="art_6"></a>

### art_6

Article 6

With regard to TLD name registries, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | an authoritative domain name resolution service is completely unavailable; |
| --- | --- |

| (b) | for a period of more than one hour, the average response time of an authoritative domain name resolution service to DNS requests is more than 10 seconds, |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the technical operation of the TLD is compromised. |
| --- | --- |

<a id="art_7"></a>

### art_7

Article 7

With regard to cloud computing service providers, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | a cloud computing service provided is completely unavailable for more than 30 minutes; |
| --- | --- |

| (b) | the availability of a cloud computing service of a provider is limited for more than 5 % of the cloud computing service’s users in the Union, or for more than 1 million of the cloud computing service’s users in the Union, whichever number is smaller, for a duration of more than one hour; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a cloud computing service is compromised as a result of a suspectedly malicious action, |
| --- | --- |

| (d) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a cloud computing service is compromised with an impact on more than 5 % of that cloud computing service’s users in the Union, or on more than 1 million of that cloud computing service’s users in the Union, whichever number is smaller. |
| --- | --- |

<a id="art_8"></a>

### art_8

Article 8

With regard to data centre service providers, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | a data centre service of a data centre operated by the provider is completely unavailable; |
| --- | --- |

| (b) | the availability of a data centre service of a data centre operated by the provider is limited for a duration of more than one hour; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a data centre service is compromised as a result of a suspectedly malicious action; |
| --- | --- |

| (d) | physical access to a data centre operated by the provider is compromised. |
| --- | --- |

<a id="art_9"></a>

### art_9

Article 9

With regard to content delivery network providers, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | a content delivery network is completely unavailable for more than 30 minutes; |
| --- | --- |

| (b) | the availability of a content delivery network is limited for more than 5 % of the content delivery network’s users in the Union, or for more than 1 million of the content delivery network’s users in the Union, whichever number is smaller, for a duration of more than one hour; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a content delivery network is compromised as a result of a suspectedly malicious action; |
| --- | --- |

| (d) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a content delivery network is compromised with an impact on more than 5 % of that content delivery network’s users in the Union, or on more than 1 million of that content delivery network’s users in the Union, whichever number is smaller. |
| --- | --- |

<a id="art_10"></a>

### art_10

Article 10

With regard to managed service providers and managed security service providers, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | a managed service or managed security service is completely unavailable for more than 30 minutes; |
| --- | --- |

| (b) | the availability of a managed service or managed security service is limited for more than 5 % of the service’s users in the Union, or for more than 1 million of the service’s users in the Union, whichever number is smaller, for a duration of more than one hour; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a managed service or managed security service is compromised as a result of a suspectedly malicious action; |
| --- | --- |

| (d) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a managed service or a managed security service, is compromised with an impact on more than 5 % of that managed service’s or that managed security service’s users in the Union, or on more than 1 million of the service users in the Union, whichever number is smaller. |
| --- | --- |

<a id="art_11"></a>

### art_11

Article 11

With regard to providers of online marketplaces, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | an online marketplace is completely unavailable for more than 5 % of an online marketplace’s users in the Union, or for more than 1 million of an online marketplace’s users in the Union, whichever number is smaller; |
| --- | --- |

| (b) | more than 5 % of an online marketplace’s users in the Union, or more than 1 million of an online marketplace’s users in the Union, whichever number is smaller, are impacted by limited availability of that online marketplace; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of an online marketplace is compromised as a result of a suspectedly malicious action; |
| --- | --- |

| (d) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of an online marketplace is compromised with an impact on more than 5 % of that online marketplace’s users in the Union, or on more than 1 million of that online marketplace’s users in the Union, whichever number is smaller. |
| --- | --- |

<a id="art_12"></a>

### art_12

Article 12

With regard to providers of online search engines, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | an online search engine is completely unavailable for more than 5 % of that online search engine’s users in the Union, or for more than 1 million of that online search engine’s users in the Union, whichever number is smaller; |
| --- | --- |

| (b) | more than 5 % of an online search engine’s users in the Union, or more than 1 million of an online search engine’s users in the Union, whichever number is smaller, are impacted by limited availability of that online search engine; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of an online search engine is compromised as a result of a suspectedly malicious action; |
| --- | --- |

| (d) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of an online search engine is compromised with an impact on more than 5 % of that online search engine’s users in the Union, or on more than 1 million of that online search engine’s users in the Union, whichever number is smaller. |
| --- | --- |

<a id="art_13"></a>

### art_13

Article 13

With regard to providers of social networking services platforms, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | a social networking service platform is completely unavailable for more than 5 % of that social networking service platform’s users in the Union, or for more than 1 million of that social networking service platform’s users in the Union, whichever number is smaller; |
| --- | --- |

| (b) | more than 5 % of a social networking service platform’s users in the Union, or more than 1 million of a social networking service platform’s users in the Union, whichever number is smaller, are impacted by limited availability of that social networking service platform; |
| --- | --- |

| (c) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a social networking service platform is compromised as a result of a suspectedly malicious action; |
| --- | --- |

| (d) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a social networking service platform is compromised with an impact on more than 5 % of that social networking service platform’s users in the Union, or on more than 1 million of that social networking service platform’s users in the Union, whichever number is smaller. |
| --- | --- |

<a id="art_14"></a>

### art_14

Article 14

With regard to trust service providers, an incident shall be considered significant under Article 3(1)(g) where it fulfils one or more of the following criteria:

| (a) | a trust service is completely unavailable for more than 20 minutes; |
| --- | --- |

| (b) | a trust service is unavailable to users, or relying parties, for more than one hour calculated on a calendar week basis; |
| --- | --- |

| (c) | more than 1 % of the users or relying parties in the Union, or more than 200 000 users or relying parties in the Union, whichever number is smaller, are impacted by limited availability of a trust service; |
| --- | --- |

| (d) | physical access to an area where network and information systems are located and to which access is restricted to trusted personnel of the trust service provider, or the protection of such physical access, is compromised; |
| --- | --- |

| (e) | the integrity, confidentiality or authenticity of stored, transmitted or processed data related to the provision of a trust service is compromised with an impact on more than 0,1 % of users or relying parties, or more than 100 of users or relying parties, whichever number is smaller, of the trust service in the Union. |
| --- | --- |

<a id="art_15"></a>

### art_15

Article 15

Commission Implementing Regulation (EU) 2018/151 (4) is repealed.

<a id="art_16"></a>

### art_16

Article 16

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
