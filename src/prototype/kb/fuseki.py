from src.prototype.lib import pbs_util
import os
import subprocess

def serve_forever(#dataset_path,
                  #namespace,
                  config,
                  port):
    os.chdir('../jena_fuseki/apache-jena-fuseki-2.4.0')
    os.execv("/bin/bash", [
        "bash",
        "-c",
        ' '.join([
            "./fuseki-server",
            #"--loc", dataset_path,
            "--config", config,
            "--port", str(port),
            #namespace
        ]),
    ])

def spawn(#dataset_path,
          #namespace,
          config,
          port):
    subprocess.Popen([
        "./fuseki-server",
        # "--loc", dataset_path,
        "--config", config,
        "--port", str(port),
    ], cwd="../jena_fuseki/apache-jena-fuseki-2.4.0")