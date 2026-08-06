---
lex_id: 'eu-eurlex:32024r2979:2024-11-28'
title: 'Commission Implementing Regulation (EU) 2024/2979 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014'
valid_from: '2024-11-28'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2979'
source_sha256: '646c7b2ddcb4c11f81d1bc07cd3c089d3899903c13ab1221f2155b037f950c26'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article premier

Le présent règlement établit les règles relatives à l’intégrité et aux fonctionnalités essentielles des portefeuilles, qui sont mises à jour régulièrement pour tenir compte de l’évolution des technologies et des normes ainsi que des travaux réalisés sur la base de la recommandation (UE) 2021/946, dont l’architecture et le cadre de référence.

<a id="art_2"></a>

### art_2

Article 2

Aux fins du présent règlement, on entend par:

| 1) | «application cryptographique sécurisée de portefeuille»: une application qui gère des actifs critiques en étant liée aux fonctions cryptographiques et non cryptographiques fournies par le dispositif cryptographique sécurisé de portefeuille et en utilisant ces fonctions; |
| --- | --- |

| 2) | «unité de portefeuille»: une configuration unique d’une solution de portefeuille comprenant des instances de portefeuille, des applications cryptographiques sécurisées de portefeuille et des dispositifs/éléments cryptographiques sécurisés de portefeuille fournie à un utilisateur de portefeuille donné par un fournisseur de portefeuilles; |
| --- | --- |

| 3) | «actifs critiques»: les actifs se trouvant à l’intérieur d’une unité de portefeuille ou en rapport avec celle-ci et dont l’importance est tellement exceptionnelle que la capacité à utiliser l’unité de portefeuille serait très sérieusement affaiblie si leur disponibilité, leur confidentialité ou leur intégrité étaient compromises; |
| --- | --- |

| 4) | «fournisseur de données d’identification personnelle»: une personne physique ou morale chargée de délivrer et de révoquer les données d’identification personnelle et de veiller à ce que les données d’identification personnelle d’un utilisateur soient cryptographiquement liées à une unité de portefeuille; |
| --- | --- |

| 5) | «utilisateur de portefeuille»: un utilisateur qui contrôle l’unité de portefeuille; |
| --- | --- |

| 6) | «partie utilisatrice de portefeuille»: une partie utilisatrice qui a l’intention de se fier à des unités de portefeuille pour fournir des services publics ou privés au moyen d’une interaction numérique; |
| --- | --- |

| 7) | «fournisseur de portefeuille»: une personne physique ou morale qui fournit des solutions de portefeuille; |
| --- | --- |

| 8) | «attestation d’unité de portefeuille»: un objet de données qui décrit les composants de l’unité de portefeuille ou permet l’authentification et la validation de ces composants; |
| --- | --- |

| 9) | «politique de divulgation intégrée»: un ensemble de règles, intégrées dans une attestation électronique d’attributs par son fournisseur, qui indique les conditions qu’une partie utilisatrice de portefeuille doit remplir pour accéder à l’attestation électronique d’attributs; |
| --- | --- |

| 10) | «instance de portefeuille»: l’application installée et configurée sur l’appareil ou dans l’environnement d’un utilisateur de portefeuille, qui fait partie d’une unité de portefeuille, et dont l’utilisateur du portefeuille se sert pour interagir avec l’unité de portefeuille; |
| --- | --- |

| 11) | «solution de portefeuille»: une combinaison de logiciels, de matériel, de services, de paramètres et de configurations, y compris des instances de portefeuille, une ou plusieurs applications cryptographiques sécurisées de portefeuille et un ou plusieurs dispositifs cryptographiques sécurisés de portefeuille; |
| --- | --- |

| 12) | «dispositif cryptographique sécurisé de portefeuille»: un dispositif inviolable qui fournit un environnement lié à l’application cryptographique sécurisée de portefeuille et utilisé par celle-ci pour protéger les actifs critiques et fournir des fonctions cryptographiques pour l’exécution sécurisée d’opérations critiques; |
| --- | --- |

| 13) | «opération cryptographique de portefeuille»: un mécanisme cryptographique nécessaire dans le cadre de l’authentification de l’utilisateur du portefeuille et de la délivrance ou présentation de données d’identification personnelle ou d’attestations électroniques d’attributs; |
| --- | --- |

| 14) | «certificat d’accès de partie utilisatrice de portefeuille»: un certificat de cachet électronique ou de signature électronique authentifiant et validant la partie utilisatrice de portefeuille, délivré par un fournisseur de certificats d’accès de partie utilisatrice de portefeuille; |
| --- | --- |

| 15) | «fournisseur de certificats d’accès de partie utilisatrice de portefeuille»: une personne physique ou morale mandatée par un État membre pour délivrer des certificats d’accès de partie utilisatrice aux parties utilisatrices de portefeuille enregistrées dans cet État membre. |
| --- | --- |

<a id="art_3"></a>

### art_3

Article 3

1. Les unités de portefeuille n’exécutent aucune des fonctionnalités énumérées à l’article 5 bis, paragraphe 4, du règlement (UE) no 910/2014, sauf l’authentification de l’utilisateur de portefeuille pour accéder à l’unité de portefeuille, tant que l’unité de portefeuille n’a pas authentifié l’utilisateur du portefeuille.

2. Pour chaque unité de portefeuille, les fournisseurs de portefeuille apposent une signature ou un cachet sur au moins une attestation d’unité de portefeuille conforme aux exigences énoncées à l’article 6. Le certificat utilisé pour apposer une signature ou un cachet sur l’attestation d’unité de portefeuille est délivré sur la foi d’un certificat figurant sur la liste de confiance visée dans le règlement d’exécution (UE) 2024/2980.

<a id="art_4"></a>

### art_4

Article 4

1. Les instances de portefeuille utilisent au moins un dispositif cryptographique sécurisé de portefeuille pour gérer les actifs critiques.

2. Les fournisseurs de portefeuille garantissent l’intégrité, l’authenticité et la confidentialité de la communication entre les instances de portefeuille et les applications cryptographiques sécurisées de portefeuille.

3. Lorsque des actifs critiques sont liés à l’exécution d’une identification électronique à un niveau de garantie élevé, les opérations cryptographiques de portefeuille ou autres opérations de traitement des actifs critiques sont effectuées conformément aux exigences relatives aux caractéristiques et à la conception des moyens d’identification électronique à un niveau de garantie élevé, telles qu’elles sont énoncées dans le règlement d’exécution (UE) 2015/1502 de la Commission (11).

<a id="art_5"></a>

### art_5

Article 5

1. Les fournisseurs de portefeuille veillent à ce que les applications cryptographiques sécurisées de portefeuille:

| a) | n’effectuent d’opérations cryptographiques de portefeuille impliquant des actifs critiques autres que celles nécessaires pour que l’unité de portefeuille authentifie l’utilisateur de portefeuille que dans les cas où lesdites applications ont dûment authentifié les utilisateurs de portefeuille; |
| --- | --- |

| b) | lorsqu’elles authentifient des utilisateurs de portefeuille dans le cadre d’une identification électronique à un niveau de garantie élevé, procèdent à l’authentification des utilisateurs de portefeuille conformément aux exigences relatives aux caractéristiques et à la conception des moyens d’identification électronique à un niveau de garantie élevé, telles qu’elles sont énoncées dans le règlement d’exécution (UE) 2015/1502; |
| --- | --- |

| c) | sont capables de générer de manière sécurisée de nouvelles clés cryptographiques; |
| --- | --- |

| d) | sont capables de procéder à l’effacement sécurisé d’actifs critiques; |
| --- | --- |

| e) | sont capables de générer une preuve de la possession de clés privées; |
| --- | --- |

| f) | protègent les clés privées qu’elles ont générées pendant la durée d’existence des clés; |
| --- | --- |

| g) | satisfont aux exigences relatives aux caractéristiques et à la conception des moyens d’identification électronique à un niveau de garantie élevé, telles qu’elles sont énoncées dans le règlement d’exécution (UE) 2015/1502; |
| --- | --- |

| h) | sont les seuls composants capables d’exécuter des opérations cryptographiques de portefeuille et toute autre opération impliquant des actifs critiques dans le cadre d’une identification électronique à un niveau de garantie élevé. |
| --- | --- |

2. Lorsque les fournisseurs de portefeuille décident de fournir une application cryptographique sécurisée de portefeuille à un élément sécurisé intégré, ils fondent leur solution technique sur les spécifications techniques énumérées à l’annexe I ou sur d’autres spécifications techniques équivalentes.

<a id="art_6"></a>

### art_6

Article 6

1. Les fournisseurs de portefeuille veillent à ce que chaque unité de portefeuille contienne des attestations d’unités de portefeuille.

2. Les fournisseurs de portefeuille veillent à ce que les attestations d’unités de portefeuille visées au paragraphe 1 contiennent des clés publiques et que les clés privées correspondantes soient protégées par un dispositif cryptographique sécurisé de portefeuille.

3. Les fournisseurs de portefeuille:

| a) | informent les utilisateurs de portefeuille de leurs droits et obligations en ce qui concerne leur unité de portefeuille; |
| --- | --- |

| b) | prévoient des mécanismes, indépendants des unités de portefeuille, pour l’identification et l’authentification sécurisées des utilisateurs de portefeuille; |
| --- | --- |

| c) | veillent à ce que les utilisateurs de portefeuille aient le droit de demander la révocation de leurs attestations d’unités de portefeuille au moyen des mécanismes d’authentification visés au point b). |
| --- | --- |

<a id="art_7"></a>

### art_7

Article 7

1. Les fournisseurs de portefeuille sont les seules entités capables de révoquer les attestations d’unités de portefeuille pour les unités de portefeuille qu’ils ont fournies.

2. Les fournisseurs de portefeuille élaborent et mettent à la disposition du public une politique précisant les conditions et les délais de révocation des attestations d’unités de portefeuille.

3. Lorsque les fournisseurs de portefeuille révoquent des attestations d’unités de portefeuille, ils informent dans les 24 heures les utilisateurs de portefeuille concernés de la révocation de leurs unités de portefeuille, ainsi que de la raison de la révocation et des conséquences qui s’ensuivent pour l’utilisateur du portefeuille. Ces informations sont fournies de manière concise, facilement accessible et dans un langage clair et simple.

4. Lorsque les fournisseurs de portefeuille révoquent des attestations d’unités de portefeuille, ils mettent à la disposition du public le statut de validité de l’attestation d’unité de portefeuille, dans le respect de la vie privée, et décrivent la localisation de ces informations dans l’attestation d’unité de portefeuille.

<a id="art_8"></a>

### art_8

Article 8

Les fournisseurs de portefeuille veillent à ce que les solutions de portefeuille prennent en charge l’utilisation des données d’identification personnelle et des attestations électroniques d’attributs délivrées conformément à la liste de normes figurant à l’annexe II.

<a id="art_9"></a>

### art_9

Article 9

1. Que la transaction soit menée à bien ou non, les instances de portefeuille journalisent toutes les transactions avec les parties utilisatrices de portefeuille et les autres unités de portefeuille, y compris les signatures et cachets électroniques.

2. Les informations journalisées comprennent au moins:

| a) | la date et le lieu de la transaction; |
| --- | --- |

| b) | le nom, les coordonnées et l’identifiant unique de la partie utilisatrice de portefeuille correspondante ainsi que l’État membre dans lequel cette dernière est établie ou, dans le cas d’autres unités de portefeuille, les informations pertinentes provenant de l’attestation d’unité de portefeuille; |
| --- | --- |

| c) | le ou les types de données demandées et présentées dans la transaction; |
| --- | --- |

| d) | dans le cas d’opérations non achevées, la raison de cet inachèvement. |
| --- | --- |

3. Les fournisseurs de portefeuille garantissent l’intégrité, l’authenticité et la confidentialité des informations journalisées.

4. Les instances de portefeuille journalisent les rapports envoyés par l’utilisateur du portefeuille aux autorités chargées de la protection des données par l’intermédiaire de leur unité de portefeuille.

5. Les éléments journalisés visés aux paragraphes 1 et 2 sont accessibles au fournisseur de portefeuille, lorsqu’ils sont nécessaires à la fourniture de services de portefeuille, sur la base du consentement préalable explicite de l’utilisateur de portefeuille.

6. Les éléments journalisés visés aux paragraphes 1 et 2 restent accessibles aussi longtemps que le requiert le droit de l’Union ou le droit national.

7. Les fournisseurs de portefeuille permettent aux utilisateurs de portefeuille d’exporter les informations journalisées visées au paragraphe 2.

<a id="art_10"></a>

### art_10

Article 10

1. Les fournisseurs de portefeuille veillent à ce que les attestations électroniques d’attributs dotées de politiques de divulgation intégrées communes au sens de l’annexe III puissent être traitées par les unités de portefeuille qu’ils fournissent.

2. Les instances de portefeuille sont en mesure de traiter et de présenter ces politiques de divulgation intégrées visées au paragraphe 1 en combinaison avec les données reçues de la partie utilisatrice de portefeuille.

3. Les instances de portefeuille vérifient si la partie utilisatrice de portefeuille respecte les exigences de la politique de divulgation intégrée et informent l’utilisateur de portefeuille du résultat.

<a id="art_11"></a>

### art_11

Article 11

1. Les fournisseurs de portefeuille veillent à ce que les utilisateurs de portefeuille puissent recevoir les certificats qualifiés de signatures ou de cachets électroniques qualifiés qui sont liés à des dispositifs de création de signature ou de cachet qualifiés locaux, extérieurs ou distants par rapport aux instances de portefeuille.

2. Les fournisseurs de portefeuille veillent à ce que les solutions de portefeuille soient capables d’interagir de manière sécurisée avec l’un des types suivants de dispositifs de création de signature ou de cachet qualifiés: dispositifs de création de signature ou de cachet qualifiés locaux, externes ou gérés à distance aux fins de l’utilisation des certificats qualifiés visés au paragraphe 1.

3. Les fournisseurs de portefeuille veillent à ce que les utilisateurs de portefeuille qui sont des personnes physiques disposent, au moins à des fins non professionnelles, d’un accès gratuit aux applications de création de signature permettant la création de signatures électroniques qualifiées gratuites au moyen des certificats visés au paragraphe 1.

<a id="art_12"></a>

### art_12

Article 12

1. Les applications de création de signature utilisées par les unités de portefeuille peuvent être fournies soit par des fournisseurs de portefeuille, soit par des prestataires de services de confiance, soit par des parties utilisatrices de portefeuille.

2. Les applications de création de signature possèdent les fonctions suivantes:

| a) | apposer des signatures ou des cachets sur les données fournies par l’utilisateur de portefeuille; |
| --- | --- |

| b) | apposer des signatures ou des cachets sur les données fournies par la partie utilisatrice; |
| --- | --- |

| c) | créer des signatures ou des cachets correspondant au moins aux formats obligatoires visés à l’annexe IV; |
| --- | --- |

| d) | informer les utilisateurs de portefeuille du résultat du processus de création de signature ou de cachet. |
| --- | --- |

3. Les applications de création de signature peuvent être intégrées aux instances de portefeuille ou extérieures à celles-ci. Lorsque les applications de création de signature reposent sur des dispositifs de création de signature qualifiés distants et lorsqu’elles sont intégrées dans des instances de portefeuille, elles prennent en charge l’interface de programmation d’applications visée à l’annexe IV.

<a id="art_13"></a>

### art_13

Article 13

Les unités de portefeuille permettent d’assurer, en fonction des possibilités techniques et hors actifs critiques, l’exportation et la portabilité sécurisées des données à caractère personnel de l’utilisateur du portefeuille, afin de permettre à celui-ci de migrer vers une unité de portefeuille d’une autre solution de portefeuille dans des conditions offrant un niveau de garantie élevé au sens du règlement d’exécution (UE) 2015/1502.

<a id="art_14"></a>

### art_14

Article 14

1. Les unités de portefeuille permettent de générer des pseudonymes pour les utilisateurs de portefeuille conformément aux spécifications techniques énoncées à l’annexe V.

2. Les unités de portefeuille permettent de générer, à la demande d’une partie utilisatrice de portefeuille, un pseudonyme spécifique et exclusif pour cette dernière et lui fournissent ce pseudonyme, soit isolément, soit en combinaison avec toute donnée d’identification personnelle ou attestation électronique d’attributs demandée par elle.

<a id="art_15"></a>

### art_15

Article 15

Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
