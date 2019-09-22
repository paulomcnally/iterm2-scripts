# coding: utf-8
import random
import iterm2
import subprocess

bashCommand = 'NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && nvm version'

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='NodeJS Version',
        detailed_description='show nodejs version',
        exemplar='NodeJS Version',
        update_cadence=5,
        identifier='engineering.paulomcnally.iterm-components.node',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def node_coroutine(knobs):
        output = subprocess.check_output(['bash','-c', bashCommand]).strip()
        return 'Node: %s' % output[1:]

    await component.async_register(connection, node_coroutine)

iterm2.run_forever(main)
