from urllib import parse


def geturl(settings: dict):

    if not settings["port"]:
        settings["port"] = "5432" # Postgres default

    host = settings["host"]
    port = settings["port"]
    user = settings["user"]
    database = settings["database"]
    passwd = parse.quote_plus(settings["pass"])

    uri = f"postgres://{user}:{passwd}@{host}:{port}/{database}"

    return uri
