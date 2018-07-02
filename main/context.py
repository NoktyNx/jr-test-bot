from discord.ext import commands


class Context(commands.Context):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pool = self.bot.pool

    def __repr__(self):
        # we need this for our cache key strategy
        return '<Context>'

    @property
    def session(self):
        return self.bot.session
