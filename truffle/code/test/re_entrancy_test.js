const Victim = artifacts.require('Victim.sol')
const Attacker = artifacts.require('Attacker.sol') 

const BigNumber = web3.BigNumber

const should = require('chai')
  .use(require('chai-as-promised'))
  .use(require('chai-bignumber')(BigNumber))
  .should();


contract('PreSolution Reentrancy', function(accounts) {
  const ERROR_MSG = 'VM Exception while processing transaction: revert'
  const deploying_account = accounts[0]
  const account1 = accounts[1]
  const account2 = accounts[2]
  const account3 = accounts[3]
  const account4 = accounts[4]

  // Helper Functions
  var getBalance = web3.eth.getBalance
  var getBalanceInEth = address => web3.toBigNumber(web3.fromWei(getBalance(address).toNumber())).toNumber()

  beforeEach(async () => {
    this.Victim = await Victim.deployed()
    this.Attacker = await Attacker.deployed()
  });

  it("should exist", async() =>  {
    await this.Victim.should.exist
  });

  it("should deposit 90 Ether into the contract", async() =>  {
    await this.Victim.deposit({from: account2, value: web3.toWei(90, 'ether')})

    var balance = await web3.eth.getBalance(this.Victim.address)
    var expected = web3.toWei(90)

    balance.toNumber().toString().should.equal(expected)
  });

  it("should show account2 balance as 9", async() =>  {
    var balance = await getBalance(account2)
    var balance = balance.c[0]

    var expected = 100000

    balance.should.not.be.above(expected)
  });

  it("Attacker address should have a balance of 0", async() =>  {
    var attackerBalance = await getBalance(this.Attacker.address)
    
    var balance = attackerBalance.c[0]

    balance.should.equal(0)
  });

  it("should attack victim and have a balance of 50 ether", async() =>  {

    await this.Attacker.collect({from: account2, value: web3.toWei(1, "ether")})

    var balance = await getBalanceInEth(this.Attacker.address)

    console.log("Victim Balance after attack: " + await getBalance(this.Victim.address))
    console.log("Balance after attack: " + balance)
   
    var expected = 50

    balance.should.be.equal(expected)
  });

  it("should kill attacking contract and siphone all the funds to account1", async() =>  {

    var beforeKill = await getBalance(account2).toNumber()
    console.log("Account1 Balance before kill contract: " + beforeKill)

    await this.Attacker.kill({from: account2})

    var afterKill = await getBalance(account2).toNumber()
    console.log("Account1 Balance after kill contract: " + afterKill)

    afterKill.should.be.above(beforeKill)
  });

  it("should show Attacker contract drained of funds", async() =>  {

    var attackerBalance = await getBalance(this.Attacker.address).toNumber()
    var expected = 0

    attackerBalance.should.equal(expected)
  });


});