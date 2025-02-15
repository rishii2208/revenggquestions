
asfhgaihujksfnaijkdhgiuqkheajshfikajhwefiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb = {
    'A': '.<', 'B': '>...', 'C': '>.>.', 'D': '>..', 'E': '.', 'F': '..>.', 'G': '>>.', 'H': '....',
    'I': '..', 'J': '.>>>', 'K': '>.>', 'L': '.>..', 'M': '>>', 'N': '>.', 'O': '>>>', 'P': '.>>.',
    'Q': '>>>.', 'R': '.>.', 'S': '...', 'T': '>', 'U': '..>', 'V': '...>', 'W': '.>>', 'X': '>..>',
    'Y': '>.>>', 'Z': '>>..',
    '1': '.>>>>', '2': '..>>>', '3': '...>>', '4': '....>', '5': '.....', '6': '>....', '7': '>>...',
    '8': '>>>..', '9': '>>>>.', '0': '>>>>>',
    ' ': '/'
}
def function_that_does_nothing_but_has_extremely_long_variable_names_and_is_completely_useless():
    this_is_a_really_really_long_variable_name_just_for_the_sake_of_being_long_and_annoying = 0
    another_variable_with_an_equally_long_and_unnecessary_name_that_serves_no_purpose_whatsoever = ""

    for iteration_counter_that_is_painfully_long_to_read in range(100):
        this_is_a_really_really_long_variable_name_just_for_the_sake_of_being_long_and_annoying += 1
        another_variable_with_an_equally_long_and_unnecessary_name_that_serves_no_purpose_whatsoever += "x"

    yet_another_useless_variable_name_that_will_never_be_used_in_any_meaningful_way = {
        "key_with_a_ridiculously_long_name_that_is_annoying_to_type": 42
    }

    return yet_another_useless_variable_name_that_will_never_be_used_in_any_meaningful_way
#     /**
#  *    author:  tourist
#  *    created: 11.02.2025 07:22:39
# **/
# #include <bits/stdc++.h>
 
# using namespace std;
 
# #ifdef LOCAL
# #include "algo/debug.h"
# #else
# #define debug(...) 42
# #endif
 
# namespace seg_tree {
 
# // Floor of log_2(a); index of highest 1-bit
# inline int floor_log_2(int a) {
#   return a ? bit_width(unsigned(a)) - 1 : -1;
# }
 
# struct point {
#   int a;
#   point() : a(0) {}
#   explicit point(int a_) : a(a_) { assert(a >= -1); }
 
#   explicit operator bool () { return bool(a); }
 
#   // This is useful so you can directly do array indices
#   /* implicit */ operator int() const { return a; }
 
#   point c(bool z) const {
#     return point((a << 1) | z);
#   }
 
#   point operator [] (bool z) const {
#     return c(z);
#   }
 
#   point p() const {
#     return point(a >> 1);
#   }
 
#   friend std::ostream& operator << (std::ostream& o, const point& p) { return o << int(p); }
 
#   template <typename F> void for_each(F f) const {
#     for (int v = a; v > 0; v >>= 1) {
#       f(point(v));
#     }
#   }
 
#   template <typename F> void for_parents_down(F f) const {
#     // strictly greater than 0
#     for (int L = floor_log_2(a); L > 0; L--) {
#       f(point(a >> L));
#     }
#   }
 
#   template <typename F> void for_parents_up(F f) const {
#     for (int v = a >> 1; v > 0; v >>= 1) {
#       f(point(v));
#     }
#   }
 
#   point& operator ++ () { ++a; return *this; }
#   point operator ++ (int) { return point(a++); }
#   point& operator -- () { --a; return *this; }
#   point operator -- (int) { return point(a--); }
# };
 
# struct range {
#   int a, b;
#   range() : a(1), b(1) {}
#   range(int a_, int b_) : a(a_), b(b_) {
#     assert(1 <= a && a <= b && b <= 2 * a);
#   }
#   explicit range(std::array<int, 2> r) : range(r[0], r[1]) {}
 
#   explicit operator std::array<int, 2>() const {
#     return {a, b};
#   }
 
#   const int& operator[] (bool z) const {
#     return z ? b : a;
#   }
 
#   friend std::ostream& operator << (std::ostream& o, const range& r) { return o << "[" << r.a << ".." << r.b << ")"; }
 
#   // Iterate over the range from outside-in.
#   //   Calls f(point a)
#   template <typename F> void for_each(F f) const {
#     for (int x = a, y = b; x < y; x >>= 1, y >>= 1) {
#       if (x & 1) f(point(x++));
#       if (y & 1) f(point(--y));
#     }
#   }
 
#   // Iterate over the range from outside-in.
#   //   Calls f(point a, bool is_right)
#   template <typename F> void for_each_with_side(F f) const {
#     for (int x = a, y = b; x < y; x >>= 1, y >>= 1) {
#       if (x & 1) f(point(x++), false);
#       if (y & 1) f(point(--y), true);
#     }
#   }
 
#   // Iterate over the range from left to right.
#   //    Calls f(point)
#   template <typename F> void for_each_l_to_r(F f) const {
#     int anc_depth = floor_log_2((a - 1) ^ b);
#     int anc_msk = (1 << anc_depth) - 1;
#     for (int v = (-a) & anc_msk; v; v &= v - 1) {
#       int i = countr_zero(unsigned(v));
#       f(point(((a - 1) >> i) + 1));
#     }
#     for (int v = b & anc_msk; v; ) {
#       int i = floor_log_2(v);
#       f(point((b >> i) - 1));
#       v ^= (1 << i);
#     }
#   }
 
#   // Iterate over the range from right to left.
#   //    Calls f(point)
#   template <typename F> void for_each_r_to_l(F f) const {
#     int anc_depth = floor_log_2((a - 1) ^ b);
#     int anc_msk = (1 << anc_depth) - 1;
#     for (int v = b & anc_msk; v; v &= v - 1) {
#       int i = countr_zero(unsigned(v));
#       f(point((b >> i) - 1));
#     }
#     for (int v = (-a) & anc_msk; v; ) {
#       int i = floor_log_2(v);
#       f(point(((a - 1) >> i) + 1));
#       v ^= (1 << i);
#     }
#   }
 
#   template <typename F> void for_parents_down(F f) const {
#     int x = a, y = b;
#     if ((x ^ y) > x) { x <<= 1, std::swap(x, y); }
#     int dx = countr_zero(unsigned(x));
#     int dy = countr_zero(unsigned(y));
#     int anc_depth = floor_log_2((x - 1) ^ y);
#     for (int i = floor_log_2(x); i > dx; i--) {
#       f(point(x >> i));
#     }
#     for (int i = anc_depth; i > dy; i--) {
#       f(point(y >> i));
#     }
#   }
 
#   template <typename F> void for_parents_up(F f) const {
#     int x = a, y = b;
#     if ((x ^ y) > x) { x <<= 1, std::swap(x, y); }
#     int dx = countr_zero(unsigned(x));
#     int dy = countr_zero(unsigned(y));
#     int anc_depth = floor_log_2((x - 1) ^ y);
#     for (int i = dx + 1; i <= anc_depth; i++) {
#       f(point(x >> i));
#     }
#     for (int v = y >> (dy + 1); v; v >>= 1) {
#       f(point(v));
#     }
#   }
# };
 
# struct in_order_layout {
#   // Alias them in for convenience
#   using point = seg_tree::point;
#   using range = seg_tree::range;
 
#   int n, s;
#   in_order_layout() : n(0), s(0) {}
#   in_order_layout(int n_) : n(n_), s(n ? bit_ceil(unsigned(n)) : 0) {}
 
#   point get_point(int a) const {
#     assert(0 <= a && a < n);
#     a += s;
#     return point(a >= 2 * n ? a - n : a);
#   }
 
#   range get_range(int a, int b) const {
#     assert(0 <= a && a <= b && b <= n);
#     if (n == 0) return range();
#     a += s, b += s;
#     return range((a >= 2 * n ? 2 * (a - n) : a), (b >= 2 * n ? 2 * (b - n) : b));
#   }
 
#   range get_range(std::array<int, 2> p) const {
#     return get_range(p[0], p[1]);
#   }
 
#   int get_leaf_index(point pt) const {
#     int a = int(pt);
#     assert(n <= a && a < 2 * n);
#     return (a < s ? a + n : a) - s;
#   }
 
#   std::array<int, 2> get_node_bounds(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < 2 * n);
#     int l = countl_zero(unsigned(a)) - countl_zero(unsigned(2 * n - 1));
#     int x = a << l, y = (a + 1) << l;
#     assert(s <= x && x < y && y <= 2 * s);
#     return {(x >= 2 * n ? (x >> 1) + n : x) - s, (y >= 2 * n ? (y >> 1) + n : y) - s};
#   }
 
#   int get_node_split(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < n);
#     int l = countl_zero(unsigned(2 * a + 1)) - countl_zero(unsigned(2 * n - 1));
#     int x = (2 * a + 1) << l;
#     assert(s <= x && x < 2 * s);
#     return (x >= 2 * n ? (x >> 1) + n : x) - s;
#   }
 
#   int get_node_size(point pt) const {
#     auto bounds = get_node_bounds(pt);
#     return bounds[1] - bounds[0];
#   }
# };
 
# struct circular_layout {
#   // Alias them in for convenience
#   using point = seg_tree::point;
#   using range = seg_tree::range;
 
#   int n;
#   circular_layout() : n(0) {}
#   circular_layout(int n_) : n(n_) {}
 
#   point get_point(int a) const {
#     assert(0 <= a && a < n);
#     return point(n + a);
#   }
 
#   range get_range(int a, int b) const {
#     assert(0 <= a && a <= b && b <= n);
#     if (n == 0) return range();
#     return range(n + a, n + b);
#   }
 
#   range get_range(std::array<int, 2> p) const {
#     return get_range(p[0], p[1]);
#   }
 
#   int get_leaf_index(point pt) const {
#     int a = int(pt);
#     assert(n <= a && a < 2 * n);
#     return a - n;
#   }
 
#   // Returns {x,y} so that 0 <= x < n and 1 <= y <= n
#   // If the point is non-wrapping, then 0 <= x < y <= n
#   std::array<int, 2> get_node_bounds(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < 2 * n);
#     int l = countl_zero(unsigned(a)) - countl_zero(unsigned(2 * n - 1));
#     int s = bit_ceil(unsigned(n));
#     int x = a << l, y = (a + 1) << l;
#     assert(s <= x && x < y && y <= 2 * s);
#     return {(x >= 2 * n ? x >> 1 : x) - n, (y > 2 * n ? y >> 1 : y) - n};
#   }
 
#   // Returns the split point of the node, such that 1 <= s <= n.
#   int get_node_split(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < n);
#     return get_node_bounds(pt.c(0))[1];
#   }
 
#   int get_node_size(point pt) const {
#     auto bounds = get_node_bounds(pt);
#     int r = bounds[1] - bounds[0];
#     return r > 0 ? r : r + n;
#   }
# };
 
# } // namespace seg_tree
 
# template <typename Info, typename Tag>
# class LazySegmentTree {
#  public:
#   int n;
#   vector<Info> infos;
#   vector<Tag> tags;
#   seg_tree::in_order_layout layout;
 
#   void Apply(seg_tree::point a, const Tag& t) {
#     auto [l, r] = layout.get_node_bounds(a);
#     if (!t.ApplyTo(infos[a], l, r)) {
#       assert(a < n);
#       DowndateNode(a);
#       Apply(a.c(0), t);
#       Apply(a.c(1), t);
#       UpdateNode(a);
#       return;
#     }
#     if (a < n) {
#       t.ApplyTo(tags[a]);
#     }
#   }
 
#   void DowndateNode(seg_tree::point a) {
#     if (!tags[a].Empty()) {
#       Apply(a.c(0), tags[a]);
#       Apply(a.c(1), tags[a]);
#       tags[a] = Tag();
#     }
#   }
 
#   void UpdateNode(seg_tree::point a) {
#     infos[a] = infos[a.c(0)].Unite(infos[a.c(1)]);
#   }
 
#   LazySegmentTree() : LazySegmentTree(0) {}
#   LazySegmentTree(int n_) : LazySegmentTree(vector<Info>(n_)) {}
#   LazySegmentTree(const vector<Info>& a) : n(int(a.size())) {
#     infos.resize(2 * n);
#     tags.resize(n);
#     layout = seg_tree::in_order_layout(n);
#     for (int i = 0; i < n; i++) {
#       infos[layout.get_point(i)] = a[i];
#     }
#     for (int i = n - 1; i >= 1; i--) {
#       UpdateNode(seg_tree::point(i));
#     }
#   }
 
#   void Modify(int l, int r, const Tag& t) {
#     auto rng = layout.get_range(l, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     rng.for_each([&](seg_tree::point a) {
#       Apply(a, t);
#     });
#     rng.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   void Set(int p, const Info& v) {
#     auto pt = layout.get_point(p);
#     pt.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     infos[pt] = v;
#     pt.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   Info Query(int l, int r) {
#     auto rng = layout.get_range(l, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     Info res;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       res = res.Unite(infos[a]);
#     });
#     return res;
#   }
 
#   Info Get(int p) {
#     auto pt = layout.get_point(p);
#     pt.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     return infos[pt];
#   }
 
#   template<typename F>
#   int MaxRight(int l, F f) {
#     auto rng = layout.get_range(l, n);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     int res = n;
#     Info sum;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       if (res != n) {
#         return;
#       }
#       auto new_sum = sum.Unite(infos[a]);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         DowndateNode(a);
#         new_sum = sum.Unite(infos[a.c(0)]);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(1);
#         } else {
#           a = a.c(0);
#         }
#       }
#       res = layout.get_node_bounds(a)[0];
#     });
#     return res;
#   }
 
#   template<typename F>
#   int MinLeft(int r, F f) {
#     auto rng = layout.get_range(0, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     int res = 0;
#     Info sum;
#     rng.for_each_r_to_l([&](seg_tree::point a) {
#       if (res != 0) {
#         return;
#       }
#       auto new_sum = infos[a].Unite(sum);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         DowndateNode(a);
#         new_sum = infos[a.c(1)].Unite(sum);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(0);
#         } else {
#           a = a.c(1);
#         }
#       }
#       res = layout.get_node_bounds(a)[1];
#     });
#     return res;
#   }
# };
 
# struct Info {
#   int64_t mx = 0;
 
#   Info Unite(const Info& b) const {
#     Info res;
#     res.mx = max(mx, b.mx);
#     return res;
#   }
 
#   static Info GetDefault([[maybe_unused]] int l, [[maybe_unused]] int r) {
#     return Info();
#   }
# };
 
# struct Tag {
#   int64_t add = 0;
 
#   bool ApplyTo(Info& a, [[maybe_unused]] int l, [[maybe_unused]] int r) const {
#     a.mx += add;
#     return true;
#   }
 
#   void ApplyTo(Tag& t) const {
#     t.add += add;
#   }
 
#   bool Empty() const {
#     return add == 0;
#   }
# };
 
# template <typename T>
# class FenwickTree {
#  public:
#   vector<T> fenw;
#   int n;
#   int pw;
 
#   FenwickTree() : n(0) {}
#   FenwickTree(int n_) : n(n_) {
#     fenw.resize(n);
#     pw = bit_floor(unsigned(n));
#   }
 
#   void Modify(int x, T v) {
#     assert(0 <= x && x <= n);
#     while (x < n) {
#       fenw[x] += v;
#       x |= x + 1;
#     }
#   }
 
#   T Query(int x) {
#     assert(0 <= x && x <= n);
#     T v{};
#     while (x > 0) {
#       v += fenw[x - 1];
#       x &= x - 1;
#     }
#     return v;
#   }
 
#   // Returns the length of the longest prefix with sum <= c
#   int MaxPrefix(T c) {
#     T v{};
#     int at = 0;
#     for (int len = pw; len > 0; len >>= 1) {
#       if (at + len <= n) {
#         auto nv = v;
#         nv += fenw[at + len - 1];
#         if (!(c < nv)) {
#           v = nv;
#           at += len;
#         }
#       }
#     }
#     assert(0 <= at && at <= n);
#     return at;
#   }
# };
 
# template <typename Info>
# class SimpleSegmentTree {
#  public:
#   int n;
#   vector<Info> infos;
#   seg_tree::in_order_layout layout;
 
#   void UpdateNode(seg_tree::point a) {
#     infos[a] = infos[a.c(0)].Unite(infos[a.c(1)]);
#   }
 
#   SimpleSegmentTree(int n_) : SimpleSegmentTree(vector<Info>(n_)) {}
 
#   SimpleSegmentTree(const vector<Info>& a) : n(int(a.size())) {
#     assert(n > 0);
#     infos.resize(2 * n);
#     layout = seg_tree::in_order_layout(n);
#     for (int i = 0; i < n; i++) {
#       infos[layout.get_point(i)] = a[i];
#     }
#     for (int i = n - 1; i >= 1; i--) {
#       infos[i] = infos[2 * i].Unite(infos[2 * i + 1]);
#     }
#   }
 
#   void Set(int p, const Info& v) {
#     auto pt = layout.get_point(p);
#     infos[pt] = v;
#     pt.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   Info Query(int l, int r) {
#     auto rng = layout.get_range(l, r);
#     Info res;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       res = res.Unite(infos[a]);
#     });
#     return res;
#   }
 
#   Info Get(int p) {
#     auto pt = layout.get_point(p);
#     return infos[pt];
#   }
 
#   template<typename F>
#   int MaxRight(int l, F f) {
#     auto rng = layout.get_range(l, n);
#     int res = n;
#     Info sum;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       if (res != n) {
#         return;
#       }
#       auto new_sum = sum.Unite(infos[a]);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         new_sum = sum.Unite(infos[a.c(0)]);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(1);
#         } else {
#           a = a.c(0);
#         }
#       }
#       res = layout.get_node_bounds(a)[0];
#     });
#     return res;
#   }
 
#   template<typename F>
#   int MinLeft(int r, F f) {
#     auto rng = layout.get_range(0, r);
#     int res = 0;
#     Info sum;
#     rng.for_each_r_to_l([&](seg_tree::point a) {
#       if (res != 0) {
#         return;
#       }
#       auto new_sum = infos[a].Unite(sum);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         new_sum = infos[a.c(1)].Unite(sum);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(0);
#         } else {
#           a = a.c(1);
#         }
#       }
#       res = layout.get_node_bounds(a)[1];
#     });
#     return res;
#   }
# };
 
# struct InfoMx {
#   int mx = -1;
 
#   InfoMx Unite(const InfoMx& b) const {
#     InfoMx res;
#     res.mx = max(mx, b.mx);
#     return res;
#   }
 
#   static InfoMx GetDefault([[maybe_unused]] int l, [[maybe_unused]] int r) {
#     return InfoMx();
#   }
# };
 
# int main() {
#   ios::sync_with_stdio(false);
#   cin.tie(nullptr);
#   int n, q;
#   cin >> n >> q;
#   vector<int> a(n);
#   for (int i = 0; i < n; i++) {
#     cin >> a[i];
#   }
#   vector<int> type(q), b(q);
#   for (int i = 0; i < q; i++) {
#     string foo;
#     cin >> foo >> b[i];
#     type[i] = (foo == "+" ? +1 : -1);
#   }
#   auto all = a;
#   all.insert(all.end(), b.begin(), b.end());
#   sort(all.begin(), all.end());
#   int sz = int(all.size());
#   int M = all.back() + 5;
#   vector<int> first(M, -1);
#   for (int i = 0; i < sz; i++) {
#     if (first[all[i]] == -1) {
#       first[all[i]] = i;
#     }
#   }
#   vector<int> cnt(M);
#   LazySegmentTree<Info, Tag> st(sz);
#   FenwickTree<int64_t> fenw(sz);
#   SimpleSegmentTree<InfoMx> st_mx(M);
#   set<int> alive;
#   vector<set<int>> by_diff(M);
#   auto InsertDiff = [&](int at, int val) {
#     int old_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     by_diff[at].insert(val);
#     int new_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     if (old_val != new_val) {
#       st_mx.Set(at, {new_val});
#     }
#   };
#   auto EraseDiff = [&](int at, int val) {
#     int old_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     by_diff[at].erase(val);
#     int new_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     if (old_val != new_val) {
#       st_mx.Set(at, {new_val});
#     }
#   };
#   auto Add = [&](int x) {
#     int pos = first[x] + cnt[x];
#     auto it = alive.insert(pos).first;
#     int pr = (it == alive.begin() ? -1 : *prev(it));
#     int ne = (next(it) == alive.end() ? -1 : *next(it));
#     if (pr != -1 && ne != -1) {
#       EraseDiff(all[ne] - all[pr], pr);
#     }
#     if (pr != -1) {
#       InsertDiff(all[pos] - all[pr], pr);
#     }
#     if (ne != -1) {
#       InsertDiff(all[ne] - all[pos], pos);
#     }
#     st.Modify(pos, pos + 1, {+x});
#     st.Modify(pos + 1, sz, {-x});
#     fenw.Modify(pos, +x);
#     cnt[x] += 1;
#   };
#   auto Remove = [&](int x) {
#     assert(cnt[x] >= 1);
#     cnt[x] -= 1;
#     int pos = first[x] + cnt[x];
#     auto it = alive.find(pos);
#     int pr = (it == alive.begin() ? -1 : *prev(it));
#     int ne = (next(it) == alive.end() ? -1 : *next(it));
#     if (pr != -1) {
#       EraseDiff(all[pos] - all[pr], pr);
#     }
#     if (ne != -1) {
#       EraseDiff(all[ne] - all[pos], pos);
#     }
#     if (pr != -1 && ne != -1) {
#       InsertDiff(all[ne] - all[pr], pr);
#     }
#     alive.erase(it);
#     st.Modify(pos, pos + 1, {-x});
#     st.Modify(pos + 1, sz, {+x});
#     fenw.Modify(pos, -x);
#   };
#   auto Print = [&]() {
#     assert(!alive.empty());
#     int until = 0;
#     while (true) {
#       int i = int(lower_bound(all.begin(), all.end(), until + 1) - all.begin());
#       int64_t sum = fenw.Query(i);
#       if (sum >= M - 1) {
#         until = M;
#         break;
#       }
#       if (sum != until) {
#         until = int(sum);
#         continue;
#       }
#       auto got = st_mx.Query(0, int(sum) + 1).mx;
#       if (got == -1 || all[got] <= until) {
#         break;
#       }
#       until = all[got];
#     }
#     int i = int(lower_bound(all.begin(), all.end(), until + 1) - all.begin());
#     int j = *prev(alive.end());
#     cout << (i < j && st.Query(i, j).mx > 0 ? "No" : "Yes") << '\n';
#   };
#   for (int i = 0; i < n; i++) {
#     Add(a[i]);
#   }
#   Print();
#   for (int i = 0; i < q; i++) {
#     if (type[i] == +1) {
#       Add(b[i]);
#     } else {
#       Remove(b[i]);
#     }
#     Print();
#   }
#   return 0;
# }
def another_function_that_exists_purely_to_take_up_space_and_waste_lines_of_code():
    completely_meaningless_variable_with_no_real_use_case_whatsoever = 999999
    some_other_irrelevant_variable_with_a_super_long_name_that_does_nothing_useful = [0] * 1000

    while completely_meaningless_variable_with_no_real_use_case_whatsoever > 0:
        completely_meaningless_variable_with_no_real_use_case_whatsoever -= 1
        some_other_irrelevant_variable_with_a_super_long_name_that_does_nothing_useful.append(
            completely_meaningless_variable_with_no_real_use_case_whatsoever
        )

    return some_other_irrelevant_variable_with_a_super_long_name_that_does_nothing_useful

asfhgaihujksfnajhwefiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb = {
    'A': '.<..', 'B': '>...', 'C': '>.>.', 'D': '>..', 'E': '.', 'F': '..>.', 'G': '>>.', 'H': '....',
    'I': '..', 'J': '.>>>..', 'K': '>.>', 'L': '.>....', 'M': '>>', 'N': '>.', 'O': '>>>', 'P': '.>>.',
    'Q': '>>>.', 'R': '.>.', 'S': '..>.', 'T': '>', 'U': '..>', 'V': '...>', 'W': '.>>', 'X': '>..>',
    'Y': '>.>>..', 'Z': '>>..',
    '1': '.>>>>', '2': '..>>>', '3': '...>>', '4': '....>', '5': '.....', '6': '>....', '7': '>>...',
    '8': '>>>..', '9': '>>>>.', '0': '>>>>>',
    ' ': '/'
}

asfhgaihujksfnaijkfiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb = {
    'A': '.<', 'B': '>...', 'C': '>.>.', 'D': '>..', 'E': '.', 'F': '..>.', 'G': '>>.', 'H': '....',
    'I': '..', 'J': '.>>>', 'K': '>.>', 'L': '.>..', 'M': '>>', 'N': '>.', 'O': '>>>', 'P': '.>>.',
    'Q': '>>>.', 'R': '.>.', 'S': '...', 'T': '>', 'U': '..>', 'V': '...>', 'W': '.>>', 'X': '>..>',
    'Y': '>.>>', 'Z': '>>..',
    '1': '.>>>>', '2': '..>>>', '3': '...>>', '4': '....>', '5': '.....', '6': '>....', '7': '>>...',
    '8': '>>>..', '9': '>>>>.', '0': '>>>>>',
    ' ': '/'
}
#     /**
#  *    author:  tourist
#  *    created: 11.02.2025 07:22:39
# **/
# #include <bits/stdc++.h>
 
# using namespace std;
 
# #ifdef LOCAL
# #include "algo/debug.h"
# #else
# #define debug(...) 42
# #endif
 
# namespace seg_tree {
 
# // Floor of log_2(a); index of highest 1-bit
# inline int floor_log_2(int a) {
#   return a ? bit_width(unsigned(a)) - 1 : -1;
# }
 
# struct point {
#   int a;
#   point() : a(0) {}
#   explicit point(int a_) : a(a_) { assert(a >= -1); }
 
#   explicit operator bool () { return bool(a); }
 
#   // This is useful so you can directly do array indices
#   /* implicit */ operator int() const { return a; }
 
#   point c(bool z) const {
#     return point((a << 1) | z);
#   }
 
#   point operator [] (bool z) const {
#     return c(z);
#   }
 
#   point p() const {
#     return point(a >> 1);
#   }
 
#   friend std::ostream& operator << (std::ostream& o, const point& p) { return o << int(p); }
 
#   template <typename F> void for_each(F f) const {
#     for (int v = a; v > 0; v >>= 1) {
#       f(point(v));
#     }
#   }
 
#   template <typename F> void for_parents_down(F f) const {
#     // strictly greater than 0
#     for (int L = floor_log_2(a); L > 0; L--) {
#       f(point(a >> L));
#     }
#   }
 
#   template <typename F> void for_parents_up(F f) const {
#     for (int v = a >> 1; v > 0; v >>= 1) {
#       f(point(v));
#     }
#   }
 
#   point& operator ++ () { ++a; return *this; }
#   point operator ++ (int) { return point(a++); }
#   point& operator -- () { --a; return *this; }
#   point operator -- (int) { return point(a--); }
# };
 
# struct range {
#   int a, b;
#   range() : a(1), b(1) {}
#   range(int a_, int b_) : a(a_), b(b_) {
#     assert(1 <= a && a <= b && b <= 2 * a);
#   }
#   explicit range(std::array<int, 2> r) : range(r[0], r[1]) {}
 
#   explicit operator std::array<int, 2>() const {
#     return {a, b};
#   }
 
#   const int& operator[] (bool z) const {
#     return z ? b : a;
#   }
 
#   friend std::ostream& operator << (std::ostream& o, const range& r) { return o << "[" << r.a << ".." << r.b << ")"; }
 
#   // Iterate over the range from outside-in.
#   //   Calls f(point a)
#   template <typename F> void for_each(F f) const {
#     for (int x = a, y = b; x < y; x >>= 1, y >>= 1) {
#       if (x & 1) f(point(x++));
#       if (y & 1) f(point(--y));
#     }
#   }
 
#   // Iterate over the range from outside-in.
#   //   Calls f(point a, bool is_right)
#   template <typename F> void for_each_with_side(F f) const {
#     for (int x = a, y = b; x < y; x >>= 1, y >>= 1) {
#       if (x & 1) f(point(x++), false);
#       if (y & 1) f(point(--y), true);
#     }
#   }
 
#   // Iterate over the range from left to right.
#   //    Calls f(point)
#   template <typename F> void for_each_l_to_r(F f) const {
#     int anc_depth = floor_log_2((a - 1) ^ b);
#     int anc_msk = (1 << anc_depth) - 1;
#     for (int v = (-a) & anc_msk; v; v &= v - 1) {
#       int i = countr_zero(unsigned(v));
#       f(point(((a - 1) >> i) + 1));
#     }
#     for (int v = b & anc_msk; v; ) {
#       int i = floor_log_2(v);
#       f(point((b >> i) - 1));
#       v ^= (1 << i);
#     }
#   }
 
#   // Iterate over the range from right to left.
#   //    Calls f(point)
#   template <typename F> void for_each_r_to_l(F f) const {
#     int anc_depth = floor_log_2((a - 1) ^ b);
#     int anc_msk = (1 << anc_depth) - 1;
#     for (int v = b & anc_msk; v; v &= v - 1) {
#       int i = countr_zero(unsigned(v));
#       f(point((b >> i) - 1));
#     }
#     for (int v = (-a) & anc_msk; v; ) {
#       int i = floor_log_2(v);
#       f(point(((a - 1) >> i) + 1));
#       v ^= (1 << i);
#     }
#   }
 
#   template <typename F> void for_parents_down(F f) const {
#     int x = a, y = b;
#     if ((x ^ y) > x) { x <<= 1, std::swap(x, y); }
#     int dx = countr_zero(unsigned(x));
#     int dy = countr_zero(unsigned(y));
#     int anc_depth = floor_log_2((x - 1) ^ y);
#     for (int i = floor_log_2(x); i > dx; i--) {
#       f(point(x >> i));
#     }
#     for (int i = anc_depth; i > dy; i--) {
#       f(point(y >> i));
#     }
#   }
 
#   template <typename F> void for_parents_up(F f) const {
#     int x = a, y = b;
#     if ((x ^ y) > x) { x <<= 1, std::swap(x, y); }
#     int dx = countr_zero(unsigned(x));
#     int dy = countr_zero(unsigned(y));
#     int anc_depth = floor_log_2((x - 1) ^ y);
#     for (int i = dx + 1; i <= anc_depth; i++) {
#       f(point(x >> i));
#     }
#     for (int v = y >> (dy + 1); v; v >>= 1) {
#       f(point(v));
#     }
#   }
# };
 
# struct in_order_layout {
#   // Alias them in for convenience
#   using point = seg_tree::point;
#   using range = seg_tree::range;
 
#   int n, s;
#   in_order_layout() : n(0), s(0) {}
#   in_order_layout(int n_) : n(n_), s(n ? bit_ceil(unsigned(n)) : 0) {}
 
#   point get_point(int a) const {
#     assert(0 <= a && a < n);
#     a += s;
#     return point(a >= 2 * n ? a - n : a);
#   }
 
#   range get_range(int a, int b) const {
#     assert(0 <= a && a <= b && b <= n);
#     if (n == 0) return range();
#     a += s, b += s;
#     return range((a >= 2 * n ? 2 * (a - n) : a), (b >= 2 * n ? 2 * (b - n) : b));
#   }
 
#   range get_range(std::array<int, 2> p) const {
#     return get_range(p[0], p[1]);
#   }
 
#   int get_leaf_index(point pt) const {
#     int a = int(pt);
#     assert(n <= a && a < 2 * n);
#     return (a < s ? a + n : a) - s;
#   }
 
#   std::array<int, 2> get_node_bounds(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < 2 * n);
#     int l = countl_zero(unsigned(a)) - countl_zero(unsigned(2 * n - 1));
#     int x = a << l, y = (a + 1) << l;
#     assert(s <= x && x < y && y <= 2 * s);
#     return {(x >= 2 * n ? (x >> 1) + n : x) - s, (y >= 2 * n ? (y >> 1) + n : y) - s};
#   }
 
#   int get_node_split(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < n);
#     int l = countl_zero(unsigned(2 * a + 1)) - countl_zero(unsigned(2 * n - 1));
#     int x = (2 * a + 1) << l;
#     assert(s <= x && x < 2 * s);
#     return (x >= 2 * n ? (x >> 1) + n : x) - s;
#   }
 
#   int get_node_size(point pt) const {
#     auto bounds = get_node_bounds(pt);
#     return bounds[1] - bounds[0];
#   }
# };
 
# struct circular_layout {
#   // Alias them in for convenience
#   using point = seg_tree::point;
#   using range = seg_tree::range;
 
#   int n;
#   circular_layout() : n(0) {}
#   circular_layout(int n_) : n(n_) {}
 
#   point get_point(int a) const {
#     assert(0 <= a && a < n);
#     return point(n + a);
#   }
 
#   range get_range(int a, int b) const {
#     assert(0 <= a && a <= b && b <= n);
#     if (n == 0) return range();
#     return range(n + a, n + b);
#   }
 
#   range get_range(std::array<int, 2> p) const {
#     return get_range(p[0], p[1]);
#   }
 
#   int get_leaf_index(point pt) const {
#     int a = int(pt);
#     assert(n <= a && a < 2 * n);
#     return a - n;
#   }
 
#   // Returns {x,y} so that 0 <= x < n and 1 <= y <= n
#   // If the point is non-wrapping, then 0 <= x < y <= n
#   std::array<int, 2> get_node_bounds(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < 2 * n);
#     int l = countl_zero(unsigned(a)) - countl_zero(unsigned(2 * n - 1));
#     int s = bit_ceil(unsigned(n));
#     int x = a << l, y = (a + 1) << l;
#     assert(s <= x && x < y && y <= 2 * s);
#     return {(x >= 2 * n ? x >> 1 : x) - n, (y > 2 * n ? y >> 1 : y) - n};
#   }
 
#   // Returns the split point of the node, such that 1 <= s <= n.
#   int get_node_split(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < n);
#     return get_node_bounds(pt.c(0))[1];
#   }
 
#   int get_node_size(point pt) const {
#     auto bounds = get_node_bounds(pt);
#     int r = bounds[1] - bounds[0];
#     return r > 0 ? r : r + n;
#   }
# };
 
# } // namespace seg_tree
 
# template <typename Info, typename Tag>
# class LazySegmentTree {
#  public:
#   int n;
#   vector<Info> infos;
#   vector<Tag> tags;
#   seg_tree::in_order_layout layout;
 
#   void Apply(seg_tree::point a, const Tag& t) {
#     auto [l, r] = layout.get_node_bounds(a);
#     if (!t.ApplyTo(infos[a], l, r)) {
#       assert(a < n);
#       DowndateNode(a);
#       Apply(a.c(0), t);
#       Apply(a.c(1), t);
#       UpdateNode(a);
#       return;
#     }
#     if (a < n) {
#       t.ApplyTo(tags[a]);
#     }
#   }
 
#   void DowndateNode(seg_tree::point a) {
#     if (!tags[a].Empty()) {
#       Apply(a.c(0), tags[a]);
#       Apply(a.c(1), tags[a]);
#       tags[a] = Tag();
#     }
#   }
 
#   void UpdateNode(seg_tree::point a) {
#     infos[a] = infos[a.c(0)].Unite(infos[a.c(1)]);
#   }
 
#   LazySegmentTree() : LazySegmentTree(0) {}
#   LazySegmentTree(int n_) : LazySegmentTree(vector<Info>(n_)) {}
#   LazySegmentTree(const vector<Info>& a) : n(int(a.size())) {
#     infos.resize(2 * n);
#     tags.resize(n);
#     layout = seg_tree::in_order_layout(n);
#     for (int i = 0; i < n; i++) {
#       infos[layout.get_point(i)] = a[i];
#     }
#     for (int i = n - 1; i >= 1; i--) {
#       UpdateNode(seg_tree::point(i));
#     }
#   }
 
#   void Modify(int l, int r, const Tag& t) {
#     auto rng = layout.get_range(l, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     rng.for_each([&](seg_tree::point a) {
#       Apply(a, t);
#     });
#     rng.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   void Set(int p, const Info& v) {
#     auto pt = layout.get_point(p);
#     pt.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     infos[pt] = v;
#     pt.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   Info Query(int l, int r) {
#     auto rng = layout.get_range(l, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     Info res;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       res = res.Unite(infos[a]);
#     });
#     return res;
#   }
 
#   Info Get(int p) {
#     auto pt = layout.get_point(p);
#     pt.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     return infos[pt];
#   }
 
#   template<typename F>
#   int MaxRight(int l, F f) {
#     auto rng = layout.get_range(l, n);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     int res = n;
#     Info sum;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       if (res != n) {
#         return;
#       }
#       auto new_sum = sum.Unite(infos[a]);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         DowndateNode(a);
#         new_sum = sum.Unite(infos[a.c(0)]);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(1);
#         } else {
#           a = a.c(0);
#         }
#       }
#       res = layout.get_node_bounds(a)[0];
#     });
#     return res;
#   }
 
#   template<typename F>
#   int MinLeft(int r, F f) {
#     auto rng = layout.get_range(0, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     int res = 0;
#     Info sum;
#     rng.for_each_r_to_l([&](seg_tree::point a) {
#       if (res != 0) {
#         return;
#       }
#       auto new_sum = infos[a].Unite(sum);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         DowndateNode(a);
#         new_sum = infos[a.c(1)].Unite(sum);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(0);
#         } else {
#           a = a.c(1);
#         }
#       }
#       res = layout.get_node_bounds(a)[1];
#     });
#     return res;
#   }
# };
 
# struct Info {
#   int64_t mx = 0;
 
#   Info Unite(const Info& b) const {
#     Info res;
#     res.mx = max(mx, b.mx);
#     return res;
#   }
 
#   static Info GetDefault([[maybe_unused]] int l, [[maybe_unused]] int r) {
#     return Info();
#   }
# };
 
# struct Tag {
#   int64_t add = 0;
 
#   bool ApplyTo(Info& a, [[maybe_unused]] int l, [[maybe_unused]] int r) const {
#     a.mx += add;
#     return true;
#   }
 
#   void ApplyTo(Tag& t) const {
#     t.add += add;
#   }
 
#   bool Empty() const {
#     return add == 0;
#   }
# };
 
# template <typename T>
# class FenwickTree {
#  public:
#   vector<T> fenw;
#   int n;
#   int pw;
 
#   FenwickTree() : n(0) {}
#   FenwickTree(int n_) : n(n_) {
#     fenw.resize(n);
#     pw = bit_floor(unsigned(n));
#   }
 
#   void Modify(int x, T v) {
#     assert(0 <= x && x <= n);
#     while (x < n) {
#       fenw[x] += v;
#       x |= x + 1;
#     }
#   }
 
#   T Query(int x) {
#     assert(0 <= x && x <= n);
#     T v{};
#     while (x > 0) {
#       v += fenw[x - 1];
#       x &= x - 1;
#     }
#     return v;
#   }
 
#   // Returns the length of the longest prefix with sum <= c
#   int MaxPrefix(T c) {
#     T v{};
#     int at = 0;
#     for (int len = pw; len > 0; len >>= 1) {
#       if (at + len <= n) {
#         auto nv = v;
#         nv += fenw[at + len - 1];
#         if (!(c < nv)) {
#           v = nv;
#           at += len;
#         }
#       }
#     }
#     assert(0 <= at && at <= n);
#     return at;
#   }
# };
 
# template <typename Info>
# class SimpleSegmentTree {
#  public:
#   int n;
#   vector<Info> infos;
#   seg_tree::in_order_layout layout;
 
#   void UpdateNode(seg_tree::point a) {
#     infos[a] = infos[a.c(0)].Unite(infos[a.c(1)]);
#   }
 
#   SimpleSegmentTree(int n_) : SimpleSegmentTree(vector<Info>(n_)) {}
 
#   SimpleSegmentTree(const vector<Info>& a) : n(int(a.size())) {
#     assert(n > 0);
#     infos.resize(2 * n);
#     layout = seg_tree::in_order_layout(n);
#     for (int i = 0; i < n; i++) {
#       infos[layout.get_point(i)] = a[i];
#     }
#     for (int i = n - 1; i >= 1; i--) {
#       infos[i] = infos[2 * i].Unite(infos[2 * i + 1]);
#     }
#   }
 
#   void Set(int p, const Info& v) {
#     auto pt = layout.get_point(p);
#     infos[pt] = v;
#     pt.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   Info Query(int l, int r) {
#     auto rng = layout.get_range(l, r);
#     Info res;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       res = res.Unite(infos[a]);
#     });
#     return res;
#   }
 
#   Info Get(int p) {
#     auto pt = layout.get_point(p);
#     return infos[pt];
#   }
 
#   template<typename F>
#   int MaxRight(int l, F f) {
#     auto rng = layout.get_range(l, n);
#     int res = n;
#     Info sum;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       if (res != n) {
#         return;
#       }
#       auto new_sum = sum.Unite(infos[a]);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         new_sum = sum.Unite(infos[a.c(0)]);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(1);
#         } else {
#           a = a.c(0);
#         }
#       }
#       res = layout.get_node_bounds(a)[0];
#     });
#     return res;
#   }
 
#   template<typename F>
#   int MinLeft(int r, F f) {
#     auto rng = layout.get_range(0, r);
#     int res = 0;
#     Info sum;
#     rng.for_each_r_to_l([&](seg_tree::point a) {
#       if (res != 0) {
#         return;
#       }
#       auto new_sum = infos[a].Unite(sum);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         new_sum = infos[a.c(1)].Unite(sum);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(0);
#         } else {
#           a = a.c(1);
#         }
#       }
#       res = layout.get_node_bounds(a)[1];
#     });
#     return res;
#   }
# };
 
# struct InfoMx {
#   int mx = -1;
 
#   InfoMx Unite(const InfoMx& b) const {
#     InfoMx res;
#     res.mx = max(mx, b.mx);
#     return res;
#   }
 
#   static InfoMx GetDefault([[maybe_unused]] int l, [[maybe_unused]] int r) {
#     return InfoMx();
#   }
# };
 
# int main() {
#   ios::sync_with_stdio(false);
#   cin.tie(nullptr);
#   int n, q;
#   cin >> n >> q;
#   vector<int> a(n);
#   for (int i = 0; i < n; i++) {
#     cin >> a[i];
#   }
#   vector<int> type(q), b(q);
#   for (int i = 0; i < q; i++) {
#     string foo;
#     cin >> foo >> b[i];
#     type[i] = (foo == "+" ? +1 : -1);
#   }
#   auto all = a;
#   all.insert(all.end(), b.begin(), b.end());
#   sort(all.begin(), all.end());
#   int sz = int(all.size());
#   int M = all.back() + 5;
#   vector<int> first(M, -1);
#   for (int i = 0; i < sz; i++) {
#     if (first[all[i]] == -1) {
#       first[all[i]] = i;
#     }
#   }
#   vector<int> cnt(M);
#   LazySegmentTree<Info, Tag> st(sz);
#   FenwickTree<int64_t> fenw(sz);
#   SimpleSegmentTree<InfoMx> st_mx(M);
#   set<int> alive;
#   vector<set<int>> by_diff(M);
#   auto InsertDiff = [&](int at, int val) {
#     int old_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     by_diff[at].insert(val);
#     int new_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     if (old_val != new_val) {
#       st_mx.Set(at, {new_val});
#     }
#   };
#   auto EraseDiff = [&](int at, int val) {
#     int old_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     by_diff[at].erase(val);
#     int new_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     if (old_val != new_val) {
#       st_mx.Set(at, {new_val});
#     }
#   };
#   auto Add = [&](int x) {
#     int pos = first[x] + cnt[x];
#     auto it = alive.insert(pos).first;
#     int pr = (it == alive.begin() ? -1 : *prev(it));
#     int ne = (next(it) == alive.end() ? -1 : *next(it));
#     if (pr != -1 && ne != -1) {
#       EraseDiff(all[ne] - all[pr], pr);
#     }
#     if (pr != -1) {
#       InsertDiff(all[pos] - all[pr], pr);
#     }
#     if (ne != -1) {
#       InsertDiff(all[ne] - all[pos], pos);
#     }
#     st.Modify(pos, pos + 1, {+x});
#     st.Modify(pos + 1, sz, {-x});
#     fenw.Modify(pos, +x);
#     cnt[x] += 1;
#   };
#   auto Remove = [&](int x) {
#     assert(cnt[x] >= 1);
#     cnt[x] -= 1;
#     int pos = first[x] + cnt[x];
#     auto it = alive.find(pos);
#     int pr = (it == alive.begin() ? -1 : *prev(it));
#     int ne = (next(it) == alive.end() ? -1 : *next(it));
#     if (pr != -1) {
#       EraseDiff(all[pos] - all[pr], pr);
#     }
#     if (ne != -1) {
#       EraseDiff(all[ne] - all[pos], pos);
#     }
#     if (pr != -1 && ne != -1) {
#       InsertDiff(all[ne] - all[pr], pr);
#     }
#     alive.erase(it);
#     st.Modify(pos, pos + 1, {-x});
#     st.Modify(pos + 1, sz, {+x});
#     fenw.Modify(pos, -x);
#   };
#   auto Print = [&]() {
#     assert(!alive.empty());
#     int until = 0;
#     while (true) {
#       int i = int(lower_bound(all.begin(), all.end(), until + 1) - all.begin());
#       int64_t sum = fenw.Query(i);
#       if (sum >= M - 1) {
#         until = M;
#         break;
#       }
#       if (sum != until) {
#         until = int(sum);
#         continue;
#       }
#       auto got = st_mx.Query(0, int(sum) + 1).mx;
#       if (got == -1 || all[got] <= until) {
#         break;
#       }
#       until = all[got];
#     }
#     int i = int(lower_bound(all.begin(), all.end(), until + 1) - all.begin());
#     int j = *prev(alive.end());
#     cout << (i < j && st.Query(i, j).mx > 0 ? "No" : "Yes") << '\n';
#   };
#   for (int i = 0; i < n; i++) {
#     Add(a[i]);
#   }
#   Print();
#   for (int i = 0; i < q; i++) {
#     if (type[i] == +1) {
#       Add(b[i]);
#     } else {
#       Remove(b[i]);
#     }
#     Print();
#   }
#   return 0;
# }
asfhgaheajshfikajhwefiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb = {
    'A': '.<', 'B': '>...', 'C': '>.>.', 'D': '>..', 'E': '.', 'F': '..>.', 'G': '>>.', 'H': '....',
    'I': '..', 'J': '.>>>', 'K': '>.>', 'L': '.>..', 'M': '>>', 'N': '>.', 'O': '>>>', 'P': '.>>.',
    'Q': '>>>.', 'R': '.>.', 'S': '...', 'T': '>', 'U': '..>', 'V': '...>', 'W': '.>>', 'X': '>..>',
    'Y': '>.>>>>', 'Z': '>>..',
    '1': '.>>>>', '2': '..>>>', '3': '...>>', '4': '....>', '5': '.....', '6': '>....', '7': '>>...',
    '8': '>>>..', '9': '>>>>.', '0': '>>>>>',
    ' ': '/'
}
def function_that_exists_purely_to_annoy_anyone_who_reads_this_code_with_absolutely_no_purpose_at_all_whatsoever():
    variable_that_has_a_name_so_long_it_could_probably_wrap_around_the_earth_if_written_on_paper_repeatedly_for_no_reason = 1234567890
    another_completely_absurd_and_unnecessarily_long_variable_name_that_serves_less_purpose_than_a_chocolate_teapot = "just_vibing"
    list_with_a_name_that_is_longer_than_most_people_would_bother_to_even_read_because_this_is_purely_ridiculous = [0] * 10000

    for iterator_that_makes_you_question_all_your_life_choices_and_wonder_why_this_code_even_exists in range(5):
        variable_that_has_a_name_so_long_it_could_probably_wrap_around_the_earth_if_written_on_paper_repeatedly_for_no_reason += iterator_that_makes_you_question_all_your_life_choices_and_wonder_why_this_code_even_exists
        another_completely_absurd_and_unnecessarily_long_variable_name_that_serves_less_purpose_than_a_chocolate_teapot += "?"

        list_with_a_name_that_is_longer_than_most_people_would_bother_to_even_read_because_this_is_purely_ridiculous.append(
            variable_that_has_a_name_so_long_it_could_probably_wrap_around_the_earth_if_written_on_paper_repeatedly_for_no_reason
        )

    return list_with_a_name_that_is_longer_than_most_people_would_bother_to_even_read_because_this_is_purely_ridiculous

def another_function_that_is_so_ridiculously_named_it_would_probably_be_banned_in_some_countries_for_its_sheer_absurdity():
    absolutely_no_reason_for_this_variable_name_to_be_this_long_other_than_to_annoy_future_developers_who_have_to_read_this_code = "Why are you like this?"
    variable_name_that_is_so_unnecessarily_long_it_makes_you_question_the_meaning_of_existence_itself_while_reading_it = 3.1415926535

    while variable_name_that_is_so_unnecessarily_long_it_makes_you_question_the_meaning_of_existence_itself_while_reading_it > 0:
        absolutely_no_reason_for_this_variable_name_to_be_this_long_other_than_to_annoy_future_developers_who_have_to_read_this_code += "!"
        variable_name_that_is_so_unnecessarily_long_it_makes_you_question_the_meaning_of_existence_itself_while_reading_it -= 0.00000001

    dictionary_with_a_key_that_is_longer_than_most_dissertations_written_by_phd_students_for_no_justifiable_reason = {
        "key_that_is_so_long_it_could_actually_be_considered_a_paragraph_instead_of_a_key": 
        absolutely_no_reason_for_this_variable_name_to_be_this_long_other_than_to_annoy_future_developers_who_have_to_read_this_code
    }

    return dictionary_with_a_key_that_is_longer_than_most_dissertations_written_by_phd_students_for_no_justifiable_reason

asfhgaihukheajshfikajhwefiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb = {
    'A': '.<', 'B': '>...', 'C': '>.>.', 'D': '>..', 'E': '.', 'F': '..>.', 'G': '>>.', 'H': '....',
    'I': '..', 'J': '.>>>', 'K': '>...>', 'L': '.>..', 'M': '>>', 'N': '>.', 'O': '>>>', 'P': '.>>.',
    'Q': '>>>.', 'R': '.>.', 'S': '...', 'T': '>', 'U': '..>', 'V': '...>', 'W': '.>>', 'X': '>..>',
    'Y': '>.>>', 'Z': '>>..',
    '1': '.>>>>', '2': '..>>>', '3': '...>>', '4': '....>', '5': '.....', '6': '>....', '7': '>>...',
    '8': '>>>..', '9': '>>>>.', '0': '>>>>>',
    ' ': '/'
}
def canon_sony_but_what_the_hell_is_nikkon(text):
   
    ausfhiuqhfjasfbkjasbfhjqwhfbk = []
    for char in text.upper():
        if char in asfhgaihujksfnaijkdhgiuqkheajshfikajhwefiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb:
            ausfhiuqhfjasfbkjasbfhjqwhfbk.append(asfhgaihujksfnaijkdhgiuqkheajshfikajhwefiuwehfasjbhcjhasbfhajsfguiehqjwkafjfbshjfabujayefjshb[char].replace('.', '<').replace('-', '>'))
        else:
            ausfhiuqhfjasfbkjasbfhjqwhfbk.append('')  
    return ' '.join(ausfhiuqhfjasfbkjasbfhjqwhfbk)
# Mama told me not to try
# And I should have taken her advice
# And now I'm all twisted
# When it's all gone, I miss it

if __name__ == "__main__":

    balle_balle_shava_shav = input("Enter a string to encode: ")

    grapes_are_rotten_apples_are_fine = canon_sony_but_what_the_hell_is_nikkon(balle_balle_shava_shav)
    
# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
    print("Encoded:")
    print(grapes_are_rotten_apples_are_fine)
#     /**
#  *    author:  tourist
#  *    created: 11.02.2025 07:22:39
# **/
# #include <bits/stdc++.h>
 
# using namespace std;
 
# #ifdef LOCAL
# #include "algo/debug.h"
# #else
# #define debug(...) 42
# #endif
 
# namespace seg_tree {
 
# // Floor of log_2(a); index of highest 1-bit
# inline int floor_log_2(int a) {
#   return a ? bit_width(unsigned(a)) - 1 : -1;
# }
 
# struct point {
#   int a;
#   point() : a(0) {}
#   explicit point(int a_) : a(a_) { assert(a >= -1); }
 
#   explicit operator bool () { return bool(a); }
 
#   // This is useful so you can directly do array indices
#   /* implicit */ operator int() const { return a; }
 
#   point c(bool z) const {
#     return point((a << 1) | z);
#   }
 
#   point operator [] (bool z) const {
#     return c(z);
#   }
 
#   point p() const {
#     return point(a >> 1);
#   }
 
#   friend std::ostream& operator << (std::ostream& o, const point& p) { return o << int(p); }
 
#   template <typename F> void for_each(F f) const {
#     for (int v = a; v > 0; v >>= 1) {
#       f(point(v));
#     }
#   }
 
#   template <typename F> void for_parents_down(F f) const {
#     // strictly greater than 0
#     for (int L = floor_log_2(a); L > 0; L--) {
#       f(point(a >> L));
#     }
#   }
 
#   template <typename F> void for_parents_up(F f) const {
#     for (int v = a >> 1; v > 0; v >>= 1) {
#       f(point(v));
#     }
#   }
 
#   point& operator ++ () { ++a; return *this; }
#   point operator ++ (int) { return point(a++); }
#   point& operator -- () { --a; return *this; }
#   point operator -- (int) { return point(a--); }
# };
 
# struct range {
#   int a, b;
#   range() : a(1), b(1) {}
#   range(int a_, int b_) : a(a_), b(b_) {
#     assert(1 <= a && a <= b && b <= 2 * a);
#   }
#   explicit range(std::array<int, 2> r) : range(r[0], r[1]) {}
 
#   explicit operator std::array<int, 2>() const {
#     return {a, b};
#   }
 
#   const int& operator[] (bool z) const {
#     return z ? b : a;
#   }
 
#   friend std::ostream& operator << (std::ostream& o, const range& r) { return o << "[" << r.a << ".." << r.b << ")"; }
 
#   // Iterate over the range from outside-in.
#   //   Calls f(point a)
#   template <typename F> void for_each(F f) const {
#     for (int x = a, y = b; x < y; x >>= 1, y >>= 1) {
#       if (x & 1) f(point(x++));
#       if (y & 1) f(point(--y));
#     }
#   }
 
#   // Iterate over the range from outside-in.
#   //   Calls f(point a, bool is_right)
#   template <typename F> void for_each_with_side(F f) const {
#     for (int x = a, y = b; x < y; x >>= 1, y >>= 1) {
#       if (x & 1) f(point(x++), false);
#       if (y & 1) f(point(--y), true);
#     }
#   }
 
#   // Iterate over the range from left to right.
#   //    Calls f(point)
#   template <typename F> void for_each_l_to_r(F f) const {
#     int anc_depth = floor_log_2((a - 1) ^ b);
#     int anc_msk = (1 << anc_depth) - 1;
#     for (int v = (-a) & anc_msk; v; v &= v - 1) {
#       int i = countr_zero(unsigned(v));
#       f(point(((a - 1) >> i) + 1));
#     }
#     for (int v = b & anc_msk; v; ) {
#       int i = floor_log_2(v);
#       f(point((b >> i) - 1));
#       v ^= (1 << i);
#     }
#   }
 
#   // Iterate over the range from right to left.
#   //    Calls f(point)
#   template <typename F> void for_each_r_to_l(F f) const {
#     int anc_depth = floor_log_2((a - 1) ^ b);
#     int anc_msk = (1 << anc_depth) - 1;
#     for (int v = b & anc_msk; v; v &= v - 1) {
#       int i = countr_zero(unsigned(v));
#       f(point((b >> i) - 1));
#     }
#     for (int v = (-a) & anc_msk; v; ) {
#       int i = floor_log_2(v);
#       f(point(((a - 1) >> i) + 1));
#       v ^= (1 << i);
#     }
#   }
 
#   template <typename F> void for_parents_down(F f) const {
#     int x = a, y = b;
#     if ((x ^ y) > x) { x <<= 1, std::swap(x, y); }
#     int dx = countr_zero(unsigned(x));
#     int dy = countr_zero(unsigned(y));
#     int anc_depth = floor_log_2((x - 1) ^ y);
#     for (int i = floor_log_2(x); i > dx; i--) {
#       f(point(x >> i));
#     }
#     for (int i = anc_depth; i > dy; i--) {
#       f(point(y >> i));
#     }
#   }
 
#   template <typename F> void for_parents_up(F f) const {
#     int x = a, y = b;
#     if ((x ^ y) > x) { x <<= 1, std::swap(x, y); }
#     int dx = countr_zero(unsigned(x));
#     int dy = countr_zero(unsigned(y));
#     int anc_depth = floor_log_2((x - 1) ^ y);
#     for (int i = dx + 1; i <= anc_depth; i++) {
#       f(point(x >> i));
#     }
#     for (int v = y >> (dy + 1); v; v >>= 1) {
#       f(point(v));
#     }
#   }
# };
 
# struct in_order_layout {
#   // Alias them in for convenience
#   using point = seg_tree::point;
#   using range = seg_tree::range;
 
#   int n, s;
#   in_order_layout() : n(0), s(0) {}
#   in_order_layout(int n_) : n(n_), s(n ? bit_ceil(unsigned(n)) : 0) {}
 
#   point get_point(int a) const {
#     assert(0 <= a && a < n);
#     a += s;
#     return point(a >= 2 * n ? a - n : a);
#   }
 
#   range get_range(int a, int b) const {
#     assert(0 <= a && a <= b && b <= n);
#     if (n == 0) return range();
#     a += s, b += s;
#     return range((a >= 2 * n ? 2 * (a - n) : a), (b >= 2 * n ? 2 * (b - n) : b));
#   }
 
#   range get_range(std::array<int, 2> p) const {
#     return get_range(p[0], p[1]);
#   }
 
#   int get_leaf_index(point pt) const {
#     int a = int(pt);
#     assert(n <= a && a < 2 * n);
#     return (a < s ? a + n : a) - s;
#   }
 
#   std::array<int, 2> get_node_bounds(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < 2 * n);
#     int l = countl_zero(unsigned(a)) - countl_zero(unsigned(2 * n - 1));
#     int x = a << l, y = (a + 1) << l;
#     assert(s <= x && x < y && y <= 2 * s);
#     return {(x >= 2 * n ? (x >> 1) + n : x) - s, (y >= 2 * n ? (y >> 1) + n : y) - s};
#   }
 
#   int get_node_split(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < n);
#     int l = countl_zero(unsigned(2 * a + 1)) - countl_zero(unsigned(2 * n - 1));
#     int x = (2 * a + 1) << l;
#     assert(s <= x && x < 2 * s);
#     return (x >= 2 * n ? (x >> 1) + n : x) - s;
#   }
 
#   int get_node_size(point pt) const {
#     auto bounds = get_node_bounds(pt);
#     return bounds[1] - bounds[0];
#   }
# };
 
# struct circular_layout {
#   // Alias them in for convenience
#   using point = seg_tree::point;
#   using range = seg_tree::range;
 
#   int n;
#   circular_layout() : n(0) {}
#   circular_layout(int n_) : n(n_) {}
 
#   point get_point(int a) const {
#     assert(0 <= a && a < n);
#     return point(n + a);
#   }
 
#   range get_range(int a, int b) const {
#     assert(0 <= a && a <= b && b <= n);
#     if (n == 0) return range();
#     return range(n + a, n + b);
#   }
 
#   range get_range(std::array<int, 2> p) const {
#     return get_range(p[0], p[1]);
#   }
 
#   int get_leaf_index(point pt) const {
#     int a = int(pt);
#     assert(n <= a && a < 2 * n);
#     return a - n;
#   }
 
#   // Returns {x,y} so that 0 <= x < n and 1 <= y <= n
#   // If the point is non-wrapping, then 0 <= x < y <= n
#   std::array<int, 2> get_node_bounds(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < 2 * n);
#     int l = countl_zero(unsigned(a)) - countl_zero(unsigned(2 * n - 1));
#     int s = bit_ceil(unsigned(n));
#     int x = a << l, y = (a + 1) << l;
#     assert(s <= x && x < y && y <= 2 * s);
#     return {(x >= 2 * n ? x >> 1 : x) - n, (y > 2 * n ? y >> 1 : y) - n};
#   }
 
#   // Returns the split point of the node, such that 1 <= s <= n.
#   int get_node_split(point pt) const {
#     int a = int(pt);
#     assert(1 <= a && a < n);
#     return get_node_bounds(pt.c(0))[1];
#   }
 
#   int get_node_size(point pt) const {
#     auto bounds = get_node_bounds(pt);
#     int r = bounds[1] - bounds[0];
#     return r > 0 ? r : r + n;
#   }
# };
 
# } // namespace seg_tree
 
# template <typename Info, typename Tag>
# class LazySegmentTree {
#  public:
#   int n;
#   vector<Info> infos;
#   vector<Tag> tags;
#   seg_tree::in_order_layout layout;
 
#   void Apply(seg_tree::point a, const Tag& t) {
#     auto [l, r] = layout.get_node_bounds(a);
#     if (!t.ApplyTo(infos[a], l, r)) {
#       assert(a < n);
#       DowndateNode(a);
#       Apply(a.c(0), t);
#       Apply(a.c(1), t);
#       UpdateNode(a);
#       return;
#     }
#     if (a < n) {
#       t.ApplyTo(tags[a]);
#     }
#   }
 
#   void DowndateNode(seg_tree::point a) {
#     if (!tags[a].Empty()) {
#       Apply(a.c(0), tags[a]);
#       Apply(a.c(1), tags[a]);
#       tags[a] = Tag();
#     }
#   }
 
#   void UpdateNode(seg_tree::point a) {
#     infos[a] = infos[a.c(0)].Unite(infos[a.c(1)]);
#   }
 
#   LazySegmentTree() : LazySegmentTree(0) {}
#   LazySegmentTree(int n_) : LazySegmentTree(vector<Info>(n_)) {}
#   LazySegmentTree(const vector<Info>& a) : n(int(a.size())) {
#     infos.resize(2 * n);
#     tags.resize(n);
#     layout = seg_tree::in_order_layout(n);
#     for (int i = 0; i < n; i++) {
#       infos[layout.get_point(i)] = a[i];
#     }
#     for (int i = n - 1; i >= 1; i--) {
#       UpdateNode(seg_tree::point(i));
#     }
#   }
 
#   void Modify(int l, int r, const Tag& t) {
#     auto rng = layout.get_range(l, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     rng.for_each([&](seg_tree::point a) {
#       Apply(a, t);
#     });
#     rng.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   void Set(int p, const Info& v) {
#     auto pt = layout.get_point(p);
#     pt.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     infos[pt] = v;
#     pt.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   Info Query(int l, int r) {
#     auto rng = layout.get_range(l, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     Info res;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       res = res.Unite(infos[a]);
#     });
#     return res;
#   }
 
#   Info Get(int p) {
#     auto pt = layout.get_point(p);
#     pt.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     return infos[pt];
#   }
 
#   template<typename F>
#   int MaxRight(int l, F f) {
#     auto rng = layout.get_range(l, n);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     int res = n;
#     Info sum;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       if (res != n) {
#         return;
#       }
#       auto new_sum = sum.Unite(infos[a]);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         DowndateNode(a);
#         new_sum = sum.Unite(infos[a.c(0)]);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(1);
#         } else {
#           a = a.c(0);
#         }
#       }
#       res = layout.get_node_bounds(a)[0];
#     });
#     return res;
#   }
 
#   template<typename F>
#   int MinLeft(int r, F f) {
#     auto rng = layout.get_range(0, r);
#     rng.for_parents_down([&](seg_tree::point a) {
#       DowndateNode(a);
#     });
#     int res = 0;
#     Info sum;
#     rng.for_each_r_to_l([&](seg_tree::point a) {
#       if (res != 0) {
#         return;
#       }
#       auto new_sum = infos[a].Unite(sum);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         DowndateNode(a);
#         new_sum = infos[a.c(1)].Unite(sum);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(0);
#         } else {
#           a = a.c(1);
#         }
#       }
#       res = layout.get_node_bounds(a)[1];
#     });
#     return res;
#   }
# };
 
# struct Info {
#   int64_t mx = 0;
 
#   Info Unite(const Info& b) const {
#     Info res;
#     res.mx = max(mx, b.mx);
#     return res;
#   }
 
#   static Info GetDefault([[maybe_unused]] int l, [[maybe_unused]] int r) {
#     return Info();
#   }
# };
 
# struct Tag {
#   int64_t add = 0;
 
#   bool ApplyTo(Info& a, [[maybe_unused]] int l, [[maybe_unused]] int r) const {
#     a.mx += add;
#     return true;
#   }
 
#   void ApplyTo(Tag& t) const {
#     t.add += add;
#   }
 
#   bool Empty() const {
#     return add == 0;
#   }
# };
 
# template <typename T>
# class FenwickTree {
#  public:
#   vector<T> fenw;
#   int n;
#   int pw;
 
#   FenwickTree() : n(0) {}
#   FenwickTree(int n_) : n(n_) {
#     fenw.resize(n);
#     pw = bit_floor(unsigned(n));
#   }
 
#   void Modify(int x, T v) {
#     assert(0 <= x && x <= n);
#     while (x < n) {
#       fenw[x] += v;
#       x |= x + 1;
#     }
#   }
 
#   T Query(int x) {
#     assert(0 <= x && x <= n);
#     T v{};
#     while (x > 0) {
#       v += fenw[x - 1];
#       x &= x - 1;
#     }
#     return v;
#   }
 
#   // Returns the length of the longest prefix with sum <= c
#   int MaxPrefix(T c) {
#     T v{};
#     int at = 0;
#     for (int len = pw; len > 0; len >>= 1) {
#       if (at + len <= n) {
#         auto nv = v;
#         nv += fenw[at + len - 1];
#         if (!(c < nv)) {
#           v = nv;
#           at += len;
#         }
#       }
#     }
#     assert(0 <= at && at <= n);
#     return at;
#   }
# };
 
# template <typename Info>
# class SimpleSegmentTree {
#  public:
#   int n;
#   vector<Info> infos;
#   seg_tree::in_order_layout layout;
 
#   void UpdateNode(seg_tree::point a) {
#     infos[a] = infos[a.c(0)].Unite(infos[a.c(1)]);
#   }
 
#   SimpleSegmentTree(int n_) : SimpleSegmentTree(vector<Info>(n_)) {}
 
#   SimpleSegmentTree(const vector<Info>& a) : n(int(a.size())) {
#     assert(n > 0);
#     infos.resize(2 * n);
#     layout = seg_tree::in_order_layout(n);
#     for (int i = 0; i < n; i++) {
#       infos[layout.get_point(i)] = a[i];
#     }
#     for (int i = n - 1; i >= 1; i--) {
#       infos[i] = infos[2 * i].Unite(infos[2 * i + 1]);
#     }
#   }
 
#   void Set(int p, const Info& v) {
#     auto pt = layout.get_point(p);
#     infos[pt] = v;
#     pt.for_parents_up([&](seg_tree::point a) {
#       UpdateNode(a);
#     });
#   }
 
#   Info Query(int l, int r) {
#     auto rng = layout.get_range(l, r);
#     Info res;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       res = res.Unite(infos[a]);
#     });
#     return res;
#   }
 
#   Info Get(int p) {
#     auto pt = layout.get_point(p);
#     return infos[pt];
#   }
 
#   template<typename F>
#   int MaxRight(int l, F f) {
#     auto rng = layout.get_range(l, n);
#     int res = n;
#     Info sum;
#     rng.for_each_l_to_r([&](seg_tree::point a) {
#       if (res != n) {
#         return;
#       }
#       auto new_sum = sum.Unite(infos[a]);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         new_sum = sum.Unite(infos[a.c(0)]);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(1);
#         } else {
#           a = a.c(0);
#         }
#       }
#       res = layout.get_node_bounds(a)[0];
#     });
#     return res;
#   }
 
#   template<typename F>
#   int MinLeft(int r, F f) {
#     auto rng = layout.get_range(0, r);
#     int res = 0;
#     Info sum;
#     rng.for_each_r_to_l([&](seg_tree::point a) {
#       if (res != 0) {
#         return;
#       }
#       auto new_sum = infos[a].Unite(sum);
#       if (f(new_sum)) {
#         sum = new_sum;
#         return;
#       }
#       while (a < n) {
#         new_sum = infos[a.c(1)].Unite(sum);
#         if (f(new_sum)) {
#           sum = new_sum;
#           a = a.c(0);
#         } else {
#           a = a.c(1);
#         }
#       }
#       res = layout.get_node_bounds(a)[1];
#     });
#     return res;
#   }
# };
 
# struct InfoMx {
#   int mx = -1;
 
#   InfoMx Unite(const InfoMx& b) const {
#     InfoMx res;
#     res.mx = max(mx, b.mx);
#     return res;
#   }
 
#   static InfoMx GetDefault([[maybe_unused]] int l, [[maybe_unused]] int r) {
#     return InfoMx();
#   }
# };
 
# int main() {
#   ios::sync_with_stdio(false);
#   cin.tie(nullptr);
#   int n, q;
#   cin >> n >> q;
#   vector<int> a(n);
#   for (int i = 0; i < n; i++) {
#     cin >> a[i];
#   }
#   vector<int> type(q), b(q);
#   for (int i = 0; i < q; i++) {
#     string foo;
#     cin >> foo >> b[i];
#     type[i] = (foo == "+" ? +1 : -1);
#   }
#   auto all = a;
#   all.insert(all.end(), b.begin(), b.end());
#   sort(all.begin(), all.end());
#   int sz = int(all.size());
#   int M = all.back() + 5;
#   vector<int> first(M, -1);
#   for (int i = 0; i < sz; i++) {
#     if (first[all[i]] == -1) {
#       first[all[i]] = i;
#     }
#   }
#   vector<int> cnt(M);
#   LazySegmentTree<Info, Tag> st(sz);
#   FenwickTree<int64_t> fenw(sz);
#   SimpleSegmentTree<InfoMx> st_mx(M);
#   set<int> alive;
#   vector<set<int>> by_diff(M);
#   auto InsertDiff = [&](int at, int val) {
#     int old_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     by_diff[at].insert(val);
#     int new_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     if (old_val != new_val) {
#       st_mx.Set(at, {new_val});
#     }
#   };
#   auto EraseDiff = [&](int at, int val) {
#     int old_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     by_diff[at].erase(val);
#     int new_val = (by_diff[at].empty() ? -1 : *prev(by_diff[at].end()));
#     if (old_val != new_val) {
#       st_mx.Set(at, {new_val});
#     }
#   };
#   auto Add = [&](int x) {
#     int pos = first[x] + cnt[x];
#     auto it = alive.insert(pos).first;
#     int pr = (it == alive.begin() ? -1 : *prev(it));
#     int ne = (next(it) == alive.end() ? -1 : *next(it));
#     if (pr != -1 && ne != -1) {
#       EraseDiff(all[ne] - all[pr], pr);
#     }
#     if (pr != -1) {
#       InsertDiff(all[pos] - all[pr], pr);
#     }
#     if (ne != -1) {
#       InsertDiff(all[ne] - all[pos], pos);
#     }
#     st.Modify(pos, pos + 1, {+x});
#     st.Modify(pos + 1, sz, {-x});
#     fenw.Modify(pos, +x);
#     cnt[x] += 1;
#   };
#   auto Remove = [&](int x) {
#     assert(cnt[x] >= 1);
#     cnt[x] -= 1;
#     int pos = first[x] + cnt[x];
#     auto it = alive.find(pos);
#     int pr = (it == alive.begin() ? -1 : *prev(it));
#     int ne = (next(it) == alive.end() ? -1 : *next(it));
#     if (pr != -1) {
#       EraseDiff(all[pos] - all[pr], pr);
#     }
#     if (ne != -1) {
#       EraseDiff(all[ne] - all[pos], pos);
#     }
#     if (pr != -1 && ne != -1) {
#       InsertDiff(all[ne] - all[pr], pr);
#     }
#     alive.erase(it);
#     st.Modify(pos, pos + 1, {-x});
#     st.Modify(pos + 1, sz, {+x});
#     fenw.Modify(pos, -x);
#   };
#   auto Print = [&]() {
#     assert(!alive.empty());
#     int until = 0;
#     while (true) {
#       int i = int(lower_bound(all.begin(), all.end(), until + 1) - all.begin());
#       int64_t sum = fenw.Query(i);
#       if (sum >= M - 1) {
#         until = M;
#         break;
#       }
#       if (sum != until) {
#         until = int(sum);
#         continue;
#       }
#       auto got = st_mx.Query(0, int(sum) + 1).mx;
#       if (got == -1 || all[got] <= until) {
#         break;
#       }
#       until = all[got];
#     }
#     int i = int(lower_bound(all.begin(), all.end(), until + 1) - all.begin());
#     int j = *prev(alive.end());
#     cout << (i < j && st.Query(i, j).mx > 0 ? "No" : "Yes") << '\n';
#   };
#   for (int i = 0; i < n; i++) {
#     Add(a[i]);
#   }
#   Print();
#   for (int i = 0; i < q; i++) {
#     if (type[i] == +1) {
#       Add(b[i]);
#     } else {
#       Remove(b[i]);
#     }
#     Print();
#   }
#   return 0;
# }