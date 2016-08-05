#!/bin/bash

source common.sh

echo "installing own code"

FILES="\
	annotate_coreferences.py \
	annotate_coreferences.sh \
	article_parse.py \
	common.sh \
	get_training_samples.py \
	metacentrum_corenlp.sh \
	metacentrum_download_dumps.sh \
	metacentrum_get_training_samples.py \
	metacentrum_get_training_samples.sh \
	metacentrum_install_corenlp.sh \
	metacentrum_prepare.sh \
	metacentrum_split_wiki.sh \
	metacentrum_spotlight.py \
	metacentrum_spotlight.sh \
	myutil.py \
	nlpize_articles.py \
	nlpize_articles.sh \
	parse_xmls_to_protos.py \
	parse_xmls_to_protos.sh \
	data_stats.sh \
	sentence_pb2.py \
	split_wiki.py \
	spotlight.py \
	training_samples_pb2.py \
	wiki2text \
"

scp $FILES prvak@zuphux.metacentrum.cz:$BIN_ROOT
