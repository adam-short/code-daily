#include <stdlib.h>

struct DataItem {
  char data[2];
  int key;
}

struct DataItem* hashArray[SIZE];
struct DataItem* dummyItem;



struct Operation {
  char symbol;
  int n1;
  int n2;
}
