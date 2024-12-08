# OneKey

OneKey is a command-line password manager for storing and accessing your online credentials. Currently only supports Linux (maybe macOS too?).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install OneKey.

```bash
pip install onekey_manager
```

## Usage

```
hubert@Ubuntu:~$ one_key --help
[WARNING] You do not have an account yet. Create one with the -acc option

usage: one_key [-h] [-acc | -si | -d | -so | -k | -g | -a | -rm | -l]

options:

  -h, --help       show this help message and exit
  -acc, --add-acc  add an account for yourself
  -si, --sign-in   sign yourself in
  -d, --del-acc    delete your user account and your credentials
  -so, --sign-out  sign yourself out
  -k, --reset-key  reset your key
  -g, --get-cred   get a credential
  -a, --add-cred   add a credential
  -rm, --rm-cred   remove a credential
  -l, --list       list the current user's credentials
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
