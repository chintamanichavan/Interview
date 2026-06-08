#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

class MovieRentingSystem {
public:
    MovieRentingSystem(int n, std::vector<std::vector<int>>& entries) {
        (void)n;
        for (auto& e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            priceOf[key(shop, movie)] = price;
            available[movie].insert({price, shop});
        }
    }

    std::vector<int> search(int movie) {
        std::vector<int> res;
        auto it = available.find(movie);
        if (it != available.end()) {
            for (auto& [price, shop] : it->second) {
                if (res.size() == 5) break;
                res.push_back(shop);
            }
        }
        return res;
    }

    void rent(int shop, int movie) {
        int p = priceOf[key(shop, movie)];
        available[movie].erase({p, shop});
        rented.insert({p, shop, movie});
    }

    void drop(int shop, int movie) {
        int p = priceOf[key(shop, movie)];
        rented.erase({p, shop, movie});
        available[movie].insert({p, shop});
    }

    std::vector<std::vector<int>> report() {
        std::vector<std::vector<int>> res;
        for (auto& [price, shop, movie] : rented) {
            if (res.size() == 5) break;
            res.push_back({shop, movie});
        }
        return res;
    }

private:
    std::unordered_map<int, std::set<std::pair<int, int>>> available;  // movie -> {(price, shop)}
    std::set<std::tuple<int, int, int>> rented;                       // {(price, shop, movie)}
    std::unordered_map<long long, int> priceOf;

    static long long key(int shop, int movie) {
        return (long long)shop * 100000 + movie;
    }
};

std::string intList(const std::vector<int>& xs) {
    std::string s = "[";
    for (size_t i = 0; i < xs.size(); ++i) {
        if (i) s += ", ";
        s += std::to_string(xs[i]);
    }
    return s + "]";
}

std::string pairList(const std::vector<std::vector<int>>& xs) {
    std::string s = "[";
    for (size_t i = 0; i < xs.size(); ++i) {
        if (i) s += ", ";
        s += intList(xs[i]);
    }
    return s + "]";
}

int main() {
    std::vector<std::vector<int>> entries = {{0, 1, 5}, {0, 2, 6}, {0, 3, 7}, {1, 1, 4}, {1, 2, 7}, {2, 1, 5}};
    MovieRentingSystem m(3, entries);
    std::vector<std::string> out = {"null"};
    out.push_back(intList(m.search(1)));
    m.rent(0, 1);
    out.push_back("null");
    m.rent(1, 2);
    out.push_back("null");
    out.push_back(pairList(m.report()));
    m.drop(1, 2);
    out.push_back("null");
    out.push_back(intList(m.search(2)));

    std::string line = "[";
    for (size_t i = 0; i < out.size(); ++i) {
        if (i) line += ", ";
        line += out[i];
    }
    line += "]";
    std::cout << line << "\n";
    return 0;
}
