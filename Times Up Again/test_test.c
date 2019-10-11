#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h> 
#include <string.h>
// picoCTF{Hasten. Hurry. Ferrociously Speedy. #2edc7d0a}
// mkfifo fifo
// ./times-up-again <~/fifo | tee /dev/stderr | ~/test >~/fifo
#define true 1
#define false 0

long long nums[20];
int num_count = 0;
char buf[400];
long long ssign = 1;
int count = 0;
char curr;
int reading = false;
// char buf[1000];

long long maybe_decrease(int a1) {
  if ( rand() % 50 <= 0 )
    return a1;
  else
    return a1 - 1;
}

int get_random_op(){
  unsigned long long v0; // ST08_8
  int v2; // [rsp+14h] [rbp-Ch]
  unsigned long long v3; // [rsp+18h] [rbp-8h]

  v2 = 2764075;
  v0 = rand();
  return v0 - 3 * ((unsigned long long)(0xAAAAAAAAAAAAAAABLL * (unsigned __int128)v0 >> 64) >> 1);
}

long long do_op(int a1, long long a2, long long a3) {
  if (a1 == 0) {
    // fprintf(stderr, "+ ");
    return a2+a3;
  }

  if (a1 == 1) {
    // fprintf(stderr, "- ");
    return a2-a3;
  }

  if (a1 == 2) {
    // fprintf(stderr, "* ");
    return a2*a3;
  }
}

long long gen_expr(int a1) {
  long long v3,v4,v6,v7, result;
  int v5;
  if ( a1 ) {
    v3 = maybe_decrease(a1);
    v4 = maybe_decrease(a1);
    v5 = get_random_op();
    v6 = gen_expr(v3);
    v7 = gen_expr(v4);
    result = do_op(v5, v6, v7);
  } else {
    result = nums[num_count++];
  }
  return result;
}

int main(int argc, char** argv) {
  register long long s;
  srand(time(0));
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  read(0, &buf, 400);
  while ((curr = buf[count++]) != 0xa) {
    if (curr == 45 && buf[count] >= 48 && buf[count] <= 57) {
      ssign = -1;
    }
    if (curr >= 48 && curr <= 57) {
      if (!reading) {
        s = ssign*(curr-48);
        
        reading = true;
      } else {
        s = 10*s+ssign*(curr-48);
      }
    } else {
      if (reading) {
        reading = false;
        nums[num_count++] = s;
        ssign = 1;
      }
    }
  }
  num_count = 0;
  s = gen_expr(4);

  // for (int i = 0; i < num_count; i++) {
  //   fprintf(stderr, "%lld\n", nums[i]);
  // }
  
  // fgets(buf, 300, stdin);
  // fprintf(stderr, "%lld\n", s);
  // puts("10");
  printf("%lld\n", s);


  while(true) {
    memset(buf, 0, sizeof(buf));
    read(0, buf, 1);
    fprintf(stderr, "%s", buf);
  }
  return 0;
}

// int main() {
//   srand(time(0));
//   printf("%d", get_random_op());
//   printf("%d", get_random_op());
//   printf("%d", get_random_op());
//   printf("%d", get_random_op());
// }