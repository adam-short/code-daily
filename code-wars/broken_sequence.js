function findMissingNumber (sequence) {
  let prev = 0
  const nums = sequence.split(' ').map(x => parseInt(x))

  if (sequence === '') {
    return 0
  } else if (nums.some(x => isNaN(x))) {
    return 1
  }
  
  for (const i of nums) {
    prev += 1
    console.log(i, prev)
    if (prev != i) {
      return !isNaN(i) ? prev : 0
    }
  }

  return 0
}