#include <stdlib.h>
#include <stdio.h>


int sum (n1, n2) {
  return n1 + n2;
}

int sub (n1, n2) {
  return n1 - n2;
}

int div (n1, n2) {
  return n1 / n2;
}

int mul (n1, n2) {
  return n1 * n2;
}

// (10 / 2) * 3 + 5 ------------>   {''}
// 5 - 2            ------------>   sub(5, 2)
// 5 - 2 * 3        ------------>   sub(5, mul(2, 3))

/*
  (10 / 2) * 3 + 5
  {
    '+': [{
      '*': [{
        '/': [10, 2]
      }, 3]
    }, 5]
  }

  5 - 2 * 3
  {
    '*': [{
      '-': [5, 2]
    }, 3]
  }

  {
    'symbol': ['int or symbol dict', 'int or symbol dict']
  }


  1. branches in reverse - from last symbol to first with order of operation in.

*/

int main(int argc, char *argv[]) {

}
