# M_fujita_2020S_01_01

2019年11月10日に実施の藤田医科大学医学部ふじた未来入試（AO入試）で出題された数学の問題1(1)を解くプログラムです。

# 問題

下図のような道のある街で，道を通って最短距離で A から B まで行き，再び最短距離で A まで戻る道順を考える。
道順は全部で （ アイウ ） 通りあり，これらのうち A 以外の地点を 2 度通ることのない道順は全部で （ エオ ） 通りある。

![fig](fig.svg)

# 実行結果

引数なしでは、オリジナルの問題の解答を与えます。

```
$ python M_fujita_2020S_01_01.py
40
```

引数を与えることにより、n×n とした場合の解答を与えます。

```
$ python M_fujita_2020S_01_01.py 6
3808
```

しかし、値を大きく取り過ぎると計算時間がかかりすぎてしまいます。

# 実は・・・

```math
\displaystyle2\left\{\left(\frac{(2n-2)!}{(n-1)!(n-1)}\right)^2-\left(\frac{(2n-2)!}{(n-2)!n!}\right)^2\right\}
```
で求められます。
