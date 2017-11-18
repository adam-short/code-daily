
function randomItemOf(arr){
  let i = Math.floor(Math.random() * arr.length);
  return arr[i];
}

const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const randchar = () => randomItemOf(letters.split(''));

function randstr (length) {
  let result = [];
  for (let i = 0; i < length; i++) {
    result.push(randchar());
  }
  return result.join('');
}

console.log(randstr(parseInt(process.argv[2])));
