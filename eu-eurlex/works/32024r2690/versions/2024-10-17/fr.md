---
lex_id: 'eu-eurlex:32024r2690:2024-10-17'
title: 'Commission Implementing Regulation (EU) 2024/2690 of 17 October 2024 laying down rules for…'
valid_from: '2024-10-17'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2690'
source_sha256: '646e9e14ace9a1f96826b0c77c1c108092044ebecb1ca3fc305164923052e207'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article premier

Le présent règlement établit, en ce qui concerne les fournisseurs de services DNS, les registres des noms de domaines de premier niveau, les fournisseurs de services d’informatique en nuage, les fournisseurs de services de centres de données, les fournisseurs de réseaux de diffusion de contenu, les fournisseurs de services gérés, les fournisseurs de services de sécurité gérés, les fournisseurs de places de marché en ligne, de moteurs de recherche en ligne et de plateformes de services de réseaux sociaux et les fournisseurs de services de confiance (ci-après les «entités concernées»), les exigences techniques et méthodologiques liées aux mesures visées à l’article 21, paragraphe 2, de la directive (UE) 2022/2555 et précise plus en détail les cas dans lesquels un incident devrait être considéré comme important au sens de l’article 23, paragraphe 3, de la directive (UE) 2022/2555.

<a id="art_2"></a>

### art_2

Article 2

1. Pour les entités concernées, les exigences techniques et méthodologiques liées aux mesures de gestion des risques de cybersécurité visées à l’article 21, paragraphe 2, points a) à j), de la directive (UE) 2022/2555 sont énoncées à l’annexe du présent règlement.

2. Lorsqu’elles mettent en œuvre et appliquent les exigences techniques et méthodologiques liées aux mesures de gestion des risques de cybersécurité énoncées à l’annexe du présent règlement, les entités concernées assurent un niveau de sécurité des réseaux et des systèmes d’information adapté aux risques présents. À cette fin, lorsqu’elles se conforment aux exigences techniques et méthodologiques liées aux mesures de gestion des risques en matière de cybersécurité énoncées à l’annexe du présent règlement, elles tiennent dûment compte de leur degré d’exposition aux risques, de leur taille et de la probabilité de survenance d’incidents, ainsi que de leur gravité, y compris de leur impact sociétal et économique.

Lorsque l’annexe du présent règlement prévoit qu’une exigence technique ou méthodologique liée à une mesure de gestion des risques de cybersécurité est appliquée «s’il est besoin», «s’il y a lieu» ou «dans la mesure du possible», et lorsqu’une entité concernée estime qu’il n’est pas besoin, qu’il n’y a pas lieu, ou qu’il est impossible pour elle d’appliquer certaines de ces exigences techniques et méthodologiques, elle documente de manière compréhensible son argumentation en ce sens.

<a id="art_3"></a>

### art_3

Article 3

1. Un incident est considéré comme important au sens de l’article 23, paragraphe 3, de la directive (UE) 2022/2555 eu égard aux entités concernées lorsqu’un ou plusieurs des critères suivants sont remplis:

| a) | l’incident a causé ou est susceptible de causer à l’entité concernée une perte financière directe supérieure à 500 000 EUR ou à 5 % du chiffre d’affaires annuel total de l’entité concernée au cours de l’exercice complet précédent, le montant le plus faible étant retenu; |
| --- | --- |

| b) | l’incident a causé ou est susceptible de provoquer l’exfiltration de secrets d’affaires de l’entité concernée, au sens de l’article 2, point 1), de la directive (UE) 2016/943; |
| --- | --- |

| c) | l’incident a causé ou est susceptible de causer la mort d’une personne physique; |
| --- | --- |

| d) | l’incident a causé ou est susceptible de causer des dommages considérables à la santé d’une personne physique; |
| --- | --- |

| e) | il y a eu un accès non autorisé effectif au réseau et aux systèmes d’information d’une entité concernée, qui est suspecté d’être malveillant et est susceptible de causer une perturbation opérationnelle grave; |
| --- | --- |

| f) | l’incident répond aux critères énoncés à l’article 4; |
| --- | --- |

| g) | l’incident répond à un ou plusieurs des critères énoncés aux articles 5 à 14. |
| --- | --- |

2. Les interruptions de service programmées et les conséquences prévues des opérations de maintenance programmées effectuées par les entités concernées ou pour leur compte ne sont pas considérées comme des incidents importants.

3. Lorsqu’elles calculent le nombre d’utilisateurs touchés par un incident aux fins de l’article 7 et des articles 9 à 14, les entités concernées tiennent compte de l’ensemble des éléments suivants:

| a) | le nombre de clients ayant conclu, avec l’entité concernée, un contrat qui leur donne accès au réseau et aux systèmes d’information de l’entité concernée ou aux services proposés par ce réseau et ces systèmes d’information ou accessibles par leur intermédiaire; |
| --- | --- |

| b) | le nombre de personnes physiques et morales associées à des clients professionnels qui utilisent le réseau et les systèmes d’information de l’entité concernée ou les services proposés par ce réseau et ces systèmes d’information ou accessibles par leur intermédiaire. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

Les incidents qui, pris isolément, ne sont pas considérés comme des incidents importants au sens de l’article 3 sont considérés collectivement comme un incident important lorsqu’ils remplissent l’ensemble des critères suivants:

| a) | ils se sont produits au moins deux fois en six mois; |
| --- | --- |

| b) | ils ont la même cause originelle apparente; |
| --- | --- |

| c) | ils répondent collectivement aux critères énoncés à l’article 3, paragraphe 1, point a). |
| --- | --- |

<a id="art_5"></a>

### art_5

Article 5

En ce qui concerne les fournisseurs de services DNS, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un service de résolution de noms de domaine récursif ou faisant autorité est totalement indisponible pendant plus de 30 minutes; |
| --- | --- |

| b) | pendant une période de plus d’une heure, un service de résolution de noms de domaine récursif ou faisant autorité a un temps de réponse moyen aux demandes DNS supérieur à 10 secondes; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture du service de résolution de nom de domaine faisant autorité est compromise, sauf dans les cas où les données de moins de 1 000 noms de domaine gérées par le fournisseur de services DNS, ne représentant pas plus de 1 % des noms de domaine gérés par ce fournisseur, ne sont pas correctes en raison d’une mauvaise configuration. |
| --- | --- |

<a id="art_6"></a>

### art_6

Article 6

En ce qui concerne les registres de noms de domaine de premier niveau, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un service de résolution de noms de domaine faisant autorité est totalement indisponible; |
| --- | --- |

| b) | pendant une période de plus d’une heure, un service de résolution de noms de domaine faisant autorité a un temps de réponse moyen aux demandes DNS supérieur à 10 secondes; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées au fonctionnement technique du domaine de premier niveau est compromise. |
| --- | --- |

<a id="art_7"></a>

### art_7

Article 7

En ce qui concerne les fournisseurs de services d’informatique en nuage, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un service d’informatique en nuage est totalement indisponible pendant plus de 30 minutes; |
| --- | --- |

| b) | la disponibilité d’un service d’informatique en nuage d’un fournisseur est limitée pour plus de 5 % des utilisateurs de ce service dans l’Union, ou pour plus de 1 million d’utilisateurs de ce service dans l’Union, le plus petit nombre étant retenu, pendant plus d’une heure; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un service d’informatique en nuage est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un service d’informatique en nuage est compromise, ce qui a un impact sur plus de 5 % des utilisateurs de ce service dans l’Union, ou sur plus de 1 million d’utilisateurs de ce service dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_8"></a>

### art_8

Article 8

En ce qui concerne les fournisseurs de services de centres de données, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un service d’un centre de données exploité par le fournisseur est totalement indisponible; |
| --- | --- |

| b) | la disponibilité d’un service d’un centre de données exploité par le fournisseur est limitée pendant plus d’une heure; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un service de centre de données est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’accès physique à un centre de données exploité par le fournisseur est compromis. |
| --- | --- |

<a id="art_9"></a>

### art_9

Article 9

En ce qui concerne les fournisseurs de services de réseaux de diffusion de contenu, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un réseau de diffusion de contenu est totalement indisponible pendant plus de 30 minutes; |
| --- | --- |

| b) | la disponibilité d’un réseau de diffusion de contenu est limitée pour plus de 5 % des utilisateurs de ce réseau dans l’Union, ou pour plus de 1 million d’utilisateurs de ce réseau dans l’Union, le plus petit nombre étant retenu, pendant plus d’une heure; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un réseau de diffusion de contenu est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un réseau de diffusion de contenu est compromise, ce qui a un impact sur plus de 5 % des utilisateurs de ce réseau dans l’Union, ou sur plus de 1 million d’utilisateurs de ce réseau dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_10"></a>

### art_10

Article 10

En ce qui concerne les fournisseurs de services gérés et les fournisseurs de services de sécurité gérés, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un service géré ou un service de sécurité géré est totalement indisponible pendant plus de 30 minutes; |
| --- | --- |

| b) | la disponibilité d’un service géré ou d’un service de sécurité géré est limitée pour plus de 5 % des utilisateurs de ce service dans l’Union, ou pour plus de 1 million d’utilisateurs de ce service dans l’Union, le plus petit nombre étant retenu, pendant plus d’une heure; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un service géré ou d’un service de sécurité géré est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un service géré ou d’un service de sécurité géré est compromise, ce qui a un impact sur plus de 5 % des utilisateurs de ce service géré ou service de sécurité géré dans l’Union, ou sur plus de 1 million d’utilisateurs de ces services dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_11"></a>

### art_11

Article 11

En ce qui concerne les fournisseurs de places de marché en ligne, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | une place de marché en ligne est totalement indisponible pour plus de 5 % des utilisateurs de cette place de marché en ligne dans l’Union, ou pour plus de 1 million d’utilisateurs de cette place de marché en ligne dans l’Union, le plus petit nombre étant retenu; |
| --- | --- |

| b) | plus de 5 % des utilisateurs d’une place de marché en ligne dans l’Union, ou plus de 1 million d’utilisateurs d’une place de marché en ligne dans l’Union, le plus petit nombre étant retenu, sont touchés par la disponibilité limitée de cette place de marché en ligne; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’une place de marché en ligne est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’une place de marché en ligne est compromise, ce qui a un impact sur plus de 5 % des utilisateurs de cette place de marché en ligne dans l’Union, ou sur plus de 1 million d’utilisateurs de cette place de marché en ligne dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_12"></a>

### art_12

Article 12

En ce qui concerne les fournisseurs de moteurs de recherche en ligne, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un moteur de recherche en ligne est totalement indisponible pour plus de 5 % des utilisateurs de ce moteur de recherche en ligne dans l’Union, ou pour plus de 1 million d’utilisateurs de ce moteur de recherche en ligne dans l’Union, le plus petit nombre étant retenu; |
| --- | --- |

| b) | plus de 5 % des utilisateurs d’un moteur de recherche en ligne dans l’Union, ou plus de 1 million d’utilisateurs d’un moteur de recherche en ligne dans l’Union, le plus petit nombre étant retenu, sont touchés par la disponibilité limitée de ce moteur de recherche en ligne; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un moteur de recherche en ligne est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un moteur de recherche en ligne est compromise, ce qui a un impact sur plus de 5 % des utilisateurs de ce moteur de recherche en ligne dans l’Union, ou sur plus de 1 million d’utilisateurs de ce moteur de recherche en ligne dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_13"></a>

### art_13

Article 13

En ce qui concerne les fournisseurs de plateformes de services de réseaux sociaux, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | une plateforme de services de réseaux sociaux est totalement indisponible pour plus de 5 % des utilisateurs de cette plateforme dans l’Union, ou pour plus de 1 million d’utilisateurs de cette plateforme dans l’Union, le plus petit nombre étant retenu; |
| --- | --- |

| b) | plus de 5 % des utilisateurs d’une plateforme de services de réseaux sociaux dans l’Union, ou plus de 1 million d’utilisateurs d’une plateforme de services de réseaux sociaux dans l’Union, le plus petit nombre étant retenu, sont touchés par la disponibilité limitée de cette plateforme; |
| --- | --- |

| c) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’une plateforme de services de réseaux sociaux est compromise par une action suspectée d’être malveillante, |
| --- | --- |

| d) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’une plateforme de services de réseaux sociaux est compromise, ce qui a un impact sur plus de 5 % des utilisateurs de cette plateforme dans l’Union, ou sur plus de 1 million d’utilisateurs de cette plateforme dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_14"></a>

### art_14

Article 14

En ce qui concerne les fournisseurs de services de confiance, un incident est considéré comme important au sens de l’article 3, paragraphe 1, point g), lorsqu’il remplit un ou plusieurs des critères suivants:

| a) | un service de confiance est totalement indisponible pendant plus de 20 minutes; |
| --- | --- |

| b) | un service de confiance est indisponible pour les utilisateurs ou les parties utilisatrices pendant plus d’une heure, le calcul étant effectué sur la base d’une semaine civile; |
| --- | --- |

| c) | plus de 1 % des utilisateurs ou des parties utilisatrices dans l’Union, ou plus de 200 000 utilisateurs ou parties utilisatrices dans l’Union, le plus petit nombre étant retenu, sont touchés par la disponibilité limitée de ce service de confiance; |
| --- | --- |

| d) | l’accès physique à une zone où sont situés des réseaux et des systèmes d’information et dont l’accès est limité au personnel de confiance du fournisseur de services de confiance, ou bien la protection de cet accès physique, est compromis; |
| --- | --- |

| e) | l’intégrité, la confidentialité ou l’authenticité des données stockées, transmises ou traitées liées à la fourniture d’un service de confiance est compromise, ce qui a un impact sur plus de 0,1 % des utilisateurs ou des parties utilisatrices, ou sur plus de 100 utilisateurs ou parties utilisatrices de ce service de confiance dans l’Union, le plus petit nombre étant retenu. |
| --- | --- |

<a id="art_15"></a>

### art_15

Article 15

Le règlement d’exécution (UE) 2018/151 (4) de la Commission est abrogé.

<a id="art_16"></a>

### art_16

Article 16

Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
