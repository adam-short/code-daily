const UPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const LOWS = "abcdefghijklmnopqrstuvwxyz";

function shiftCharBy(char, shift) {
  let normchar = char.toLowerCase();
  let pos = (LOWS.indexOf(normchar) + shift) % LOWS.length;
  if (LOWS.indexOf(normchar) != -1) {
    return UPS.indexOf(char) > -1 ? UPS[pos] : LOWS[pos]
  } else {
    return char;
  }
}

function shiftStringBy(str, shift) {
  return str.split('').map((x) => shiftCharBy(x, shift)).join('');
}

let args = process.argv.slice(2);
console.log( shiftStringBy(args[0], parseInt(args[1])) );
