httpie-oauth2
===============

OAuth2 plugins for [httpie](https://github.com/jkbr/httpie) 

```bash
$ pip install git+http://github.com/yoophi/httpie-oauth2.git?#egg=httpie_oauth2
```

Usage
-----

```bash
$ export API_KEY=foo
$ export API_SECRET=secret
$ export AUTHORIZATION_URL=http://api.hostname.com/auth/token
$ http --auth-type=oauth2DM --auth=client-key:client-secret GET https://api.hostname.com/me 
```

You can also use HTTPie sessions.

```bash
# Create session
$ http --session=dm --auth-type=oauth2 --auth=username:password GET https://api.hostname.com/me
    
# Re-use auth
$ http --session=dm GET https://api.hostname.com/me
```

TODO
----

httpie oauth plugins API does not permit yet to deal with token refresh

https 프로토콜을 사용중이 아닌 경우, 아래 환경변수를 세팅해서 사용가능.

```bash
$ export OAUTHLIB_INSECURE_TRANSPORT=1
```
