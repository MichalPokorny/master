# TODO: want commons_cli_commons_cli

# Stanford CoreNLP
http_jar(
    name = "corenlp_models",
    url = "http://nlp.stanford.edu/software/stanford-english-corenlp-2016-01-10-models.jar",
    sha256 = "8ad16bb419044a8c3efc2d14b9072c56b300e6f462183c62ff1f6470c11389c0"
)

http_jar(
    name = "corenlp_srparser_model",
    url = "http://nlp.stanford.edu/software/stanford-srparser-2014-10-23-models.jar",
    sha256 = "0335b1a443a41952d18a472ac65e49b4482424ffec12ddf41703c696e72c793d"
)

# DBpedia Spotlight
http_jar(
    name = "dbpedia_spotlight",
    url = "http://spotlight.sztaki.hu/downloads/archive/version-0.1/dbpedia-spotlight.jar",
    sha256 = "760ce9440be6858f956ad98bcbb4754636c31cdf77d23c6f98019cb02412d32b"
)

http_file(
    name = "dbpedia_spotlight_model_en",
    url = "http://spotlight.sztaki.hu/downloads/archive/version-0.1/en.tar.gz",
    sha256 = "773beb985b3a28d8618e620ac7ac699a59228e81f0afa56618f13e3984a40e2f",
)

# Apache Jena Fuseki
new_http_archive(
    name = "jena",
    url = "http://mirror.dkm.cz/apache/jena/binaries/apache-jena-3.1.0.tar.gz",
    sha256 = "532ad87eab7792ff1ffae34375d4c27956aada7c659743c39027e8b48f29cbd9",
    build_file_content = """
filegroup(
    name = "everything",
    srcs = glob(
	include = ["**/*"]
    ),
    visibility = ["//visibility:public"],
)
""",
)

new_http_archive(
    name = "jena_fuseki",
    url = "http://mirror.dkm.cz/apache/jena/binaries/apache-jena-fuseki-2.4.0.tar.gz",
    sha256 = "8b4299c35374bba47c6f9644166c069c243b08eb600a71f66c3c9cc2ec7e594a",
    build_file_content = """
filegroup(
    name = "everything",
    srcs = glob(
	include = ["**/*"]
    ),
    visibility = ["//visibility:public"],
)
""",
)

new_git_repository(
    name = "cpulimit",
    commit = "bf0506b593a3b0392804c007bab98faf579bc681",
    remote = "https://github.com/MichalPokorny/cpulimit",
    build_file_content = """
package(default_visibility = ["//visibility:public"])

genrule(
    name = "cpulimit_bin",
    srcs = glob(["src/*.c", "src/*.h", "src/Makefile"]),
    cmd = ("cd external/cpulimit/src; " +
           'CFLAGS="-Wall -g -D_GNU_SOURCE -B/usr/lib/x86_64-linux-gnu" make; ' +
           "mkdir -p -v $(@D); " +
           "cd ../../..; " +
           "cp -v external/cpulimit/src/cpulimit $(@)"),
    outs = ["cpulimit"],
)
""",
)

# git_repository(
#     name = "wiki2text",
#     commit = "ae50e5c7f69be643099d90ed6ca7c0fd9501ebf4",
#     remote = "https://github.com/rspeer/wiki2text"
# )

# bazel run //src/tools/generate_workspace -- \
#    --artifact=org.apache.hadoop:hadoop-common:2.6.0 \
#    --artifact=org.apache.hadoop:hadoop-mapreduce-client-core:2.6.0 \
#    --artifact=edu.stanford.nlp:stanford-corenlp:3.6.0 \
#    --artifact=org.json:json:20160810 \
#    --artifact=org.apache.jena:apache-jena-libs:3.1.0 \
#    --artifact=org.apache.httpcomponents:httpclient:4.2.6 \
#    --artifact=org.apache.httpcomponents:httpcore:4.2.5 \
#    --artifact=com.google.protobuf:protobuf-java:3.0.0 \
#    --artifact=org.apache.hbase:hbase-client:1.2.2 \
#    --artifact=org.apache.hbase:hbase-server:1.2.2

# The following dependencies were calculated from:
# org.apache.hadoop:hadoop-common:2.6.0
# org.apache.hadoop:hadoop-mapreduce-client-core:2.6.0
# edu.stanford.nlp:stanford-corenlp:3.6.0
# org.json:json:20160810
# org.apache.jena:apache-jena-libs:3.1.0
# org.apache.httpcomponents:httpclient:4.2.6
# org.apache.httpcomponents:httpcore:4.2.5
# com.google.protobuf:protobuf-java:3.0.0
# javax.xml.parsers:jaxp-api:1.4
# org.apache.hbase:hbase-client:1.2.2
# org.apache.hbase:hbase-server:1.2.2


# javax.xml.bind:jaxb-api:jar:2.2.2
maven_jar(
    name = "javax_xml_stream_stax_api",
    artifact = "javax.xml.stream:stax-api:1.0-2",
    sha1 = "d6337b0de8b25e53e81b922352fbea9f9f57ba0b",
)

# com.google.inject:guice:jar:3.0
maven_jar(
    name = "aopalliance_aopalliance",
    artifact = "aopalliance:aopalliance:1.0",
    sha1 = "0235ba8b489512805ac13a8f9ea77a1ca5ebe3e8",
)

# org.apache.hbase:hbase-common:jar:1.2.2
# com.github.jsonld-java:jsonld-java:bundle:0.7.0
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hbase:hbase-client:jar:1.2.2
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "commons_io_commons_io",
    artifact = "commons-io:commons-io:2.4",
    sha1 = "b1b6ea3b7e4aa4f492509a4952029cd8e48019ad",
)

# edu.stanford.nlp:stanford-corenlp:jar:3.6.0
maven_jar(
    name = "javax_json_javax_json_api",
    artifact = "javax.json:javax.json-api:1.0",
    sha1 = "0a74939ecbf7294b40accb4048929577f5ddcee2",
)

# org.apache.hbase:hbase-client:jar:1.2.2 wanted version 1.9
# org.apache.httpcomponents:httpclient:jar:4.1.2
# org.apache.hbase:hbase-common:jar:1.2.2 wanted version 1.9
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-auth:jar:2.6.0
# net.java.dev.jets3t:jets3t:jar:0.9.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "commons_codec_commons_codec",
    artifact = "commons-codec:commons-codec:1.4",
    sha1 = "4216af16d38465bbab0f3dff8efa14204f7a399a",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_apache_hadoop_hadoop_auth",
    artifact = "org.apache.hadoop:hadoop-auth:2.6.0",
    sha1 = "b0b8dec23a84ac8a0d00fbd69a87d320724ae34a",
)

# com.sun.jersey:jersey-server:bundle:1.9
# com.sun.jersey:jersey-client:bundle:1.9
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# com.sun.jersey:jersey-json:bundle:1.9
maven_jar(
    name = "com_sun_jersey_jersey_core",
    artifact = "com.sun.jersey:jersey-core:1.9",
    sha1 = "8341846f18187013bb9e27e46b7ee00a6395daf4",
)

# xerces:xercesImpl:jar:2.8.0
# xalan:xalan:jar:2.7.0 wanted version 2.0.2
# com.io7m.xom:xom:jar:1.2.10
maven_jar(
    name = "xml_apis_xml_apis",
    artifact = "xml-apis:xml-apis:1.3.03",
    sha1 = "3845d5aabd62dc1954f2c0e84a799068c917ad2b",
)

# com.sun.jersey:jersey-server:bundle:1.9
# org.sonatype.sisu.inject:cglib:jar:2.2.1-v20090111
maven_jar(
    name = "asm_asm",
    artifact = "asm:asm:3.1",
    sha1 = "c157def142714c544bdea2e6144645702adf7097",
)

maven_jar(
    name = "org_apache_jena_apache_jena_libs",
    artifact = "org.apache.jena:apache-jena-libs:3.1.0",
)

# com.google.inject.extensions:guice-servlet:jar:3.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# com.sun.jersey.contribs:jersey-guice:jar:1.9
maven_jar(
    name = "com_google_inject_guice",
    artifact = "com.google.inject:guice:3.0",
    sha1 = "9d84f15fe35e2c716a02979fb62f50a29f38aefa",
)

# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0
# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_apache_avro_avro",
    artifact = "org.apache.avro:avro:1.7.4",
    sha1 = "416e7030879814f52845b97f04bb50ecd1cef372",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "net_java_dev_jets3t_jets3t",
    artifact = "net.java.dev.jets3t:jets3t:0.9.0",
    sha1 = "792bc96ee7e57b89f472aa0cb5a31015b9f59c96",
)

# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "org_apache_hadoop_hadoop_yarn_api",
    artifact = "org.apache.hadoop:hadoop-yarn-api:2.6.0",
    sha1 = "c3bcbcd82cd61b55dc5d523f26a259f8d27fc237",
)

# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-api:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "org_apache_hadoop_hadoop_annotations",
    artifact = "org.apache.hadoop:hadoop-annotations:2.6.0",
    sha1 = "8cd40a4cde2b77e6edc1ab3bb55706d626ae8b2d",
)

# javax.xml.bind:jaxb-api:jar:2.2.2
maven_jar(
    name = "javax_activation_activation",
    artifact = "javax.activation:activation:1.1",
    sha1 = "e6cb541461c2834bdea3eb920f1884d1eb508b50",
)

# com.io7m.xom:xom:jar:1.2.10
maven_jar(
    name = "xalan_xalan",
    artifact = "xalan:xalan:2.7.0",
    sha1 = "a33c0097f1c70b20fa7ded220ea317eb3500515e",
)

# org.apache.jena:jena-arq:jar:3.1.0
maven_jar(
    name = "com_github_jsonld_java_jsonld_java",
    artifact = "com.github.jsonld-java:jsonld-java:0.7.0",
    sha1 = "8e5b63444ddaf911358dc66966617454f3590353",
)

# org.codehaus.jackson:jackson-mapper-asl:jar:1.8.3
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0 wanted version 1.9.13
# org.apache.hadoop:hadoop-common:jar:2.6.0 wanted version 1.9.13
# org.codehaus.jackson:jackson-xc:jar:1.8.3
# org.codehaus.jackson:jackson-jaxrs:jar:1.8.3
# org.apache.avro:avro:jar:1.7.4 wanted version 1.8.8
# com.sun.jersey:jersey-json:bundle:1.9
maven_jar(
    name = "org_codehaus_jackson_jackson_core_asl",
    artifact = "org.codehaus.jackson:jackson-core-asl:1.8.3",
    sha1 = "3130e71a7d929347c5b112e43fe29428dfc070e0",
)

# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "com_sun_jersey_contribs_jersey_guice",
    artifact = "com.sun.jersey.contribs:jersey-guice:1.9",
    sha1 = "5963c28c47df7e5d6ad34cec80c071c368777f7b",
)

# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "org_apache_hbase_hbase_common",
    artifact = "org.apache.hbase:hbase-common:1.2.2",
    sha1 = "4bff30dc3e7d39d6b78093a00cee1c3569afe67a",
)

# com.github.jsonld-java:jsonld-java:bundle:0.7.0
maven_jar(
    name = "com_fasterxml_jackson_core_jackson_databind",
    artifact = "com.fasterxml.jackson.core:jackson-databind:2.3.3",
    sha1 = "63b77400b5f1cf83a81823562c48d3120ef5518e",
)

# net.java.dev.jets3t:jets3t:jar:0.9.0
maven_jar(
    name = "com_jamesmurty_utils_java_xmlbuilder",
    artifact = "com.jamesmurty.utils:java-xmlbuilder:0.4",
    sha1 = "ac5962e48cdee3a0a6e1f8e00fcb594747ac5aaf",
)

# com.github.jsonld-java:jsonld-java:bundle:0.7.0
# com.fasterxml.jackson.core:jackson-databind:bundle:2.3.3
maven_jar(
    name = "com_fasterxml_jackson_core_jackson_core",
    artifact = "com.fasterxml.jackson.core:jackson-core:2.3.3",
    sha1 = "7d8c5d79cc99995e21e6f955857312d8409f02a1",
)

# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "com_yammer_metrics_metrics_core",
    artifact = "com.yammer.metrics:metrics-core:2.2.0",
    sha1 = "f82c035cfa786d3cbec362c38c22a5f5b1bc8724",
)

# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "org_apache_hbase_hbase_protocol",
    artifact = "org.apache.hbase:hbase-protocol:1.2.2",
    sha1 = "e68ad3928a464dd40482068b92ff2cbf9c8de286",
)

# org.apache.curator:curator-framework:bundle:2.6.0
# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_apache_curator_curator_client",
    artifact = "org.apache.curator:curator-client:2.6.0",
    sha1 = "b9007c357ad1a78066fc6004e8b1feaa2318f6f3",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_apache_curator_curator_recipes",
    artifact = "org.apache.curator:curator-recipes:2.6.0",
    sha1 = "8736b0fc42e6bf006d585fe85c90aaa4ade5cbef",
)

maven_jar(
    name = "org_apache_httpcomponents_httpcore",
    artifact = "org.apache.httpcomponents:httpcore:4.2.5",
)

# org.apache.hbase:hbase-protocol:jar:1.2.2
# org.apache.hbase:hbase-annotations:jar:1.2.2
# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.zookeeper:zookeeper:pom:3.4.6 wanted version 1.2.16
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# org.slf4j:slf4j-log4j12:jar:1.7.5
maven_jar(
    name = "log4j_log4j",
    artifact = "log4j:log4j:1.2.17",
    sha1 = "5af35056b4d257e4b64b9e8069c0746e8b08629f",
)

# org.apache.hbase:hbase-client:jar:1.2.2 wanted version 2.5.0
# org.apache.hbase:hbase-protocol:jar:1.2.2 wanted version 2.5.0
# org.apache.hbase:hbase-common:jar:1.2.2 wanted version 2.5.0
maven_jar(
    name = "com_google_protobuf_protobuf_java",
    artifact = "com.google.protobuf:protobuf-java:3.0.0",
)

# org.apache.zookeeper:zookeeper:pom:3.4.6
maven_jar(
    name = "jline_jline",
    artifact = "jline:jline:0.9.94",
    sha1 = "99a18e9a44834afdebc467294e1138364c207402",
)

# com.google.inject:guice:jar:3.0
maven_jar(
    name = "org_sonatype_sisu_inject_cglib",
    artifact = "org.sonatype.sisu.inject:cglib:2.2.1-v20090111",
    sha1 = "07ce5e983fd0e6c78346f4c9cbfa39d83049dda2",
)

# org.jruby.joni:joni:jar:2.1.2
# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "org_jruby_jcodings_jcodings",
    artifact = "org.jruby.jcodings:jcodings:1.0.8",
    sha1 = "33fa45fd853c277b888e3d5a2e6a4604b7c11e2c",
)

# org.apache.curator:curator-framework:bundle:2.6.0
# org.apache.curator:curator-recipes:bundle:2.6.0
# org.apache.curator:curator-client:bundle:2.6.0
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hbase:hbase-client:jar:1.2.2
# org.apache.hadoop:hadoop-auth:jar:2.6.0
maven_jar(
    name = "org_apache_zookeeper_zookeeper",
    artifact = "org.apache.zookeeper:zookeeper:3.4.6",
    sha1 = "01b2502e29da1ebaade2357cd1de35a855fa3755",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "commons_net_commons_net",
    artifact = "commons-net:commons-net:3.1",
    sha1 = "2298164a7c2484406f2aa5ac85b205d39019896f",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# com.sun.jersey.contribs:jersey-guice:jar:1.9
maven_jar(
    name = "com_sun_jersey_jersey_server",
    artifact = "com.sun.jersey:jersey-server:1.9",
    sha1 = "3a6ea7cc5e15c824953f9f3ece2201b634d90d18",
)

# org.apache.hadoop:hadoop-auth:jar:2.6.0
maven_jar(
    name = "org_apache_directory_server_apacheds_kerberos_codec",
    artifact = "org.apache.directory.server:apacheds-kerberos-codec:2.0.0-M15",
    sha1 = "1c16e4e477183641c5f0dd5cdecd27ec331bacb5",
)

# org.apache.hbase:hbase-common:jar:1.2.2
# org.htrace:htrace-core:jar:3.0.4
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.mortbay.jetty:jetty:jar:6.1.26
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "org_mortbay_jetty_jetty_util",
    artifact = "org.mortbay.jetty:jetty-util:6.1.26",
    sha1 = "e5642fe0399814e1687d55a3862aa5a3417226a9",
)

maven_jar(
    name = "org_apache_hbase_hbase_client",
    artifact = "org.apache.hbase:hbase-client:1.2.2",
)

# org.apache.commons:commons-compress:jar:1.4.1
maven_jar(
    name = "org_tukaani_xz",
    artifact = "org.tukaani:xz:1.0",
    sha1 = "ecff5cb8b1189514c9d1d8d68eb77ac372e000c9",
)

# org.apache.thrift:libthrift:pom:0.9.2 wanted version 1.5.8
# org.apache.jena:jena-core:jar:3.1.0 wanted version 1.7.20
# org.apache.jena:jena-arq:jar:3.1.0 wanted version 1.7.20
# org.apache.directory.api:api-util:bundle:1.0.0-M20
# org.apache.jena:jena-tdb:jar:3.1.0 wanted version 1.7.20
# org.apache.jena:jena-shaded-guava:jar:3.1.0 wanted version 1.7.20
# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0
# org.apache.jena:apache-jena-libs:pom:3.1.0 wanted version 1.7.20
# org.slf4j:jcl-over-slf4j:jar:1.7.5
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.jena:jena-iri:jar:3.1.0 wanted version 1.7.20
# org.apache.hadoop:hadoop-auth:jar:2.6.0
# edu.stanford.nlp:stanford-corenlp:jar:3.6.0 wanted version 1.7.12
# org.apache.curator:curator-client:bundle:2.6.0 wanted version 1.7.6
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# org.apache.jena:jena-base:jar:3.1.0 wanted version 1.7.20
# org.apache.avro:avro:jar:1.7.4 wanted version 1.6.4
# org.apache.directory.api:api-asn1-api:bundle:1.0.0-M20
# org.apache.directory.server:apacheds-kerberos-codec:bundle:2.0.0-M15
# com.yammer.metrics:metrics-core:jar:2.2.0 wanted version 1.7.2
# org.apache.directory.server:apacheds-i18n:bundle:2.0.0-M15
# org.apache.zookeeper:zookeeper:pom:3.4.6 wanted version 1.6.1
# org.slf4j:slf4j-log4j12:jar:1.7.5
maven_jar(
    name = "org_slf4j_slf4j_api",
    artifact = "org.slf4j:slf4j-api:1.7.5",
    sha1 = "6b262da268f8ad9eff941b25503a9198f0a0ac93",
)

# org.apache.jena:jena-tdb:jar:3.1.0
maven_jar(
    name = "org_apache_jena_jena_arq",
    artifact = "org.apache.jena:jena-arq:3.1.0",
    sha1 = "9f306f67f35a15d5c0ec486fef8e1e2ece34d0ee",
)

# org.apache.jena:jena-core:jar:3.1.0
maven_jar(
    name = "org_apache_jena_jena_iri",
    artifact = "org.apache.jena:jena-iri:3.1.0",
    sha1 = "13d22953f9ede17bee10eda82c4d6d2060c8a8c6",
)

# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "org_apache_htrace_htrace_core",
    artifact = "org.apache.htrace:htrace-core:3.1.0-incubating",
    sha1 = "f73606e7c9ede5802335c290bf47490ad6d51df3",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_mortbay_jetty_jetty",
    artifact = "org.mortbay.jetty:jetty:6.1.26",
    sha1 = "2f546e289fddd5b1fab1d4199fbb6e9ef43ee4b0",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "com_google_code_gson_gson",
    artifact = "com.google.code.gson:gson:2.2.4",
    sha1 = "a60a5e993c98c864010053cb901b7eab25306568",
)

# org.apache.directory.server:apacheds-kerberos-codec:bundle:2.0.0-M15
maven_jar(
    name = "org_apache_directory_api_api_util",
    artifact = "org.apache.directory.api:api-util:1.0.0-M20",
    sha1 = "a871abf060b3cf83fc6dc4d7e3d151fce50ac3cb",
)

# org.apache.jena:jena-arq:jar:3.1.0
maven_jar(
    name = "org_slf4j_jcl_over_slf4j",
    artifact = "org.slf4j:jcl-over-slf4j:1.7.20",
    sha1 = "722d5b58cb054a835605fe4d12ae163513f48d2e",
)

# com.fasterxml.jackson.core:jackson-databind:bundle:2.3.3
maven_jar(
    name = "com_fasterxml_jackson_core_jackson_annotations",
    artifact = "com.fasterxml.jackson.core:jackson-annotations:2.3.0",
    sha1 = "f5e853a20b60758922453d56f9ae1e64af5cb3da",
)

maven_jar(
    name = "org_apache_httpcomponents_httpclient",
    artifact = "org.apache.httpcomponents:httpclient:4.2.6",
)

# com.sun.jersey:jersey-json:bundle:1.9
maven_jar(
    name = "com_sun_xml_bind_jaxb_impl",
    artifact = "com.sun.xml.bind:jaxb-impl:2.2.3-1",
    sha1 = "56baae106392040a45a06d4a41099173425da1e6",
)

# org.apache.jena:jena-arq:jar:3.1.0
maven_jar(
    name = "org_apache_httpcomponents_httpclient_cache",
    artifact = "org.apache.httpcomponents:httpclient-cache:4.2.6",
    sha1 = "21dc2e715f7177fb218579bd5fc8aba135efa29a",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "commons_httpclient_commons_httpclient",
    artifact = "commons-httpclient:commons-httpclient:3.1",
    sha1 = "964cd74171f427720480efdec40a7c7f6e58426a",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_htrace_htrace_core",
    artifact = "org.htrace:htrace-core:3.0.4",
    sha1 = "d7461828faf28411f37f8570d896292db277d838",
)

# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "io_netty_netty_all",
    artifact = "io.netty:netty-all:4.0.23.Final",
    sha1 = "0294104aaf1781d6a56a07d561e792c5d0c95f45",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "com_sun_jersey_jersey_json",
    artifact = "com.sun.jersey:jersey-json:1.9",
    sha1 = "1aa73e1896bcc7013fed247157d7f676226eb432",
)

# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0 wanted version 1.9.13
# com.sun.jersey:jersey-json:bundle:1.9
maven_jar(
    name = "org_codehaus_jackson_jackson_jaxrs",
    artifact = "org.codehaus.jackson:jackson-jaxrs:1.8.3",
    sha1 = "3604ca9f572170e2ef5813141ec1f0e0100efd19",
)

# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hbase:hbase-client:jar:1.2.2
# org.apache.hadoop:hadoop-yarn-api:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "commons_lang_commons_lang",
    artifact = "commons-lang:commons-lang:2.6",
    sha1 = "0ce1edb914c94ebc388f086c6827e8bdeec71ac2",
)

# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0
maven_jar(
    name = "org_apache_hadoop_hadoop_yarn_common",
    artifact = "org.apache.hadoop:hadoop-yarn-common:2.6.0",
    sha1 = "9dd33fb5183f8faac731868eff69ac2b7678b75b",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
# com.google.guava:guava:jar:11.0.2
maven_jar(
    name = "com_google_code_findbugs_jsr305",
    artifact = "com.google.code.findbugs:jsr305:1.3.9",
    sha1 = "40719ea6961c0cb6afaeb6a921eaa1f6afd4cfdf",
)

# org.apache.zookeeper:zookeeper:pom:3.4.6
# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0 wanted version 3.6.2.Final
maven_jar(
    name = "io_netty_netty",
    artifact = "io.netty:netty:3.7.0.Final",
    sha1 = "07a8c35599c68c0bf383df74469aa3e03d9aca87",
)

# org.apache.jena:jena-arq:jar:3.1.0
maven_jar(
    name = "org_apache_jena_jena_core",
    artifact = "org.apache.jena:jena-core:3.1.0",
    sha1 = "9762d7180fc8bb6bf8a15b86bc41bd49f4147136",
)

# org.apache.hbase:hbase-protocol:jar:1.2.2
# org.apache.hbase:hbase-annotations:jar:1.2.2
# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "com_github_stephenc_findbugs_findbugs_annotations",
    artifact = "com.github.stephenc.findbugs:findbugs-annotations:1.3.9-1",
    sha1 = "a6b11447635d80757d64b355bed3c00786d86801",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "commons_configuration_commons_configuration",
    artifact = "commons-configuration:commons-configuration:1.6",
    sha1 = "32cadde23955d7681b0d94a2715846d20b425235",
)

maven_jar(
    name = "javax_xml_parsers_jaxp_api",
    artifact = "javax.xml.parsers:jaxp-api:1.4",
)

# org.apache.avro:avro:jar:1.7.4
maven_jar(
    name = "com_thoughtworks_paranamer_paranamer",
    artifact = "com.thoughtworks.paranamer:paranamer:2.3",
    sha1 = "4a85963a752c0a2f715c3924bfc686865e7e1bc6",
)

# com.sun.jersey:jersey-json:bundle:1.9
maven_jar(
    name = "org_codehaus_jettison_jettison",
    artifact = "org.codehaus.jettison:jettison:1.1",
    sha1 = "1a01a2a1218fcf9faa2cc2a6ced025bdea687262",
)

# org.apache.avro:avro:jar:1.7.4
maven_jar(
    name = "org_xerial_snappy_snappy_java",
    artifact = "org.xerial.snappy:snappy-java:1.0.4.1",
    sha1 = "f88b89a5a21a466aeb0ecf0c063605bd584b4947",
)

maven_jar(
    name = "edu_stanford_nlp_stanford_corenlp",
    artifact = "edu.stanford.nlp:stanford-corenlp:3.6.0",
)

# org.apache.jena:jena-arq:jar:3.1.0
# org.apache.jena:jena-base:jar:3.1.0
maven_jar(
    name = "org_apache_commons_commons_csv",
    artifact = "org.apache.commons:commons-csv:1.0",
    sha1 = "8a0796ad6541a144eb1c00b93e06fbac03a9f313",
)

# org.apache.hbase:hbase-protocol:jar:1.2.2
# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "org_apache_hbase_hbase_annotations",
    artifact = "org.apache.hbase:hbase-annotations:1.2.2",
    sha1 = "38e8bca77581113c02a4e8d3492b10f698b4e072",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "org_apache_commons_commons_math3",
    artifact = "org.apache.commons:commons-math3:3.1.1",
    sha1 = "6719d757a98ff24a83d9d727bef9cec83f59b6e1",
)

# junit:junit:jar:4.12
maven_jar(
    name = "org_hamcrest_hamcrest_core",
    artifact = "org.hamcrest:hamcrest-core:1.3",
    sha1 = "42a25dc3219429f0e5d060061f71acb49bf010a0",
)

# edu.stanford.nlp:stanford-corenlp:jar:3.6.0
maven_jar(
    name = "com_googlecode_efficient_java_matrix_library_ejml",
    artifact = "com.googlecode.efficient-java-matrix-library:ejml:0.23",
    sha1 = "fb9a880674f0d241d727ee2bc5e6a839d3007fe8",
)

# org.apache.directory.server:apacheds-kerberos-codec:bundle:2.0.0-M15
maven_jar(
    name = "org_apache_directory_server_apacheds_i18n",
    artifact = "org.apache.directory.server:apacheds-i18n:2.0.0-M15",
    sha1 = "71c61c84683152ec2a6a65f3f96fe534e304fa22",
)

# com.google.inject:guice:jar:3.0
# com.sun.jersey.contribs:jersey-guice:jar:1.9
maven_jar(
    name = "javax_inject_javax_inject",
    artifact = "javax.inject:javax.inject:1",
    sha1 = "6975da39a7040257bd51d21a231b76c915872d38",
)

# org.apache.jena:jena-base:jar:3.1.0
maven_jar(
    name = "com_github_andrewoma_dexx_collection",
    artifact = "com.github.andrewoma.dexx:collection:0.6",
    sha1 = "9364d0beacd4dbb3168a274b1dc4fef1a4023616",
)

# de.jollyday:jollyday:jar:0.4.7 wanted version 2.2.7
# com.sun.xml.bind:jaxb-impl:jar:2.2.3-1
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "javax_xml_bind_jaxb_api",
    artifact = "javax.xml.bind:jaxb-api:2.2.2",
    sha1 = "aeb3021ca93dde265796d82015beecdcff95bf09",
)

# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0 wanted version 1.9.13
# com.sun.jersey:jersey-json:bundle:1.9
maven_jar(
    name = "org_codehaus_jackson_jackson_xc",
    artifact = "org.codehaus.jackson:jackson-xc:1.8.3",
    sha1 = "1226667dcdb7c259b3ee07e112ed83446554516e",
)

maven_jar(
    name = "org_apache_hbase_hbase_server",
    artifact = "org.apache.hbase:hbase-server:1.2.2",
)

# edu.stanford.nlp:stanford-corenlp:jar:3.6.0
# de.jollyday:jollyday:jar:0.4.7 wanted version 2.1
maven_jar(
    name = "joda_time_joda_time",
    artifact = "joda-time:joda-time:2.9",
    sha1 = "e8a58b7f5853b693b8c4795a714fe77c266c3acc",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "javax_servlet_servlet_api",
    artifact = "javax.servlet:servlet-api:2.5",
    sha1 = "5959582d97d8b61f4d154ca9e495aafd16726e34",
)

# edu.stanford.nlp:stanford-corenlp:jar:3.6.0
maven_jar(
    name = "de_jollyday_jollyday",
    artifact = "de.jollyday:jollyday:0.4.7",
    sha1 = "aa1c57aa11494985854b8ec8d39574754db67f22",
)

# org.apache.zookeeper:zookeeper:pom:3.4.6
# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0 wanted version 1.7.5
maven_jar(
    name = "org_slf4j_slf4j_log4j12",
    artifact = "org.slf4j:slf4j-log4j12:1.6.1",
    sha1 = "bd245d6746cdd4e6203e976e21d597a46f115802",
)

# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "com_sun_jersey_jersey_client",
    artifact = "com.sun.jersey:jersey-client:1.9",
    sha1 = "d3c4b2b5f89db32c96ceddcb863684821910a7bb",
)

# org.apache.jena:jena-core:jar:3.1.0 wanted version 1.3
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "commons_cli_commons_cli",
    artifact = "commons-cli:commons-cli:1.2",
    sha1 = "2bf96b7aa8b611c177d329452af1dc933e14501c",
)

# org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# com.sun.jersey.contribs:jersey-guice:jar:1.9
maven_jar(
    name = "com_google_inject_extensions_guice_servlet",
    artifact = "com.google.inject.extensions:guice-servlet:3.0",
    sha1 = "610cde0e8da5a8b7d8efb8f0b8987466ffebaaf9",
)

# org.apache.jena:jena-core:jar:3.1.0 wanted version 2.11.0
# com.io7m.xom:xom:jar:1.2.10
maven_jar(
    name = "xerces_xercesImpl",
    artifact = "xerces:xercesImpl:2.8.0",
    sha1 = "cfd3ebe2f8034e660344f9108c3e2daf78c29cc3",
)

# org.apache.jena:jena-arq:jar:3.1.0
maven_jar(
    name = "org_apache_thrift_libthrift",
    artifact = "org.apache.thrift:libthrift:0.9.2",
    sha1 = "9b067e2e2c5291e9f0d8b3561b1654286e6d81ee",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "xmlenc_xmlenc",
    artifact = "xmlenc:xmlenc:0.52",
    sha1 = "d82554efbe65906d83b3d97bd7509289e9db561a",
)

# org.apache.jena:jena-core:jar:3.1.0
maven_jar(
    name = "org_apache_jena_jena_base",
    artifact = "org.apache.jena:jena-base:3.1.0",
    sha1 = "b8eb06db8462d570c8d7896aaf29b3b76e1dafa2",
)

maven_jar(
    name = "org_apache_hadoop_hadoop_common",
    artifact = "org.apache.hadoop:hadoop-common:2.6.0",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hbase:hbase-common:jar:1.2.2 wanted version 3.2.2
maven_jar(
    name = "commons_collections_commons_collections",
    artifact = "commons-collections:commons-collections:3.2.1",
    sha1 = "761ea405b9b37ced573d2df0d1e3a4e0f9edc668",
)

# org.apache.hbase:hbase-protocol:jar:1.2.2
# org.apache.hbase:hbase-annotations:jar:1.2.2
# org.apache.hbase:hbase-common:jar:1.2.2
# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "junit_junit",
    artifact = "junit:junit:4.12",
    sha1 = "2973d150c0dc1fefe998f834810d68f278ea58ec",
)

# org.apache.hadoop:hadoop-common:jar:2.6.0
maven_jar(
    name = "com_jcraft_jsch",
    artifact = "com.jcraft:jsch:0.1.42",
    sha1 = "a86104b0f2e0c0bab5b0df836065823a99b5e334",
)

# net.java.dev.jets3t:jets3t:jar:0.9.0 wanted version 1.1.1
# org.apache.httpcomponents:httpclient:jar:4.1.2 wanted version 1.1.1
# org.htrace:htrace-core:jar:3.0.4 wanted version 1.1.1
# org.apache.hbase:hbase-protocol:jar:1.2.2 wanted version 1.2
# org.apache.hbase:hbase-client:jar:1.2.2 wanted version 1.2
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-api:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# org.apache.hbase:hbase-common:jar:1.2.2 wanted version 1.2
maven_jar(
    name = "commons_logging_commons_logging",
    artifact = "commons-logging:commons-logging:1.1.3",
    sha1 = "f6f66e966c70a83ffbdb6f17a0919eaf7c8aca7f",
)

# org.apache.hbase:hbase-client:jar:1.2.2
maven_jar(
    name = "org_jruby_joni_joni",
    artifact = "org.jruby.joni:joni:2.1.2",
    sha1 = "1f08024ec70e86a716188b7d069b0c2d2f183e14",
)

# org.apache.avro:avro:jar:1.7.4
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
maven_jar(
    name = "org_apache_commons_commons_compress",
    artifact = "org.apache.commons:commons-compress:1.4.1",
    sha1 = "b02e84a993d88568417536240e970c4b809126fd",
)

maven_jar(
    name = "org_json_json",
    artifact = "org.json:json:20160810",
)

maven_jar(
    name = "org_apache_hadoop_hadoop_mapreduce_client_core",
    artifact = "org.apache.hadoop:hadoop-mapreduce-client-core:2.6.0",
)

# org.apache.jena:jena-arq:jar:3.1.0
# org.apache.jena:jena-base:jar:3.1.0
maven_jar(
    name = "org_apache_commons_commons_lang3",
    artifact = "org.apache.commons:commons-lang3:3.3.2",
    sha1 = "90a3822c38ec8c996e84c16a3477ef632cbc87a3",
)

# org.apache.directory.server:apacheds-kerberos-codec:bundle:2.0.0-M15
maven_jar(
    name = "org_apache_directory_api_api_asn1_api",
    artifact = "org.apache.directory.api:api-asn1-api:1.0.0-M20",
    sha1 = "5e6486ffa3125ba44dc410ead166e1d6ba8ac76d",
)

# edu.stanford.nlp:stanford-corenlp:jar:3.6.0
maven_jar(
    name = "com_io7m_xom_xom",
    artifact = "com.io7m.xom:xom:1.2.10",
    sha1 = "4165e25bef19aad134f6498cc277110b9bc5e52b",
)

# org.apache.jena:apache-jena-libs:pom:3.1.0
maven_jar(
    name = "org_apache_jena_jena_tdb",
    artifact = "org.apache.jena:jena-tdb:3.1.0",
    sha1 = "ee0d6be78e09cf04e757542eb32d37f3b30715b3",
)

# org.apache.curator:curator-client:bundle:2.6.0 wanted version 16.0.1
# org.apache.curator:curator-framework:bundle:2.6.0 wanted version 16.0.1
# org.apache.hbase:hbase-client:jar:1.2.2 wanted version 12.0.1
# org.apache.hadoop:hadoop-common:jar:2.6.0
# org.apache.curator:curator-recipes:bundle:2.6.0 wanted version 16.0.1
# org.apache.hadoop:hadoop-yarn-api:jar:2.6.0
# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0
# org.apache.hbase:hbase-common:jar:1.2.2 wanted version 12.0.1
# org.htrace:htrace-core:jar:3.0.4 wanted version 12.0.1
maven_jar(
    name = "com_google_guava_guava",
    artifact = "com.google.guava:guava:11.0.2",
    sha1 = "35a3c69e19d72743cac83778aecbee68680f63eb",
)

# org.apache.hadoop:hadoop-yarn-common:jar:2.6.0 wanted version 1.9.13
# org.apache.hadoop:hadoop-common:jar:2.6.0 wanted version 1.9.13
# org.codehaus.jackson:jackson-xc:jar:1.8.3
# org.codehaus.jackson:jackson-jaxrs:jar:1.8.3
# org.apache.avro:avro:jar:1.7.4 wanted version 1.8.8
# com.sun.jersey:jersey-json:bundle:1.9
# org.apache.hbase:hbase-client:jar:1.2.2 wanted version 1.9.13
maven_jar(
    name = "org_codehaus_jackson_jackson_mapper_asl",
    artifact = "org.codehaus.jackson:jackson-mapper-asl:1.8.3",
    sha1 = "e684dfaa93b95a507779099cf100804dd1b0378c",
)

# org.apache.curator:curator-recipes:bundle:2.6.0
# org.apache.hadoop:hadoop-auth:jar:2.6.0
maven_jar(
    name = "org_apache_curator_curator_framework",
    artifact = "org.apache.curator:curator-framework:2.6.0",
    sha1 = "81a699c39d127b5b4ff97cc77da7650b53e5b5ed",
)

# org.apache.jena:jena-arq:jar:3.1.0
# org.apache.jena:jena-base:jar:3.1.0
maven_jar(
    name = "org_apache_jena_jena_shaded_guava",
    artifact = "org.apache.jena:jena-shaded-guava:3.1.0",
    sha1 = "6e2400a81e3d6d50a894daa07db0501fc900c659",
)
