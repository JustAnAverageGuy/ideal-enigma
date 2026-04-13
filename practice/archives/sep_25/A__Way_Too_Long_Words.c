#include <stdio.h>
#include <string.h>

void solve() {

  char buf[101];
  scanf("%s", buf);
  int n = strlen(buf);
  if (n <= 10) {
    printf("%s\n", buf);
        return;
  }
  printf("%c%d%c\n", buf[0], n - 2, buf[n - 1]);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);

  while (T--) {
        solve();
  }
}
