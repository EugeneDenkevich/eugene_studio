![workflow](https://github.com/EugeneDenkevich/eugene_studio/actions/workflows/push_master.yaml/badge.svg)
# Eugene Studio
## Done:
- registration
- logging in
- logging out
- CI/CD

To run:
```bash
cp app/.env-example app/.env
```
```bash
docker compose up --build -d
```

To check the logining, set up the environment:
windows:
```bash
python -m venv .venv
```
```bash
.venv/Scripts/activate
```
```bash
pip install -r app/requirements.txt
```
linux:
```bash
python -m venv .venv
```
```bash
source .venv/bin/activate
```
```bash
pip install -r app/requirements.txt
```

And:
- Use the route http://127.0.0.1:8000/swagger to view and use swagger.

- Use /auth/bearer/register endpoint to register your new user. Use 1 or 2 in the role field.

- Use /auth/bearer/login: put your email in the username field. You will get the authorization token which need to get the information by protected route above.

- Use httpie (included in requirements.txt) by this command:
```bash
http GET 127.0.0.1:8000/protected-route Authorization:'Bearer <token>'
```
Paste your authorization token instead of `<token>`.
