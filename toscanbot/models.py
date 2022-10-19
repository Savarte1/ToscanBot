from tortoise.models import Model
from tortoise import fields


class GuildSettings(Model):
    id = fields.IntField(pk=True)
    guild_id = fields.BigIntField()
    admin = fields.BigIntField()
    moderator = fields.BigIntField()
    welcome = fields.BigIntField()
    departure = fields.BigIntField()
    admin_log = fields.BigIntField()
    mod_log = fields.BigIntField()


class GuildWelcome(Model):
    id = fields.IntField(pk=True)
    guild_id = fields.BigIntField(unique=True)
    welcome = fields.TextField()
    departure = fields.TextField()

class MemberSettings(Model):
    id = fields.IntField(pk=True)
    guild = fields.BigIntField()
    user = fields.BigIntField()
    nsvexempt = fields.BooleanField()


class NSVGuildSettings(Model):
    id = fields.IntField(pk=True)
    guild_id = fields.BigIntField()
    visitor = fields.BigIntField()
    verified = fields.BigIntField()
    wa_member = fields.BigIntField()
    lobby = fields.BigIntField()


class NSVRegionSettings(Model):
    id = fields.IntField(pk=True)
    guild_id = fields.ForeignKeyField("models.NSVGuildSettings")
    region = fields.CharField(50)
    role = fields.BigIntField()


class NSVNations(Model):
    id = fields.IntField(pk=True)
    dbid = fields.BigIntField()
    nation = fields.CharField(50)
    region = fields.CharField(50)
    exists = fields.BooleanField()
    lastver = fields.DatetimeField()


class NSVUsers(Model):
    id = fields.IntField(pk=True)
    user = fields.BigIntField()


class NSVGuildUsers(Model):
    id = fields.IntField(pk=True)
    guild = fields.BigIntField()
    user = fields.BigIntField()
    exempt = fields.BooleanField()


class PollPinPolls(Model):
    id = fields.IntField(pk=True)
    guild_id = fields.BigIntField()
    poll = fields.CharField(30)
    owner = fields.BigIntField()
    role = fields.BigIntField()

    class Meta:
        unique_together = (("guild_id", "poll"),)


class PollPinPins(Model):
    id = fields.IntField(pk=True)
    poll_id = fields.ForeignKeyField("models.PollPinPolls")
    user = fields.BigIntField()
    pin = fields.BigIntField()

    class Meta:
        unique_together = (("poll_id", "pin"), ("poll_id", "user"))
