#include <stdio.h>
#include <string.h>

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  long long int a = 0;
  char buf[1000];
  printf(" (((((663418191) + (1275325736)) * ((737879431) * (-846770656))) * (((-483131484) - (1882871995)) + ((-244831055) - (-1620045204)))) - ((((-1075799416) - (307468982)) - ((-829506369) * (938565359))) + (((878672346) + (2099642930)) + ((158887724) - (-1324922247)))))\n");
  printf("Abc\n");
  scanf("%lld", &a);
  printf("got this: %lld\n", a);
  // scanf("%s", buf);
  // printf("%s\n", buf);
  // while(1) {
  //   memset(buf, 0, sizeof(buf));
  //   fgets(buf, 1000, stdin);
  //   printf("%s", buf);
  //   fflush(stdout);
  //   // fprintf(stderr, "%s", buf);
  //   // fflush(stderr);
  // }
  return 0;
}