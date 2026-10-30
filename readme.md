# Password Weigher
**Python tool to check the strength of password**, managed via 'weights' method. User inputs password and process is shown if `debug == True`, final output is compared to score brackets (unsecure to very strong).

> ## Points Handling:
>
> **Additions:**
> - `1` Per Character
> - `2` Per Symbol
>
> **Removals:**
> - `-1` for all uppercase/lowercase, all numbers or all letters
> - `-2` for consecutive numbers ('152543534')
> - `-3` for consecutive letters ('qirtnqnhfi')
> - `-4` for sequenced numbers ('12345')
> - `-6` for sequenced letters ('abcdef')
> - `-10` for common password (e.g. 'password', 'abc')

> ## Strength Output:
> 
> - Very Strong: `undecided` - best possible outcome
> - Strong: `undecided`
> - Moderate: `undecided`
> - Bare Minimum: `undecided`
> - Unsecure: `undecided` - worst possible outcome, via score being <5 or common password

`main.py` for entire program processsing, `weights.json` for singular assigned points ('weights') to sum final score and decide strength output, `common.json` with a database of 'common' passwords that should not be used (e.g. 'password', 'abc123').