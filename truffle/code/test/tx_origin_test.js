const TxOriginVictim = artifacts.require('TxOriginVictim.sol')
const TxOriginAttacker = artifacts.require('TxOriginAttacker.sol') 

const BigNumber = web3.BigNumber

const should = require('chai')
  .use(require('chai-as-promised'))
  .use(require('chai-bignumber')(BigNumber))
  .should();

contract('PreSolution Tx Origin Attack', function(accounts) { 
  const ERROR_MSG = 'VM Exception while processing transaction: revert'
  const deploying_account = accounts[0]
  const account1 = accounts[1]
  const account2 = accounts[2]
  const account3 = accounts[3]
  const account4 = accounts[4]

  /**
   * Helper Functions 
   */
  const helperBigNumber = (x) => new BigNumber(x);
  const helperRoundBigNum = (x) => helperBigNumber(x).toNumber();
  const helperFixedBigNum = (x) => helperBigNumber(x).toFixed(20);
  async function helperTryCatch(x) {let bool = true; try {await x;} catch(err){bool = false;} return bool;}
  const getBalance = web3.eth.getBalance
  const helperGetBalanceInEth = address => web3.toBigNumber(web3.fromWei(getBalance(address).toNumber())).toNumber()
  const etherToWei = (x) => helperRoundBigNum(web3.toWei(x, "ether"));
  async function sendTransaction(sender, receiver, amount) { await web3.eth.sendTransaction({from: sender, to: receiver, value: web3.toWei(amount, "ether")})};

  before(async () => {
    this.txOriginVictim = await TxOriginVictim.new({from: deploying_account})
    this.txOriginAttacker = await TxOriginAttacker.new({from: account1})
  });

  it("should exist", async() =>  {
    await this.txOriginVictim.should.exist
    await this.txOriginAttacker.should.exist
  });

  it("should have account1 as the owner of the attacking contract", async() => {
    let owner = await this.txOriginAttacker.getOwner.call();
    owner.should.equal(account1);
  });

  it("should fund the victim wallet", async() => {
    await sendTransaction(deploying_account, this.txOriginVictim.address, 0.2);

    let balanceOfVicim = helperRoundBigNum(getBalance(this.txOriginVictim.address));
    balanceOfVicim.should.equal(etherToWei(0.2));
  });

  it("should drain victim of funds account1", async() => {
    let owner = await this.txOriginVictim.getOwner.call();
    owner.should.equal(deploying_account);

    await this.txOriginVictim.transferTo(this.txOriginAttacker.address, etherToWei(0.00213), {from: deploying_account})

    balanceOfVicim = helperRoundBigNum(getBalance(this.txOriginVictim.address));
    balanceOfVicim.should.equal(0);
  });


});