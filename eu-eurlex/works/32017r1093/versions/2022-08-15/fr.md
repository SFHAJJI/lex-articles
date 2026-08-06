---
lex_id: 'eu-eurlex:32017r1093:2022-08-15'
title: 'Commission Implementing Regulation (EU) 2017/1093 of 20 June 2017 laying down implementing…'
valid_from: '2022-08-15'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02017R1093-20220815'
source_sha256: '7677cf6fb2d1f4cd212a71fbb08613414719f59c798de164a8e4347211df97ef'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_premier"></a>

### Article premier — Rapports hebdomadaires

**1.** Les entreprises d'investissement et les opérateurs de marché exploitant une plate-forme de négociation élaborent le rapport hebdomadaire prévu par l'article 58, paragraphe 1, point a), de la directive 2014/65/UE séparément pour chacun des dérivés sur matières premières, des quotas d'émission et des dérivés sur quotas d'émission qui sont négociés sur ladite plate-forme, en respectant le format défini dans les tableaux de l'annexe I du présent règlement.

**2.** Les rapports visés au paragraphe 1 agrègent toutes les positions détenues par les différentes personnes appartenant à chacune des catégories du tableau 1 de l'annexe I sur chaque dérivé sur matières premières, quota d'émission et dérivé sur quota d'émission qui est négocié sur cette plate-forme de négociation.

<a id="art_2"></a>

### Article 2 — Rapports quotidiens

**1.** Les entreprises d'investissement fournissent aux autorités compétentes la ventilation de leurs positions visée par l'article 58, paragraphe 2, de la directive 2014/65/UE, au moyen d'un rapport de position quotidien respectant le format défini dans les tableaux de l'annexe II du présent règlement.

**2.** Le rapport visé au paragraphe 1 contient toutes les positions détenues pour toutes les échéances de tous les contrats.

<a id="art_3"></a>

### Article 3 — Format des rapports

Les opérateurs de plates-formes de négociation et les entreprises d'investissement soumettent les rapports visés aux articles 1 et 2 dans un format XML standard commun.

<a id="art_4"></a>

### Article 4 — Entrée en vigueur

Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au *Journal officiel de l'Union européenne*.

Il est applicable à partir du 3 janvier 2018.

Le présent règlement est obligatoire dans tous ses éléments et directement applicable dans tout État membre.

<a id="annexe_i"></a>

### ANNEXE I

**Format des rapports hebdomadaires**

*Tableau 1*

**Rapports hebdomadaires**

| {Nom de la plate-forme de négociation}{Identifiant de la plate-forme de négociation}{Date à laquelle le rapport hebdomadaire fait référence}{Date et heure de publication}{Nom du dérivé sur matières premières, du quota d'émission ou du dérivé sur quota d'émission}{Code produit de la plate-forme}{Type de rapport} |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Unité de volume des positions |  | Entreprises d'investissement et établissements de crédit | Fonds d'investissement | Autres établissements financiers | Entreprises commerciales | Exploitants soumis à des obligations de conformité dans le cadre de la directive 2003/87/CE |  |  |  |  |  |
| Longues | Courtes | Longues | Courtes | Longues | Courtes | Longues | Courtes | Longues | Courtes |  |  |  |
| Nombre de positions |  | Réduction de risques directement associés à des activités commerciales |  |  |  |  |  |  |  |  |  |  |
| Autres |  |  |  |  |  |  |  |  |  |  |  |  |
| Total |  |  |  |  |  |  |  |  |  |  |  |  |
| Variations depuis le rapport précédent (+/–) |  | Réduction de risques directement associés à des activités commerciales |  |  |  |  |  |  |  |  |  |  |
| Autres |  |  |  |  |  |  |  |  |  |  |  |  |
| Total |  |  |  |  |  |  |  |  |  |  |  |  |
| Pourcentage du total des positions ouvertes |  | Réduction de risques directement associés à des activités commerciales |  |  |  |  |  |  |  |  |  |  |
| Autres |  |  |  |  |  |  |  |  |  |  |  |  |
| Total |  |  |  |  |  |  |  |  |  |  |  |  |
| Nombre de personnes détenant une position dans chaque catégorie |  |  | Combinées | Combinées | Combinées | Combinées | Combinées |  |  |  |  |  |
| Total |  |  |  |  |  |  |  |  |  |  |  |  |

*Tableau 2*

**Tableau des symboles du tableau 3**

| SYMBOLE | TYPE DE DONNÉES | DÉFINITION |
| --- | --- | --- |
| {ALPHANUM-n} | Jusqu'à n caractères alphanumériques | Texte libre. |
| {DECIMAL-n/m} | Nombre décimal de maximum n chiffres au total dont m chiffres tout au plus peuvent être des décimales | Champ numérique pouvant contenir des valeurs positives ou négatives:— utiliser comme séparateur décimal le point (.) (point),— faire précéder les valeurs négatives du signe moins (–).Le cas échéant, les valeurs sont arrondies et non tronquées. |
| {DATEFORMAT} | Format de date ISO 8601 | Les dates doivent respecter le format:AAAA-MM-JJ. |
| {DATE_TIME_FORMAT} | Format de date et heure ISO 8601 | — Date et heure selon le format suivant:— AAAA-MM-JJThh:mm:ss.ddddddZ.— «AAAA» correspond à l'année,— «MM» au mois,— «JJ» au jour,— «T» — signifie que la lettre «T» doit être utilisée pour introduire l'heure,— «hh» correspond à l'heure,— «mm» aux minutes,— «ss.dddddd» aux secondes et aux fractions de secondes,— «Z» correspond à l'heure TUC.Dates et heures doivent être déclarées en TUC. |
| {MIC} | 4 caractères alphanumériques | Identifiant de marché au sens de la norme ISO 10383. |
| {INTEGER-n} | Nombre entier de n chiffres au maximum | Champ numérique pouvant contenir des entiers positifs ou négatifs. |

*Tableau 3*

**Tableau des éléments à fournir pour chaque dérivé sur matières premières, quota d'émission ou dérivé sur quota d'émission aux fins de l'article 1er**

| CHAMP | INFORMATIONS À DÉCLARER | FORMAT DE DÉCLARATION |
| --- | --- | --- |
| Nom de la plate-forme de négociation | Indiquer le nom complet de la plate-forme de négociation. | {ALPHANUM-350} |
| Identifiant de la plate-forme de négociation | Indiquer le MIC du segment de la plate-forme de négociation selon ISO 10383. S'il n'existe pas de MIC de segment de marché, utiliser le code MIC d'exploitation (*operating MIC*). | {MIC} |
| Date à laquelle le rapport hebdomadaire fait référence | Indiquer la date du vendredi de la semaine civile durant laquelle la position est détenue. | {DATEFORMAT} |
| Date et heure de publication | Indiquer la date et l'heure de publication du rapport sur le site web de la plate-forme de négociation. | {DATE_TIME_FORMAT} |
| Nom du dérivé sur matières premières, du quota d'émission ou du dérivé sur quota d'émission | Indiquer le nom du dérivé sur matières premières, du quota d'émission ou du dérivé sur quota d'émission, identifié par le code produit de la plate-forme. | {ALPHANUM-350} |
| Code produit de la plate-forme | Fournir l'identifiant alphanumérique unique et univoque utilisé par la plate-forme de négociation pour regrouper dans un même produit des contrats aux échéances et aux prix d'exercice différents. | {ALPHANUM-12} |
| Type de rapport | Indiquer si le rapport est nouveau ou s'il fait suite à l'annulation ou à la modification d'un rapport précédent.En cas d'annulation ou de modification d'un rapport précédent, fournir un rapport contenant tous les détails du rapport d'origine, et indiquer «CANC» dans la case «Type de rapport».En cas de modification, fournir un nouveau rapport contenant tous les détails du rapport d'origine et toutes les modifications nécessaires et indiquer «AMND» dans la case «Type de rapport». | «NEWT» — Nouveau rapport«CANC» — Annulation«AMND» — Modification |
| Nombre de positions | Indiquer le volume total de positions ouvertes détenues le vendredi en fin de séance. Ce volume devrait être donné soit en nombre de lots (si les limites de position sont exprimées en lots) soit en unités de sous-jacent.Les contrats d'option sont inclus dans l'agrégat et indiqués sur une base équivalent delta. | {DECIMAL-15/2} |
| Unité de volume des positions | Indiquer les unités utilisées pour le nombre des positions. | «LOTS» LOTSsi le volume des positions est exprimé en lotsou si le volume des positions est exprimé en lotsou{ALPHANUM-25} — description des unités utilisées si le volume est donné en unités de sous-jacent |
| Variations depuis le rapport précédent (+/–) | Augmentation ou diminution du volume des positions par rapport au vendredi précédent.Pour une diminution, fournir un nombre négatif (précédé du signe moins [–]). | {DECIMAL-15/2} |
| Pourcentage du total des positions ouvertes | Indiquer le pourcentage des positions par rapport au total des positions ouvertes. | {DECIMAL-5/2} |
| Nombre de personnes détenant une position dans chaque catégorie | Indiquer le nombre de personnes détenant une position dans la catégorie.Si le nombre de personnes détenant une position dans la catégorie est inférieur au nombre précisé dans l'acte délégué de la Commission adopté conformément à l'article 58, paragraphe 6, de la MiFID II (1), placer un point (.) dans cette case. | {INTEGER-7}ou{ALPHANUM-1} si le champ doit ne doit contenir qu'un point (.). |
| (1)Règlement délégué (UE) 2017/565 de la Commission du 25 avril 2016 complétant la directive 2014/65/UE du Parlement européen et du Conseil en ce qui concerne les exigences organisationnelles et les conditions d'exercice applicables aux entreprises d'investissement et la définition de certains termes aux fins de ladite directive (JO L 87 du 31.3.2017, p. 1). |  |  |

<a id="annexe_ii"></a>

### ANNEXE II

**Format des rapports quotidiens**

*Tableau 1*

**Tableau des symboles du tableau 2**

| SYMBOLE | TYPE DE DONNÉES | DÉFINITION |
| --- | --- | --- |
| {ALPHANUM-n} | Jusqu'à n caractères alphanumériques | Texte libre. |
| {DECIMAL-n/m} | Nombre décimal de maximum n chiffres au total dont m chiffres tout au plus peuvent être des décimales | Champ numérique pouvant contenir des valeurs positives ou négatives:— utiliser comme séparateur décimal le point (.),— faire précéder les valeurs négatives du signe moins (–).Le cas échéant, les valeurs sont arrondies et non tronquées. |
| {DATEFORMAT} | Format de date ISO 8601 | Les dates doivent respecter le format:AAAA-MM-JJ. |
| {DATE_TIME_FORMAT} | Format de date et heure ISO 8601 | — Date et heure selon le format suivant:— AAAA-MM-JJThh:mm:ss.ddddddZ.— «AAAA» correspond à l'année,— «MM» au mois,— «JJ» au jour,— «T» — signifie que la lettre «T» doit être utilisée pour introduire l'heure,— «hh» correspond à l'heure,— «mm» aux minutes,— «ss.dddddd» aux secondes et aux fractions de secondes,— «Z» correspond à l'heure TUC.Dates et heures doivent être déclarées en TUC. |
| {ISIN} | 12 caractères alphanumériques | Code ISIN au sens de la norme ISO 6166. |
| {LEI} | 20 caractères alphanumériques | Identifiant de l'entité juridique suivant la norme ISO 17442 |
| {MIC} | 4 caractères alphanumériques | Identifiant de marché au sens de la norme ISO 10383. |
| {NATIONAL_ID} | 35 caractères alphanumériques | Identifiant visé à l'article 6 du règlement délégué (UE) 2017/590 de la Commission (1) sur les obligations de déclaration des transactions au titre de l'article 26 du règlement (UE) no 600/2014 du Parlement européen et du Conseil (2) et à l'annexe II dudit règlement. |
| {INTEGER-n} | Nombre entier de n chiffres au maximum | Champ numérique pouvant contenir des entiers positifs ou négatifs. |
| (1)Règlement délégué (UE) 2017/590 de la Commission du 28 juillet 2016 complétant le règlement (UE) no 600/2014 du Parlement européen et du Conseil par des normes techniques de réglementation pour la déclaration de transactions aux autorités compétentes (JO L 87 du 31.3.2017, p. 449).(2)Règlement (UE) no 600/2014 du Parlement européen et du Conseil du 15 mai 2014 concernant les marchés d'instruments financiers et modifiant le règlement (UE) no 648/2012 (JO L 173 du 12.6.2014, p. 84). |  |  |

*Tableau 2*

**Tableau des éléments à fournir pour toutes les positions détenues pour toutes les échéances de tous les contrats aux fins de l’article 2**

| CHAMP | INFORMATIONS À DÉCLARER | FORMAT DE DÉCLARATION |
| --- | --- | --- |
| Date et heure de présentation du rapport | Indiquer la date et l’heure de présentation du rapport. | {DATE_TIME_FORMAT} |
| Numéro de référence du rapport | Fournir l’identifiant unique, attribué par la personne présentant le rapport, qui permet à celle-ci et à l’autorité compétente destinataire d’identifier sans ambiguïté le rapport. | {ALPHANUM-52} |
| Date de la séance de négociation de la position concernée | Date à laquelle la position déclarée est détenue à la clôture de la séance sur la plate-forme de négociation concernée. | {DATEFORMAT} |
| Type de rapport | Indiquer si le rapport est nouveau ou s’il fait suite à l’annulation ou à la modification d’un rapport précédent.En cas d’annulation ou de modification d’un rapport précédent, fournir un rapport contenant tous les détails du rapport d’origine et portant son numéro de référence et indiquer «CANC» dans la case «Type de rapport».Pour les modifications, fournir un nouveau rapport contenant tous les détails du rapport d’origine et toutes les modifications nécessaires, et portant le numéro de référence du rapport d’origine, et indiquer «AMND» dans la case «Type de rapport». | «NEWT» — Nouveau«CANC» — Annulation«AMND» — Modification |
| Identifiant de l’entité déclarante | Identifiant de l’entreprise d’investissement déclarante. Indiquer l’identifiant d’entité juridique (code LEI), pour les entités juridiques, ou le numéro national d’identité {NATIONAL_ID}, pour les personnes physiques qui n’ont pas de LEI. | {LEI}ou{NATIONAL_ID} – Personnes physiques |
| Identifiant du détenteur de la position | Indiquer l’identifiant d’entité juridique (code LEI), pour les entités juridiques, ou le numéro national d’identité {NATIONAL_ID}, pour les personnes physiques qui n’ont pas de LEI. (Remarque: si la position est détenue par l’entreprise déclarante pour son compte propre, ce champ doit être identique au champ «Identifiant de l’entité déclarante»). | {LEI}ou{NATIONAL_ID} – Personnes physiques |
| Adresse électronique du détenteur de la position | Adresse électronique pour les notifications relatives à la position. | {ALPHANUM-256} |
| Identifiant de l’entité mère ultime | Indiquer l’identifiant d’entité juridique (code LEI), pour les entités juridiques, ou le numéro national d’identité {NATIONAL_ID}, pour les personnes physiques qui n’ont pas de LEI. Remarque: ce champ peut être identique au champ «Identifiant de l’entité déclarante» ou au champ «Identifiant du détenteur de la position» si l’entité mère ultime détient ses propres positions ou établit ses propres rapports. | {LEI}ou{NATIONAL_ID} – Personnes physiques |
| Adresse électronique de l’entité mère ultime | Adresse électronique pour toute correspondance concernant des positions agrégées. | {ALPHANUM-256} |
| Situation par rapport à l’entreprise mère d’un organisme de placement collectif | Indiquer si le détenteur de la position est un organisme de placement collectif qui prend des décisions d’investissement indépendamment de son entreprise mère conformément à l’article 4, paragraphe 2, du règlement délégué (UE) 2022/1301 de la Commission (*1). | «TRUE» — le détenteur de la position est un organisme de placement collectif qui prend ses décisions d’investissement de manière indépendante«FALSE» — le détenteur de la position n’est pas un organisme de placement collectif qui prend ses décisions d’investissement de manière indépendante |
| Code d’identification du contrat négocié sur une plate-forme de négociation | Identifiant du dérivé sur matières premières, du quota d’émission ou du dérivé sur quota d’émission. Voir le champ «Identifiant de la plate-forme de négociation» pour le traitement des contrats de gré à gré économiquement équivalents à des contrats négociés sur une plate-forme de négociation. | {ISIN} |
| Code produit de la plate-forme | Fournir l’identifiant alphanumérique unique et univoque utilisé par la plate-forme de négociation pour regrouper dans un même produit des contrats aux échéances et aux prix d’exercice différents. | {ALPHANUM-12} |
| Identifiant de la plate-forme de négociation | Fournir le code MIC de segment selon ISO 10383 pour les positions déclarées concernant des contrats négociés sur la plate-forme. S’il n’existe pas de code MIC du segment de marché, utiliser le code MIC d’exploitation (operating MIC). | {MIC} |
| Utiliser le code MIC «XXXX» pour les positions hors plate-forme de négociation concernant des contrats de gré à gré économiquement équivalents.Utiliser le code MIC «XOFF» pour les instruments dérivés cotés ou les quotas d’émission négociés hors marché. |  |  |
| Type de position | Indiquer s’il s’agit d’une position sur des contrats à terme (*futures*), des options, des quotas d’émission ou dérivés sur quotas d’émission, ou tout autre type de contrat. | «OPTN» — Options, y compris les options sur FUTR ou OTHR qui peuvent être négociées séparément, hormis les produits dont le caractère optionnel n’est qu’un élément incorporé«FUTR» — Contrats à terme (*futures*)«EMIS» — Quotas d’émission et dérivés sur quotas d’émission«OTHR» — Tout autre type de contrat |
| Échéance de la position | Indiquer si l’échéance du contrat sur lequel porte la position concerne le mois *spot* ou tous les autres mois. Remarque: fournir des rapports distincts pour les mois *spot* et pour tous les autres mois. | «SPOT» — mois *spot*, y compris toutes les positions dans les types de position EMIS«OTHR» — tous les autres mois |
| Volume des positions | Indiquer le volume net des positions détenues sur des dérivés sur matières premières, sur quotas d’émission ou sur dérivés sur quotas d’émission, exprimé soit en lots, si les limites de position sont exprimées en lots, soit en unités de sous-jacent.Ce volume doit être un nombre positif pour les positions longues et un nombre négatif pour les positions courtes. | {DECIMAL-15/2} |
| Unité de volume des positions | Indiquer les unités utilisées pour le volume des positions. | «LOTS» — si le volume des positions est exprimé en lots{ALPHANUM-25} — description des unités utilisées si le volume des positions est exprimé en unités du sous-jacent«UNIT» — si le volume des positions est exprimé en unités |
| Volume des positions en équivalent delta | Si la position est de type «OPTN» ou option sur «EMIS», indiquer le volume des positions en équivalent delta déclaré dans le champ «Volume des positions».Ce volume doit être un nombre positif pour les achats d’options d’achat et les ventes d’options de vente et un nombre négatif pour les achats d’options de vente et ventes d’options d’achat. | {DECIMAL-15/2} |
| Indicateur de l’aptitude de la position à réduire les risques associés aux activités commerciales | Indiquer si la position réduit les risques conformément à l’article 7 du règlement délégué (UE) 2022/1301. | «TRUE» — la position réduit les risques«FALSE» — la position ne réduit pas les risques |
| (*1)Règlement délégué (UE) 2022/1301 de la Commission du 31 mars 2022 modifiant les normes techniques de réglementation définies dans le règlement délégué (UE) 2020/1226 en ce qui concerne les informations à fournir conformément aux exigences de notification STS pour les titrisations synthétiques inscrites au bilan (JO L 197 du xx.xx.2022, p. 10). |  |  |
