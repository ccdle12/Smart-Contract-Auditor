const Attacker = artifacts.require('Attacker.sol')
const Victim = artifacts.require('Victim')

module.exports = function(deployer) {
  deployer.deploy(Victim).then(() => deployer.deploy(Attacker, Victim.address))
};
