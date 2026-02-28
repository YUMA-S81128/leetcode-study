# 連結リスト (Linked List) と ListNode について

LeetCodeの問題で頻出するデータ構造である「単方向連結リスト（Singly-Linked List）」とその構成要素である `ListNode` についての基本的な考え方と操作方法のまとめです。

## 1. 連結リストとは？
Pythonの通常のリスト（配列）のように `[2, 4, 3]` とデータが1つの変数にまとまっておらず、インデックス番号でのアクセス（`l1[0]` など）ができません。

その代わり、個々の「ノード（`ListNode`）」が数珠つなぎになっています。
各ノードは、以下の2つの情報を持っています。
*   `val`: 自分の持っている値（データ）
*   `next`: 次のノードへの**参照（リンク）**

リストの最後を表すために、一番最後のノードの `next` には必ず `None` が入ります。

## 2. ListNode の定義
連結リストのノードは、一般的に以下のようなクラスで定義されます。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 💡 重要なポイント： `next` に入っているのは「数字」ではない！
`val` にはただの数字（整数）が入りますが、**`next` には「次の `ListNode` という箱そのもの」が丸ごと入っています**（または何もないことを表す `None`）。

**【例】11（1 -> 1 -> None）を返す場合**
```python
# ① 後ろの箱（10の位の1）を作る。これには次は無いので next は None（空っぽ）。
node_10s_place = ListNode(1)

# ② 前の箱（1の位の1）を作る。
# ここで、next に【さっき作った箱（node_10s_place）】をドカンと丸ごと入れます！
head_node = ListNode(1, node_10s_place)
```

このとき、`head_node` の中身は以下のようになっています。
*   `head_node.val` ＝ `1` （ただの数字）
*   `head_node.next` ＝ **`node_10s_place` という箱そのもの！**

そのため、呼び出し側は以下のようにたどることができます。
```python
print(head_node.val)        # 出力: 1 （1の位）
print(head_node.next.val)   # 出力: 1 （10の位。nextの中に別の箱が入っているからvalを見れる）
print(head_node.next.next)  # 出力: None （空っぽなのでおしまい）
```

## 3. 次のノードへの移り方（走査・トラバース）
連結リストの最大の特徴は、「現在のノードが持っている `next` の情報を使って、次のノードへ移動していく」ことです。
手元の変数を、次につながっているノード自身で上書きし続けることで順番にたどることができます。

**【例】連結リストを先頭から順に表示する**

```python
# 例として、3つのノードを繋げたリストを作る
# node_c(9) <- node_b(8) <- head(7)
node_c = ListNode(9)
node_b = ListNode(8, node_c)
head = ListNode(7, node_b)

# 先頭のノードを変数にセットする
current = head  

# 現在見ているノードが存在する限りループする（ノードがなくなったら None になる）
while current is not None:
    print(current.val)  # 現在のノードの値を取り出す
    
    # 次のノードへ移動する（自分自身を次のノードで上書き）
    current = current.next
```

### ループ中の動き
*   **1回目**: `current` は `[値:7, 次:node_b]` 
*   **2回目**: `current` は `[値:8, 次:node_c]` に変わる
*   **3回目**: `current` は `[値:9, 次:None]` に変わる
*   **4回目**: `current` は `None` になり、ループが終了する

## 4. 呼び出し側での受け取り方と操作
連結リストを返す関数は、リスト全体をまとめた専用のオブジェクトではなく、**「構造の先頭にあるノード1つだけ（`ListNode`）」**を返します。

呼び出し側は、先頭のノードさえ受け取れば、あとは `next` を頼りに芋づる式に引っぱっていくことで、すべてのデータを取得できます。個別のノードの変数名（上記の `node_b` や `node_c` など）を知る必要は一切ありません。

**【例】関数から返された連結リストの値を全て取得する**

```python
# 何かの関数が、先ほどの [7 -> 8 -> 9] というリストの先頭ノードを返したとする
result_node = some_function_that_returns_listnode()

# 受け取った先頭ノードからスタート
current = result_node
obtained_values = []

# ノードが尽きるまで（Noneになるまで）次へ進む
while current is not None:
    obtained_values.append(current.val)
    
    # 次のノードへ移動
    current = current.next

print(obtained_values)  # 出力: [7, 8, 9]
```
