# M_fujita_2020S_01_01

2019年11月10日に実施の藤田医科大学医学部ふじた未来入試（AO入試）で出題された数学の問題1(1)を解くプログラムです。

# 問題

下図のような道のある街で，道を通って最短距離で A から B まで行き，再び最短距離で A まで戻る道順を考える。
道順は全部で （ アイウ ） 通りあり，これらのうち A 以外の地点を 2 度通ることのない道順は全部で （ エオ ） 通りある。

<svg x=0 y=0 width=190 height=130 style="background-color: #fff">
  <line x1="20" y1="20" x2="170" y2="20" stroke="black" />
  <line x1="20" y1="50" x2="170" y2="50" stroke="black" />
  <line x1="20" y1="80" x2="170" y2="80" stroke="black" />
  <line x1="20" y1="110" x2="170" y2="110" stroke="black" />
  <line x1="20" y1="20" x2="20" y2="110" stroke="black" />
  <line x1="70" y1="20" x2="70" y2="110" stroke="black" />
  <line x1="120" y1="20" x2="120" y2="110" stroke="black" />
  <line x1="170" y1="20" x2="170" y2="110" stroke="black" />
  <text x="9" y="121">A</text>
  <text x="171" y="19">B</text>
</svg>

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

<img src="https://render.githubusercontent.com/render/math?math=\displaystyle2\left\{\left(\frac{(2n-2)!}{(n-1)!(n-1)}\right)^2-\left(\frac{(2n-2)!}{(n-2)!n!}\right)^2\right\}" >
で求められます。
