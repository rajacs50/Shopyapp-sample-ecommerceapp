def delay(client):
    client.client.get("/api/delay")


def db_slow(client):
    client.client.get("/api/simulate-db-slow")