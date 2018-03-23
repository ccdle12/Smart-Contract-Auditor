# Smart-Contract-Auditor

## Installation - Docker

In root directory, run:
```./dockerbuild.sh```

This will run build an instance of ganache (replacement of testrpc)

### Run - Truffle

The terminal will look like it's stalled, it will show:

```
Creating smartcontractauditor_truffle_1 ... done
```

Press any button

You will see a prompt:

```
:/code# 
```

Go into the truffle folder and the code:

```
cd ./truffle/code
```

Compile, Migrate and Test the contracts:

```
truffle compile
truffle migrate
truffle test
```

### Run - Auditor
Open a new terminal

```
cd ./auditor
```

Run - it will look like the terminal has stalled, it hasn't - press any button to continue

```
./run-container.sh
```

Go to the code folder:

```
cd ./opt/source-code
```

Run tests

```
python tests.py
```


## Installation - Manual (Mac OSX)
``` brew install python3 ```

``` sudo easy_install pip ```

``` npm install -g ganache-cli ```

### Run - Ganache

Run Ganache:

```ganache-cli```

### Run - Truffle

Open a new terminal

Go To:

``` cd ./truffle```

Compile, Migrate and Test Truffle:

```
truffle compile
truffle migrate
truffle test
```

### Run - Auditor

Open a new terminal

Go To:

``` cd ./auditor```

Run tests

```
python test.py
```


