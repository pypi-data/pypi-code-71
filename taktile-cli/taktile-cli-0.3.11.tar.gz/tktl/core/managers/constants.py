TEMPLATE_PROJECT_DIRS = [
    "src/",
    "assets/",
    "tests/",
]

TEMPLATE_PROJECT_FILES = [
    "template/src/endpoints.py",
    "template/assets/model.joblib",
    "template/assets/loans_test.pqt",
    "template/tests/test_accuracy.py",
    "template/tests/test_plausibility.py",
    "template/tests/test_schema.py",
    "template/.gitignore",
    "template/.gitattributes",
    "template/.buildfile",
    "template/.dockerignore",
    "template/README.md",
    "template/requirements.txt",
]


CONFIG_FILE_TEMPLATE = """

# The default branch from which models will vbe deployed
default_branch_name: master

service:

  # The number of replicas of your service
  # Replicas are exact copies of your service, each request will be randomly directed to each of them
  replicas: 1

  # Format: <instance_kind>.<instance_size>
  # Only 'gp' (general purpose) instance_kind is supported for now
  # instance_size can be: small, medium, large
  instance_type: gp.small

  # Can be rest or grpc
  service_type: rest

# Assets: model and data
# Assets are the artifacts that comprise model and data.  These will be loaded inside the container
# when it gets built. Tktl will automatically package them for you, so all you need to do
# is define how they are loaded in the `src/endpoints.py file`


# Supported paths:
#  - A local path (default) which will use git-lfs to store it GitHub's server
#  - An s3 path. If this is picked and the bucket is private, the correct AWS keys should
#    be provided

# Versioning
# Every time someone pushes code to your repository, a deployment may be created. The deployment will
# only happen however if a new version of the model is found. That happens in three cases:

# 1. A different version is specified in this file
# 2. The md5 of the model or data has changed. This is detected automatically by taktile
# 3. The source code inside `src` has changed

# With events 2 and 3, a new version of the model will be published, and the tktl.yaml file will be
# automatically updated by the Taktile GitHub App

model:
  path: assets/model.pkl
  version: 1

data:
  path: assets/data.pkl
  version: 1

version: {version}
"""
