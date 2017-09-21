var Decimal = require('decimal.js');
Decimal.set({ precision: 120 });

let b1 = new Decimal(1);
let b2 = new Decimal(2);
let b4 = new Decimal(4);
let b8 = new Decimal(8);
let b16 = new Decimal(16);

let seedk = k => b1.div(b16.pow(k));
let k8_1 = k => b4.div(b8.mul(k).add(1));
let k8_4 = k => b2.div(b8.mul(k).add(4));
let k8_5 = k => b1.div(b8.mul(k).add(5));
let k8_6 = k => b1.div(b8.mul(k).add(6));
let BBPFORMULA = n => seedk(n) * (k8_1(n) - k8_4(n) - k8_5(n) - k8_6(n));

let guessPI = n => {
  let sum = new Decimal(0);
  for (let k = 0; k < n; k++) {
    sum = sum.add(BBPFORMULA(k));
  }
  return sum;
}

console.log(guessPI(parseInt(process.argv[2])).toString());
