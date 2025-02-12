def error500(client):
    client.client.get("/api/error500")
