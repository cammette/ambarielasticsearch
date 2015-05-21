from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()
tmp_dir = Script.get_tmp_dir()


conf_dir = "/etc/elasticsearch"

es_user = "elasticsearch"
user_group = "elasticsearch"


logging_yaml = config['configurations']['logging']['content']
elasticsearch_yaml = config['configurations']['elasticsearch']['content']
