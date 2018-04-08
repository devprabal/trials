#include <iostream>
#include <stack>
using namespace std;
int main(int argc, char const *argv[]) {
  int N, Q, X, countHarry = 0, countRemove = 0, netWorth = 0;
  int itr; // for WorthOfCoins
  std::cin >> N;
  int WorthOfCoins[N];
  for (int i = 0; i < N; i++) {
    std::cin >> WorthOfCoins[i];
  }
  std::cin >> Q >> X;
  string Instructions[Q];
  for (int i = 0; i < Q; i++) {
    std::cin >> Instructions[i];
  }
  stack<int> monk;
  for (int i = 0; i < Q; i++) {
    if (Instructions[i] == "Harry") {
      monk.push(WorthOfCoins[itr]);
      itr++;
      countHarry++;
      netWorth = netWorth + monk.top();
    }
    if (Instructions[i] == "Remove") {
      countRemove++;
      netWorth = netWorth - monk.top();
      monk.pop();
    }
  }
  if (netWorth == X) {
    std::cout << countHarry - countRemove;
  } else {
    std::cout << -1;
  }

  return 0;
}
