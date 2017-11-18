const args = process.argv.slice[2];
const arr = args[0];
const size = args[1];

function chunks(arr, size) {
  let newArr = [];
  for (var i = 0; i < arr.length; i += size) {
    newArr.push(arr.slice(i, i+size));
  }
  return newArr;
}

function reversedChunks(arr, size) {
  return chunk(arr,size).reverse();
}

function flattenedChunks(chunks) {
  let flat = [];
  for (var i = 0; i < chunks.length; i++) {
    for (var k = 0; k < chunks[i].length; k++) {
      flat.push(chunks[i][k]);
    }
  }
  return flat;
}

console.log(flattenedChunks(reversedChunks(arr, size)).join(" "));
