export const bootstrap = (): void => {
    class BankAccount {
        protected holder: string;
        protected balance: number;

        constructor(holder: string, balance: number) {
            this.holder = holder;
            this.balance = balance;
        }

        public getHolder():string {
            return this.holder;
        }
    }

    class ChekingAccount extends BankAccount {
        private overdrafLimit: number;

        constructor(holder:string, balance:number, overdrafLimit: number) {
            super(holder, balance);
            this.overdrafLimit = overdrafLimit;
        }

        public getOverdrafLimit(): number {
            return this.overdrafLimit
        }
    }

    class SavingsAccount extends BankAccount {
        private interestRate: number;

        constructor(holder: string, balance: number, interestRate: number) {
            super(holder, balance);
            this.interestRate = interestRate;
        }

        public getInterestRate(): number {
            return this.interestRate;
        }
    }

    // lista de contas bancárias
    const accountList: BankAccount[] = [
        new ChekingAccount('Alice', 1500, 300),
        new SavingsAccount('João', 4000, 0.005),
        new ChekingAccount('Maria', 10000, 3000),
        new SavingsAccount('Paulo', 1000, 0.005),
    ];

    function processAcounts(accounts: BankAccount[]): void {
        accounts.forEach(account => {
            if(account instanceof ChekingAccount) {
                console.log('Processando a conta corrente: ', account.getOverdrafLimit());
            } else if (account instanceof SavingsAccount) {
                console.log('Processando a conta poupança: ', account.getInterestRate());
            }
            console.log('-----------');
        });
    } 

    processAcounts(accountList);

    // const a = new BankAccount('Jorge', 1500);
    // const b = new ChekingAccount(25000);

    // console.log(a);
    // console.log(typeof a);
    // // instanceof retorna true ou false, caso o objeto seja instanceado pela classe
    // console.log(a instanceof BankAccount);
    // console.log(a instanceof ChekingAccount);

    // function showDetails(account: BankAccount | ChekingAccount): void {
    //     if(account instanceof BankAccount) {
    //         console.log(account.getHolder());
    //     } else if(account instanceof ChekingAccount) {
    //         console.log(account.getOverdrafLimit());
    //     }else {
    //         console.error('Conta não identificada');
    //     }
    // }

    // showDetails(a);
    // showDetails(b);

};