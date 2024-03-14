"""
Copyright (c) 2023 Wind River Systems, Inc.

SPDX-License-Identifier: Apache-2.0

"""
import click

from tiler.cmd.options import config_option
from tiler.cmd import pass_state_context


@click.command(
    help="Build Debian ISO using live-build.")
@pass_state_context
@config_option
def iso(state, config):
    raise Exception("Not Implemeneted")
