from typing import Dict, NamedTuple, Optional, TypedDict

import validators

from ..errors import CliError
from .config import Config


class Profile(NamedTuple):
    display_name: str
    region: str
    arn: str
    aws_saml_url: Optional[str] = None
    ansible_bucket: Optional[str] = None


class OrgParams(TypedDict, total=False):
    resource_env_var: Optional[str]
    users: Dict[str, str]
    domain: str
    aws_saml_url: str
    aws_okta_params: Dict[str, str]
    saml2aws_params: Dict[str, str]
    profiles: Dict[str, Profile]


# For legacy reasons, we need to maintain multiple org slugs for LD.
# This allows us to put the config in one place.
LaunchDarklyParams: OrgParams = {
    "resource_env_var": "ENVIRONMENT",
    "users": {"ssh": "ubuntu", "ansible": "ansible"},
    "domain": "launchdarkly.com",
    "aws_saml_url": (
        "https://launchdarkly.okta.com/home/amazon_aws/0oaj4aow7gPk26Fy6356/272"
    ),
    "aws_okta_params": {
        "mfa_provider": "OKTA",
        "mfa_factor_type": "push",
        "assume_role_ttl": "1h",
        "session_ttl": "30m",
    },
    "saml2aws_params": {"mfa": "PUSH", "aws_session_duration": "1800"},
    "profiles": {
        "production": Profile(
            display_name="Production",
            region="us-east-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-production",
            ansible_bucket="launchdarkly-sym-ansible-production",
        ),
        "staging": Profile(
            display_name="Staging",
            region="us-east-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-staging",
            ansible_bucket="launchdarkly-sym-ansible-staging",
        ),
        "catamorphic": Profile(
            display_name="Catamorphic",
            region="us-east-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-catamorphic",
            ansible_bucket="launchdarkly-sym-ansible-catamorphic",
        ),
        "prod-intuit": Profile(
            display_name="Prod: Intuit",
            region="us-west-2",
            arn="arn:aws:iam::527291094460:role/ops/SSHAdmin-production",
            ansible_bucket="launchdarkly-sym-ansible-prod-intuit",
        ),
        "staging-intuit": Profile(
            display_name="Staging: Intuit",
            region="us-west-2",
            arn="arn:aws:iam::527291094460:role/ops/SSHAdmin-staging",
            ansible_bucket="launchdarkly-sym-ansible-staging-intuit",
        ),
        "production_apac": Profile(
            display_name="Production: APAC",
            region="ap-southeast-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-production",
            ansible_bucket="launchdarkly-sym-ansible-production",
        ),
        "production_euw1": Profile(
            display_name="Production: EU West 1",
            region="eu-west-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-production",
            ansible_bucket="launchdarkly-sym-ansible-production",
        ),
        "staging_apac": Profile(
            display_name="Staging: APAC",
            region="ap-southeast-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-staging",
            ansible_bucket="launchdarkly-sym-ansible-staging",
        ),
        "staging_euw1": Profile(
            display_name="Staging: EU West 1",
            region="eu-west-1",
            arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-staging",
            ansible_bucket="launchdarkly-sym-ansible-staging",
        ),
    },
}

PARAMS: Dict[str, OrgParams] = {
    "launch-darkly": LaunchDarklyParams,
    "launchdarkly": LaunchDarklyParams,
    "sym": {
        "resource_env_var": "ENVIRONMENT",
        "users": {"ssh": "ubuntu", "ansible": "ubuntu"},
        "domain": "symops.io",
        "aws_saml_url": (
            "https://dev-291131.okta.com/home/amazon_aws/0oaqlmsn7GMVgAyBK4x6/272"
        ),
        "aws_okta_params": {
            "mfa_provider": "OKTA",
            "mfa_factor_type": "push",
            "assume_role_ttl": "1h",
            "session_ttl": "30m",
        },
        "saml2aws_params": {"mfa": "PUSH", "aws_session_duration": "1800"},
        "profiles": {
            "test": Profile(
                display_name="Test",
                region="us-east-1",
                arn="arn:aws:iam::838419636750:role/SSMTestRole",
            ),
            "test_euw1": Profile(
                display_name="Test: EU West 1",
                region="eu-west-1",
                arn="arn:aws:iam::838419636750:role/SSMTestRole",
            ),
            "test-custom": Profile(
                display_name="TestCustom",
                region="us-east-1",
                arn="arn:aws:iam::838419636750:role/SSMTestRoleCustomBucket",
                ansible_bucket="sym-ansible-dev",
            ),
        },
    },
    "healthy-health": {
        "resource_env_var": "ENVIRONMENT",
        "users": {"ssh": "ubuntu"},
        "domain": "healthy-health.co",
        "aws_saml_url": (
            "https://healthy-health.okta.com/home/amazon_aws/0oagrj7yFaVtJoI2N5d5/272"
        ),
        "aws_okta_params": {
            "mfa_provider": "OKTA",
            "mfa_factor_type": "push",
            "assume_role_ttl": "1h",
            "session_ttl": "30m",
        },
        "saml2aws_params": {"mfa": "PUSH", "aws_session_duration": "1800"},
        "profiles": {
            "prod": Profile(
                display_name="Prod",
                region="us-east-1",
                arn="arn:aws:iam::223440862848:role/ssm-healthy-health-user-prod",
            ),
        },
    },
}


def get_org_params() -> OrgParams:
    return PARAMS[Config.get_org()]


def get_aws_saml_url(resource: str) -> str:
    org_params = get_org_params()
    profile = org_params["profiles"][resource]
    return profile.aws_saml_url or org_params["aws_saml_url"]


def get_aws_okta_params() -> Dict[str, str]:
    return get_org_params()["aws_okta_params"]


def get_saml2aws_params() -> Dict[str, str]:
    return get_org_params()["saml2aws_params"]


def get_profiles() -> Dict[str, Profile]:
    return get_org_params()["profiles"]


def get_domain() -> str:
    return get_org_params()["domain"]


def get_ssh_user() -> str:
    return get_org_params()["users"]["ssh"]


def get_ansible_user() -> str:
    return get_org_params()["users"]["ansible"]


def get_resource_env_vars() -> Optional[str]:
    try:
        return ("SYM_RESOURCE", get_org_params()["resource_env_var"])
    except KeyError:
        return "SYM_RESOURCE"


def get_profile(resource: str) -> Profile:
    return get_profiles()[resource]


def set_login_fields(org: str, email: str):
    if org not in PARAMS:
        raise CliError(f"Invalid org: {org}")

    config = Config.instance()
    config["org"] = org

    if not validators.email(email):
        raise CliError(f"Invalid email: {email}")

    if (domain := email.split("@")[-1]) != get_domain():
        raise CliError(f"Invalid domain: {domain}")

    config["email"] = email
