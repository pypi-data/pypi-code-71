import os
#field which is used to store meta information about the file in ElasticSearch, e.g. path, extension, type
META_FIELD = "properties"
ES_URL = os.getenv("DOCPARSER_ES_URL", "http://elastic-dev.texta.ee:9200")
