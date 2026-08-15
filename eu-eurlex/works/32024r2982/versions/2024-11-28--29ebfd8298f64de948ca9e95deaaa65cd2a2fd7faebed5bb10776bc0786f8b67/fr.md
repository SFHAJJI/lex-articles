---
lex_id: 'eu-eurlex:32024r2982:2024-11-28--29ebfd8298f64de948ca9e95deaaa65cd2a2fd7faebed5bb10776bc0786f8b67'
title: 'Commission Implementing Regulation (EU) 2024/2982 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014'
valid_from: '2024-11-28'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2982'
source_sha256: '45abc3829002498e0c68f2d715eb7dc5209de32032b7b49cfcbe9f9fed9d54db'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article premier

Le présent règlement fixe des règles relatives aux protocoles et aux interfaces des solutions de portefeuille concernant:

| 1) | la délivrance de données d’identification personnelle et d’attestations électroniques d’attributs aux unités de portefeuille; |
| --- | --- |

| 2) | la présentation des attributs des données d’identification personnelle et des attestations électroniques d’attributs aux parties utilisatrices de portefeuille et à d’autres unités de portefeuille; |
| --- | --- |

| 3) | la communication des demandes d’effacement de données aux parties utilisatrices de portefeuille; |
| --- | --- |

| 4) | le signalement des parties utilisatrices de portefeuille aux autorités de contrôle instituées en vertu de l’article 51 du règlement (UE) 2016/679.Le présent règlement est mis à jour régulièrement pour tenir compte de l’évolution des technologies et des normes ainsi que des travaux réalisés sur la base de la recommandation (UE) 2021/946, et en particulier sur l’architecture et le cadre de référence. |
| --- | --- |

<a id="art_2"></a>

### art_2

Article 2

Aux fins du présent règlement, on entend par:

| 1) | «partie utilisatrice de portefeuille»: une partie utilisatrice qui a l’intention de se fier à des unités de portefeuille pour la fourniture de services publics ou privés au moyen d’une interaction numérique; |
| --- | --- |

| 2) | «utilisateur de portefeuille»: un utilisateur qui contrôle l’unité de portefeuille; |
| --- | --- |

| 3) | «solution de portefeuille»: une combinaison de logiciels, de matériel, de services, de paramètres et de configurations, y compris des instances de portefeuille, une ou plusieurs applications cryptographiques sécurisées de portefeuille et un ou plusieurs dispositifs cryptographiques sécurisés de portefeuille; |
| --- | --- |

| 4) | «unité de portefeuille»: une configuration unique d’une solution de portefeuille comprenant des instances de portefeuille, des applications cryptographiques sécurisées de portefeuille et des dispositifs cryptographiques sécurisés de portefeuille, fournie par un fournisseur de portefeuille à un utilisateur de portefeuille donné; |
| --- | --- |

| 5) | «fournisseur de portefeuille»: une personne physique ou morale qui fournit des solutions de portefeuille; |
| --- | --- |

| 6) | «instance de portefeuille»: l’application installée et configurée sur l’appareil ou dans l’environnement d’un utilisateur de portefeuille, qui fait partie d’une unité de portefeuille et dont l’utilisateur de portefeuille se sert pour interagir avec l’unité de portefeuille; |
| --- | --- |

| 7) | «application cryptographique sécurisée de portefeuille»: une application qui gère des actifs critiques en étant liée aux fonctions cryptographiques et non cryptographiques fournies par le dispositif cryptographique sécurisé de portefeuille et en utilisant ces fonctions; |
| --- | --- |

| 8) | «dispositif cryptographique sécurisé de portefeuille»: un dispositif inviolable qui fournit un environnement lié à l’application cryptographique sécurisée de portefeuille et utilisé par celle-ci pour protéger les actifs critiques et fournir des fonctions cryptographiques pour l’exécution sécurisée d’opérations critiques; |
| --- | --- |

| 9) | «actifs critiques»: les actifs se trouvant à l’intérieur d’une unité de portefeuille ou en rapport avec celle-ci et dont l’importance est tellement exceptionnelle que la capacité de se fier à l’unité de portefeuille serait très sérieusement affaiblie si leur disponibilité, leur confidentialité ou leur intégrité étaient compromises; |
| --- | --- |

| 10) | «certificat d’accès de partie utilisatrice de portefeuille»: un certificat de cachet électronique ou de signature électronique qui authentifie et valide la partie utilisatrice de portefeuille et qui est délivré par un fournisseur de certificats d’accès de partie utilisatrice de portefeuille; |
| --- | --- |

| 11) | «fournisseur de certificats d’accès de partie utilisatrice de portefeuille»: une personne physique ou morale mandatée par un État membre pour délivrer des certificats d’accès de partie utilisatrice aux parties utilisatrices de portefeuille enregistrées dans cet État membre; |
| --- | --- |

| 12) | «attestation d’unité de portefeuille»: un objet de données qui décrit les composants de l’unité de portefeuille ou permet l’authentification et la validation de ces composants; |
| --- | --- |

| 13) | «politique de divulgation intégrée»: un ensemble de règles, intégrées dans une attestation électronique d’attributs par son fournisseur, qui indique les conditions qu’une partie utilisatrice de portefeuille doit remplir pour accéder à l’attestation électronique d’attributs; |
| --- | --- |

| 14) | «certificat d’enregistrement de partie utilisatrice de portefeuille»: un objet de données qui indique les attributs pour lesquels la partie utilisatrice a enregistré son intention de les demander aux utilisateurs; |
| --- | --- |

| 15) | «fournisseur de données d’identification personnelle»: une personne physique ou morale chargée de délivrer et de révoquer les données d’identification personnelle et de veiller à ce que les données d’identification personnelle d’un utilisateur soient liées de manière cryptographique à une unité de portefeuille; |
| --- | --- |

| 16) | «liaison cryptographique»: la méthode permettant de lier les données d’identification personnelle ou les attestations électroniques d’attributs aux unités de portefeuille à l’aide de moyens cryptographiques. |
| --- | --- |

<a id="art_3"></a>

### art_3

Article 3

Concernant les protocoles et les interfaces visés aux articles 4 et 5, les fournisseurs de portefeuille veillent à ce que les unités de portefeuille:

| 1) | authentifient et valident les certificats d’accès de partie utilisatrice de portefeuille lors d’interactions avec des parties utilisatrices de portefeuille; |
| --- | --- |

| 2) | authentifient et valident les attestations d’unité de portefeuille d’autres unités de portefeuille lors d’interactions avec d’autres unités de portefeuille; |
| --- | --- |

| 3) | authentifient et valident les demandes introduites au moyen de certificats d’accès de partie utilisatrice de portefeuille ou d’attestations d’unité de portefeuille correspondant à d’autres unités de portefeuille, le cas échéant; |
| --- | --- |

| 4) | authentifient et valident le certificat d’enregistrement de partie utilisatrice de portefeuille, le cas échéant; |
| --- | --- |

| 5) | affichent aux utilisateurs de portefeuille les informations contenues dans les certificats d’accès de partie utilisatrice de portefeuille ou dans les attestations d’unité de portefeuille; |
| --- | --- |

| 6) | affichent aux utilisateurs de portefeuille, le cas échéant, les attributs que ceux-ci sont tenus de présenter; |
| --- | --- |

| 7) | affichent aux utilisateurs de portefeuille, le cas échéant, les informations contenues dans le certificat d’enregistrement de partie utilisatrice de portefeuille; |
| --- | --- |

| 8) | présentent les attestations d’unité de portefeuille de l’unité de portefeuille aux parties utilisatrices de portefeuille ou aux unités de portefeuille qui en font la demande; |
| --- | --- |

| 9) | ne présentent aucun attribut demandé aux parties utilisatrices de portefeuille ou aux unités de portefeuille tant que les exigences suivantes ne sont pas remplies:a)il a été vérifié que l’application cryptographique sécurisée de portefeuille a authentifié l’identité de l’utilisateur de portefeuille;b)il a été vérifié que les politiques de divulgation intégrées ont été traitées au sein de l’unité de portefeuille conformément à l’article 11 du règlement d’exécution (UE) 2024/2979, le cas échéant;c)il a été vérifié que les utilisateurs de portefeuille ont approuvé partiellement ou intégralement la présentation; |
| --- | --- |
| a) | il a été vérifié que l’application cryptographique sécurisée de portefeuille a authentifié l’identité de l’utilisateur de portefeuille; |
| b) | il a été vérifié que les politiques de divulgation intégrées ont été traitées au sein de l’unité de portefeuille conformément à l’article 11 du règlement d’exécution (UE) 2024/2979, le cas échéant; |
| c) | il a été vérifié que les utilisateurs de portefeuille ont approuvé partiellement ou intégralement la présentation; |

| 10) | permettent des techniques de protection de la vie privée qui garantissent la non-associabilité lorsque les attestations électroniques d’attributs n’exigent pas l’identification de l’utilisateur de portefeuille au moment de la présentation d’attestations ou de données d’identification personnelle entre différentes parties utilisatrices de portefeuille. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

1. Les fournisseurs de portefeuille veillent à ce que les solutions de portefeuille prennent en charge les protocoles et les interfaces permettant la délivrance de données d’identification personnelle et d’attestations électroniques d’attributs aux unités de portefeuille.

2. Les fournisseurs de portefeuille veillent à ce que les unités de portefeuille ne demandent la délivrance de données d’identification personnelle et d’attestations électroniques d’attributs qu’à des parties disposant d’un certificat d’accès de partie utilisatrice de portefeuille authentique et valide attestant qu’elles sont:

| a) | un fournisseur de données d’identification personnelle; |
| --- | --- |

| b) | un fournisseur d’une attestation électronique d’attributs qualifiée; |
| --- | --- |

| c) | un fournisseur d’une attestation électronique d’attributs délivrée par un organisme du secteur public responsable d’une source authentique ou pour son compte; ou |
| --- | --- |

| d) | un fournisseur d’attestations électroniques d’attributs non qualifiées. |
| --- | --- |

3. En ce qui concerne la délivrance de données d’identification personnelle et d’attestations électroniques d’attributs à une unité de portefeuille, les fournisseurs de portefeuille veillent à ce que les exigences suivantes soient respectées:

| a) | lorsque les utilisateurs de portefeuille se servent de leur unité de portefeuille pour demander la délivrance de données d’identification personnelle ou d’attestations électroniques d’attributs à des fournisseurs de données d’identification personnelle ou à des fournisseurs d’attestations électroniques d’attributs qui permettent la délivrance de données d’identification personnelle ou d’attestations électroniques dans plusieurs formats, l’unité de portefeuille en fait la demande dans tous les formats visés à l’article 8 du règlement d’exécution (UE) 2024/2979 portant modalités d’application du règlement (UE) no 910/2014 en ce qui concerne l’intégrité et les fonctionnalités essentielles des portefeuilles européens d’identité numérique; |
| --- | --- |

| b) | lorsque les utilisateurs de portefeuille se servent de leur unité de portefeuille pour interagir avec des fournisseurs de données d’identification personnelle ou des fournisseurs d’attestations électroniques d’attributs, les unités de portefeuille permettent l’authentification et la validation des composants de l’unité de portefeuille en présentant les attestations d’unité de portefeuille à ces fournisseurs à leur demande; |
| --- | --- |

| c) | les solutions de portefeuille prennent en charge les mécanismes qui permettent aux fournisseurs de données d’identification personnelle de vérifier la délivrance, la mise à disposition et l’activation conformément aux exigences en matière de niveau de garantie élevé énoncées dans le règlement d’exécution (UE) 2015/1502 de la Commission (11); |
| --- | --- |

| d) | les unités de portefeuille vérifient l’authenticité et la validité des données d’identification personnelle et des attestations électroniques d’attributs. |
| --- | --- |

<a id="art_5"></a>

### art_5

Article 5

1. Les fournisseurs de portefeuille veillent à ce que les solutions de portefeuille prennent en charge les protocoles et les interfaces permettant la présentation d’attributs aux parties utilisatrices de portefeuille, à distance et, le cas échéant, à proximité, conformément aux normes énumérées en annexe.

2. Les fournisseurs de portefeuille veillent à ce que, à la demande des utilisateurs, les unités de portefeuille répondent aux demandes dûment authentifiées et validées des parties utilisatrices de portefeuille mentionnées à l’article 3, conformément aux normes énumérées en annexe.

3. Les fournisseurs de portefeuille veillent à ce que les unités de portefeuille permettent d’apporter la preuve qu’elles détiennent les clés privées correspondant aux clés publiques utilisées dans les liaisons cryptographiques.

4. Les fournisseurs de portefeuille veillent à ce que les solutions de portefeuille prennent en charge la divulgation sélective d’attributs de données d’identification personnelle et d’attestations électroniques d’attributs.

5. Les paragraphes 1 à 4 s’appliquent mutatis mutandis aux interactions entre deux unités de portefeuille qui se trouvent à proximité l’une de l’autre.

<a id="art_6"></a>

### art_6

Article 6

1. Les fournisseurs de portefeuille veillent à ce que les unités de portefeuille prennent en charge les protocoles et les interfaces permettant aux utilisateurs de portefeuille de demander aux parties utilisatrices de portefeuille avec lesquelles ils ont interagi au moyen de ces unités de portefeuille d’effacer leurs données à caractère personnel fournies par l’intermédiaire de ces unités de portefeuille, conformément à l’article 17 du règlement (UE) 2016/679.

2. Les protocoles et les interfaces visés au paragraphe 1 permettent aux utilisateurs de portefeuille de sélectionner les parties utilisatrices de portefeuille à qui doivent être présentées les demandes d’effacement de données.

3. Les unités de portefeuille permettent à l’utilisateur de portefeuille de visualiser les demandes d’effacement de données précédemment soumises par leur intermédiaire.

<a id="art_7"></a>

### art_7

Article 7

1. Les fournisseurs de portefeuille veillent à ce que les unités de portefeuille permettent aux utilisateurs de portefeuille de signaler facilement des parties utilisatrices de portefeuille aux autorités de contrôle instituées en vertu de l’article 51 du règlement (UE) 2016/679.

2. Les fournisseurs de portefeuille mettent en œuvre les protocoles et les interfaces de signalement des parties utilisatrices de portefeuille conformément au droit procédural national des États membres.

3. Les fournisseurs de portefeuille veillent à ce que les unités de portefeuille permettent aux utilisateurs de portefeuille d’étayer leurs signalements, notamment en joignant des informations pertinentes permettant d’identifier les parties utilisatrices de portefeuille, et les propres déclarations dans un format lisible par la machine.

<a id="art_8"></a>

### art_8

Article 8

Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
