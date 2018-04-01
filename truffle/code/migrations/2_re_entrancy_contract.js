const ReentrancyVictim = artifacts.require('ReentrancyVictim')

module.exports = function(deployer) {
  deployer.deploy(ReentrancyVictim);
};
