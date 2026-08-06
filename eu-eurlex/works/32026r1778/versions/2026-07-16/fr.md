---
lex_id: 'eu-eurlex:32026r1778:2026-07-16'
title: 'Commission Implementing Regulation (EU) 2026/1778 of 16 July 2026 laying down the implementation arrangements for the digital product passport registry set up under Regulation (EU) 2024/1781'
valid_from: '2026-07-16'
valid_to: 'open'
source: 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1778'
source_sha256: '86d0e1fb51025c0cafdafe205844fd3531c10fbf5c9aef78d278a0f664f05121'
license: 'EU reuse-with-attribution (Commission Decision 2011/833/EU)'
attribution: '© European Union, 1998-2026; reuse with attribution (Commission Decision 2011/833/EU); consolidated texts have no legal effect'
generator: 'xhtml-eu/1 · lex derive'
---

<a id="art_1"></a>

### art_1

Article premier

1. Le présent règlement définit les modalités d’application relatives au fonctionnement du registre des passeports numériques de produit établi conformément à l’article 13 du règlement (UE) 2024/1781, y compris les règles qui s’appliquent aux opérateurs économiques qui mettent sur le marché ou mettent en service l’un des produits suivants nécessitant l’existence d’un passeport numérique de produit et son enregistrement dans le registre:

| (a) | les produits couverts par des actes délégués adoptés en vertu de l’article 4 du règlement (UE) 2024/1781; |
| --- | --- |

| (b) | les batteries couvertes par l’article 77 du règlement (UE) 2023/1542; |
| --- | --- |

| (c) | les produits de construction couverts par l’article 76 du règlement (UE) 2024/3110; |
| --- | --- |

| (d) | les jouets couverts par l’article 19 du règlement (UE) 2025/2509; |
| --- | --- |

| (e) | les détergents et les agents de surface destinés aux utilisateurs finals couverts par l’article 21 du règlement (UE) 2026/405; |
| --- | --- |

| (f) | tout autre produit couvert par la législation de l’Union nécessitant un passeport numérique de produit et son enregistrement dans le registre établi en vertu de l’article 13 du règlement (UE) 2024/1781. |
| --- | --- |

2. Ces modalités de mise en œuvre comprennent également les règles régissant l’utilisation du registre par les acteurs de la chaîne de valeur, les autorités nationales compétentes, les autorités douanières et la Commission. Les modalités et règles de mise en œuvre visées au paragraphe 1 du présent article concernent:

| (a) | la gestion de l’accès au registre; |
| --- | --- |

| (b) | le processus de vérification qui permet de vérifier les opérateurs économiques et les acteurs de la chaîne de valeur; |
| --- | --- |

| (c) | la configuration technique du registre, y compris le référentiel sémantique, le système d’enregistrement par fichiers journaux lié aux modèles d’échange de données et la gestion des versions logicielles; |
| --- | --- |

| (d) | le processus d’enregistrement et de stockage des identifiants uniques; |
| --- | --- |

| (e) | le processus d’enregistrement et de stockage des codes de marchandises pour les produits destinés à être placés sous le régime douanier de la «mise en libre pratique»; |
| --- | --- |

| (f) | les exigences relatives à l’enregistrement, le cas échéant, du niveau de granularité adéquat du passeport numérique de produit: modèle, lot ou article; |
| --- | --- |

| (g) | les statuts liés aux données du passeport numérique de produit enregistré; |
| --- | --- |

| (h) | les données qui permettront la traçabilité des produits au sein de leur groupe de produits concerné, sur l’ensemble des niveaux de granularité visés à l’article 8, paragraphe 2, applicables à leur passeport numérique de produit; |
| --- | --- |

| (i) | la mise à jour et la suppression des données d’enregistrement; |
| --- | --- |

| (j) | la protection des données à caractère personnel; |
| --- | --- |

| (k) | les mesures visant à prévenir, à détecter et à contrer toute utilisation abusive ou frauduleuse du registre; |
| --- | --- |

| (l) | les audits techniques; |
| --- | --- |

| (m) | les mesures garantissant la disponibilité du registre et des données qu’il contient. |
| --- | --- |

<a id="art_2"></a>

### art_2

Article 2

Aux fins du présent règlement, on entend par:

| (1) | «registre des passeports numériques de produit», ou «registre», le système d’information établi et tenu à jour par la Commission conformément à l’article 13 du règlement (UE) 2024/1781; |
| --- | --- |

| (2) | «identifiants de connexion», un ensemble d’identifiants uniques, par exemple un nom d’utilisateur et un mot de passe, qui permettent à un utilisateur de vérifier son identité afin de s’authentifier dans le registre; |
| --- | --- |

| (3) | «jeton d’authentification», un jeton qui transmet de manière sécurisée des informations sur une authentification réussie et qui est utilisé en tant que preuve d’une session authentifiée ou d’un accès délégué entre des applications et le système d’information sur les passeports numériques de produit; |
| --- | --- |

| (4) | «processus de vérification de l’identité», le processus par lequel une personne physique ou morale fournit la preuve de son identité et, le cas échéant, de son établissement; |
| --- | --- |

| (5) | «opérateur économique vérifié», un opérateur économique qui a mené à bien le processus de vérification de son identité dans le registre conformément à l’article 4; |
| --- | --- |

| (6) | ««acteur de la chaîne de valeur», une personne physique ou morale, autre que l’opérateur économique, qui exerce des activités dans la chaîne de valeur d’un produit nécessitant un passeport numérique de produit et son enregistrement dans le registre, telle qu’un réparateur, un reconditionneur, une entreprise de remanufacturage ou un recycleur; |
| --- | --- |

| (7) | «acteur de la chaîne de valeur vérifié», un acteur de la chaîne de valeur qui a mené à bien le processus de vérification de son identité dans le registre conformément à l’article 5; |
| --- | --- |

| (8) | «référentiel sémantique», un ensemble de modèles de données et de définitions sémantiques composés d’un ensemble structuré et logiquement interconnecté de termes et de leurs significations précisant les éléments essentiels du passeport numérique de produit, les définitions des noms ou termes, les éléments de données et l’ontologie associés à certaines données afin de garantir une compréhension commune à tous les utilisateurs, ainsi qu’une interprétation multilingue utilisée pour la validation des passeports numériques de produit et pour relier les données du registre aux passeports numériques de produit; |
| --- | --- |

| (9) | «interopérabilité sémantique», la capacité des systèmes d’information et des organisations sur lesquelles ils reposent à échanger des données de manière à ce que la signification des informations échangées soit comprise mutuellement et puisse être interprétée sans ambiguïté par toutes les parties, quelle que soit la technologie ou la juridiction sous-jacente; |
| --- | --- |

| (10) | «vocabulaire contrôlé», un ensemble structuré, faisant autorité, de termes normalisés ayant des significations définies en vue d’assurer une représentation cohérente des attributs de données dans les passeports numériques de produit; |
| --- | --- |

| (11) | «spécification sémantique», tout élément publié dans le référentiel sémantique, y compris les ontologies, les modèles de données, les vocabulaires contrôlés et les listes de codes, ainsi que leurs métadonnées de version et les informations indiquant leur origine; |
| --- | --- |

| (12) | «conformité sémantique», la mesure dans laquelle les données figurant sur un passeport numérique de produit satisfont aux spécifications sémantiques applicables, en ce sens que:a)tous les éléments de données requis en application des actes délégués adoptés en vertu de l’article 4, du règlement (UE) 2024/1781 ou au titre d’autres actes législatifs de l’Union sont présents;b)les éléments de données obligatoires (requis et définis) et facultatifs (non requis mais définis) définis en application des actes délégués adoptés en vertu de l’article 4 du règlement (UE) 2024/1781 ou au titre d’autres actes législatifs de l’Union sont conformes aux exigences applicables, notamment en ce qui concerne la structure, le format, le type de valeur, le vocabulaire contrôlé et les règles d’applicabilité; etc)ces éléments de données sont susceptibles d’être interprétés de manière cohérente par d’autres systèmes par référence au référentiel sémantique applicable; |
| --- | --- |
| a) | tous les éléments de données requis en application des actes délégués adoptés en vertu de l’article 4, du règlement (UE) 2024/1781 ou au titre d’autres actes législatifs de l’Union sont présents; |
| b) | les éléments de données obligatoires (requis et définis) et facultatifs (non requis mais définis) définis en application des actes délégués adoptés en vertu de l’article 4 du règlement (UE) 2024/1781 ou au titre d’autres actes législatifs de l’Union sont conformes aux exigences applicables, notamment en ce qui concerne la structure, le format, le type de valeur, le vocabulaire contrôlé et les règles d’applicabilité; et |
| c) | ces éléments de données sont susceptibles d’être interprétés de manière cohérente par d’autres systèmes par référence au référentiel sémantique applicable; |

| (13) | «modèle de données», un cadre structuré qui organise des éléments de données, normalise leur structure, détermine leur relation mutuelle et identifie les entités, leurs attributs et la relation entre ces entités; |
| --- | --- |

| (14) | «système d’enregistrement», un système automatisé qui enregistre et stocke des informations sur toutes les opérations et interactions effectuées dans le registre; |
| --- | --- |

| (15) | «modèle d’échange de données», un cadre structuré permettant l’échange de données entre différents systèmes et différentes plateformes; |
| --- | --- |

| (16) | «empreinte de la version du passeport numérique de produit», le résultat généré à partir des données électroniques pertinentes à l’aide d’un algorithme cryptographique correspondant à la version pertinente du passeport numérique de produit; |
| --- | --- |

| (17) | «téléchargement de données massives», l’extraction d’un jeu de données exceptionnellement volumineux ou complexe - généralement d’un ordre de grandeur allant des téraoctets à des pétaoctets - qui dépasse les capacités de traitement ou de stockage d’outils conventionnels ou d’une seule machine locale ou qui interfère avec les garanties en matière de surveillance. |
| --- | --- |

Les définitions des termes «produit», «groupe de produits», «passeport numérique de produit», «prestataire de services de passeport numérique de produit», «mise sur le marché», «mise en service» et «opérateur économique» figurant respectivement à l’article 2, points 1), 5), 28), 32), 40), 41) et 46), du règlement (UE) 2024/1781 s’appliquent.

Aux fins du présent règlement, le «passeport numérique de produit» inclut le passeport de batterie établi par l’article 77 du règlement (UE) 2023/1542.

Les définitions des termes «authentification», «signature électronique qualifiée», «prestataire de services de confiance qualifié», «cachet électronique qualifié», «certificat qualifié de cachet électronique» et «horodatage électronique» figurant respectivement à l’article 3, points 5), 12), 20), 27), 30) et 33), du règlement (UE) no 910/2014 s’appliquent.

La définition du terme «format lisible par machine» figurant à l’article 2, point 13), de la directive (UE) 2019/1024 du Parlement européen et du Conseil (12) s’applique.

La définition du terme «traitement» figurant à l’article 3, point 3), du règlement (UE) 2018/1725 du Parlement européen et du Conseil (13) s’applique.

La définition du terme «incident» figurant à l’article 6, point 6), de la directive (UE) 2022/2555 du Parlement européen et du Conseil (14) s’applique.

La définition du terme «responsable du traitement» figurant à l’article 3, point 8), du règlement (UE) 2018/1725 s’applique.

Les définitions des termes «surveillance du marché», «autorité de surveillance du marché» et «mise en libre pratique» figurant respectivement à l’article 3, points 3), 4) et 25), du règlement (UE) 2019/1020 du Parlement européen et du Conseil (15) s’appliquent.

Les définitions des termes «autorités douanières» et «contrôles douaniers» figurant respectivement à l’article 5, points 1) et 3), du règlement (UE) no 952/2013 s’appliquent.

<a id="art_3"></a>

### art_3

Article 3

Le registre est composé des éléments suivants:

| (a) | un site web fournissant une interface utilisateur sécurisée qui permet aux opérateurs économiques, aux acteurs de la chaîne de valeur, aux autorités nationales compétentes et aux autorités douanières d’accéder au registre; |
| --- | --- |

| (b) | une API pour l’enregistrement des passeports numériques de produit et la réception d’informations provenant du registre; |
| --- | --- |

| (c) | une plateforme de vérification permettant de confirmer et de vérifier l’existence et l’exhaustivité des passeports numériques de produit; |
| --- | --- |

| (d) | un dispositif permettant de générer des identifiants d’enregistrement uniques; |
| --- | --- |

| (e) | une composante de stockage au moins pour les identifiants uniques et les codes de marchandises des produits destinés à être placés sous le régime douanier de la «mise en libre pratique»; |
| --- | --- |

| (f) | une liste des prestataires de services de passeport numérique de produit vérifiés enregistrés dans le registre; |
| --- | --- |

| (g) | un référentiel sémantique; |
| --- | --- |

| (h) | un système d’enregistrement par fichiers journaux; |
| --- | --- |

| (i) | des dispositifs d’identification et d’autorisation pour les utilisateurs du registre. |
| --- | --- |

<a id="art_4"></a>

### art_4

Article 4

1. Les opérateurs économiques qui sont des personnes physiques agissant en qualité de commerçants individuels sont qualifiés d’«opérateurs économiques vérifiés» si l’une des conditions suivantes est remplie:

| (a) | lorsqu’ils sont tenus d’être établis dans l’Union, ils fournissent une preuve de leur identité au moyen d’une signature électronique qualifiée étayée par un certificat qualifié de signature électronique conformément au règlement (UE) no 910/2014, ou ils fournissent la preuve de leur identité par un moyen d’identification électronique qui satisfait aux exigences du règlement (UE) no 910/2014 concernant le niveau de garantie «élevé», ou par une attestation électronique d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’opérateur économique; |
| --- | --- |

| (b) | lorsqu’ils ne sont pas tenus d’être établis dans l’Union, ils fournissent la preuve de leur identité au moyen d’une signature électronique qualifiée étayée par un certificat qualifié de signature électronique conformément au règlement (UE) no 910/2014, ou par une attestation électronique d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’opérateur économique. |
| --- | --- |

2. Les opérateurs économiques agissant en tant que personnes morales sont qualifiés d’«opérateurs économiques vérifiés» si l’une des conditions suivantes est remplie:

| (a) | lorsqu’ils sont tenus d’être établis dans l’Union, ils fournissent la preuve de leur identité et de leur établissement dans l’Union au moyen d’un cachet électronique qualifié étayé par un certificat qualifié de cachet électronique délivré par un prestataire de services de confiance qualifié conformément au règlement (UE) no 910/2014, ou après avoir fourni la preuve de leur identité et de leur établissement au moyen d’une attestation électronique qualifiée d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’opérateur économique; |
| --- | --- |

| (b) | lorsqu’ils ne sont pas tenus d’être établis dans l’Union, ils fournissent la preuve de leur identité et, le cas échéant, de leur établissement au moyen d’un cachet électronique qualifié étayé par un certificat qualifié de cachet électronique, délivré par un prestataire de services de confiance qualifié conformément au règlement (UE) no 910/2014, ou au moyen d’une attestation électronique d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’opérateur économique. |
| --- | --- |

3. Sans préjudice d’autres dispositions du droit de l’Union, l’accès au registre des passeports numériques de produit est accordé aux opérateurs économiques vérifiés aux fins de l’enregistrement des passeports numériques de produit.

4. Les opérateurs économiques conservent le statut d’opérateurs économiques vérifiés jusqu’à l’expiration de leurs moyens d’identification électronique, pour une période ne dépassant toutefois pas trois ans à compter de la date de vérification conformément au paragraphe 1 ou 2. À l’expiration de ces moyens ou de la période de trois ans, la date la plus proche étant retenue, les opérateurs économiques ne peuvent plus enregistrer de nouveaux passeports numériques de produit dans le registre ni modifier toute donnée visée à l’article 8. Ils ne peuvent procéder de la sorte que s’ils ont renouvelé avec succès le processus de vérification de leur identité conformément au paragraphe 1 ou 2. Le statut du passeport numérique de produit dans le registre est mis à jour en conséquence.

5. Sans préjudice du paragraphe 4, lorsque le registre des passeports numériques de produit est intégré à un autre système d’information de l’Union disposant d’un processus de vérification de l’identité équivalent ou identique, l’opérateur économique déjà enregistré dans ce système d’information n’est pas tenu de se soumettre à un nouveau processus de vérification de l’identité dans le registre des passeports numériques de produit.

<a id="art_5"></a>

### art_5

Article 5

1. Les acteurs de la chaîne de valeur qui sont des personnes physiques agissant en tant que commerçants individuels obtiennent un statut vérifié dans le registre si l’une des deux conditions suivantes est remplie:

| (a) | lorsqu’ils sont tenus d’être établis dans l’Union, ils fournissent une preuve de leur identité au moyen d’une signature électronique qualifiée étayée par un certificat qualifié de signature électronique conformément au règlement (UE) no 910/2014, ou ils fournissent la preuve de leur identité par un moyen d’identification électronique qui satisfait aux exigences du règlement (UE) no 910/2014 concernant le niveau de garantie «élevé», ou par une attestation électronique d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’acteur de la chaîne de valeur; |
| --- | --- |

| (b) | lorsqu’ils ne sont pas tenus d’être établis dans l’Union, ils fournissent la preuve de leur identité au moyen d’une signature électronique qualifiée étayée par un certificat qualifié de signature électronique conformément au règlement (UE) no 910/2014, ou par une attestation électronique d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’acteur de la chaîne de valeur. |
| --- | --- |

2. Les acteurs de la chaîne de valeur agissant en tant que personnes morales obtiennent un statut vérifié dans le registre si l’une des conditions suivantes est remplie:

| (a) | lorsqu’ils sont tenus d’être établis dans l’Union, ils fournissent la preuve de leur identité et de leur établissement dans l’Union au moyen d’un cachet électronique qualifié étayé par un certificat qualifié de cachet électronique délivré par un prestataire de services de confiance qualifié conformément au règlement (UE) no 910/2014, ou ils fournissent la preuve de leur identité et de leur établissement au moyen d’une attestation électronique qualifiée d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’acteur de la chaîne de valeur; |
| --- | --- |

| (b) | lorsqu’ils ne sont pas tenus d’être établis dans l’Union, ils fournissent la preuve de leur identité et, le cas échéant, de leur établissement au moyen d’un cachet électronique qualifié étayé par un certificat qualifié de cachet électronique, délivré par un prestataire de services de confiance qualifié conformément au règlement (UE) no 910/2014, ou au moyen d’une attestation électronique d’attributs délivrée en vertu du droit de l’Union qui permet l’identification de l’acteur de la chaîne de valeur. |
| --- | --- |

3. Seuls les acteurs de la chaîne de valeur vérifiés ont accès au registre et peuvent effectuer, lorsque le droit de l’Union applicable le prévoit, des actions dans le registre.

4. Un acteur de la chaîne de valeur conserve le statut d’acteur vérifié jusqu’à l’expiration de ses moyens d’identification électronique et, en tout état de cause, pas plus de trois ans à compter de la date de vérification conformément au paragraphe 1 ou 2. À l’expiration de ces moyens ou de la période de trois ans, la date la plus proche étant retenue, ces acteurs ne peuvent plus procéder à des enregistrements ni modifier toute donnée dans le registre. Ils ne peuvent procéder de la sorte que s’ils ont renouvelé avec succès le processus de vérification de leur identité conformément au paragraphe 1 ou 2.

5. Sans préjudice du paragraphe 4, lorsque le registre des passeports numériques de produit est intégré à un autre système d’information de l’Union disposant d’un processus de vérification de l’identité équivalent ou identique, l’acteur de la chaîne de valeur déjà enregistré dans ce système d’information n’est pas tenu de se soumettre à un nouveau processus de vérification de l’identité dans le registre des passeports numériques de produit.

<a id="art_6"></a>

### art_6

Article 6

1. Lorsque le droit de l’Union le prévoit, les opérateurs économiques vérifiés et les acteurs de la chaîne de valeur vérifiés peuvent déléguer des droits d’accès à des utilisateurs tiers agissant pour leur compte.

2. Toute donnée à caractère personnel intégrée dans le profil d’utilisateur d’un opérateur économique vérifié ou d’un acteur de la chaîne de valeur vérifié est traitée conformément au règlement (UE) 2018/1725.

3. Chaque opérateur économique et chaque acteur de la chaîne de valeur sont responsables de la gestion de leur processus de vérification électronique conformément aux articles 4 et 5, respectivement.

4. Il incombe à l’opérateur économique vérifié et à l’acteur de la chaîne de valeur vérifié de mettre à jour leurs données en cas de modification pertinente.

<a id="art_6a"></a>

### art_6a

Article 6 bis

Les passeports numériques de produit enregistrés peuvent être transférés à un autre opérateur économique vérifié ou, le cas échéant, à un acteur de la chaîne de valeur vérifié qui assume les obligations de l’acteur précédent en ce qui concerne les passeports numériques de produit concernés à partir de la date indiquée pour le transfert.

<a id="art_7"></a>

### art_7

Article 7

1. Au plus tard le 18 février 2027, les États membres désignent un administrateur national qui fera office de point de contact officiel unique pour la Commission aux fins de la gestion des droits d’accès au registre concernant cet État membre.

2. Les États membres communiquent à la Commission le nom et les coordonnées de leur administrateur national désigné respectif et notifient à la Commission toute modification ultérieure concernant cet administrateur.

3. L’administrateur national désigné peut déléguer les droits d’accès au registre aux autorités nationales compétentes de son État membre. Cette délégation est effectuée sous l’entière responsabilité de l’État membre et de manière à garantir la sécurité, l’intégrité et la confidentialité des données du registre consultées conformément au présent règlement.

4. Les autorités nationales auxquelles l’accès a été accordé par leur administrateur national désigné peuvent déléguer et gérer les droits d’accès au registre au sein de leur autorité respective.

5. Les données à caractère personnel contenues dans les profils d’utilisateur et les comptes d’utilisateur des autorités nationales compétentes et des autorités douanières sont traitées par la Commission en sa qualité de responsable du traitement conformément au règlement (UE) 2018/1725.

<a id="art_8"></a>

### art_8

Article 8

1. Pour les produits visés à l’article 1er, paragraphe 1, point a), un passeport numérique de produit est enregistré par un opérateur économique vérifié qui met ce produit sur le marché ou le met en service au niveau précisé dans les actes délégués applicables (au niveau du modèle, du lot ou de l’article) adoptés en vertu de l’article 4 du règlement (UE) 2024/1781.

2. Pour les produits visés à l’article 1er, paragraphe 1, points b) à f), un passeport numérique de produit est enregistré par l’acteur concerné au niveau (du modèle, du lot ou de l’article) précisé dans la législation pertinente de l’Union.

Lorsque le droit de l’Union prévoit qu’un tiers peut effectuer des actions dans le registre pour le compte des acteurs visés au premier ou au deuxième alinéa, ce tiers, une fois vérifié conformément à l’article 19, paragraphe 4, sera autorisé à effectuer des actions d’enregistrement dans le registre.

3. Lorsque le même produit est soumis à différentes règles de l’Union imposant l’enregistrement de son passeport numérique de produit à différents niveaux de granularité, il convient d’enregistrer le passeport numérique du produit pour le produit concerné au niveau le plus détaillé requis par la législation applicable de l’Union.

4. Lorsque le passeport numérique de produit est créé au niveau de l’article, conformément au paragraphe 1, les identifiants des lots et des modèles sont associés à ce passeport numérique de produit si une conception par lots et par modèles existe pour le produit.

5. Lorsque le passeport numérique de produit est créé au niveau du lot, conformément au paragraphe 1, les identifiants des modèles sont associés à ce passeport numérique de produit si une conception par modèles existe pour le produit.

6. Pour enregistrer un passeport numérique de produit, l’acteur concerné visé au paragraphe 1 utilise soit l’interface utilisateur sécurisée du registre prévue à l’article 3, point a), soit l’API prévue à l’article 3, point b).

7. Lorsqu’une demande d’enregistrement est soumise, la Commission consulte le contenu du passeport numérique de produit et confirme automatiquement:

| (a) | la conformité sémantique des données fournies dans le passeport numérique de produit, comme prévu dans les actes délégués applicables adoptés en vertu de l’article 4 du règlement (UE) 2024/1781 ou dans les actes délégués applicables adoptés en vertu de l’article 77 du règlement (UE) 2023/1542, ou en vertu d’autres dispositions du droit de l’Union prévoyant l’enregistrement des données relatives au passeport numérique de produit dans le registre; |
| --- | --- |

| (b) | le cas échéant, la cohérence entre les données obligatoires à télécharger dans le registre et la valeur des données fournies dans le passeport numérique de produit; |
| --- | --- |

| (c) | la conformité du passeport numérique de produit avec le niveau de granularité (modèle, lot ou article) prévu dans les actes délégués applicables adoptés en vertu de l’article 4 du règlement (UE) 2024/1781 ou dans les actes délégués applicables adoptés en vertu de l’article 77 du règlement (UE) 2023/1542, ou en vertu d’autres dispositions du droit de l’Union prévoyant un niveau de granularité spécifique pour l’enregistrement du passeport numérique de produit dans le registre; |
| --- | --- |

| (d) | le cas échéant, la validité du code de marchandise du produit par rapport aux gammes autorisées pour le groupe de produits concerné; |
| --- | --- |

| (e) | le cas échéant, le lien vers la sauvegarde hébergée par un prestataire de services de passeport numérique de produit. |
| --- | --- |

8. Après une vérification réussie conformément au paragraphe 6, le registre génère et stocke un identifiant d’enregistrement unique et permanent, qui fait partie des données d’enregistrement.

9. En outre, la Commission stocke dans le registre les informations suivantes, qui font partie des données d’enregistrement:

| (a) | le cas échéant, les identifiants uniques; |
| --- | --- |

| (b) | le cas échéant, le code de marchandise du produit; |
| --- | --- |

| (c) | le cas échéant, la référence au prestataire de services de passeport numérique de produit; |
| --- | --- |

| (d) | les informations relatives au responsable de l’enregistrement, y compris la date et l’heure de l’enregistrement et l’intégrité du passeport numérique de produit, en tant qu’éléments de preuve de l’événement d’enregistrement. |
| --- | --- |

10. Lorsque l’acteur concerné visé au paragraphe 1 a soumis avec succès les données dans le registre, la Commission communique automatiquement à cet acteur concerné l’identifiant d’enregistrement unique associé à ce produit spécifique, généré conformément au paragraphe 9. L’identifiant d’enregistrement unique est communiqué par l’intermédiaire de l’interface utilisateur ou de la réponse de l’API, en fonction du service utilisé par l’acteur concerné lors de l’enregistrement.

<a id="art_9"></a>

### art_9

Article 9

1. Un opérateur économique ou, le cas échéant, un tiers agissant pour le compte de l’opérateur économique qui a enregistré un passeport numérique de produit dans le registre conformément à l’article 8 est en mesure de générer, à tout moment, une preuve d’enregistrement pour un ou plusieurs passeports numériques de produit dont cet opérateur économique est responsable.

2. La preuve d’enregistrement sert à démontrer, y compris auprès de tiers, que l’obligation d’enregistrement pour ce passeport numérique de produit a été remplie. Elle est générée sous la forme d’un document électronique sécurisé qui peut être téléchargé à partir du registre par l’acteur qui a enregistré le passeport numérique de produit, et contient au moins les données suivantes:

| (a) | un identifiant de produit unique; |
| --- | --- |

| (b) | le cas échéant, le code de marchandise visé à l’article 8, paragraphe 9, point b); |
| --- | --- |

| (c) | le nom et l’identité de l’opérateur économique vérifié responsable de l’enregistrement visé à l’article 8, paragraphe 9, point d); |
| --- | --- |

| (d) | la date et l’heure de l’enregistrement de la dernière version du passeport numérique de produit pour laquelle la preuve est générée, conformément à l’article 8, paragraphe 9, point d), données validées par un horodatage électronique de la Commission; |
| --- | --- |

| (e) | une empreinte de la version du passeport numérique de produit pour laquelle la preuve est générée. |
| --- | --- |

3. La preuve d’enregistrement est garantie au moyen d’un cachet électronique qualifié conformément à l’article 38 du règlement (UE) no 910/2014 et comporte l’horodatage électronique de la Commission visé au paragraphe 2, point d).

4. La Commission met la preuve d’enregistrement à la disposition de l’opérateur économique demandeur vérifié dans le registre, au moyen de l’interface utilisateur sécurisée du registre ou de l’API, en fonction du service choisi par l’opérateur économique. Cette preuve reste disponible pendant une période de 90 jours civils à compter de la date de sa production.

<a id="art_10"></a>

### art_10

Article 10

1. Toute modification des données d’enregistrement du passeport numérique de produit, y compris concernant sa création, sa modification et sa suppression, est consignée dans le système d’enregistrement du registre conformément à l’article 14 et prise en considération dans le statut de l’enregistrement.

2. Le registre prend en charge les différentes versions des données enregistrées et conserve un horodatage de la Commission pour chaque mise à jour.

3. Si le droit de l’Union ne prévoit pas de durée spécifique pour la disponibilité d’un passeport numérique de produit, les données d’enregistrement de ce passeport, visées à l’article 8, paragraphes 7 et 8, sont automatiquement supprimées du registre dix ans après l’enregistrement. Si le droit de l’Union prévoit une durée spécifique pour la disponibilité d’un passeport numérique de produit, la durée de conservation de ces données est alignée sur la durée de disponibilité du passeport numérique de produit.

4. Les utilisateurs du registre ont le droit de demander la suppression de leur compte respectif s’ils ne sont plus responsables des activités liées au registre.

<a id="art_11"></a>

### art_11

Article 11

1. Le modèle de données applicable à chaque groupe de produits est fondé, lorsqu’il est disponible, sur les actes délégués adoptés en vertu de l’article 4 du règlement (UE) 2024/1781 ou d’autres actes législatifs applicables de l’Union.

2. Le cas échéant, les modèles de données peuvent s’appuyer sur les ressources sémantiques, les vocabulaires contrôlés et les modèles de données de référence existants de l’Union.

3. Toutes les données contenues dans un passeport numérique de produit sont structurées conformément aux modèles de données communs et aux définitions sémantiques publiés dans le référentiel sémantique visé à l’article 12.

4. Les modèles de données font l’objet de différentes versions.

<a id="art_12"></a>

### art_12

Article 12

1. La Commission établit et tient à jour un référentiel sémantique des passeports numériques de produit, qui constitue une source faisant autorité, lisible par machine, pour les modèles de données, les définitions sémantiques et les vocabulaires applicables aux passeports numériques de produit dans tous les groupes de produits. Le référentiel sémantique est élaboré et sa maintenance est réalisée conformément au règlement (UE) 2024/903 du Parlement européen et du Conseil (16).

2. Le référentiel sémantique comprend au moins les éléments suivants:

| (a) | la signification sémantique des attributs de données requis dans un passeport numérique de produit et les spécifications techniques pour créer, le cas échéant, des liens dactylographiés et résolubles entre différents passeports numériques de produit, ainsi que des liens entre les attributs du passeport numérique de produit et les éléments de preuve sous-jacents communiqués tout au long de la chaîne de valeur du produit; |
| --- | --- |

| (b) | les modèles de données pour les différents produits relevant du champ d’application du présent règlement et leurs formats; |
| --- | --- |

| (c) | les métadonnées collectées concernant les modèles de données pour les produits; |
| --- | --- |

| (d) | la signification sémantique des rôles prévus dans les actes délégués applicables adoptés en vertu de l’article 4 du règlement (UE) 2024/1781, ou par d’autres actes législatifs de l’Union applicables à tout produit pour lequel il convient d’utiliser un passeport numérique de produit; |
| --- | --- |

| (e) | des étiquettes et définitions multilingues pour tous les attributs de données obligatoires. |
| --- | --- |

3. Les métadonnées visées au paragraphe 2, point c), sont conformes aux spécifications DCAT-AP (17).

4. La Commission veille à ce que, pour tout attribut de modèle de données nouvellement introduit dans le référentiel sémantique, les étiquettes et définitions multilingues visées au paragraphe 2, point e), soient publiées dans le référentiel sémantique.

5. Le référentiel sémantique comprend un service de recherche permettant à tout utilisateur de lire, de rechercher et d’extraire des définitions sémantiques et des structures de données.

6. La Commission veille à ce que le contenu du référentiel sémantique soit accessible au moyen d’API documentées publiquement. Ces API prennent en charge des formats de données communs et fournissent des ressources sémantiques lisibles par machine pour faciliter leur utilisation automatisée par des systèmes externes.

7. L’accès au référentiel sémantique et à ses API, ainsi que leur utilisation, sont gratuits.

<a id="art_13"></a>

### art_13

Article 13

1. La Commission fournit un service d’assistance pour veiller à ce que les opérateurs économiques, les acteurs de la chaîne de valeur, les autorités nationales compétentes et les autorités douanières puissent bénéficier d’une assistance technique sur demande. Le service d’assistance fonctionnera tout au long de l’année de 8 h 00 à 20 h 00, heure de Bruxelles. De plus amples informations opérationnelles sont disponibles sur le site web de la Commission. Par ailleurs, la Commission mettra au point, au plus tard pour février 2029, un outil d’assistance technique automatisé, qui sera accessible 24 heures sur 24 tout au long de l’année.

2. Les échanges écrits entre les opérateurs économiques, les acteurs de la chaîne de valeur, les autorités nationales compétentes ou les autorités douanières et le service d’assistance sont conservés pendant six mois après la clôture de la demande d’assistance technique visée au paragraphe 1 et sont mis à la disposition des autorités de surveillance du marché sur demande.

<a id="art_14"></a>

### art_14

Article 14

1. La Commission met en place, tient à jour et gère un système d’enregistrement par fichiers journaux. Elle veille à ce qu’une piste d’audit complète, précise et fiable soit créée dans ce système.

2. Dans le système d’enregistrement par fichiers journaux, la Commission consigne les événements se rapportant à l’ensemble des catégories d’actions suivantes:

| (a) | les données relatives aux entrées d’accès et d’authentification; |
| --- | --- |

| (b) | les modifications de données effectuées par tous les utilisateurs du registre, y compris le chargement ou la mise à jour des données visées à l’article 13, paragraphe 4, du règlement (UE) 2024/1781 ou des données devant être chargées dans le registre en vertu d’autres actes législatifs de l’Union qui imposent l’utilisation du passeport numérique de produit pour un produit donné; |
| --- | --- |

| (c) | les actions administratives réalisées par tous les utilisateurs du registre, y compris la création, la modification ou la suppression de comptes d’utilisateur, les modifications des droits d’accès et des autorisations, ainsi que toute modification de la configuration du registre et toute autre action administrative effectuée par les utilisateurs du registre; |
| --- | --- |

| (d) | les fichiers journaux d’échange de données. |
| --- | --- |

3. Pour garantir que les données stockées dans le registre sont traitées de manière sécurisée et dans le respect du droit de l’Union, la Commission conserve les fichiers journaux pendant une période:

| (a) | de six mois pour les catégories d’actions visées au paragraphe 2, point a); |
| --- | --- |

| (b) | de cinq ans pour les catégories d’actions visées au paragraphe 2, points c) et d); |
| --- | --- |

| (c) | correspondant à la durée de l’enregistrement des événements se rapportant aux catégories d’actions visées au paragraphe 2, point b). |
| --- | --- |

4. En cas d’incident présumé et aux fins des audits et des contrôles de sécurité aléatoires effectués par les autorités nationales compétentes et les autorités douanières, la Commission met les registres pertinents visés au paragraphe 2 à la disposition des autorités nationales concernées.

5. La Commission applique des mesures techniques et organisationnelles appropriées pour garantir la sécurité de tous les fichiers journaux et protéger leur intégrité, en particulier contre le traitement non autorisé ou illicite, la perte, la destruction ou les dégâts d’origine accidentelle. Ces mesures garantissent, au minimum, l’immuabilité et la confidentialité des fichiers journaux.

<a id="art_15"></a>

### art_15

Article 15

1. La Commission publie sur son site internet des orientations et des instructions sur la manière d’enregistrer et de gérer les données dans le registre.

2. Le registre est accessible à tout moment, sauf pendant les activités de maintenance nécessaires, telles que le déploiement de nouvelles versions logicielles, et sans préjudice du paragraphe 3. Dans de tels cas, la Commission publie un avis préalable d’inaccessibilité sur le site web public du registre.

3. La Commission peut suspendre la mise à disposition du registre, sans préavis, lorsque cela est nécessaire en raison d’un dysfonctionnement, d’une cyberattaque ou d’un besoin urgent et impérieux en matière de sécurité, jusqu’à ce que le problème soit résolu.

4. Lorsque l’indisponibilité temporaire ou le dysfonctionnement du registre empêche les enregistrements, la Commission enregistre la date et l’heure de l’indisponibilité et met ces informations à la disposition des opérateurs économiques, des acteurs de la chaîne de valeur, des autorités nationales compétentes et des autorités douanières, à leur demande, pendant au moins cinq ans.

<a id="art_16"></a>

### art_16

Article 16

1. La Commission assure la sécurité du registre et de ses composantes conformément à l’article 3. À cette fin, elle peut procéder à des audits techniques et à des contrôles aléatoires des éléments qui composent le registre.

2. Aux fins du paragraphe 1, la Commission prend les mesures nécessaires pour:

| (a) | empêcher tout accès non autorisé au registre; |
| --- | --- |

| (b) | empêcher tout traitement non autorisé des données du registre; |
| --- | --- |

| (c) | détecter toute activité non autorisée dans le registre; |
| --- | --- |

| (d) | empêcher toute violation de données dans le registre; |
| --- | --- |

| (e) | veiller à ce que les événements liés à la sécurité soient enregistrés conformément aux normes de sécurité des technologies de l’information appliquées par la Commission. |
| --- | --- |

<a id="art_17"></a>

### art_17

Article 17

Lorsque la Commission détecte une activité inappropriée ou frauduleuse dans le registre, y compris une activité liée au téléchargement de données massives, elle prend les mesures nécessaires pour éviter et contrer cette activité ainsi que pour en atténuer les effets.

Tout utilisateur qui a connaissance d’un comportement malveillant dans le registre ou qui a des motifs raisonnables de soupçonner un tel comportement en informe immédiatement la Commission et, le cas échéant, les États membres concernés.

<a id="art_18"></a>

### art_18

Article 18

1. La Commission stocke les données à caractère personnel suivantes dans le registre afin de garantir la vérification de l’identité de tous les utilisateurs:

| (a) | le prénom et le nom de famille de chaque utilisateur, ou le prénom et le nom de la personne légalement autorisée à agir en tant que représentant légal de l’opérateur économique, le cas échéant; |
| --- | --- |

| (b) | les identifiants d’authentification associés à l’utilisateur, y compris les identifiants de connexion ou les jetons d’authentification, nécessaires pour l’accès sécurisé au registre; |
| --- | --- |

| (c) | l’adresse postale des opérateurs économiques et des acteurs de la chaîne de valeur qui sont des utilisateurs; |
| --- | --- |

| (d) | l’adresse électronique de chaque utilisateur; |
| --- | --- |

| (e) | les métadonnées intégrées dans les documents chargés, lorsque ces métadonnées permettent l’identification ou la vérification d’un utilisateur. |
| --- | --- |

2. Dans le cas de personnes physiques, la Commission est également tenue de conserver des identifiants personnels, tels qu’un numéro de passeport, un numéro de carte d’identité nationale ou un numéro national d’identification électronique, un numéro d’enregistrement civil, un numéro d’identification fiscale délivré par l’autorité nationale compétente de l’État membre concerné, ou tout identifiant de pays tiers attribué à une personne ou tout document permettant d’identifier cette personne.

3. Les données à caractère personnel sont traitées conformément au règlement (UE) 2018/1725.

<a id="art_19"></a>

### art_19

Article 19

1. Un opérateur économique vérifié qui enregistre un passeport numérique de produit fournit à la Commission, en tant que gestionnaire du registre, toutes les informations nécessaires à l’enregistrement conformément à l’article 8. L’opérateur économique vérifié est responsable de l’exactitude et de l’exhaustivité des informations soumises au moment de l’enregistrement.

2. L’opérateur économique vérifié veille à ce que les informations stockées dans le registre du passeport numérique de produit soient à tout moment exactes, complètes et à jour.

3. L’opérateur économique vérifié est chargé d’appliquer des mesures de sécurité techniques et organisationnelles appropriées aux systèmes informatiques et aux identifiants qu’il utilise pour accéder au registre, afin d’empêcher l’accès non autorisé aux données d’enregistrement ou toute modification de celles-ci par l’intermédiaire de son système informatique.

4. Lorsqu’un opérateur économique vérifié autorise un tiers à effectuer des actions d’enregistrement dans le registre en son nom, ce tiers doit se soumettre au processus de vérification conformément à l’article 5. L’opérateur économique vérifié reste pleinement responsable du respect des obligations énoncées dans le présent règlement.

5. Chaque opérateur économique vérifié est responsable des données qu’il transmet à la Commission, en tant que gestionnaire du registre, et est considéré comme le responsable du traitement des données qu’il transmet.

<a id="art_20"></a>

### art_20

Article 20

1. Lorsqu’un acteur de la chaîne de valeur vérifié autorise un tiers à agir en son nom, l’acteur de la chaîne de valeur vérifié reste responsable du respect des obligations énoncées dans le présent règlement.

2. Tout acteur de la chaîne de valeur vérifié est chargé d’appliquer des mesures de sécurité techniques et organisationnelles appropriées aux systèmes informatiques et aux identifiants qu’il utilise pour accéder au registre, afin d’empêcher l’accès non autorisé aux données d’enregistrement ou toute modification de celles-ci par l’intermédiaire de son système informatique.

3. Lorsque le droit de l’Union prévoit que les acteurs de la chaîne de valeur chargent des informations dans le registre des passeports numériques de produit, chaque acteur de la chaîne de valeur vérifié est responsable des données qu’il soumet à la Commission, en tant que gestionnaire du registre, et est considéré comme le responsable du traitement des données qu’il transmet.

<a id="art_21"></a>

### art_21

Article 21

1. La Commission veille à ce que les données stockées dans le registre soient traitées de manière sécurisée et dans le respect du droit de l’Union, y compris des règles applicables en matière de protection des données à caractère personnel.

2. La Commission est propriétaire du registre et responsable de sa gestion, y compris de son développement, de sa disponibilité, de son suivi, de sa mise à jour, de sa maintenance et de son hébergement.

3. Les données que la Commission peut obtenir du registre peuvent être transmises aux services compétents au sein de la Commission ou aux autorités nationales compétentes aux fins de l’exécution des mesures requises en vertu d’autres actes législatifs de l’Union, y compris aux fins de la surveillance du marché, de la protection des consommateurs et du respect des obligations douanières.

<a id="art_22"></a>

### art_22

Article 22

1. Lorsque les États membres créent une interconnexion avec le registre, ils sont considérés comme les propriétaires de leurs systèmes d’information respectifs, ce qui inclut toute composante mise au point par ces États membres aux fins de l’interconnexion. Ils sont responsables de la mise au point, du développement, de la disponibilité, du suivi, de la mise à jour, de la maintenance et de l’hébergement des composantes utilisées pour accéder au registre sous leur responsabilité.

2. Les États membres garantissent un niveau de sécurité approprié des composantes nationales utilisées pour accéder au registre, conformément au droit de l’Union. Sans retard injustifié, ils informent la Commission des modifications et mises à jour apportées aux composantes relevant de leur responsabilité qui peuvent avoir une incidence sur le fonctionnement, la disponibilité et la fiabilité du registre.

3. Les États membres peuvent traiter les données issues du registre. Lorsque les États membres traitent des données issues du registre, ces données sont traitées conformément au droit de l’Union.

4. Lorsqu’ils traitent des données à caractère personnel afin de satisfaire à leurs obligations définies dans le droit de l’Union ou dans leur législation nationale qui est conforme au droit de l’Union, les États membres sont considérés comme les responsables du traitement au sens de l’article 4, point 7), du règlement (UE) 2016/679.

5. Les États membres sont responsables de toutes les activités de traitement de données effectuées sous leur contrôle, ce qui inclut:

| (a) | la gestion de l’enregistrement et de l’intégration des autorités nationales compétentes et, le cas échéant, des autorités douanières, par l’intermédiaire de l’administrateur national désigné visé à l’article 7, paragraphe 2; |
| --- | --- |

| (b) | les mesures garantissant que tout traitement de données réalisé sous leur contrôle est effectué conformément au règlement (UE) 2016/679; |
| --- | --- |

| (c) | le retrait des droits d’accès d’un utilisateur au registre en cas d’accès non autorisé ou incorrect au registre. |
| --- | --- |

<a id="art_23"></a>

### art_23

Article 23

Dans le cadre du suivi et de l’évaluation du règlement (UE) 2024/1781 et de sa contribution au fonctionnement du marché intérieur, la Commission procède, au plus tard pour la fin de 2032, puis tous les six ans, à une évaluation du présent règlement afin de tenir compte du fonctionnement du registre des passeports numériques de produit et, le cas échéant, présente un projet de proposition de révision.

<a id="art_24"></a>

### art_24

Article 24

Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
