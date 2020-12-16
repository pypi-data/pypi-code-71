"""

Copyright (C) 2016-2021 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from sregistry.logger import bot


def main(args, parser, extra):

    from sregistry.main import get_client

    image = args.image
    cli = get_client(image, quiet=args.quiet)
    cli.announce(args.command)

    # If the client doesn't have the command, exit
    if not hasattr(cli, "delete"):
        msg = "delete is not implemented for %s. Why don't you add it?"
        bot.exit(msg % cli.client_name)

    cli.delete(image=image, force=args.force)
