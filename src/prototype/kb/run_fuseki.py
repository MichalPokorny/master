from src.prototype.kb import fuseki
from src.prototype.kb import fuseki_config
from src.prototype.lib import zk
from src import paths
import datetime

# NOTE: must be absolute path
config_file_path = '/tmp/fuseki-config.ttl'
fuseki_config.write_config(
    config_file_path,
    datasets = {
        'merged': paths.WORK_DIR + '/fuseki-datasets/merged',
        # TODO: 'merged' when we merge it
    },
)

# TODO: not really Hador...
zk.set_wikidata_endpoint('http://hador:3030/merged/query')
zk.set_dbpedia_endpoint('http://hador:3030/merged/query')

print("Starting Fuseki...", datetime.datetime.now())
fuseki.serve_forever(
    config = config_file_path,
    port = 3030
)