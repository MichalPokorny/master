from prototype.lib import article_repo
from prototype.lib import parse_xmls_to_protos
from xml.etree import ElementTree
import paths
from prototype.lib import dbpedia

dbpedia_client = dbpedia.DBpediaClient()

def document_to_html(document):
    html = ""
    html += "<pre>"
    html += document.text
    html += "</pre>"
    html += ""

    for sentence in document.sentences:
        html += "<pre>"
        html += sentence.text
        html += "</pre>"

        for coreference in document.coreferences:
            for mention in coreference.mentions:
                if mention.sentence_id == sentence.id:
                    html += str(coreference.wikidata_entity_id) + ": " + str(mention) + "<br>"

        for mention in document.find_spotlight_mentions_between(sentence.start_offset(),
                                                                sentence.end_offset()):
            html += "<b>" + str(dbpedia_client.dbpedia_uri_to_wikidata_id(mention.uri)) + "</b> "
            html += str(mention) + "<br>"

        for token in sentence.tokens:
            html += str(token) + "<br>"

    html += "<h2>Coreferences</h2>"
    for coreference in document.coreferences:
        for mention in coreference.mentions:
            html += "<i>" + str(mention) + "</i>: "
            mention_start = document.get_mention_start(mention)
            mention_end = document.get_mention_end(mention)
            for resource in document.find_spotlight_mentions_between(mention_start, mention_end):
                html += str(resource)
            html += "<br>"

        html += "<hr>"

    return html

article_repository = article_repo.ArticleRepo()
article = article_repository.load_article("Douglas Adams")
proto = parse_xmls_to_protos.document_to_proto(
    title = "Douglas Adams",
    root = ElementTree.fromstring(article['corenlp_xml']),
    spotlight_json = article['spotlight_json'],
    plaintext = article['plaintext'],
)
print(document_to_html(proto))
