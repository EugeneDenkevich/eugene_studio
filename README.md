# eugene_studio

To run:
```bash
cp app/.env-example app/.env
```
```bash
docker-compose up --build -d
```

- Use the route http://127.0.0.1:8000/swagger to view and use swagger.

- Use /auth/bearer/register endpoint to register your new user. Use 1 or 2 in the role field.

- After successful registration use /auth/bearer/login. Use your email in the username field. You will get the authorization token which need to get the information by protected route.

- Use POSTman or httpie which included in requirements.txt to do a GET request on 127.0.0.1:8000/protected-route. If you use POSTman, add 'Authorization: Baerer <token>' in headers. If you use httpie, use this:
```bash
http GET 127.0.0.1:8000/protected-route Authorization:'Bearer <token>'
```
Don't forget to paste your authorization token instead of <token>.
