### Steps to recreate
./dockerbuild.sh (remove containers and images, run docker compose)

docker attach smartcontractauditor_truffle_1 (attach the truffle image)

in the docker truffle image
    - cd ./truffle
    - mkdir code
    - cd ./code
    - truffle init

open truffle.js in code folder

edit the file to look like:

```
networks: {
    development: {
      host: 'ganache', // Name of ganache-cli service in docker-compose
      port: 8545,
      network_id: '*', // Match any network id
      gas:4712388,
    }
  }
```

Run truffle commands:

```
truffle compile
truffle migrate
```