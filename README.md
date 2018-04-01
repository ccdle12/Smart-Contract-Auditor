# Smart-Contract-Auditor

## Installation - Docker

In root directory, run:
```./dockerbuild.sh```

This will run build an instance of ganache (replacement of testrpc)

### Run - Truffle

Open a terminal and run:

```
docker attach smartcontractauditor_truffle_1
```

Go into the truffle folder and the code:

```
cd ./truffle/code
```

Compile, Migrate and Test the contracts:

```
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

``` npm install -g mocha ```

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


