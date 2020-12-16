""" Node Manager Command Line Interface

    The node manager is responsible for:
    1) Creating, updating and deleting configurations (=nodes).
    2) Starting, Stopping nodes

    Configuration Commands
    * node new
    * node list
    * node files
    * node start
    * node stop
    * node attach
"""
import click
import sys
import questionary as q
import docker
import time
import os.path

from pathlib import Path
from threading import Thread
from colorama import Fore, Style

from vantage6.common import (
    warning, error, info, debug,
    bytes_to_base64s, check_config_write_permissions
)
from vantage6.common.globals import (STRING_ENCODING, APPNAME)
from vantage6.common.docker_addons import pull_if_newer
from vantage6.client import Client
from vantage6.client.encryption import RSACryptor


from vantage6.cli.context import NodeContext
from vantage6.cli.globals import (
    DEFAULT_NODE_ENVIRONMENT as N_ENV,
    DEFAULT_NODE_SYSTEM_FOLDERS as N_FOL
)
from vantage6.cli.configuration_wizard import (
    configuration_wizard,
    select_configuration_questionaire
)


@click.group(name="node")
def cli_node():
    """Subcommand `vnode`."""
    pass

#
#   list
#
@cli_node.command(name="list")
def cli_node_list():
    """Lists all nodes in the default configuration directory."""

    client = docker.from_env()
    check_if_docker_deamon_is_running(client)

    running_nodes = client.containers.list(
        filters={"label": f"{APPNAME}-type=node"})

    running_node_names = []
    for node in running_nodes:
        running_node_names.append(node.name)

    header = \
        "\nName"+(21*" ") + \
        "Environments"+(20*" ") + \
        "Status"+(10*" ") + \
        "System/User"

    click.echo(header)
    click.echo("-"*len(header))

    running = Fore.GREEN + "Online" + Style.RESET_ALL
    stopped = Fore.RED + "Offline" + Style.RESET_ALL

    # system folders
    configs, f1 = NodeContext.available_configurations(
        system_folders=True)
    for config in configs:
        status = running if f"{APPNAME}-{config.name}-system" in \
            running_node_names else stopped
        click.echo(
            f"{config.name:25}"
            f"{str(config.available_environments):32}"
            f"{status:25} System "
        )

    # user folders
    configs, f2 = NodeContext.available_configurations(
        system_folders=False)
    for config in configs:
        status = running if f"{APPNAME}-{config.name}-user" in \
            running_node_names else stopped
        click.echo(
            f"{config.name:25}"
            f"{str(config.available_environments):32}"
            f"{status:25} User   "
        )

    click.echo("-"*85)
    if len(f1)+len(f2):
        warning(
             f"{Fore.RED}Failed imports: {len(f1)+len(f2)}{Style.RESET_ALL}")

#
#   new
#
@cli_node.command(name="new")
@click.option("-n", "--name", default=None)
@click.option('-e', '--environment', default="",
              help='configuration environment to use')
@click.option('--system', 'system_folders', flag_value=True)
@click.option('--user', 'system_folders', flag_value=False, default=N_FOL)
def cli_node_new_configuration(name, environment, system_folders):
    """Create a new configation file.

    Checks if the configuration already exists. If this is not the case
    a questionaire is invoked to create a new configuration file.
    """
    # select configuration name if none supplied
    if not name:
        name = q.text("Please enter a configuration-name:").ask()

    # remove spaces, from name
    name_new = name.replace(" ", "-")
    if name != name_new:
        info(f"Replaced spaces from configuration name: {name_new}")
        name = name_new

    if not environment:
        environment = q.select(
            "Please select the environment you want to configure:",
            ["application", "prod", "acc", "test", "dev"]
        ).ask()

    # check that this config does not exist
    if NodeContext.config_exists(name, environment, system_folders):
        error(
            f"Configuration {name} and environment"
            f"{environment} already exists!"
        )
        exit(1)

    # Check that we can write in this folder
    if not check_config_write_permissions(system_folders):
        error("Your user does not have write access to all folders. Exiting")
        exit(1)

    # create config in ctx location
    flag = "--system" if system_folders else ""
    cfg_file = configuration_wizard("node", name, environment, system_folders)
    info(f"New configuration created: {Fore.GREEN}{cfg_file}{Style.RESET_ALL}")
    info(f"You can start the node by running "
         f"{Fore.GREEN}vnode start {flag}{Style.RESET_ALL}")

#
#   files
#
@cli_node.command(name="files")
@click.option("-n", "--name", default=None, help="configuration name")
@click.option('-e', '--environment', default=N_ENV,
              help='configuration environment to use')
@click.option('--system', 'system_folders', flag_value=True)
@click.option('--user', 'system_folders', flag_value=False, default=N_FOL)
def cli_node_files(name, environment, system_folders):
    """ Prints location important files.

        If the specified configuration cannot be found, it exits. Otherwise
        it returns the absolute path to the output.
    """
    # select configuration name if none supplied
    name, environment = (name, environment) if name else \
        select_configuration_questionaire("node", system_folders)

    # raise error if config could not be found
    if not NodeContext.config_exists(name, environment, system_folders):
        error(
            f"The configuration {Fore.RED}{name}{Style.RESET_ALL} with "
            f"environment {Fore.RED}{environment}{Style.RESET_ALL} could "
            f"not be found."
        )
        exit(1)

    # create node context
    ctx = NodeContext(name, environment=environment,
                      system_folders=system_folders)

    # return path of the configuration
    info(f"Configuration file = {ctx.config_file}")
    info(f"Log file           = {ctx.log_file}")
    info(f"data folders       = {ctx.data_dir}")
    info(f"Database labels and files")

    for label, path in ctx.databases.items():
        info(f" - {label:15} = {path}")


#
#   start
#
help_ = {
    'config': 'absolute path to configuration-file; overrides NAME',
    'environment': 'configuration environment to use',
}
@cli_node.command(name='start')
@click.option("-n", "--name", default=None, help="configuration name")
@click.option("-c", "--config", default=None, help=help_['config'])
@click.option('-e', '--environment', default=N_ENV, help=help_['environment'])
@click.option('--system', 'system_folders', flag_value=True)
@click.option('--user', 'system_folders', flag_value=False, default=N_FOL)
@click.option('-i', '--image', default=None, help="Node Docker image to use")
@click.option('--keep/--auto-remove', default=False,
              help="Keep image after finishing")
@click.option('--mount-src', default='',
              help="mount vantage6-master package source")
def cli_node_start(name, config, environment, system_folders, image, keep,
                   mount_src):
    """Start the node instance.

        If no name or config is specified the default.yaml configuation is
        used. In case the configuration file not excists, a questionaire is
        invoked to create one. Note that in this case it is not possible to
        specify specific environments for the configuration (e.g. test,
        prod, acc).
    """
    info("Starting node...")
    info("Finding Docker deamon")
    docker_client = docker.from_env()
    check_if_docker_deamon_is_running(docker_client)

    NodeContext.LOGGING_ENABLED = False
    if config:
        name = Path(config).stem
        ctx = NodeContext(name, environment, system_folders, config)

    else:
        # in case no name is supplied, ask the user to select one
        if not name:
            name, environment = select_configuration_questionaire(
                "node", system_folders)

        # check that config exists, if not a questionaire will be invoked
        if not NodeContext.config_exists(name, environment, system_folders):
            question = f"Configuration '{name}' using environment"
            question += f" '{environment}' does not exist.\n  Do you want to"
            question += f" create this config now?"

            if q.confirm(question).ask():
                configuration_wizard("node", name, environment, system_folders)

            else:
                error("Config file couldn't be loaded")
                sys.exit(0)


        ctx = NodeContext(name, environment, system_folders)

    # check that this node is not already running
    running_nodes = docker_client.containers.list(
        filters={"label": f"{APPNAME}-type=node"}
    )

    suffix = "system" if system_folders else "user"
    for node in running_nodes:
        if node.name == f"{APPNAME}-{name}-{suffix}":
            error(f"Node {Fore.RED}{name}{Style.RESET_ALL} is already running")
            exit(1)

    # make sure the (host)-task and -log dir exists
    info("Checking that data and log dirs exist")
    ctx.data_dir.mkdir(parents=True, exist_ok=True)
    ctx.log_dir.mkdir(parents=True, exist_ok=True)

    if image is None:
        image = ctx.config.get(
            "image",
            "harbor.vantage6.ai/infrastructure/node:latest"
        )

    info(f"Pulling latest node image '{image}'")
    try:
        # docker_client.images.pull(image)
        pull_if_newer(image)

    except Exception:
        warning(' ... alas, no dice!')
    else:
        info(" ... success!")

    info("Creating Docker data volume")
    data_volume = docker_client.volumes.create(
        f"{ctx.docker_container_name}-vol")

    info("Creating file & folder mounts")
    # FIXME: should only mount /mnt/database.csv if it is a file!
    # FIXME: should obtain mount points from DockerNodeContext
    mounts = [
        # (target, source)
        ("/mnt/database.csv", str(ctx.databases["default"])),
        ("/mnt/log", str(ctx.log_dir)),
        ("/mnt/data", data_volume.name),
        ("/mnt/config", str(ctx.config_dir)),
        ("/var/run/docker.sock", "/var/run/docker.sock"),
    ]

    if mount_src:
        # If mount_src is a relative path, docker willl consider it a volume.
        mount_src = os.path.abspath(mount_src)
        mounts.append(('/vantage6', mount_src))

    # FIXME: Code duplication: Node.__init__() (vantage6/node/__init__.py)
    #   uses a lot of the same logic. Suggest moving this to
    #   ctx.get_private_key()
    filename = ctx.config.get("encryption", {}).get("private_key")

    # filename may be set to an empty string
    if not filename:
        filename = 'private_key.pem'

    # Location may be overridden by the environment
    filename = os.environ.get('PRIVATE_KEY', filename)

    # If ctx.get_data_file() receives an absolute path, it is returned as-is
    fullpath = Path(ctx.get_data_file(filename))

    if fullpath:
        if Path(fullpath).exists():
            mounts.append(("/mnt/private_key.pem", str(fullpath)))
        else:
            warning(f"private key file provided {fullpath}, "
                    "but does not exists")

    volumes = {}
    for mount in mounts:
        volumes[mount[1]] = {'bind': mount[0], 'mode': 'rw'}

    # Be careful not to use 'environment' as it would override the function
    # argument ;-).
    env = {
        "DATA_VOLUME_NAME": data_volume.name,
        "DATABASE_URI": "/mnt/database.csv",
        "PRIVATE_KEY": "/mnt/private_key.pem"
    }

    system_folders_option = "--system" if system_folders else "--user"
    cmd = f'vnode-local start -c /mnt/config/{name}.yaml -n {name} -e '\
          f'{environment} --dockerized {system_folders_option}'

    info(f"Runing Docker container")
    # debug(f"  with command: '{cmd}'")
    # debug(f"  with mounts: {volumes}")
    # debug(f"  with environment: {env}")

    container = docker_client.containers.run(
        image,
        command=cmd,
        volumes=volumes,
        detach=True,
        labels={
            f"{APPNAME}-type": "node",
            "system": str(system_folders),
            "name": ctx.config_file_name
        },
        environment=env,
        name=ctx.docker_container_name,
        auto_remove=not keep,
        tty=True
    )

    info(f"Success! container id = {container}")


#
#   stop
#
@cli_node.command(name='stop')
@click.option("-n", "--name", default=None, help="configuration name")
@click.option('--system', 'system_folders', flag_value=True)
@click.option('--user', 'system_folders', flag_value=False, default=N_FOL)
@click.option('--all', 'all_nodes', flag_value=True)
def cli_node_stop(name, system_folders, all_nodes):
    """Stop a running container. """

    client = docker.from_env()
    check_if_docker_deamon_is_running(client)

    running_nodes = client.containers.list(
        filters={"label": f"{APPNAME}-type=node"})

    if not running_nodes:
        warning("No nodes are currently running.")
        return

    running_node_names = [node.name for node in running_nodes]

    if all_nodes:
        for name in running_node_names:
            container = client.containers.get(name)
            container.kill()
            info(f"Stopped the {Fore.GREEN}{name}{Style.RESET_ALL} Node.")
    else:
        if not name:
            name = q.select("Select the node you wish to stop:",
                            choices=running_node_names).ask()
        else:

            post_fix = "system" if system_folders else "user"
            name = f"{APPNAME}-{name}-{post_fix}"

        if name in running_node_names:
            container = client.containers.get(name)
            container.kill()
            info(f"Stopped the {Fore.GREEN}{name}{Style.RESET_ALL} Node.")
        else:
            error(f"{Fore.RED}{name}{Style.RESET_ALL} is not running?")


#
#   attach
#
@cli_node.command(name='attach')
@click.option("-n", "--name", default=None, help="configuration name")
@click.option('--system', 'system_folders', flag_value=True)
@click.option('--user', 'system_folders', flag_value=False, default=N_FOL)
def cli_node_attach(name, system_folders):
    """Attach the logs from the docker container to the terminal."""

    client = docker.from_env()
    check_if_docker_deamon_is_running(client)

    running_nodes = client.containers.list(
        filters={"label": f"{APPNAME}-type=node"})
    running_node_names = [node.name for node in running_nodes]

    if not name:
        name = q.select("Select the node you wish to inspect:",
                        choices=running_node_names).ask()
    else:
        post_fix = "system" if system_folders else "user"
        name = f"{APPNAME}-{name}-{post_fix}"

    if name in running_node_names:
        container = client.containers.get(name)
        logs = container.attach(stream=True, logs=True)
        Thread(target=print_log_worker, args=(logs,), daemon=True).start()
        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                info("Closing log file. Keyboard Interrupt.")
                exit(0)
    else:
        error(f"{Fore.RED}{name}{Style.RESET_ALL} was not running!?")


#
#   create-private-key
#
@cli_node.command(name='create-private-key')
@click.option("-n", "--name", default=None, help="configuration name")
@click.option('-e', '--environment', default="",
              help='configuration environment to use')
@click.option('--system', 'system_folders', flag_value=True)
@click.option('--user', 'system_folders', flag_value=False, default=N_FOL)
@click.option('--no-upload', 'upload', flag_value=False, default=True)
@click.option("-o", "--organization-name", default=None,
              help="Organization name")
@click.option('--overwrite', 'overwrite', flag_value=True, default=False)
def cli_node_create_private_key(name, environment, system_folders, upload,
                                organization_name, overwrite):
    """Create and upload a new private key (use with caughtion)"""

    # retrieve context
    name, environment = (name, environment) if name else \
        select_configuration_questionaire("node", system_folders)

    # raise error if config could not be found
    NodeContext.LOGGING_ENABLED = False
    if not NodeContext.config_exists(name, environment, system_folders):
        error(
            f"The configuration {Fore.RED}{name}{Style.RESET_ALL} with "
            f"environment {Fore.RED}{environment}{Style.RESET_ALL} could "
            f"not be found."
        )
        exit(1)

    # Create node context
    ctx = NodeContext(name, environment, system_folders)

    # Authenticate with the server to obtain organization name if it wasn't
    # provided
    if organization_name is None:
        client = create_client_and_authenticate(ctx)
        organization_name = client.whoami.organization_name

    # generate new key, and save it
    filename = f"privkey_{organization_name}.pem"
    file_ = ctx.type_data_folder(system_folders) / filename

    if file_.exists():
        warning(f"File '{Fore.CYAN}{file_}{Style.RESET_ALL}' exists!")

        if overwrite:
            warning("'--override' specified, so it will be overwritten ...")

    if file_.exists() and not overwrite:
        error("Could not create private key!")
        warning(
            f"If you're **sure** you want to create a new key, "
            f"please run this command with the '--overwrite' flag"
        )
        warning("Continuing with existing key instead!")
        private_key = RSACryptor(file_).private_key

    else:
        try:
            info("Generating new private key")
            private_key = RSACryptor.create_new_rsa_key(file_)

        except Exception as e:
            error(f"Could not create new private key '{file_}'!?")
            debug(e)
            info("Bailing out ...")
            exit(1)

        warning(f"Private key written to '{file_}'")
        warning(
            "If you're running multiple nodes, be sure to copy the private "
            "key to the appropriate directories!"
        )

    # create public key
    info("Deriving public key")
    public_key = RSACryptor.create_public_key_bytes(private_key)

    # update config file
    info("Updating configuration")
    ctx.config["encryption"]["private_key"] = str(file_)
    ctx.config_manager.put(environment, ctx.config)
    ctx.config_manager.save(ctx.config_file)

    # upload key to the server
    if upload:
        info(
            "Uploading public key to the server. "
            "This will overwrite any previously existing key!"
        )

        if 'client' not in locals():
            client = create_client_and_authenticate(ctx)

        try:
            client.request(
                f"/organization/{client.whoami.organization_id}",
                method="patch",
                json={"public_key": bytes_to_base64s(public_key)}
            )

        except Exception as e:
            error("Could not upload the public key!")
            debug(e)
            exit(1)

    else:
        warning("Public key not uploaded!")

    info("[Done]")


#
#   clean
#
@cli_node.command(name='clean')
def cli_node_clean():
    """ This command erases docker volumes"""
    client = docker.from_env()
    check_if_docker_deamon_is_running(client)

    # retrieve all volumes
    volumes = client.volumes.list()
    canditates = []
    msg = "This would remove the following volumes: "
    for volume in volumes:
        if volume.name[-6:] == "tmpvol":
            canditates.append(volume)
            msg += volume.name + ","
    info(msg)

    confirm = q.confirm(f"Are you sure?")
    if confirm.ask():
        for volume in canditates:
            try:
                volume.remove()
                # info(volume.name)
            except docker.errors.APIError as e:
                error(f"Failed to remove volume {Fore.RED}'{volume.name}'"
                      f"{Style.RESET_ALL}. Is it still in use?")
                debug(e)
                exit(1)
    info("Done!")


def print_log_worker(logs_stream):
    for log in logs_stream:
        print(log.decode(STRING_ENCODING), end="")


def check_if_docker_deamon_is_running(docker_client):
    try:
        docker_client.ping()
    except Exception:
        error("Docker socket can not be found. Make sure Docker is running.")
        exit(1)


def create_client_and_authenticate(ctx):
    """Create a client and authenticate."""
    host = ctx.config['server_url']
    port = ctx.config['port']
    api_path = ctx.config['api_path']

    info(f"Connecting to server at '{host}:{port}{api_path}'")
    username = q.text("Username:").ask()
    password = q.password("Password:").ask()

    client = Client(host, port, api_path)

    try:
        client.authenticate(username, password)

    except Exception as e:
        error("Could not authenticate with server!")
        debug(e)
        exit(1)

    return client
