#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  if (argc != 3) {
    return 1;
  }

  char input[] = argv[1];
  int shift = atoi(argv[2]);
  for (int i = 0; i < 25; i++) {
    if (input[i] + shift >= 122) {
      input[i] = 97 + (shift - 1);
    } else {
      input[i] = input[i] + shift;
    }
  }

  printf("Shifted message is '%s'.\n", input);

  return 0;
}
