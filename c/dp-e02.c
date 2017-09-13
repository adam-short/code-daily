#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {

  if (argc != 3) {
    return 1;
  }

  int mass = atoi(argv[1]);
  int acceleration = atoi(argv[2]);

  printf("If F = M * A, M is %d and A is %d  :  F is %d.\n",
         mass, acceleration, mass * acceleration);

  return 0;
}
