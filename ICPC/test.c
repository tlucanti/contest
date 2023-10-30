
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct PairValue{
  #define KEY_STRING_MAX 255
  char KeyName[KEY_STRING_MAX + 1];
  int  ValueCount;
  struct PairValue* Next;
} PairValue;

typedef struct HashMap{
  #define MAP_MAX 128
  PairValue* data[MAP_MAX];
} HashMap;

unsigned HashIndex(const char* key) {
  unsigned sum = 0;
  for( char* c = key; *c; c++ ){
    sum += *c;
    sum = sum % MAP_MAX;
  }
  return sum;
}

HashMap* HashInit() {
  HashMap *ret = malloc(sizeof(HashMap));
  bzero(ret, sizeof(HashMap));
  return ret;
}

void HashAdd(HashMap *map, PairValue *value) {
  unsigned idx = HashIndex(value->KeyName);

  if (map->data[idx]) {
	  PairValue *p = map->data[idx];
	  while (p->Next) {
		  p = p->Next;
	  }
	  p->Next = value;
  } else {
    map->data[idx] = value;
  }
  value->Next = NULL;
}

PairValue* HashFind(HashMap *map, const char* key) {
  unsigned idx = HashIndex(key);
  for( PairValue* val = map->data[idx]; val != NULL; val = val->Next ) {
    if (strcmp(val->KeyName, key) == 0) {
      return val;
    }
  }
  return NULL;
}

void HashDelete(HashMap *map, const char* key) {
  unsigned idx = HashIndex(key);

  for( PairValue* val = map->data[idx], *prev = NULL; val != NULL; prev = val, val = val->Next ) {
    if (strcmp(val->KeyName, key) == 0) {
      if (prev) {
        prev->Next = val->Next;
      }
      else {
        map->data[idx] = val->Next;
      }
    }
  }
}

void HashDump(HashMap *map) {
  for( unsigned idx = 0; idx < MAP_MAX; idx++ ) {
    for( PairValue* val = map->data[idx]; val != NULL; val = val->Next ) {
      printf("%s", val->KeyName);
      printf("\n");
    }
  }
}

int main() {
  PairValue value;
  char searchKey[KEY_STRING_MAX + 1];
  char deleteKey[KEY_STRING_MAX + 1];

  scanf("%255s", value.KeyName);
  scanf("%255s", searchKey);
  scanf("%255s", deleteKey);

  HashMap *map = HashInit();
  HashAdd(map, &value);
  PairValue *foundValue = HashFind(map, searchKey);
  if (foundValue) {
    printf("found value: ");
    printf("%s", foundValue->KeyName);
    printf("\n");
  }

  HashDelete(map, deleteKey);
  HashDump(map);
}
