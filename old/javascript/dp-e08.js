
function bottlesSong () {
  for (let i=100; i >= 1; i--) {
    console.log(`${i} bottles of beer on the wall, ${i} bottles of beer.`);
    console.log(`Take one down and pass it around, ${i-1>0 ? i-1 : 'no more'} bottles of beer on the wall.`);
  }
  console.log("No more bottles of beer on the wall, no more bottles of beer.");
  console.log("Go to the store and buy some more, 99 bottles of beer on the wall.");
}

bottlesSong();
