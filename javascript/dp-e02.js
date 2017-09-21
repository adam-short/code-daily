let args = process.argv.slice(2);
let variables = args.slice(1).map((x) => parseInt(x));


let simple = (p, r, pe) => p + (p * (r/100) * pe);
let compound = (p, r, pe) => p * Math.pow((1 + r/100), pe);

if (args.length != 4) {
  console.log("ERROR: in format TYPE PRINCIPAL RATE PERIODS");
} else if (args[0] == 'simple') {
  console.log(simple(...variables));
} else if (args[0] == 'compound') {
  console.log(compound(...variables));
} else {
  console.log("Must use either 'simple' or 'compund' for type.");
}
