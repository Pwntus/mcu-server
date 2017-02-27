# mcu-server

## Install local cloud-connect npm module

```bash
$ cd cloud-connect
/cloud-connect$ sudo npm link && cd ..
$ npm link cloud-connect
$ npm install
```

### Run cloud-connect subscribe

Configure Cloud Connect credentials and pub/sub path in `package.json`.

```bash
$ npm run sub
```

### Subscribe path

> Replace dash `-` with whitespace.

```
pub/<root domain>/<sub domain>/<thing name>
sub/<root domain>/<sub domain>/<thing name>

E.g.
sub/UIT IFI course/pau001/00000273
```
