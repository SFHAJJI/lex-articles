---
lex_id: 'eu-eurlex:32025r0416:2024-11-29'
title: 'Commission Delegated Regulation (EU) 2025/416 of 29 November 2024 supplementing Regulation (EU) 2023/1114'
valid_from: '2024-11-29'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32025R0416'
source_sha256: '269a01ebd29b19b3712fa4abb54fda99d3b18f288926ed39576bc4578afd55b0'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article premier

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs tiennent à la disposition de l’autorité compétente les informations, visées aux articles 2 à 15, sur chaque ordre portant sur des crypto-actifs qui est affiché par l’intermédiaire de leurs systèmes, ou lui donnent accès à ces informations, selon le format indiqué dans les tableaux 2 et 3 de l’annexe, dans la mesure où elles concernent l’ordre en question.

2. Les données visées au paragraphe 1 sont présentées dans un format JSON suivant la méthode définie par la norme ISO 20022.

<a id="art_2"></a>

### art_2

Article 2

1. Pour tous les ordres sur crypto-actifs, les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs conservent des enregistrements permettant d’identifier tous les acteurs suivants:

| a) | tout participant de la plate-forme de négociation de crypto-actifs qui est une entité juridique et qui soumet un ordre à cette plate-forme, tel qu’identifié conformément à l’article 4 et au champ 1 du tableau 2 de l’annexe; |
| --- | --- |

| b) | tout participant de la plate-forme de négociation de crypto-actifs qui est une personne physique et qui soumet un ordre à cette plate-forme, tel qu’identifié conformément au champ 2 du tableau 2 de l’annexe; |
| --- | --- |

| c) | tout client pour le compte duquel le participant de la plate-forme de négociation de crypto-actifs visé au point a) ou b) soumet l’ordre à cette plate-forme, tel qu’identifié conformément au champ 3 du tableau 2 de l’annexe; |
| --- | --- |

| d) | la personne ou l’algorithme informatique qui, au sein du participant à la plate-forme de négociation de crypto-actifs visé au point a) ou b), est responsable de la décision d’investissement liée à l’ordre, tel(le) qu’identifié(e) conformément au champ 4 du tableau 2 de l’annexe; |
| --- | --- |

| e) | la personne ou l’algorithme informatique qui, au sein du participant à la plate-forme de négociation de crypto-actifs visé au point a) ou b), est responsable de l’exécution de l’ordre, tel(le) qu’identifié(e) conformément au champ 5 du tableau 2 de l’annexe. |
| --- | --- |

Aux fins du point d), lorsque la décision d’investissement est prise par plusieurs personnes, les prestataires de services sur crypto-actifs qui exploitent une plate-forme de négociation de crypto-actifs conservent un enregistrement de la personne qui assume la responsabilité principale de cette décision. Un prestataire de services sur crypto-actifs qui exploite une plate-forme de négociation de crypto-actifs n’identifie cette personne ou cet algorithme informatique que si la décision d’investissement est prise soit pour le compte du participant, soit pour le compte d’un client qui lui a confié un mandat discrétionnaire à cet effet.

2. Si un participant d’une plate-forme de négociation de crypto-actifs a l’intention d’attribuer un ordre à un client après avoir soumis cet ordre à cette plate-forme, mais qu’il n’a pas encore procédé à cette attribution au moment de soumettre l’ordre, ce client est identifié comme indiqué dans le champ 3 du tableau 2 de l’annexe.

3. Si plusieurs ordres de clients différents sont soumis ensemble à la plate-forme de négociation de crypto-actifs sous la forme d’un ordre groupé, les informations visées dans le champ 3 du tableau 2 de l’annexe sont enregistrées pour chaque client.

<a id="art_3"></a>

### art_3

Article 3

1. Le prestataire de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs identifie les personnes physiques dans ses enregistrements de carnets d’ordres à l’aide de la désignation issue de la concaténation du code ISO 3166-1 alpha-2 précisé dans la norme ISO 3166 et de l’identifiant national de client, indiqués à l’annexe II du règlement délégué (UE) 2017/590, correspondant à la nationalité de chaque personne. Le code pays à deux lettres doit correspondre à la nationalité de la personne physique.

2. L’identifiant national de client visé au paragraphe 1 est attribué conformément à l’ordre des priorités prévu à l’annexe II du règlement délégué (UE) 2017/590, l’identifiant ayant le plus haut degré de priorité parmi ceux de la personne concernée devant être utilisé, que celui-ci soit déjà connu ou non du prestataire de services sur crypto-actifs exploitant la plate-forme de négociation de crypto-actifs.

3. Dans le cas d’une personne physique possédant la nationalité de plusieurs pays de l’espace économique européen (EEE), il convient d’utiliser le code pays de la première nationalité selon l’ordre alphabétique des codes ISO 3166-1 alpha-2 concernés et l’identifiant de cette nationalité attribué conformément au paragraphe 2. Lorsqu’une personne physique possède la nationalité d’un pays non-EEE, il convient d’utiliser l’identifiant ayant le plus haut degré de priorité parmi ceux prévus dans le champ «Tous les autres pays» de l’annexe II du règlement délégué (UE) 2017/590. Lorsqu’une personne physique possède la nationalité d’un pays de l’EEE et d’un pays non-EEE, il convient d’utiliser le code pays de la nationalité de l’EEE, et l’identifiant de plus haut degré de priorité de cette nationalité attribué conformément au paragraphe 2.

4. Lorsqu’une personne physique est résidente d’un pays autre que celui dont elle possède la nationalité, le prestataire de services sur crypto-actifs qui exploite la plate-forme de négociation de crypto-actifs l’identifie aussi d’après son pays de résidence, comme indiqué dans le champ 50 du tableau 2 de l’annexe.

5. Il convient d’exclure les préfixes de noms et d’ajouter le signe «#» aux prénoms et aux noms de famille de moins de cinq caractères. Tous les caractères sont à inscrire en capitales. L’utilisation d’apostrophes, d’accents, de traits d’union, de signes de ponctuation ou d’espaces est interdite.

6. Lorsque l’identifiant attribué conformément au paragraphe 2 correspond à la mention CONCAT, le prestataire de services sur crypto-actifs qui exploite la plate-forme de négociation de crypto-actifs identifie la personne physique par la concaténation des éléments suivants, dans l’ordre indiqué:

| a) | la date de naissance de la personne au format AAAAMMJJ; |
| --- | --- |

| b) | les cinq premiers caractères de son prénom; |
| --- | --- |

| c) | les cinq premiers caractères de son nom de famille. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs identifient chaque entité juridique dans leurs enregistrements de carnets d’ordres à l’aide de l’identifiant d’entité prévu par l’article 14 du règlement délégué de la Commission définissant des normes techniques adopté en application de l’article 68, paragraphe 10, premier alinéa, point b).

2. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs identifient les crypto-actifs dans leurs enregistrements de carnets d’ordres à l’aide des identifiants d’actifs prévus par l’article 15 du règlement délégué de la Commission définissant des normes techniques adopté en application de l’article 68, paragraphe 10, premier alinéa, point b).

3. Lorsqu’il utilise l’identifiant d’entité juridique LEI pour identifier des entités juridiques, conformément au paragraphe 1, le prestataire de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs veille à ce que la longueur et la composition du code LEI repris dans ses enregistrements de carnets d’ordres soient conformes à la norme ISO 17442 et à ce que ce code LEI figure dans la base de données internationale des codes LEI gérée par le Comité de surveillance réglementaire des identifiants d’entités juridiques, et corresponde bien à l’entité concernée.

<a id="art_5"></a>

### art_5

Article 5

La qualité en laquelle le participant de la plate-forme de négociation de crypto-actifs soumet un ordre est enregistrée comme indiqué dans le champ 7 du tableau 2 de l’annexe.

<a id="art_6"></a>

### art_6

Article 6

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent la date et l’heure de la survenance de chaque événement mentionné dans le champ 20 du tableau 2 de l’annexe, comme indiqué dans le champ 8 du tableau 2 de l’annexe.

2. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent la date et l’heure de chaque élément d’information mentionné dans les champs 47, 48 et 49 du tableau 2 de l’annexe, comme indiqué dans le champ 8 du tableau 2 de l’annexe.

<a id="art_7"></a>

### art_7

Article 7

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent les durées de validité des ordres, et les restrictions attachées à ceux-ci, qui sont visées dans les champs 9 et 10 du tableau 2 de l’annexe.

2. Pour chaque période de validité, les dates et heures délimitant la période sont enregistrées comme indiqué dans le champ 11 du tableau 2 de l’annexe.

<a id="art_8"></a>

### art_8

Article 8

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs qui utilisent des systèmes de négociation basés sur la priorité prix-visibilité-temps enregistrent l’horodatage de la priorité pour tous les ordres, comme indiqué dans le champ 12 du tableau 2 de l’annexe.

2. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs qui utilisent des systèmes de négociation basés sur la priorité taille-temps enregistrent les quantités qui déterminent la priorité accordée aux ordres, comme indiqué dans le champ 13 du tableau 2 de l’annexe, ainsi que l’horodatage de la priorité visé au paragraphe 1.

3. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs qui utilisent une combinaison associant la priorité prix-visibilité-temps et la priorité taille-temps, et qui affichent les ordres dans leur carnet d’ordres selon la priorité temps, enregistrent l’horodatage de la priorité pour tous les ordres, comme indiqué dans le champ 12 du tableau 2 de l’annexe.

4. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs qui utilisent une combinaison associant la priorité prix-visibilité-temps et la priorité taille-temps, et qui affichent les ordres dans leur carnet d’ordres selon la priorité taille-temps, enregistrent les quantités qui déterminent la priorité accordée aux ordres, comme indiqué dans le champ 13 du tableau 2 de l’annexe, ainsi que l’horodatage de la priorité visé au paragraphe 1.

5. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs attribuent à chaque événement un numéro de séquence, comme indiqué dans le champ 14 du tableau 2 de l’annexe, qu’ils enregistrent.

<a id="art_9"></a>

### art_9

Article 9

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs attribuent à chaque ordre un code d’identification individuel, comme indiqué dans le champ 19 du tableau 2 de l’annexe, qu’ils enregistrent. Ce code d’identification est propre à:

| a) | un carnet d’ordres; |
| --- | --- |

| b) | une séance; et |
| --- | --- |

| c) | un crypto-actif. |
| --- | --- |

Ce code est valable depuis la réception de l’ordre par l’exploitant de la plate-forme de négociation de crypto-actifs jusqu’à sa suppression du carnet d’ordres. Il s’applique aux ordres rejetés, quel que soit le motif du rejet.

2. L’exploitant de la plate-forme de négociation de crypto-actifs enregistre les informations pertinentes, visées dans le champ 31 du tableau 2 de l’annexe, relatives aux ordres de stratégie avec fonctionnalité implicite (strategy orders with implied functionality, ou «SOIF») qui sont diffusés auprès du public. Le statut de l’ordre mentionné dans ce champ indique s’il s’agit d’un ordre implicite.

3. Lors de l’exécution d’un ordre de stratégie avec fonctionnalité implicite, les informations le concernant sont enregistrées par l’exploitant de la plate-forme de négociation de crypto-actifs comme indiqué dans les champs pertinents du tableau 2 de l’annexe.

4. Lors de l’exécution d’un ordre de stratégie avec fonctionnalité implicite, un code d’identification des ordres liés à la stratégie est indiqué, le même code étant attribué à tous les ordres liés à la stratégie en question. Le code d’identification des ordres liés à une stratégie prend la forme précisée dans le champ 44 du tableau 2 de l’annexe.

5. Les ordres permettant une stratégie de routage qui sont soumis à une plate-forme de négociation de crypto-actifs sont identifiés par cette plate-forme comme étant des «ordres acheminés», comme indiqué dans le champ 31 du tableau 2 de l’annexe, lorsqu’ils sont redirigés vers une autre plate-forme. Les ordres permettant une stratégie de routage qui sont soumis à une plate-forme de négociation de crypto-actifs conservent le même code d’identification pendant toute leur durée de vie, que leur solde éventuel soit ou non réinscrit dans le carnet d’ordres.

<a id="art_10"></a>

### art_10

Article 10

Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent les informations visées dans le champ 20 du tableau 2 de l’annexe en ce qui concerne tous les nouveaux ordres.

<a id="art_11"></a>

### art_11

Article 11

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent selon leurs propres spécifications le type d’ordres auquel appartient chaque ordre qu’ils reçoivent, comme indiqué dans le champ 21 du tableau 2 de l’annexe.

2. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs classent chaque ordre reçu soit en tant qu’ordre à cours limité, soit en tant qu’ordre stop, comme indiqué dans le champ 22 du tableau 2 de l’annexe.

<a id="art_12"></a>

### art_12

Article 12

Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent toutes les informations sur les cours qui concernent chaque ordre, comme indiqué dans la section I du tableau 2 de l’annexe.

<a id="art_13"></a>

### art_13

Article 13

Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent toutes les instructions reçues pour chaque ordre comme indiqué dans la section J du tableau 2 de l’annexe.

<a id="art_14"></a>

### art_14

Article 14

Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs attribuent à chaque transaction résultant de l’exécution totale ou partielle d’un ordre un code d’identification de transaction individuel, comme indiqué dans le champ 46 du tableau 2 et, selon le cas, dans le champ 1 du tableau 3 de l’annexe, et l’enregistrent.

<a id="art_15"></a>

### art_15

Article 15

1. Les prestataires de services sur crypto-actifs exploitant une plate-forme de négociation de crypto-actifs enregistrent les phases de négociation, ainsi que les cours et volumes de fixing indicatifs, comme indiqué dans la section K du tableau 2 de l’annexe.

2. Lorsque les autorités compétentes demandent des informations visées à la section K, il y a lieu de considérer que les informations visées dans les champs 8 et 14 à 17 du tableau 2 de l’annexe doivent figurer dans la réponse à cette demande.

<a id="art_16"></a>

### art_16

Article 16

Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
