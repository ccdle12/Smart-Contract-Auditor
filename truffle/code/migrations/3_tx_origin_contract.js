const TxOriginVictim = artifacts.require('TxOriginVictim')

module.exports = function(deployer) {
  deployer.deploy(TxOriginVictim);
};
