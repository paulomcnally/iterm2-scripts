# coding: utf-8
import random
import iterm2
import subprocess

bashCommand = 'PATH="$HOME/.rbenv/bin:$PATH" && PATH="$HOME/.rbenv/shims:$PATH" && rbenv global'

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Ruby Version',
        detailed_description='show Ruby version',
        exemplar='Ruby Version',
        update_cadence=5,
        identifier='engineering.paulomcnally.iterm-components.ruby',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def ruby_coroutine(knobs):
        output = subprocess.check_output(['bash','-c', bashCommand]).strip()
        return 'Ruby: %s' % output

    await component.async_register(connection, ruby_coroutine)

iterm2.run_forever(main)
