/* FANCY VERSION */
function mxdiflg(a1, a2) {
    const diffs = [].concat.apply([], a1.map((x) => a2.map((y) => Math.abs(x.length - y.length))))
    
    return a1.length === 0 || a2.length === 0 ? -1 : Math.max(...diffs)
}

/* SIMPLE VERSION */
function mxdiflg_simple(a1, a2) {
  let highest = -1;
  for (var i = 0; i < a1.length; i += 1) {
    for (var k = 0; k < a2.length; k += 1) {
      const diff = Math.abs(a1[i].length - a2[k].length)
      if (diff > highest) {
        highest = diff
      }
    }
  }
  
  return highest
}

const s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
const s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

console.log(mxdiflg(s1, s2))
console.log(mxdiflg_simple(s1, s2))