#include <stdio.h>

int main() {
  int grade[3];
  int average;

  grade[0] = 80;
  grade[1] = 90;
  grade[2] = 78;

  average = (grade[0] + grade[1] + grade[2]) / 3;
  printf("The average of the 3 grades is: %d.\n", average);

  return 0;
}
