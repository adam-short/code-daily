const ALPHABET = {
    ".-" : "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

const morse2Letter = morse => ALPHABET[morse] ? ALPHABET[morse] : "?";
const morse2Word = morseWord => morseWord.split(' ').map(morse2Letter).join('');
const translate = morseSentence => morseSentence.map(morse2Word).join('');
const breakOnSlash = inp => inp.split(' / ');

function reverseObject(obj) {
  const keys = Object.keys(obj);
  return keys.reduce((result, key) => {
    result[obj[key]] = key;
    return result;
  }, {});
}

function decrypt(inp) {
  const morseSentence = breakOnSlash(inp);
  return translate(morseSentence);
}

function encrypt(inp) {
  const reversed = reverseObject(ALPHABET);
  const words = inp.toUpperCase().split(' ');
  const result = words.map((w) => w.split('').map((l) => reversed[l]).join(' '));
  return result.join(' / ');
}

if (process.argv[3] == '-d'){
  console.log(decrypt(process.argv[2]));
} else if (process.argv[3] == '-e') {
  console.log(encrypt(process.argv[2]));
} else {
  console.log("You need -d or -e.");
}
