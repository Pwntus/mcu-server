# MQTT client with Cloud Connect cognito authentication

## Install local cloud-connect npm module

```bash
$ cd cloud-connect
/cloud-connect$ sudo npm link && cd ..
$ npm link cloud-connect
$ npm install
```

### Run cloud-connect subscribe

```bash
$ npm run sub
```

Configure Cloud Connect credentials and pub/sub path in `package.json`.

#### Subscribe path

> Replace dash `-` with whitespace.

```
pub/<root domain>/<sub domain>/<thing name>
sub/<root domain>/<sub domain>/<thing name>

E.g.
sub/UIT IFI course/pau001/00000273
```
