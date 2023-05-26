tokenTime =
timeBuff = str(tokenTime)                                # The time on server when token validity start
timeBuff = timeBuff +  FIELD_SEPARATOR

timeBuff = timeBuff +  str(ACCESS_TOKEN_LIVE_TIME)                          # The length of time the token is valid.
timeBuff = timeBuff +  FIELD_SEPARATOR

timeBuff = timeBuff +  SERVER_KEY                          # The length of time the token is valid.
timeBuff = timeBuff +  FIELD_SEPARATOR

serverTimeSha = getHash(timeBuff)

print(serverTimeSha)