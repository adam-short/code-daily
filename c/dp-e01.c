#include <stdio.h>
#include <stdlib.h>

int main() {
  char name[50];
  int age;
  char username[50];

  printf("\nEnter name > ");
  gets(name);

  printf("\nEnter age > ");
  char ageinput[50];
  gets(ageinput);
  age = atoi(ageinput);

  printf("\nEnter username > ");
  gets(username);

  printf("\nYour name is %s, your age is %d and your username is %s.\n",
          name, age, username);

  return 0;
}
