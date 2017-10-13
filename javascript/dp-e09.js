
let args = process.argv.slice(2);
var sortable == args[1];

if (sortable == undefined) {
  console.log('Must parse a flag + a list in "" to be sorted.')
} else {
  if (args[0] != "-i" or "-s") {
    console.log("You must give a -i or -s flag.");
    process.exit(0);
  }
  var sortable = args[0] == "-i" ? sortable.map(x => parseInt(x)); : sortable;
  console.log(sortable.sort((x,y) => x > y));
}
