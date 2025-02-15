#include <iostream>
#include <string>
using namespace std;
template <typename T>
T inverse(T a, T m) {
  T u = 0, v = 1;
  while (a != 0) {
    T t = m / a;
    m -= t * a; swap(a, m);
    u -= t * v; swap(u, v);
  }
  assert(m == 1);
  return u;
}
 
template <typename T>
class Modular {
 public:
  using Type = typename decay<decltype(T::value)>::type;
 
  constexpr Modular() : value() {}
  template <typename U>
  Modular(const U& x) {
    value = normalize(x);
  }
 
  template <typename U>
  static Type normalize(const U& x) {
    Type v;
    if (-mod() <= x && x < mod()) v = static_cast<Type>(x);
    else v = static_cast<Type>(x % mod());
    if (v < 0) v += mod();
    return v;
  }
 
  const Type& operator()() const { return value; }
  template <typename U>
  explicit operator U() const { return static_cast<U>(value); }
  constexpr static Type mod() { return T::value; }
 
  Modular& operator+=(const Modular& other) { value += other.value; value -= (value >= mod()) * mod(); return *this; }
  Modular& operator-=(const Modular& other) { value -= other.value; value += (value < 0) * mod(); return *this; }
  template <typename U> Modular& operator+=(const U& other) { return *this += Modular(other); }
  template <typename U> Modular& operator-=(const U& other) { return *this -= Modular(other); }
  Modular& operator++() { return *this += 1; }
  Modular& operator--() { return *this -= 1; }
  Modular operator++(int) { Modular result(*this); *this += 1; return result; }
  Modular operator--(int) { Modular result(*this); *this -= 1; return result; }
  Modular operator-() const { return Modular(-value); }
 
  template <typename U = T>
  typename enable_if<is_same<typename Modular<U>::Type, int>::value, Modular>::type& operator*=(const Modular& rhs) {
    value = normalize(static_cast<int64_t>(value) * static_cast<int64_t>(rhs.value));
    return *this;
  }
  template <typename U = T>
  typename enable_if<is_same<typename Modular<U>::Type, int64_t>::value, Modular>::type& operator*=(const Modular& rhs) {
    int64_t q = int64_t(static_cast<long double>(value) * rhs.value / mod());
    value = normalize(value * rhs.value - q * mod());
    return *this;
  }
  template <typename U = T>
  typename enable_if<!is_integral<typename Modular<U>::Type>::value, Modular>::type& operator*=(const Modular& rhs) {
    value = normalize(value * rhs.value);
    return *this;
  }
 
  Modular& operator/=(const Modular& other) { return *this *= Modular(inverse(other.value, mod())); }
 
  friend const Type& abs(const Modular& x) { return x.value; }
 
  template <typename U>
  friend bool operator==(const Modular<U>& lhs, const Modular<U>& rhs);
 
  template <typename U>
  friend bool operator<(const Modular<U>& lhs, const Modular<U>& rhs);
 
  template <typename V, typename U>
  friend V& operator>>(V& stream, Modular<U>& number);
 
 private:
  Type value;
};
 
template <typename T> bool operator==(const Modular<T>& lhs, const Modular<T>& rhs) { return lhs.value == rhs.value; }
template <typename T, typename U> bool operator==(const Modular<T>& lhs, U rhs) { return lhs == Modular<T>(rhs); }
template <typename T, typename U> bool operator==(U lhs, const Modular<T>& rhs) { return Modular<T>(lhs) == rhs; }
 
template <typename T> bool operator!=(const Modular<T>& lhs, const Modular<T>& rhs) { return !(lhs == rhs); }
template <typename T, typename U> bool operator!=(const Modular<T>& lhs, U rhs) { return !(lhs == rhs); }
template <typename T, typename U> bool operator!=(U lhs, const Modular<T>& rhs) { return !(lhs == rhs); }
 
template <typename T> bool operator<(const Modular<T>& lhs, const Modular<T>& rhs) { return lhs.value < rhs.value; }
 
template <typename T> Modular<T> operator+(const Modular<T>& lhs, const Modular<T>& rhs) { return Modular<T>(lhs) += rhs; }
template <typename T, typename U> Modular<T> operator+(const Modular<T>& lhs, U rhs) { return Modular<T>(lhs) += rhs; }
template <typename T, typename U> Modular<T> operator+(U lhs, const Modular<T>& rhs) { return Modular<T>(lhs) += rhs; }
 
template <typename T> Modular<T> operator-(const Modular<T>& lhs, const Modular<T>& rhs) { return Modular<T>(lhs) -= rhs; }
template <typename T, typename U> Modular<T> operator-(const Modular<T>& lhs, U rhs) { return Modular<T>(lhs) -= rhs; }
template <typename T, typename U> Modular<T> operator-(U lhs, const Modular<T>& rhs) { return Modular<T>(lhs) -= rhs; }
 
template <typename T> Modular<T> operator*(const Modular<T>& lhs, const Modular<T>& rhs) { return Modular<T>(lhs) *= rhs; }
template <typename T, typename U> Modular<T> operator*(const Modular<T>& lhs, U rhs) { return Modular<T>(lhs) *= rhs; }
template <typename T, typename U> Modular<T> operator*(U lhs, const Modular<T>& rhs) { return Modular<T>(lhs) *= rhs; }
 
template <typename T> Modular<T> operator/(const Modular<T>& lhs, const Modular<T>& rhs) { return Modular<T>(lhs) /= rhs; }
template <typename T, typename U> Modular<T> operator/(const Modular<T>& lhs, U rhs) { return Modular<T>(lhs) /= rhs; }
template <typename T, typename U> Modular<T> operator/(U lhs, const Modular<T>& rhs) { return Modular<T>(lhs) /= rhs; }
 
template<typename T, typename U>
Modular<T> power(const Modular<T>& a, const U& b) {
  assert(b >= 0);
  Modular<T> x = a, res = 1;
  U p = b;
  while (p > 0) {
    if (p & 1) res *= x;
    x *= x;
    p >>= 1;
  }
  return res;
}
 
template <typename T>
bool IsZero(const Modular<T>& number) {
  return number() == 0;
}
 
template <typename T>
string to_string(const Modular<T>& number) {
  return to_string(number());
}
 
// U == std::ostream? but done this way because of fastoutput
template <typename U, typename T>
U& operator<<(U& stream, const Modular<T>& number) {
  return stream << number();
}
 
// U == std::istream? but done this way because of fastinput
template <typename U, typename T>
U& operator>>(U& stream, Modular<T>& number) {
  typename common_type<typename Modular<T>::Type, int64_t>::type x;
  stream >> x;
  number.value = Modular<T>::normalize(x);
  return stream;
}
 
// using ModType = int;
 
// struct VarMod { static ModType value; };
// ModType VarMod::value;
// ModType& md = VarMod::value;
// using Mint = Modular<VarMod>;
 
constexpr int md = int(1e9) + 7;
using Mint = Modular<std::integral_constant<decay<decltype(md)>::type, md>>;
 
// vector<Mint> fact(1, 1);
// vector<Mint> inv_fact(1, 1);
 
// Mint C(int n, int k) {
//   if (k < 0 || k > n) {
//     return 0;
//   }
//   while ((int) fact.size() < n + 1) {
//     fact.push_back(fact.back() * (int) fact.size());
//     inv_fact.push_back(1 / fact.back());
//   }
//   return fact[n] * inv_fact[k] * inv_fact[n - k];
// }
string asjfbasjhbjhbhbjhbjsafjn(const string& text) {
    string iufhasikjbkqewhuroqahfj = "";
    for (char wkuhsafiujbekajfbs : text) {
        if (isalpha(wkuhsafiujbekajfbs)) {
            char kjehasfkbwkajbshbjasf = isupper(wkuhsafiujbekajfbs) ? 'A' : 'a';
            iufhasikjbkqewhuroqahfj += char((wkuhsafiujbekajfbs - kjehasfkbwkajbshbjasf + 13) % 26 + kjehasfkbwkajbshbjasf);
        } else {
            iufhasikjbkqewhuroqahfj += wkuhsafiujbekajfbs;
        }
    }
    return iufhasikjbkqewhuroqahfj;
}
// 10000
// 1
// 0
// 1
// 1
// 1
// 2
// 1
// 3
// 1
// 4
// 1
// 5
// 1
// 6
// 1
// 7
// 1
// 8
// 1
// 9
// 1
// 10
// 1
// 11
// 1
// 12
// 1
// 13
// 1
// 14
// 1
// 15
// 1
// 16
// 1
// 17
// 1
// 18
// 1
// 19
// 2
// 0 0
// 2
// 0 1
// 2
// 0 2
// 2
// 0 3
// 2
// 0 4
// 2
// 0 5
// 2
// 0 6
// 2
// 0 7
// 2
// 0 8
// 2
// 0 9
// 2
// 0 10
// 2
// 1 0
// 2
// 1 1
// 2
// 1 2
// 2
// 1 3
// 2
// 1 4
// 2
// 1 5
// 2
// 1 6
// 2
// 1 7
// 2
// 1 8
// 2
// 1 9
// 2
// 1 10
// 2
// 2 0
// 2
// 2 1
// 2
// 2 2
// 2
// 2 3
// 2
// 2 4
// 2
// 2 5
// 2
// 2 6
// 2
// 2 7
// 2
// 2 8
// 2
// 2 9
// 2
// 2 10
// 2
// 3 0
// 2
// 3 1
// 2
// 3 2
// 2
// 3 3
// 2
// 3 4
// 2
// 3 5
// 2
// 3 6
// 2
// 3 7
// 2
// 3 8
// 2
// 3 9
// 2
// 3 10
// 2
// 4 0
// 2
// 4 1
// 2
// ...
// Output
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 1
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 3
// 3
// 3
// 3
// 3
// 3
// 3
// 3
// 2
// 3
// 3
// 3
// 3
// 3
// 3
// 3
// 3
// 2
// 3
// 3...
// Answer
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// #include <bits/stdc++.h>
 
// using namespace std;
 
// #ifdef LOCAL
// #include "algo/debug.h"
// #else
// #define debug(...) 42
// #endif
 
// int main() {
//   ios::sync_with_stdio(false);
//   cin.tie(nullptr);
//   int tt;
//   cin >> tt;
//   while (tt--) {
//     int n;
//     cin >> n;
//     vector<int> a(n);
//     for (int i = 0; i < n; i++) {
//       cin >> a[i];
//     }
//     vector<vector<int>> at(n + 1);
//     for (int i = 0; i < n; i++) {
//       if (a[i] <= n) {
//         at[a[i]].push_back(i);
//       }
//     }
//     if (at[0].empty()) {
//       cout << n << '\n';
//       continue;
//     }
//     int ans = n - int(at[0].size());
//     vector<int> seq;
//     for (int i = 0; i < n; i++) {
//       if (a[i] > 0 || i == at[0][0]) {
//         seq.push_back(a[i]);
//       }
//     }
//     vector<bool> was(n + 1, false);
//     int mex = 0;
//     bool fail = false;
//     for (int i = int(seq.size()) - 1; i >= 0; i--) {
//       if (seq[i] < mex) {
//         fail = true;
//         break;
//       }
//       was[seq[i]] = true;
//       while (was[mex]) {
//         mex += 1;
//       }
//     }
//     if (!fail) {
//       ans += 1;
//     }
//     cout << ans << '\n';
//   }
//   return 0;
// }
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 1
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 2
// 3
int main() {
    string akusjfhuiukhqwiuehafskjbakhsfb;
    cout << "Enter text to encode: ";
    getline(cin, akusjfhuiukhqwiuehafskjbakhsfb);
    cout << "Encoded text: " << asjfbasjhbjhbhbjhbjsafjn(akusjfhuiukhqwiuehafskjbakhsfb) << endl;
    return 0;
}

