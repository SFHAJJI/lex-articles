---
lex_id: 'eu-eurlex:32025r1155:2025-06-12'
title: 'Commission Delegated Regulation (EU) 2025/1155 of 12 June 2025 supplementing Regulation (EU) No 600/2014'
valid_from: '2025-06-12'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R1155'
source_sha256: '3c8da463230d091866c8edc285b35d27c136097e02dcfaca40177c2ab013b203'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

For the purposes of this Regulation, the following definitions shall apply:

| (a) | ‘input data’ means data transmitted by data contributors to the CTP, in accordance with Article 22a(1) of Regulation (EU) No 600/2014; |
| --- | --- |

| (b) | ‘output data’ means data disseminated by the CTP, in accordance with Article 27h(1), point (d), of Regulation (EU) No 600/2014. |
| --- | --- |

<a id="art_2"></a>

### art_2

Article 2

1. For the transmission of input data, data contributors shall offer CTPs at least one transmission protocol that complies with the minimum requirements for the quality of transmission protocols specified in Tables 1 to 4 of Annex I.

2. Upon agreement on the selected transmission protocol for the transmission of input data, CTPs and data contributors shall ensure that the minimum requirements referred to in paragraph 1 are consistently met without interruption.

<a id="art_3"></a>

### art_3

Article 3

1. Data contributors shall transmit input data to the data centres of the CTPs as close to real time as technically possible and without artificial delays.

2. Data contributors shall transmit to the CTP for shares and ETFs pre-trade input data as close to real time as is technically possible and in any case no later than 50 milliseconds after the timestamp of the order with a 95 % of confidence interval measured on a daily basis.

3. Data contributors shall transmit to the CTP for shares and ETFs post-trade input data related to transactions executed on a trading venue as close to real time as is technically possible and in any case no later than 50 milliseconds after the timestamp of the transaction with a 95 % of confidence interval measured on a daily basis.

4. Data contributors shall transmit to the CTP for shares and ETFs post-trade input data related to transactions executed outside of a trading venue as close to real time as is technically possible and in any case within 50 milliseconds after the timestamp of the reception of the trade report from the investment firm or DPE with a 95 % of confidence interval measured on a daily basis.

5. Data contributors shall transmit to the CTP for bonds and to the CTP for OTC derivatives post-trade input data related to transactions executed on a trading venue as close to real time as is technically possible and in any case within 500 milliseconds after the timestamp of the execution of the relevant transaction.

6. Data contributors shall transmit to the CTP for bonds and to the CTP for OTC derivatives post-trade input data related to transactions executed outside of a trading venue as close to real time as is technically possible and in any case within 500 milliseconds after the timestamp of the reception of the trade report from the investment firm or DPE.

<a id="art_4"></a>

### art_4

Article 4

Data contributors shall transmit to the data centres of CTPs input data in a format that adheres to the ISO 20022 methodology.

<a id="art_5"></a>

### art_5

Article 5

1. With regard to core market data for a given bond, data contributors shall transmit to the data centre of the CTP, by reference to each transaction, the details set out in Table 6 of Annex II that are flagged as ‘input’ or ‘both’ in the last column of Table 6.

2. With regard to regulatory data, data contributors shall transmit to the data centre of the CTP, by reference to each financial instrument, the details set out in Table 2 of Annex II that are flagged as ‘both’ in the last column of Table 2.

3. With regard to regulatory data, data contributors shall transmit to the data centre of the CTP, by reference to each trading system, the details set out in Table 3 of Annex II that are flagged as ‘both’ in the last column of Table 3.

<a id="art_6"></a>

### art_6

Article 6

1. With regard to post-trade core market data for a given share or ETF, data contributors shall transmit to the data centre of the CTP all of the following:

| (a) | by reference to each transaction, the details set out in Table 7 of Annex II that are flagged as ‘input’ or ‘both’ in the last column of Table 7; |
| --- | --- |

| (b) | on the first day of each month (n), the list of transactions which were executed in the month prior to that (n-1) in accordance with Article 4(1), point (c), of Regulation (EU) No 600/2014. |
| --- | --- |

2. With regard to pre-trade core market data for a given share or ETF, data contributors shall transmit to the data centre of the CTP, by reference to each best bid and offer and each price at which the auction system would best satisfy its trading algorithm, the details set out in Table 2 of Annex III.

3. With regard to regulatory data, data contributors shall transmit to the data centre of the CTP, by reference to each financial instrument, the details set out in Table 4 of Annex II that are flagged as ‘both’ in the last column of Table 4.

4. With regard to regulatory data, data contributors shall transmit to the data centre of the CTP, by reference to each trading system, the details set out in Table 5 of Annex II that are flagged as ‘both’ in the last column of Table 5.

<a id="art_7"></a>

### art_7

Article 7

1. With regard to core market data for a given bond, the CTP shall disseminate, by reference to each transaction, the details set out in Table 6 of Annex II that are flagged as ‘output’ or ‘both’ in the last column of Table 6.

2. With regard to regulatory data relating to bonds, the CTP shall disseminate:

| (a) | by reference to each financial instrument, the details set out in Table 2 of Annex II that are flagged as ‘output’ or ‘both’ in the last column of Table 2; |
| --- | --- |

| (b) | by reference to each trading system, the details set out in Table 3 of Annex II that are flagged as ‘output’ or ‘both’ in the last column of Table 3. |
| --- | --- |

<a id="art_8"></a>

### art_8

Article 8

1. With regard to post-trade core market data for a given share or ETF, the CTP shall disseminate, by reference to each transaction, the details set out in Table 7 of Annex II that are flagged as ‘output’ or ‘both’ in the last column of Table 7.

2. With regard to pre-trade core market data for a given share or ETF, the CTP shall disseminate, by reference to the European best bid and offer or the price at which the auction system would best satisfy its trading algorithm, the details set out in Tables 3, 4 and 5 of Annex III.

3. With regard to regulatory data relating to shares and ETFs, the CTP shall disseminate all of the following:

| (a) | by reference to each financial instrument, the details set out in Table 4 of Annex II that are flagged as ‘output’ or ‘both’ in the last column of that Table; |
| --- | --- |

| (b) | by reference to each trading system, the details set out in Table 5 of Annex II that are flagged as ‘output’ or ‘both’ in the last column of Table 5. |
| --- | --- |

<a id="art_9"></a>

### art_9

Article 9

1. CTPs shall disseminate the output data in a Graphical User Interface to ensure human readability.

2. CTPs shall also disseminate the output data in at least the following two formats simultaneously:

| (a) | Comma-Separated Values; |
| --- | --- |

| (b) | a format that adheres to the ISO 20022 methodology. |
| --- | --- |

3. CTPs shall:

| (a) | make instructions available to the public, explaining how and where to easily access and use the data, including the identification of the electronic format; |
| --- | --- |

| (b) | make public any changes to the instructions referred to in point (a) at least three months before they come into effect, unless there is an urgent and duly justified need for changes in instructions to take effect more quickly; |
| --- | --- |

| (c) | include on the homepage of their website a link to the instructions referred to in point (a). |
| --- | --- |

<a id="art_10"></a>

### art_10

Article 10

1. CTPs shall set up and maintain appropriate arrangements that ensure that they accurately collect, consolidate and publish the information received from data contributors and do not introduce any errors or omit information. CTPs shall correct the information where they have themselves caused the error or omission.

2. CTPs shall continuously monitor in real-time the performance of their IT systems to ensure that the input data they have received are successfully consolidated and published.

3. CTPs shall perform periodic reconciliations between the input data they receive and the output data they publish to verify whether the output data have been correctly published.

4. CTPs shall put in place mechanisms to confirm to data contributors that they have received the input data and shall assign a transaction identification code to each input data message they receive. CTPs shall refer to the transaction identification code in any subsequent communication with the data contributor in relation to a specific set of information reported.

5. CTPs shall set up and maintain arrangements to identify received input data that are incomplete, do not fulfil the requirements laid down in Articles 5 and 6, or contain information that is likely to be erroneous. Those arrangements shall include automated price and volume alerts, taking into account:

| (a) | the sector and the segment in which the financial instrument is traded; |
| --- | --- |

| (b) | liquidity levels, including historical trading levels; |
| --- | --- |

| (c) | appropriate price and volume benchmarks; |
| --- | --- |

| (d) | where needed, other parameters that are proper for the characteristics of the financial instrument. |
| --- | --- |

6. CTPs that find out that the input data they received are incomplete or do not fulfil any other reporting requirements in this Regulation shall not publish those input data and shall promptly alert the data contributor submitting those input data.

7. CTPs that find out that the input data they received are likely to be erroneous shall disseminate the corresponding output data and shall promptly flag the potential data quality issue both to the public and to the data contributor.

8. Upon receiving a notification of a data quality issue, data contributors shall acknowledge the issue and, where necessary, initiate the process of resubmitting corrected data.

9. CTPs shall monitor the timeliness of input data received from data contributors for the identification of serious and repeated breaches of the requirements laid down in Article 3.

10. CTPs shall delete and amend information in a trade report upon request from the data contributor providing the information where that data contributor cannot delete or amend its own information for technical reasons.

11. CTPs shall communicate with their clients via formalised interactive communication mechanisms through which data users may flag to the CTP any potential inaccuracies in the dissemination of output data.

12. CTPs shall publish non-discretionary policies describing the measures to enforce data quality and how those measures are applied. Those policies shall contain clear guidance on the application of such measures, ensuring adherence to non-discretionary application, proportionality, timeliness, consistency, and transparency.

<a id="art_11"></a>

### art_11

Article 11

Operators of trading venues and their members, participants or users, systematic internalisers, DPEs, APAs and CTPs shall synchronise the business clocks they use to record the date and time of any reportable event with the Coordinated Universal Time (‘UTC’) issued and maintained by the timing centres listed in the database maintained by the Bureau international des poids et mesures. Operators of trading venues and their members, participants or users, systematic internalisers, DPEs, APAs and CTPs may also synchronise the business clocks they use to record the date and time of any reportable event with UTC disseminated by a satellite system, provided that any offset from UTC is accounted for and removed from the timestamp.

<a id="art_12"></a>

### art_12

Article 12

1. Operators of trading venues and systematic internalisers shall ensure that their business clocks adhere to the levels of accuracy specified in Table 1 of Annex IV according to the gateway-to-gateway latency of each of their trading systems. Gateway-to-gateway latency shall be the time measured from the moment a message is received by an outer gateway of the trading venue’s system, sent through the order submission protocol, processed by the matching engine, and then sent back until an acknowledgement is sent from the gateway.

2. By way of derogation from paragraph 1, operators of trading venues and systematic internalisers that operate a voice trading system, or a request for quote trading system where the response requires human intervention or does not allow for algorithmic trading, or a system that formalises negotiated transactions in accordance with Article 4(1), point (b), of Regulation (EU) No 600/2014, shall ensure that their business clocks do not diverge by more than one second from UTC referred to in Article 11. The operator of the trading venue or systematic internaliser shall ensure that times are recorded to at least a one second granularity.

3. Operators of trading venues and systematic internalisers that operate multiple types of trading systems shall ensure that each system adheres to the level of accuracy applicable to that system in accordance with paragraphs 1 and 2.

<a id="art_13"></a>

### art_13

Article 13

1. Members, participants, or users of trading venues shall ensure that their business clocks used to record the time of reportable events adhere to the level of accuracy specified in Table 2 of Annex IV.

2. Members, participants or users of trading venues that engage in multiple types of trading activities shall ensure that the systems that they use to record the time of reportable events adhere to the level of accuracy applicable to each of those trading activities in accordance with the requirements set out in Table 2 of Annex IV.

<a id="art_14"></a>

### art_14

Article 14

1. DPEs shall record the date and time of reportable events up to one millisecond or better.

2. DPEs shall ensure that their business clocks used to record the time of reportable events do not diverge by more than one millisecond from the reference time laid down in Article 11.

3. By way of derogation from paragraphs 1 and 2, DPEs that have also acquired the status of systematic internaliser shall comply with Article 12.

<a id="art_15"></a>

### art_15

Article 15

1. APAs and CTPs shall record the date and time of reportable events up to one millisecond or better.

2. APAs and CTPs shall ensure that their business clocks used to record the time of reportable events do not diverge by more than one millisecond from the reference time laid down in Article 11.

<a id="art_16"></a>

### art_16

Article 16

Operators of trading venues and their members, participants, or users shall establish a system of traceability to UTC. They shall be able to demonstrate traceability to UTC by documenting the system design, functioning and specifications. They shall be able to identify the exact point at which a timestamp is applied and to demonstrate that the point within the system where the timestamp is applied remains consistent. They shall review the compliance of the system of traceability to UTC with this Regulation at least once a year.

<a id="art_17"></a>

### art_17

Article 17

1. For the purposes of redistributing part of the revenue generated by the consolidated tape to data contributors that meet one or more of the criteria laid down in Article 27h(6) of Regulation (EU) No 600/2014, the CTP for shares and ETFs shall determine:

| (a) | the amount of the revenue to be redistributed, based on the total revenue generated by the consolidated tape over the calculation window, as specified by the CTP; and |
| --- | --- |

| (b) | the list of regulated markets, MTFs, and SME growth markets that transmitted input data over the assessment period, either for the full period or for part of it (the ‘eligible data contributors’). |
| --- | --- |

2. After having determined the amount of revenue to be redistributed and the list of eligible data contributors in accordance with paragraph 1, the CTP for shares and ETFs shall perform the calculations set out in Articles 18 to 21. The CTP for shares and ETFs shall perform such calculations at least on an annual basis and, in any case, before the twentieth day of the month following the calculation window, using the trades recorded by each data contributor over the assessment period. The CTP for shares and ETFs shall apply the resulting percentages of such calculations retroactively over the latest calculation window.

3. For the purposes of paragraphs 1 and 2, the calculation window shall correspond to each individual period over which part of the revenue of the consolidated tape is redistributed.

4. For the purposes of paragraph 2, the assessment period shall correspond to the 12 months over which the relevant trading volume to be multiplied by each individual weighting is considered.

<a id="art_18"></a>

### art_18

Article 18

1. To calculate the amount of the revenue to be redistributed to eligible data contributors that meet the criterion under Article 27h(6), point (a), of Regulation (EU) No 600/2014, the CTP for shares and ETFs shall determine the total annual trading volume generated in shares for each eligible data contributor that is a regulated market or an SME growth market by summing each transaction record received by that data contributor.

2. The CTP for shares and ETFs shall determine the total annual trading volume in shares in the Union by summing all transaction records received by all data contributors.

3. For the purposes of the calculations referred to in paragraphs 1 and 2, transactions shall be single counted.

4. To determine whether an eligible data contributor meets the criterion laid down in Article 27h(6), point (a), of Regulation (EU) No 600/2014, the CTP for shares and ETFs shall divide the amount determined under paragraph 1 by the amount determined under paragraph 2 for each regulated market and SME growth market, identified by operating Market Identifier Code (‘MIC’), as specified in ISO 10383.

5. For each eligible data contributor meeting the criterion laid down in Article 27h(6), point (a), of Regulation (EU) No 600/2014, identified by segment MIC, as specified in ISO 10383, or by operating MIC, whenever there is no segment MIC, the CTP for shares and ETFs shall multiply the relevant trading volume generated by that MIC, as determined under paragraph 1, by a weighting of 4,5.

<a id="art_19"></a>

### art_19

Article 19

1. To determine whether an eligible data contributor meets the criterion laid down in Article 27h(6), point (b), of Regulation (EU) No 600/2014, the CTP for shares and ETFs shall, for each eligible data contributor, assess whether such data contributor provided initial admission to trading of shares or ETFs on 27 March 2019 or thereafter. That assessment shall be based on the information published by ESMA in accordance with Article 7(6) of Commission Delegated Regulation (EU) 2017/585 (9).

The CTP for shares and ETFs shall determine:

| (a) | for each eligible data contributor meeting the criterion laid down in Article 27h(6), point (a), of Regulation (EU) No 600/2014, the total annual trading volume generated in shares and ETFs, by summing each transaction record received by that data contributor; |
| --- | --- |

| (b) | for each eligible data contributor not meeting the criterion laid down in Article 27h(6), point (a), of Regulation (EU) No 600/2014, the total annual trading volume pertaining to the shares and ETFs that were initially admitted to trading on 27 March 2019 or thereafter, by summing each relevant transaction record received by that data contributor. |
| --- | --- |

For the purposes of the calculations referred to in points (a) and (b), transactions shall be single counted.

2. For each eligible data contributor meeting the criterion laid down in Article 27h(6), point (b), of Regulation (EU) No 600/2014, identified by segment MIC, as specified in ISO 10383, or by operating MIC, whenever there is no segment MIC, the CTP for shares and ETFs shall multiply the relevant trading volume generated by that MIC, as determined under paragraph 1, second subparagraph, by a weighting of 4,0.

<a id="art_20"></a>

### art_20

Article 20

1. To determine whether an eligible data contributor meets the criterion laid down in Article 27h(6), point (c), of Regulation (EU) No 600/2014, the CTP for shares and ETFs shall, for each eligible data contributor, determine the total annual pre-trade transparent trading volume generated in shares and ETFs.

For the purposes of the calculation referred to in the first subparagraph, the CTP for shares and ETFs shall include all transaction records received from the eligible data contributors which are not flagged as negotiated transactions subject to conditions other than the current market price (‘PRIC flag’), reference price transactions (‘RFPT flag’), negotiated transactions in liquid financial instruments (‘NLIQ flag’), negotiated transactions in illiquid financial instruments (‘OILQ flag’) as set out in Table 4 of Annex I to Delegated Regulation (EU) 2017/587, or as transactions subject to the pre-trade large in scale waiver as set out in Article 6(1), point (b). Transactions shall in all cases be single counted.

2. For each eligible data contributor meeting the criterion laid down in Article 27h(6), point (c), of Regulation (EU) No 600/2014, identified by segment MIC, as specified in ISO 10383, or by operating MIC whenever there is no segment MIC, the CTP for shares and ETFs shall multiply the relevant trading volume generated by that MIC, as determined under paragraph 1 of this Article, by a weighting of 1,5.

<a id="art_21"></a>

### art_21

Article 21

1. For each eligible data contributor, the CTP for shares and ETFs shall sum up the results of the multiplications of the weightings by the trading volumes, as set out in Articles 18 to 20.

2. The CTP for shares and ETFs shall determine the total sum of the results of the calculations under paragraph 1 for all eligible data contributors.

3. The CTP for shares and ETFs shall divide the sum per data contributor, as set out in paragraph 1, by the total sum, as set out in paragraph 2. The resulting percentages for each data contributor shall be multiplied by the total amount of the revenue to be redistributed.

<a id="art_22"></a>

### art_22

Article 22

1. When deciding whether to suspend the participation of a data contributor in the revenue redistribution scheme as laid down in Article 27h(8), point (c), of Regulation (EU) No 600/2014, the CTP for shares and ETFs shall take into account whether any of the following criteria is met:

| (a) | for three consecutive days, the data contributor has failed to submit trade reports or order reports or has submitted more than three trade reports or order reports later than as close to real time as is technically possible, as laid down in Article 3, and those trade reports or order reports account for at least a volume of transactions or orders that in a percentage is not lower than 10 % of the total volume of transactions or orders submitted in a single day; |
| --- | --- |

| (b) | for three consecutive days, the data contributor has submitted more than three trade reports or order reports that are incomplete or contain potentially erroneous data, as laid down in Article 10, and those trade reports or order reports account for at least a volume of transactions or orders that in percentage is not lower than 10 % of the total volume of transactions or orders submitted in a single day; |
| --- | --- |

| (c) | the data contributor no longer meets the minimum requirements for the quality of the transmission protocols set out in Article 2; |
| --- | --- |

| (d) | the data contributor no longer meets the requirements on the level of accuracy to which business clocks are to be synchronised, as set out in Chapter III. |
| --- | --- |

2. The CTP for shares and ETFs may decide not to suspend the participation of a data contributor in the revenue redistribution scheme where the situations set out in paragraph 1 occurred due to circumstances that were out of the ordinary, unavoidable, or unexpected.

<a id="art_23"></a>

### art_23

Article 23

1. Where the CTP for shares and ETFs has found a repeated and serious breach by a data contributor of the criteria set out in Article 22(1), points (a) and (b), it shall inform the data contributor thereof as soon as possible and, in any case, within two business days from the moment it has found the repeated and serious breach. In the notification to the data contributor, the CTP shall:

| (a) | identify the trade reports or order reports in relation to which the data contributor is deemed in breach and the number of days for which the revenue redistribution may be suspended; |
| --- | --- |

| (b) | provide information to the data contributor supporting its assessment. |
| --- | --- |

Within one week from the notification referred to in the first subparagraph, the data contributor may provide additional information to the CTP seeking to prove that the data requirements were not breached, or that an exceptional circumstance, as referred to in Article 22(2), occurred, and request that the CTP reviews its assessment based on the additional information.

The CTP shall review its assessment taking into account the additional information provided by the data contributor and, where it considers the information not to be complete, set a deadline by which the data contributor is to provide additional information.

2. On the last day of the period in relation to which the revenue is redistributed, the CTP shall draw up its final assessment on whether the criteria for the temporary suspension of the participation of a data contributor in the revenue redistribution scheme, in accordance with Article 22(1), are met.

The CTP shall inform the data contributor of its final assessment within two business days after the last day of the period in relation to which revenue is redistributed. The CTP shall inform the data contributor of the reasons for its final assessment, including the data requirements deemed in breach, and specify the amount of revenue that may be retained.

Within one week from receipt of the information referred to in the second subparagraph of this paragraph, the data contributor may provide additional information to the CTP proving that the data requirements referred to in Article 22a, 22b and 22c of Regulation (EU) No 600/2014 were not breached, or that an exceptional circumstance, as referred to in Article 22(2), occurred, and request that the CTP reviews its final assessment based on the additional information.

The CTP shall review its final assessment taking into account the additional information provided by the data contributor and, where it considers the information not to be complete, set a deadline by which the data contributor is to provide additional information.

3. The CTP shall inform the data contributor concerned of its final decision on the suspension of the participation in the revenue redistribution scheme no later than two weeks after informing the data contributor of the final assessment referred to in the second subparagraph of paragraph 2.

Where the CTP takes a final decision to suspend a data contributor from the revenue redistribution scheme it may redistribute the retained revenue to the other eligible data contributors in the redistribution window following that decision.

<a id="art_24"></a>

### art_24

Article 24

1. Where the CTP for shares and ETFs finds, on the basis of the additional information provided by the data contributor in accordance with Article 23(1), second subparagraph, and Article 23(2), third subparagraph, that the data requirements referred to in Articles 22a, 22b and 22c of Regulation (EU) No 600/2014 have not been breached, it shall redistribute the revenue retained, with interest, no later than two weeks after the final decision referred to in Article 23(3).

2. For the purposes of the calculation of the interest referred to in paragraph 1, the CTP shall take into account the average rate of the European Central Bank’s deposit facility, or where the CTP is established in a Member State whose currency is not the euro, the official interest rate for overnight credit charged by the central bank of the Member State where the CTP is established, over the period of the suspension of the revenue redistribution scheme.

<a id="art_25"></a>

### art_25

Article 25

Delegated Regulation (EU) 2017/574 is repealed with effect from 2 March 2026.

References to the repealed Delegated Regulation shall be construed as references to this Regulation and shall be read in accordance with the correlation table set out in Annex V.

<a id="art_26"></a>

### art_26

Article 26

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

Articles 11 to 16 shall apply from 2 March 2026.
