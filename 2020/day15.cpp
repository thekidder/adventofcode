#include <iostream>
#include <vector>

using namespace std;

// run with:
// g++ -O3 day15.cpp; time ./a.out

int main() {
  int nums[] = {0,14,1,3,7,9};
  // int nums[] = {0,3,6};
  int size = sizeof(nums)/sizeof(nums[0]);
  vector<int> turns = vector<int>(100, -1);

  int last, num = 0;

  for (int i = 0; i < size; i++) {
    int n = nums[i];
    turns[n*2] = i;
    turns[n*2+1] = 0;
    last = n;
  }

  for (int i = size; i < 30000000; i++) {
    if (turns.size() < last*2+1) {
      turns.resize(last*2+1, -1);
    }
    num = turns[last*2+1];
    if (turns.size() < num*2+1) {
      turns.resize(num*2+1, -1);
    }
    if (num == 0 || turns[num*2] > 0) {
      turns[num*2+1] = i - turns[num*2];
      turns[num*2] = i;
    } else {
      turns[num*2] = i;
      turns[num*2+1] = 0;
    }
    last = num;
  }

  cout << num << endl;
}
