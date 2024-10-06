// from random import randint

// N = randint(1, 1_00_000)
// print(N)

// A = [randint(1,N) for i in range(N)]
// print(*A,sep='\n')

// TEAMSIZE = randint(1,N)
// print(TEAMSIZE)

// K = randint(1,N)
// print(K)

# include <iostream>
# include <cstdlib>

using namespace std;

#define print(x) cout << (x) << '\n'

int randint(int a, int b){
    int randNum = rand()%(b-a + 1) + a;
    return randNum;
}


int main(){
    
    auto N = randint(1, 1'00'000);
    print(N);


    for (int i =0; i<N; i++) cout << randint(1,(int) 1e9) << '\n';

    auto TEAMSIZE = randint(1,N);
    print(TEAMSIZE);

    auto K = randint(1,N);
    print(K);

}