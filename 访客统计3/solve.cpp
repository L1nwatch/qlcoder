#include <cstdio>
#include <cstring>
#include <bitset>

using namespace std;

long long twist(long long u, long long v)
{
    return (((u & 0x80000000L) | (v & 0x7fffffffL)) >> 1) ^ ((v & 1) == 1 ? 0x9908b0dfL : 0);
}

long long state[624];
int left = 1;

void next_state()
{
    int p = 0;
    left = 624;
    for (int j = 228; --j > 0; p++)
    {
        state[p] = state[p + 397] ^ twist(state[p], state[p + 1]);
    }

    for (int j = 397; --j > 0; p++)
    {
        state[p] = state[p - 227] ^ twist(state[p], state[p + 1]);
    }

    state[p] = state[p - 227] ^ twist(state[p], state[0]);
}

long long next()
{
    if (--left == 0) { next_state(); }
    return state[624 - left];
}

int main()
{
    long long limit = 50000000000L;

    for (int j = 1; j < 624; j++)
    {
        state[j] = (1812433253L * (state[j - 1] ^ (state[j - 1] >> 30)) + j);
        state[j] &= 0xfffffffffL;
    }
    bitset<1073741823> &statistic_bitset = *(new bitset<1073741823>());
    for (long long i = 0; i < limit; i++)
    {
        if (i % 100000 == 0)
        {
            printf("[*] 正在进行 %lld, 总共 %lld\n", i, limit);
        }

        long long tmp_long = next();
        if ((tmp_long & 0x000000000000003f) == 0x0000000000000000)
        {
            tmp_long >>= 6;
        }
        statistic_bitset.set(tmp_long, true);
    }

    printf("[*] 最终结果为: %lld * 64\n", statistic_bitset.count());


    return 0;
}

