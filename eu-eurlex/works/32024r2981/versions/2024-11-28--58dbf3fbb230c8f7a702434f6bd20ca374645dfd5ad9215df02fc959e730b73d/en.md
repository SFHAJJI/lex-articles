---
lex_id: 'eu-eurlex:32024r2981:2024-11-28--58dbf3fbb230c8f7a702434f6bd20ca374645dfd5ad9215df02fc959e730b73d'
title: 'Commission Implementing Regulation (EU) 2024/2981 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014'
valid_from: '2024-11-28'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2981'
source_sha256: 'e45c7c805a4c14082e8537d14805b159e86aa279c45a4715e2a2e161952be210'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article 1

This Regulation sets out reference standards and establishes specifications and procedures to build a robust framework for the certification of wallets to be updated on a regular basis to keep in line with technology and standards developments and with the work carried out on the basis of Recommendation (EU) 2021/946 on a common Union Toolbox for a coordinated approach towards a European Digital Identity Framework, and in particular the Architecture and Reference Framework.

<a id="art_2"></a>

### art_2

Article 2

For the purpose of this Regulation, the following definitions apply:

| (1) | ‘wallet solution’ means a combination of software, hardware, services, settings, and configurations, including wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic devices; |
| --- | --- |

| (2) | ‘scheme owner’ means an organisation which is responsible for developing and maintaining a certification scheme; |
| --- | --- |

| (3) | ‘object of certification’ means products, processes and services or a combination thereof to which specified requirements apply; |
| --- | --- |

| (4) | ‘wallet secure cryptographic application’ means an application that manages critical assets by being linked to and using the cryptographic and non-cryptographic functions provided by the wallet secure cryptographic device; |
| --- | --- |

| (5) | ‘wallet instance’ means the application installed and configured on a wallet user’s device or environment, which is part of a wallet unit, and that the wallet user uses to interact with the wallet unit; |
| --- | --- |

| (6) | ‘wallet secure cryptographic device’ means a tamper-resistant device that provides an environment that is linked to and used by the wallet secure cryptographic application to protect critical assets and provide cryptographic functions for the secure execution of critical operations; |
| --- | --- |

| (7) | ‘risk register’ means a record of information relevant to the certification process about identified risks; |
| --- | --- |

| (8) | ‘wallet provider’ means a natural or legal person who provides wallet solutions; |
| --- | --- |

| (9) | ‘certification body’ means a third-party conformity assessment body operating certification schemes; |
| --- | --- |

| (10) | ‘wallet unit’ means a unique configuration of a wallet solution that includes wallet instances, wallet secure cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual wallet user; |
| --- | --- |

| (11) | ‘critical assets’ means assets within or in relation to a wallet unit of such extraordinary importance that where their availability, confidentiality or integrity are compromised, this would have a very serious, debilitating effect on the ability to rely on the wallet unit; |
| --- | --- |

| (12) | ‘wallet user’ means a user who is in control of the wallet unit; |
| --- | --- |

| (13) | ‘incident’ means an incident as defined in point (6) of Article 6 of Directive (EU) 2022/2555 of the European Parliament and of the Council (10); |
| --- | --- |

| (14) | ‘embedded disclosure policy’ means a set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes. |
| --- | --- |

<a id="art_3"></a>

### art_3

Article 3

1. Member States shall assign a scheme owner for each national certification scheme.

2. The object of certification defined in national certification schemes shall be the provision and operation of wallet solutions and of the electronic identification schemes under which they are provided.

3. In accordance with Implementing Regulation (EU) 2015/1502, the object of certification in national certification schemes shall include the following elements:

| (a) | the software components, including settings and configurations of a wallet solution and of the electronic identification scheme under which the wallet solutions are provided; |
| --- | --- |

| (b) | the hardware components and platforms on which the software components referred to in point (b) run on or rely upon for critical operations, in cases where they are provided directly or indirectly by the wallet solution and electronic identification scheme under which they are provided and when they are required to meet the desired level of assurance for those software components. When the hardware components and platforms are not provided by the wallet provider, national certification schemes shall formulate assumptions for evaluation of the hardware components and platforms, under which resistance against attackers with high attack potential in line with Implementing Regulation (EU) 2015/1502 can be provided, and specify the evaluation activities to confirm these assumptions as referred in Annex IV; |
| --- | --- |

| (c) | the processes that support the provision and operation of a wallet solution, including the user onboarding process as referred to in Article 5a of Regulation (EU) No 910/2014, covering at least enrolment, electronic means management and organisation pursuant to section 2.1, 2.2, and 2.4 of Annex I to Implementing Regulation (EU) 2015/1502. |
| --- | --- |

4. National certification schemes shall include a description of the specific architecture of the wallet solutions and of the electronic identification scheme under which they are provided. When national certification schemes cover more than one specific architecture, they shall include a profile for each specific architecture.

5. For each profile, national certification schemes shall set out at least the following:

| (a) | the specific architecture of a wallet solution and of the electronic identification scheme under which they are provided; |
| --- | --- |

| (b) | the security controls associated to assurance levels set out in Article 8 of Regulation (EU) No 910/2014; |
| --- | --- |

| (c) | an evaluation plan drawn-up in accordance with section 7.4.1 of EN ISO/IEC 17065;2012; |
| --- | --- |

| (d) | the security requirements necessary to address the cybersecurity risks and threats listed in the risk register set out in Annex I of this Regulation, up to the required assurance level, and to meet, where applicable, the objectives defined in Article 51 of Regulation (EU) 2019/881; |
| --- | --- |

| (e) | a mapping of the controls referred to in point (b) of this paragraph to the components of the architecture; |
| --- | --- |

| (f) | a description of how the security controls, the mapping, the security requirements and the evaluation plan referred to in points (b) to (c) allow providers of wallet solutions and the electronic identification scheme under which they are provided to adequately address the cybersecurity risks and threats identified in the risk register referred to in point (d), up to the required assurance level based on a risk assessment to refine and complement the risks and threats listed in the risk register with risks and threats specific to the architecture. |
| --- | --- |

6. The evaluation plan referred to in paragraph 5, point (c) shall list evaluation activities to be included in the evaluation of wallet solutions and of the electronic identification scheme under which they are provided.

7. The evaluation activity referred to in paragraph 6 shall require providers of wallet solutions and the electronic identification scheme under which they are provided to provide information meeting the requirements listed in Annex II.

<a id="art_4"></a>

### art_4

Article 4

1. National certification schemes shall cover functional, cybersecurity and data protection requirements by using, when available and applicable, the following certification schemes:

| (a) | European cybersecurity certification schemes established pursuant to Regulation (EU) 2019/881, including the EUCC; |
| --- | --- |

| (b) | national cybersecurity certification schemes covered by the EUCC, in accordance with Article 49 of Implementing Regulation (EU) 2024/482. |
| --- | --- |

2. National certification schemes may, in addition, when available and applicable, refer to:

| (a) | other relevant national certification schemes; |
| --- | --- |

| (b) | international, European, and national standards; |
| --- | --- |

| (c) | technical specifications that meet the requirements set out in Annex II to Regulation (EU) No 1025/2012 of the European Parliament and of the Council (11). |
| --- | --- |

3. National certification schemes shall:

| (a) | specify the elements listed in section 6.5 of EN ISO/IEC 17067:2013; |
| --- | --- |

| (b) | be implemented as a type 6 scheme, in accordance with section 5.3.8 of EN ISO/IEC 17067:2013. |
| --- | --- |

4. National certification schemes shall comply with the following requirements:

| (a) | only providers referred to in Article 5a(2) of Regulation (EU) No 910/2014 are eligible to be issued certificates under the national certification schemes; |
| --- | --- |

| (b) | only the Trust Mark is used as mark of conformity; |
| --- | --- |

| (c) | providers of wallet solutions and the electronic identification scheme under which they are provided include references to Regulation (EU) No 910/2014 and this Regulation when referring to the scheme; |
| --- | --- |

| (d) | providers of wallet solutions and the electronic identification scheme under which they are provided, complement the scheme’s risk assessment as referred to in Article 3, paragraph 5 point (f), to identify risks and threats specific to their implementation and propose appropriate treatment measures for all relevant risks and threats; |
| --- | --- |

| (e) | responsibilities and the legal action are established and include references to the applicable national legislation, which defines the responsibilities and possible legal action, where certification under the scheme is being used fraudulently. |
| --- | --- |

5. The assessment referred to in paragraph 4, point (d) shall be shared with the certification body for evaluation.

<a id="art_5"></a>

### art_5

Article 5

1. National certification schemes shall contain incident and vulnerability management requirements in accordance with paragraphs 2 to 9.

2. The holder of a certificate of conformity of a wallet solution and of the electronic identification scheme under which it is provided shall notify their certification body without undue delay of any breach or compromise of the wallet solution, or of the electronic identification scheme under which it is provided, that is likely to impact its conformity with the requirements of the national certification schemes’ requirements.

3. The holder of a certificate of conformity shall establish, maintain and operate a vulnerability management policy and procedures, taking into account the procedures set out in existing European and international standards, including EN ISO/IEC 30111:2019.

4. The holder of the certificate of conformity shall notify the issuing certification body of the vulnerabilities and changes affecting the wallet solution, based on defined criteria on the impact of these vulnerabilities and changes.

5. The holder of the certificate of conformity shall prepare a vulnerability impact analysis report for any vulnerability that affects the software components of the wallet solution. The report shall include the following information:

| (a) | the impact of the vulnerability on the certified wallet solution; |
| --- | --- |

| (b) | possible risks associated with the proximity or likelihood of an attack; |
| --- | --- |

| (c) | whether the vulnerability can be remedied using available means; |
| --- | --- |

| (d) | where the vulnerability can be remedied using available means, possible ways to remedy the vulnerability. |
| --- | --- |

6. Where notification is required in paragraph 4, the holder of the certificate of conformity shall transmit, without undue delay, the vulnerability impact analysis report referred to in paragraph 5 to the certification body.

7. The holder of a certificate of conformity shall establish, maintain and operate a vulnerability management policy meeting the requirements set out in Annex I to the Cyber Resilience Act (12).

8. National certification schemes shall establish vulnerability disclosure requirements applicable to certification bodies.

9. The holder of a certificate of conformity shall disclose and register any publicly known and remediated vulnerability in the wallet solution or in one of the online repositories referred to in Annex V.

<a id="art_6"></a>

### art_6

Article 6

1. National certification schemes shall contain a process for reviewing their operation on a periodic basis. That process shall aim at confirming their adequacy and at identifying aspects requiring improvement, taking into account feedback from stakeholders.

2. National certification schemes shall include provisions concerning their maintenance. This process shall include at least the following requirements:

| (a) | rules for the governance of the national certification schemes’ definition and requirements; |
| --- | --- |

| (b) | the establishment of timelines for the issuance of certificates following the adoption of updated versions of the national certification schemes, both for new certificates of conformity and for previously issued ones; |
| --- | --- |

| (c) | a periodic review of the national certification schemes, to ensure that the national certification schemes’ requirements are being applied in a consistent manner, taking into account at least the following aspects:—requests for clarification addressed to the scheme owner related to the national certification scheme requirements;—feedback from stakeholders and other interested parties;—responsiveness of the national certification scheme owner to requests of information. |
| --- | --- |
| — | requests for clarification addressed to the scheme owner related to the national certification scheme requirements; |
| — | feedback from stakeholders and other interested parties; |
| — | responsiveness of the national certification scheme owner to requests of information. |

| (d) | rules for monitoring reference documents and procedures for the evolution of national certification schemes’ reference versions, including at least transition periods; |
| --- | --- |

| (e) | a process to ensure the latest cybersecurity risks and threats as listed in the risk register set out in Annex I of this Regulation are covered; |
| --- | --- |

| (f) | a process for managing other changes in national certification schemes. |
| --- | --- |

3. National certification schemes shall contain requirements for performing evaluations on currently certified products within a certain period after the revision of the scheme, or after the release of new specifications or standards, or new versions thereof, with which the wallet solutions and the electronic identification scheme under which they are provided shall comply.

<a id="art_7"></a>

### art_7

Article 7

1. Scheme owners shall develop and maintain national certification schemes and govern their operations.

2. Scheme owners may subcontract all or part of their tasks to a third party. When subcontracting to a private party, scheme owners shall set out the duties and responsibilities of all parties by contract. Scheme owners shall remain responsible for all subcontracted activities performed by their subcontractors.

3. Scheme owners shall perform their monitoring activities, if applicable, at least on the basis of the following information:

| (a) | information coming from certification bodies, national accreditation bodies, and relevant market surveillance authorities; |
| --- | --- |

| (b) | information resulting from its own or another authority’s audits and investigations; |
| --- | --- |

| (c) | complaints and appeals received pursuant to Article 15. |
| --- | --- |

4. Scheme owners shall inform the Cooperation Group of revisions to the national certification schemes. That notification shall provide adequate information for the Cooperation Group to issue recommendations to scheme owners and opinions about the updated national certification schemes.

<a id="art_8"></a>

### art_8

Article 8

1. National certification schemes shall contain cybersecurity requirements based on a risk assessment of each specific supported architecture. Those cybersecurity requirements shall aim to treat the identified cybersecurity risks and threats, as established in the risk register set out in Annex I.

2. In line with Article 5a(23) of Regulation (EU) No 910/2014, national certification schemes shall require wallet solutions, and the electronic identification schemes under which they are provided, to be resistant against attackers with high attack potential for assurance level high, as referred to Implementing Regulation (EU) 2015/1502.

3. National certification schemes shall establish security criteria, which shall include the following requirements:

| (a) | Cyber Resilience Act where applicable, or requirements meeting the security objectives set out in Article 51 of Regulation (EU) 2019/881; |
| --- | --- |

| (b) | the establishment and implementation of policies and procedures concerning the management of risks associated with the operation of a wallet solution, including the identification and assessment of risks and the mitigation of the identified risks; |
| --- | --- |

| (c) | the establishment and implementation of policies and procedures related to the management of changes and to the management of vulnerabilities in accordance with Article 5 of this Regulation; |
| --- | --- |

| (d) | the establishment and implementation of human resource management policies and procedures, including requirements on expertise, reliability, experience, security training, and qualifications of personnel involved in the development or operation of the wallet solution; |
| --- | --- |

| (e) | requirements relating to the wallet solution’s operating environment, including in the form of assumptions on the security of the devices and platforms on which the software components of the wallet solution run, including WSCDs and where applicable and relevant, conformity assessment requirements to confirm that those assumptions are verified on the relevant devices and platforms; |
| --- | --- |

| (f) | for each assumption that is not backed by a certificate of conformity or other acceptable assurance information, a description of the mechanism that the wallet provider uses to enforce the assumption, as well as a justification that the mechanism is sufficient to ensure that the assumption is verified; |
| --- | --- |

| (g) | the establishment and implementation of measures to ensure the use of a currently certified version of the wallet solution. |
| --- | --- |

4. National certification schemes shall contain functional requirements relating to update mechanisms for every software component of the wallet solutions and the electronic identification scheme under which they are provided for the operations listed in Annex III.

5. National certification schemes shall require that the following information and documentation is provided or otherwise made available to the certification body by the applicant for certification:

| (a) | evidence related to the information referred to in Annex IV, point 1, including where necessary details on the wallet solution and its source code, including:—architecture information: for every component of the wallet solution (including product, process and service components), a description of its essential security properties, including its external dependencies;—controls and assurance levels: for every security control of the wallet solution, a description of the control and the required assurance level, based on the Annex to Implementing Regulation (EU) 2015/1502, which sets out a number of technical specifications and procedures that apply to the various controls implemented by the electronic identification means;—mapping the controls to architecture components: a description of how the controls of the wallet are implemented using the different components of the wallet solution, based on a rationale explaining why a given assurance level is required, and how the control is implemented with all required security aspects at the appropriate level;—rationale and justification of risk coverage: a justification of:—the mapping of controls to components;—the suitability of the proposed evaluation plan to appropriately cover all controls;—the coverage provided by the controls of the cybersecurity risks and threats identified in the risk register, complemented by controls of risks and threats specific to the implementation, at the appropriate assurance level; |
| --- | --- |
| — | architecture information: for every component of the wallet solution (including product, process and service components), a description of its essential security properties, including its external dependencies; |
| — | controls and assurance levels: for every security control of the wallet solution, a description of the control and the required assurance level, based on the Annex to Implementing Regulation (EU) 2015/1502, which sets out a number of technical specifications and procedures that apply to the various controls implemented by the electronic identification means; |
| — | mapping the controls to architecture components: a description of how the controls of the wallet are implemented using the different components of the wallet solution, based on a rationale explaining why a given assurance level is required, and how the control is implemented with all required security aspects at the appropriate level; |
| — | rationale and justification of risk coverage: a justification of:—the mapping of controls to components;—the suitability of the proposed evaluation plan to appropriately cover all controls;—the coverage provided by the controls of the cybersecurity risks and threats identified in the risk register, complemented by controls of risks and threats specific to the implementation, at the appropriate assurance level; |
| — | the mapping of controls to components; |
| — | the suitability of the proposed evaluation plan to appropriately cover all controls; |
| — | the coverage provided by the controls of the cybersecurity risks and threats identified in the risk register, complemented by controls of risks and threats specific to the implementation, at the appropriate assurance level; |

| (b) | the information listed in Annex V; |
| --- | --- |

| (c) | a complete list of the certificates of conformity and other assurance information used as evidence during the evaluation activities; |
| --- | --- |

| (d) | any other information relevant for the evaluation activities. |
| --- | --- |

<a id="art_9"></a>

### art_9

Article 9

1. Certification bodies shall be accredited by national accreditation bodies appointed pursuant to Regulation (EC) No 765/2008 of the European Parliament and of the Council (13) in accordance with EN ISO/IEC 17065:2012, provided that they comply with the requirements set out in national certification schemes in accordance with paragraph 2.

2. For the purposes of accreditation, certification bodies shall comply with all the following competence requirements:

| (a) | detailed and technical knowledge of the relevant architectures of a wallet solution and of the electronic identification scheme under which they are provided, as well as of the threats and risks relevant to those architectures; |
| --- | --- |

| (b) | knowledge of available security solutions and of their properties pursuant to the Annex of Implementing Regulation (EU) 2015/1502; |
| --- | --- |

| (c) | knowledge of the activities performed in virtue of certificates of conformity applied to components of the wallet solution and the electronic identification scheme under which they are provided, as being the object of certification; |
| --- | --- |

| (d) | detailed knowledge of the applicable national certification scheme as established in accordance with Chapter II. |
| --- | --- |

3. Certification bodies shall perform their surveillance activities in particular on the basis of the following information:

| (a) | information coming from national accreditation bodies, and relevant market surveillance authorities; |
| --- | --- |

| (b) | information resulting from their own or another authority’s audits and investigations; |
| --- | --- |

| (c) | complaints and appeals received pursuant to Article 15. |
| --- | --- |

<a id="art_10"></a>

### art_10

Article 10

Certification bodies may subcontract the evaluation activities, as set out in Article 13, to third parties. Where evaluation activities are subcontracted, national certification schemes shall establish the following:

| (1) | all subcontractors of the certification body performing evaluation activities shall, as applicable and appropriate for the activities to be performed, meet the requirements of harmonised standards like EN ISO/IEC 17025:2017 for testing, EN ISO/IEC 17020:2012 for inspection, EN ISO/IEC 17021-1:2015 for audit, and EN ISO/IEC 17029:2019 for validation and verification; |
| --- | --- |

| (2) | certification bodies shall take responsibility for all evaluation activities outsourced to other bodies and demonstrate that they have taken appropriate measures during their accreditation, including by relying on their subcontractors’ own accreditation, when applicable; |
| --- | --- |

| (3) | the degree to which prior agreement to outsourcing needs shall be obtained from scheme owners or the client whose wallet solution is being certified under the certification scheme. |
| --- | --- |

<a id="art_11"></a>

### art_11

Article 11

Certification bodies shall notify the supervisory body referred to in Article 46a(1) of Regulation (EU) No 910/2014 of the issuance, suspension and cancellation of certificates of conformity of wallet solutions and the electronic identification scheme under which they are provided.

<a id="art_12"></a>

### art_12

Article 12

1. Certification bodies shall suspend, without undue delay, the certificate of conformity of the wallet solutions and the electronic identification scheme under which they are provided after they confirm that the notified security breach or compromise impacts the conformity with the national certification schemes’ requirements, of the wallet solution or of the electronic identification scheme under which they are provided.

2. Certification bodies shall cancel the certificate of conformity that has been suspended following a security breach or compromise that has not been remedied in a timely manner.

3. Certification bodies shall cancel certificates of conformity where an identified vulnerability has not been remedied commensurately with its severity and potential impact in a timely manner, in accordance with Articles 5c(4) and 5e(2) of Regulation (EU) No 910/2014.

<a id="art_13"></a>

### art_13

Article 13

1. National certification schemes shall contain methods and procedures to be used by the conformity assessment bodies when conducting their evaluation activities in accordance with EN ISO/IEC 17065:2012, which shall cover at least the following aspects:

| (a) | the methods and procedures to conduct evaluation activities, including those related to WSCD, as set out in Annex IV; |
| --- | --- |

| (b) | the audit of the implementation of the wallet solution and the electronic identification scheme under which they are provided, based on the risk register, set out in Annex I and complemented where necessary by implementation-specific risks; |
| --- | --- |

| (c) | functional testing activities, based, when available and appropriate, on test suites that are defined according to technical specifications or standards; |
| --- | --- |

| (d) | assessment of the existence and suitability of maintenance processes, including at least version management, update management and vulnerability management; |
| --- | --- |

| (e) | assessment of the operating effectiveness of the maintenance processes, including at least version management, update management and vulnerability management; |
| --- | --- |

| (f) | dependency analysis provided by the wallet provider, including a methodology to assess the acceptability of assurance information, which shall include the elements set out in Annex VI; |
| --- | --- |

| (g) | vulnerability assessment, at the appropriate level, including:—a review of the design of the wallet solution, and where applicable, of its source code;—testing of the resistance of the wallet solution against attackers with high attack potential for assurance level ‘high’ pursuant to Section 2.2.1 of the Annex to Implementing Regulation (EU) 2015/1502; |
| --- | --- |
| — | a review of the design of the wallet solution, and where applicable, of its source code; |
| — | testing of the resistance of the wallet solution against attackers with high attack potential for assurance level ‘high’ pursuant to Section 2.2.1 of the Annex to Implementing Regulation (EU) 2015/1502; |

| (h) | assessment of the evolution of the threat environment and its impact on the coverage of the risks by the wallet solution, to determine which evaluation activities are required on the various components of the wallet solution. |
| --- | --- |

2. National certification schemes shall contain an evaluation to determine whether the implementation of wallet solutions and the electronic identification scheme under which those wallet solutions are provided match the architecture set out in Article 3 paragraph 5, point (a), as well as an evaluation to determine whether the evaluation plan proposed together with the implementation matches the evaluation plan referred to in Article 3 paragraph 5, point (c).

3. National certification schemes shall set out sampling rules, in order to avoid the repetition of identical evaluation activities and to focus on activities that are specific to a given variant. Those sampling rules shall allow functional and security tests to be performed only on a sample of variants of a target component of a wallet solution and the electronic identification scheme under which they a provided and on a sample of target devices. National certification schemes shall require all certification bodies to justify their use of sampling.

4. National certification schemes shall require the evaluation, by the certification body, of the WSCA based on the methods and procedures set out in Annex IV.

<a id="art_14"></a>

### art_14

Article 14

1. National certification schemes shall set out an attestation activity for the purpose of issuing a certificate of conformity, in accordance with section V(a) of EN ISO/IEC 17067:2013, Table 1, including the following aspects:

| (a) | the content of the certificate of conformity as set out in Annex VII; |
| --- | --- |

| (b) | how the results of the evaluation are to be reported in the public certification report, including at least a summary of the preliminary audit and validation plan, as set out in Annex VIII; |
| --- | --- |

| (c) | the content of the evaluation results reported in the certification assessment report, including the elements set out in Annex VIII. |
| --- | --- |

2. The certification assessment report may be made available to the Cooperation Group and to the Commission.

<a id="art_15"></a>

### art_15

Article 15

National certification schemes shall contain procedures or references to the applicable national legislation, which define the mechanism to effectively lodge and handle complaints and appeals in relation to their implementation of the certification scheme or to a certificate of conformity issued. These procedures shall include the provision of information to the complainant of the progress of the proceedings and on the decision taken, and information to the complainant on the right to an effective judicial remedy. National certification schemes shall require that all complaints and appeals that have not been or cannot be resolved by the certification body are sent to the scheme owner for assessment and resolution.

<a id="art_16"></a>

### art_16

Article 16

1. National certification schemes shall require certification bodies to implement surveillance activities consisting of surveillance evaluation of processes combined with random tests or inspections.

2. National certification schemes shall contain requirements for scheme owners to monitor the compliance of certification bodies with their obligations pursuant to Regulation (EU) No 910/2014 and pursuant to national certification schemes, if applicable.

3. National certification schemes shall contain requirements for certification bodies to monitor the following:

| (a) | compliance by holders of a certificate of conformity issued under national certification schemes with their obligations concerning certification pursuant to Regulation (EU) No 910/2014 and pursuant to national certification schemes; |
| --- | --- |

| (b) | compliance of the certified wallet solution with the requirements set out in national certification schemes. |
| --- | --- |

<a id="art_17"></a>

### art_17

Article 17

National certification schemes shall set out the consequences of non-conformity of a certified wallet solution and of the electronic identification scheme under which they are provided, with the requirements set out in this Regulation. Those consequences shall include the following aspects:

| (1) | the obligation on the certification body to inform the holder of the certificate of conformity and to request the holder of the certificate of conformity to apply remedial actions; |
| --- | --- |

| (2) | the obligation on the certification body to inform other relevant market surveillance authorities where the non-conformity concerns relevant Union legislation; |
| --- | --- |

| (3) | the conditions for carrying out remedial actions by the holder of the certificate of conformity; |
| --- | --- |

| (4) | the conditions for the suspension of a certificate of conformity by the certification body and for restoration of the certificate of conformity after the non-conformity has been remediated; |
| --- | --- |

| (5) | the conditions for cancellation of a certificate of conformity by the certification body; |
| --- | --- |

| (6) | the consequences of non-compliance by the certification body with the requirements of the national certification scheme. |
| --- | --- |

<a id="art_18"></a>

### art_18

Article 18

1. The validity of certificates of conformity issued under national certification schemes shall be subject to regular evaluation activities by the certification body carried out in accordance with the requirements set out in Annex IX.

2. National certification schemes shall contain a process for the recertification of wallet solutions and the electronic identification scheme under which they are provided, upon request of the holder of the certificate of conformity before the expiry of the initial certificate of conformity. That process for recertification shall include a full evaluation of the wallet solution and of the electronic identification scheme under which they are provided, including a vulnerability assessment, following the principles set out in Annex IX.

3. National certification schemes shall contain a process for managing changes in a certified wallet solution and the electronic identification scheme under which they are provided. That process shall include rules for determining whether a change is to be covered by a special evaluation as referred to in paragraph 4 or by the verification of the operating effectiveness of the maintenance processes as referred to Annex IV.

4. National certification schemes shall contain a process for special evaluations in accordance with EN ISO/IEC 17065:2012. That process for special evaluations shall include a selection of activities to be performed to address the specific issue that triggered the special evaluation.

5. National certification schemes shall set out rules related to the cancellation of a certificate of conformity.

<a id="art_19"></a>

### art_19

Article 19

1. National certification schemes shall contain requirements for certification bodies concerning a record system for all relevant information produced in connection with the conformity assessment activities that they perform, including data issued and received by providers of wallet solutions and the electronic identification schemes under which they are provided. The records of such information shall be stored in a secure manner. The records may be kept electronically and shall remain accessible for as long as required by Union law or national law, and for at least five years, after the cancellation or expiry of the relevant certificate of conformity.

2. National certification schemes shall set out requirements for the holder of the certificate of conformity to store the following information securely for the purpose of this Regulation, and for at least five years after the cancellation or expiry of the relevant certificate of conformity:

| (a) | records of the information provided to the certification body or any of its sub-contractors during the certification process; |
| --- | --- |

| (b) | specimens of hardware components that have been included in the scope of certification for the wallet solution. |
| --- | --- |

3. National certification schemes shall require the holder of the certificate of conformity to make the information referred to in paragraph 1 available to the certification body or the supervisory body referred to in Article 46a(1) of Regulation (EU) No 910/2014 upon request.

<a id="art_20"></a>

### art_20

Article 20

Under national certification schemes, all persons or organisations that are granted access to information in the execution of activities under the national certification scheme shall be required to ensure the security and protection of trade secrets and other confidential information, as well as preserving intellectual property rights, and take the necessary and appropriate technical and organisational measures to ensure this confidentiality.

<a id="art_21"></a>

### art_21

Article 21

This Regulation shall be subject to review, on the adoption of the first European cybersecurity certification scheme for wallet solutions and the electronic identification schemes under which they are provided, with the objective of taking into account the contribution of such a European cybersecurity certification scheme to the overall certification of wallet solutions and the electronic identification schemes under which they are provided.

<a id="art_22"></a>

### art_22

Article 22

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
