# mcu-server

## Install local cloud-connect npm module

```bash
~$ cd cloud-connect
~/cloud-connect$ sudo npm link && cd ..
~$ npm link cloud-connect
~$ npm install
```

### Run cloud-connect subscribe

```bash
~$ npm run sub
```

### Subscribe path

> Replace dash `-` with whitespace.

```
pub/<root domain>/<sub domain>/<thing name>
sub/<root domain>/<sub domain>/<thing name>
```
