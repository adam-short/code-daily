function solution (number) {
  sum = 0
  for (let x = 0; x < number; x += 1) {
    if (x % 3 === 0 || x % 5 === 0) {
      sum += x
    }
  }

  return sum
}

console.log(solution(10))
console.log(solution(200))