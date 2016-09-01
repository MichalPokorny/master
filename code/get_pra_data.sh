#!/bin/bash
# TODO: and replace for smaller names.
# TODO: and remove UUIDs
./s-query --service=http://hador:3030/wikidata/query '
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?a ?b ?c
WHERE { { ?a wdt:P21 ?c } UNION
	{ ?a wdt:P22 ?c } UNION
	{ ?a wdt:P25 ?c } UNION
	{ ?a wdt:P27 ?c } UNION
	{ ?a wdt:P7 ?c } UNION
	{ ?a wdt:P9 ?c } UNION
	{ ?a wdt:P26 ?c } UNION
	{ ?a wdt:P451 ?c } UNION
	{ ?a wdt:P40 ?c } UNION
	{ ?a wdt:P43 ?c } UNION
	{ ?a wdt:P44 ?c } UNION
	{ ?a wdt:P1038 ?c } UNION
	{ ?a wdt:P1290 ?c } . ?a ?b ?c } LIMIT 10000' > result
