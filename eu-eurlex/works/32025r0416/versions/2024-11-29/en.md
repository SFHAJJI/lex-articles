---
lex_id: 'eu-eurlex:32025r0416:2024-11-29'
title: 'Commission Delegated Regulation (EU) 2025/416 of 29 November 2024 supplementing Regulation (EU) 2023/1114'
valid_from: '2024-11-29'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R0416'
source_sha256: 'd4e6d8af03dec2224b70aa749e327bbe7e68d70cec5344f6b0dd9fbcddccdd1c'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

1. Crypto-asset service providers operating a trading platform for crypto-assets shall keep at the disposal of the competent authority, or give the competent authority access to the details of each order in crypto-assets advertised through their systems set out in Articles 2 to 15, as specified in the format laid down in Tables 2 and 3 of the Annex, insofar as they pertain to the order concerned.

2. The data referred to in paragraph 1 shall be in a JSON format in accordance with the methodology laid out in standard ISO 20022.

<a id="art_2"></a>

### art_2

Article 2

1. For all orders in crypto-assets, crypto-asset service providers operating a trading platform for crypto-assets shall keep records to identify all of the following:

| (a) | the participant to the trading platform for crypto-assets that is a legal entity and submits the order to the trading platform for crypto-assets, as identified in accordance with Article 4 and field 1 of Table 2 of the Annex; |
| --- | --- |

| (b) | the participant to the trading platform for crypto-assets who is a natural person and submits the order to the trading platform for crypto-assets, as identified in accordance with field 2 of Table 2 of the Annex; |
| --- | --- |

| (c) | the client on whose behalf the participant to the trading platform for crypto-assets referred to in points (a) or (b) submits the order to the trading platform for crypto-assets, as identified in accordance with field 3 of Table 2 of the Annex; |
| --- | --- |

| (d) | the person or the computer algorithm within the participant to the trading platform for crypto-assets referred to in points (a) and (b) that is responsible for the investment decision in relation to the order, as identified in accordance with field 4 of Table 2 of the Annex; |
| --- | --- |

| (e) | the person or the computer algorithm within the participant to the trading platform for crypto-assets referred to in points (a) and (b) that is responsible for the execution of the order, as identified in accordance with field 5 of Table 2 of the Annex. |
| --- | --- |

For the purposes of point (d), where more than one persons take the investment decision, the crypto-asset service provider operating a trading platform for crypto-assets shall keep records of the person with primary responsibility for that decision. A crypto-asset service provider operating a trading platform for crypto-assets shall only identify such a person or computer algorithm where the investment decision is made on behalf of either the participant, or a client in accordance with a discretionary mandate to it by the client.

2. Where a participant to the trading platform for crypto-assets intends to allocate an order to its client following submission of the order to the trading platform for crypto-assets and has not yet allocated the order to its client at the time of the submission of the order, that client shall be identified as specified in field 3 of Table 2 of the Annex.

3. Where several orders of different clients are submitted to the trading platform for crypto-assets together as an aggregated order, the information referred to in field 3 of Table 2 of the Annex shall be recorded in respect of each client.

<a id="art_3"></a>

### art_3

Article 3

1. Crypto-asset service provider operating a trading platform for crypto-assets shall identify natural persons in the order book records by using the designation resulting from the concatenation of the ISO 3166-1 alpha-2 specified in ISO 3166 followed by the national client identifier as specified in Annex II of Delegated Regulation (EU) 2017/590 based on the nationality of the person. The two-letter country code shall correspond to the nationality of natural person.

2. The national client identifier referred to in paragraph 1 shall be assigned in accordance with the priority levels provided in Annex II of Delegated Regulation (EU) 2017/590 using the highest priority identifier that a person has regardless of whether that identifier is already known to the crypto-asset service provider operating a trading platform for crypto-assets.

3. Where a natural person is a national of more than one European Economic Area (EEA) country, the country code of the first nationality when sorted alphabetically by its ISO 3166-1 alpha-2 code and the identifier of that nationality assigned in accordance with paragraph 2 shall be used. Where a natural person has a non-EEA nationality, the highest priority identifier in accordance with the field referring to ‘all other countries’ provided in Annex II of Delegated Regulation (EU) 2017/590 shall be used. Where a natural person has an EEA and a non-EEA nationality, the country code of the EEA nationality and the highest priority identifier of that nationality assigned in accordance with paragraph 2 shall be used.

4. Where a natural person is a resident of a country other than the one of its nationality, crypto-asset service providers operating a trading platform for crypto-assets shall also identify that natural person based on the country of its residence as specified in field 50 of Table 2 of the Annex.

5. Prefixes to names shall be excluded and first names and surnames shorter than five characters shall be appended by ‘#’. All characters shall be in upper case. No apostrophes, accents, hyphens, punctuation marks or spaces shall be used.

6. Where the identifier assigned in accordance with paragraph 2 is based on CONCAT, the natural person shall be identified by the crypto-asset service provider operating a trading platform for crypto-assets using the concatenation of the following elements in the following order:

| (a) | the date of birth of that person in the format YYYYMMDD; |
| --- | --- |

| (b) | the five first characters of the first name of that person; |
| --- | --- |

| (c) | the five first characters of the surname of that person. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

1. Crypto-asset service providers operating a trading platform for crypto-assets shall identify legal entities in order book records by using the entity identifier in accordance with Article 14 of Commission Delegated Regulation establishing technical standards adopted pursuant to Article 68(10), first subparagraph, point (b).

2. Crypto-asset service providers operating a trading platform for crypto-assets shall identify crypto-assets in order book records by using the asset identifiers in accordance with Article 15 of Commission Delegated Regulation establishing technical standards adopted pursuant to Article 68(10), first subparagraph, point (b).

3. Where using the Legal Entity Identifier (LEI) to identify legal entities in accordance with paragraph 1, the crypto-asset service provider operating a trading platform for crypto-assets shall ensure that the length and construction of the LEI code recorded in the order book records is compliant with the ISO 17442 standard and that the LEI code is included in the Global LEI database maintained by the Central Operating Unit appointed by the Regulatory Oversight Committee, and refers to the entity concerned.

<a id="art_5"></a>

### art_5

Article 5

The trading capacity in which the participant of the trading platform for crypto-assets submits an order shall be recorded as specified in field 7 of Table 2 of the Annex.

<a id="art_6"></a>

### art_6

Article 6

1. Crypto-asset service providers operating a trading platform for crypto-assets shall maintain a record of the date and time of the occurrence of each event listed in field 20 of Table 2 of the Annex as specified in field 8 of Table 2 of the Annex.

2. Crypto-asset service providers operating a trading platform for crypto-assets shall maintain a record of the date and time for each data element listed in fields 47, 48 and 49 of Table 2 of the Annex, as specified in field 8 of Table 2 of the Annex.

<a id="art_7"></a>

### art_7

Article 7

1. Crypto-asset service providers operating a trading platform for crypto-assets shall keep a record of the validity periods and order restrictions that are listed in fields 9 and 10 of Table 2 of the Annex.

2. Records of the dates and times in respect of validity periods shall be maintained for each validity period as specified in field 11 of Table 2 of the Annex.

<a id="art_8"></a>

### art_8

Article 8

1. Crypto-asset service providers operating a trading platform for crypto-assets which operate trading systems on a price visibility-time priority shall maintain a record of the priority time stamp for all orders as specified in field 12 of Table 2 of the Annex.

2. Crypto-asset service providers operating a trading platform for crypto-assets which operate trading systems on a size-time priority basis shall maintain a record of the quantities which determine the priority of orders as specified in field 13 of Table 2 of the Annex and the priority time stamp referred to in paragraph 1.

3. Crypto-asset service providers operating a trading platform for crypto-assets which use a combination of price-visibility-time priority and size-time priority and display orders on their order book in time priority shall maintain a record of the priority time stamp for all orders as specified in field 12 of Table 2 of the Annex.

4. Crypto-asset service providers operating a trading platform for crypto-assets which use a combination of price-visibility-time priority and size-time priority and display orders on their order book in size-time priority shall maintain a record of the quantities which determine the priority of orders as specified in field 13 of Table 2 of the Annex and the priority time stamp referred to in paragraph 1.

5. Crypto-asset service providers operating a trading platform for crypto-assets shall assign and maintain a sequence number for each event as specified in field 14 of Table 2 of the Annex.

<a id="art_9"></a>

### art_9

Article 9

1. Crypto-asset service providers operating a trading platform for crypto-assets shall maintain an individual identification code for each order as specified in field 19 of Table 2 of the Annex. The identification code shall be unique per following:

| (a) | order book; |
| --- | --- |

| (b) | trading day; and |
| --- | --- |

| (c) | crypto-asset. |
| --- | --- |

The code shall be valid starting from the receipt of the order by the operator of the trading platform for crypto-assets until the removal of the order from the order book. The identification code shall apply to rejected orders irrespective of the ground for their rejection.

2. The operator of the trading platform for crypto-assets shall maintain the relevant details of strategy orders with implied functionality (‘SOIF’) that are disseminated to the public as specified in field 31 of Table 2 of the Annex. The order status referred to in that field shall specify whether the order is an implicit order.

3. Upon execution of a SOIF, its details shall be maintained by the operator of the trading platform for crypto-assets as specified in the relevant fields in Table 2 of the Annex.

4. Upon execution of a SOIF, a strategy linked order identification code shall be indicated using the same identification code for all orders connected to the particular strategy. The strategy linked order identification code shall be specified in accordance with field 44 of Table 2 of the Annex.

5. Orders submitted to a trading platform for crypto-assets allowing for a routing strategy shall be identified by that trading platform for crypto-assets as ‘routed’ as specified in field 31 of Table 2 of the Annex when they are routed to another trading platform for crypto-assets. Orders submitted to a trading platform for crypto-assets allowing for a routing strategy shall retain the same identification code for their lifetime, regardless of whether any remaining quantity is re-posted on the order book.

<a id="art_10"></a>

### art_10

Article 10

Crypto-asset service providers operating a trading platform for crypto-assets shall maintain a record of the details referred to in field 20 of Table 2 of the Annex in relation to all new orders.

<a id="art_11"></a>

### art_11

Article 11

1. Crypto-asset service providers operating a trading platform for crypto-assets shall maintain a record of the order type for each order received using their own specification as specified in field 21 of Table 2 of the Annex.

2. Crypto-asset service providers operating a trading platform for crypto-assets shall classify each order received either as a limit order or as a stop order as specified in field 22 of Table 2 of the Annex.

<a id="art_12"></a>

### art_12

Article 12

Crypto-asset service providers operating a trading platform for crypto-assets shall maintain a record of all price-related details referring to the respective orders, as specified in Section I of Table 2 of the Annex.

<a id="art_13"></a>

### art_13

Article 13

Crypto-asset service providers operating a trading platform for crypto-assets shall maintain records of all order instructions received for each order as specified in Section J of Table 2 of the Annex.

<a id="art_14"></a>

### art_14

Article 14

Crypto-asset service providers operating a trading platform for crypto-assets shall maintain an individual transaction identification code for each transaction resulting from the full or partial execution of an order as specified in field 46 of Table 2 and field 1 of Table 3 of the Annex, as applicable.

<a id="art_15"></a>

### art_15

Article 15

1. Crypto-asset service providers operating a trading platform for crypto-assets shall maintain a record of the trading phases and indicative auction price and volume, as specified in Section K of Table 2 of the Annex.

2. Where competent authorities request details referred to in Section K, it shall be considered that the details referred to in fields 8 and 14 to 17 of Table 2 of the Annex are to be provided based on that request.

<a id="art_16"></a>

### art_16

Article 16

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
