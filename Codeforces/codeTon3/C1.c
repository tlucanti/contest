#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d\n", &t);
    char *a = malloc(2000100);
    char *b = malloc(2000100);

    while (t--) {
        int n;
        scanf("%d\n", &n);
        scanf("%*s\n%*s\n", n, a, n, b);

        for (int i=0; i < n; ++i) {
            a[i] = a[i] - '0';
            b[i] = b[i] - '0';
        }
        int ok = 1;
        int ans[n + 10];
        int ansi = 0;

        int invs = 0;

        if (memcmp(a, b, n * sizeof(char)) != 0) {
            for (int i=0; i < n; ++i) {
                if (a[i] != 1 - b[i]) {
                    ok = 0;
                    break ;
                }
            }
        } else {
            ans[ansi++] = 1;
            ans[ansi++] = n;
            for (int i=0; i < n; ++i) {
                a[i] = 1 - a[i];
            }
        }
        if (!ok) {
            printf("NO\n");
            continue ;
        }
        printf("YES\n");
        for (int i=0; i < n; ++i) {
            if (a[i] == 1) {
                ans[ansi++] = i + 1;
                ans[ansi++] = i + 1;
                ++invs;
            }
        }
        if (invs % 2 == 0) {
            ans[ansi++] = 1;
            ans[ansi++] = n;
            ans[ansi++] = 1;
            ans[ansi++] = 1;
            ans[ansi++] = 2;
            ans[ansi++] = n;
        }
        printf("%d\n", ansi / 2);
        for (int i=0; i < ansi; i += 2) {
            printf("%d %d\n", ans[i], ans[i + 1]);
        }
    }
    return 0;
}
