#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <vector>

class LFUCache {
public:
  LFUCache(int capacity) : cap(capacity), minFreq(0) {}

  int get(int key) {
    auto it = keyVal.find(key);
    if (it == keyVal.end())
      return -1;
    bump(key);
    return it->second;
  }

  void put(int key, int value) {
    if (cap <= 0)
      return;
    if (keyVal.count(key)) {
      keyVal[key] = value;
      bump(key);
      return;
    }
    if ((int)keyVal.size() >= cap) {
      int ek = freqList[minFreq].front();
      freqList[minFreq].pop_front();
      keyVal.erase(ek);
      keyFreq.erase(ek);
      keyIter.erase(ek);
    }
    keyVal[key] = value;
    keyFreq[key] = 1;
    freqList[1].push_back(key);
    keyIter[key] = std::prev(freqList[1].end());
    minFreq = 1;
  }

private:
  int cap, minFreq;
  std::unordered_map<int, int> keyVal, keyFreq;
  std::unordered_map<int, std::list<int>>
      freqList; // freq -> keys, front = oldest
  std::unordered_map<int, std::list<int>::iterator> keyIter; // key -> its node

  void bump(int key) {
    int f = keyFreq[key];
    freqList[f].erase(keyIter[key]);
    if (freqList[f].empty()) {
      freqList.erase(f);
      if (minFreq == f)
        ++minFreq;
    }
    keyFreq[key] = f + 1;
    freqList[f + 1].push_back(key);
    keyIter[key] = std::prev(freqList[f + 1].end());
  }
};

int main() {
  std::vector<std::string> ops = {"LFUCache", "put", "put", "get", "put", "get",
                                  "get",      "put", "get", "get", "get"};
  std::vector<std::vector<int>> args = {{2}, {1, 1}, {2, 2}, {1}, {3, 3}, {2},
                                        {3}, {4, 4}, {1},    {3}, {4}};
  LFUCache *c = nullptr;
  std::string out = "[";
  for (size_t i = 0; i < ops.size(); ++i) {
    if (i)
      out += ", ";
    if (ops[i] == "LFUCache") {
      delete c;
      c = new LFUCache(args[i][0]);
      out += "null";
    } else if (ops[i] == "get") {
      out += std::to_string(c->get(args[i][0]));
    } else {
      c->put(args[i][0], args[i][1]);
      out += "null";
    }
  }
  out += "]";
  std::cout << out << "\n";
  delete c;
  return 0;
}
