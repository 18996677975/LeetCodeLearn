<p>给定一个头节点为 <code>head</code> 的单链表用于记录一系列核心肌群训练编号，请将该系列训练编号 <strong>倒序</strong> 记录于链表并返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2,3,4,5]
<strong>输出：</strong>[5,4,3,2,1]
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2]
<strong>输出：</strong>[2,1]
</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>链表中节点的数目范围是 <code>[0, 5000]</code></li> 
 <li><code>-5000 &lt;= Node.val &lt;= 5000</code></li> 
</ul>

<p>&nbsp;</p>

<p><strong>注意</strong>：本题与主站 206 题相同：<a href="https://leetcode-cn.com/problems/reverse-linked-list/">https://leetcode-cn.com/problems/reverse-linked-list/</a></p>

<p>&nbsp;</p>

<details><summary><strong>Related Topics</strong></summary>递归 | 链表</details><br>

<div>👍 634, 👎 0<span style='float: right;'><span style='color: gray;'><a href='https://github.com/labuladong/fucking-algorithm/discussions/939' target='_blank' style='color: lightgray;text-decoration: underline;'>bug 反馈</a> | <a href='https://labuladong.online/algo/fname.html?fname=jb插件简介' target='_blank' style='color: lightgray;text-decoration: underline;'>使用指南</a> | <a href='https://labuladong.online/algo/images/others/%E5%85%A8%E5%AE%B6%E6%A1%B6.jpg' target='_blank' style='color: lightgray;text-decoration: underline;'>更多配套插件</a></span></span></div>

<div id="labuladong"><hr>

**通知：[新版网站会员](https://labuladong.online/algo/intro/site-vip/) 限时优惠；算法可视化编辑器上线，[点击体验](https://labuladong.online/algo/intro/visualize/)！**



<p><strong><a href="https://labuladong.online/algo/slug.html?slug=fan-zhuan-lian-biao-lcof" target="_blank">⭐️labuladong 题解</a></strong></p>
<details><summary><strong>labuladong 思路</strong></summary>

## 基本思路

这道题和 [206. 反转链表](/problems/reverse-linked-list) 相同。

递归实现反转链表常常用来考察递归思想，我这里就用纯递归来翻转链表。

**对于递归算法，最重要的就是明确递归函数的定义**。具体来说，我们的 `reverse` 函数定义是这样的：

**输入一个节点 `head`，将「以 `head` 为起点」的链表反转，并返回反转之后的头结点**。

明白了函数的定义，再来看这个问题。比如说我们想反转这个链表：

![](https://labuladong.github.io/pictures/反转链表/1.jpg)

那么输入 `reverse(head)` 后，会在这里进行递归：

```java
ListNode last = reverse(head.next);
```

不要跳进递归（你的脑袋能压几个栈呀？），而是要根据刚才的函数定义，来弄清楚这段代码会产生什么结果：

![](https://labuladong.github.io/pictures/反转链表/2.jpg)

这个 `reverse(head.next)` 执行完成后，整个链表就成了这样：

![](https://labuladong.github.io/pictures/反转链表/3.jpg)

并且根据函数定义，`reverse` 函数会返回反转之后的头结点，我们用变量 `last` 接收了。

现在再来看下面的代码：

```java
head.next.next = head;
```

![](https://labuladong.github.io/pictures/反转链表/4.jpg)

接下来：

```java
head.next = null;
return last;
```

![](https://labuladong.github.io/pictures/反转链表/5.jpg)

神不神奇，这样整个链表就反转过来了！

**详细题解：[递归魔法：反转单链表](https://labuladong.online/algo/fname.html?fname=递归反转链表的一部分)**

**标签：单链表**

## 解法代码

提示：🟢 标记的是我写的解法代码，🤖 标记的是 chatGPT 翻译的多语言解法代码。如有错误，可以 [点这里](https://github.com/labuladong/fucking-algorithm/issues/1113) 反馈和修正。

<div class="tab-panel"><div class="tab-nav">
<button data-tab-item="cpp" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">cpp🤖</button>

<button data-tab-item="python" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">python🤖</button>

<button data-tab-item="java" class="tab-nav-button btn active" data-tab-group="default" onclick="switchTab(this)">java🟢</button>

<button data-tab-item="go" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">go🤖</button>

<button data-tab-item="javascript" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">javascript🤖</button>
</div><div class="tab-content">
<div data-tab-item="cpp" class="tab-item " data-tab-group="default"><div class="highlight">

```cpp
// 注意：cpp 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // 如果链表为空或只有一个节点，则直接返回该链表
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* last = nullptr;
        // 开始迭代翻转节点
        while (head != nullptr) {
            // 先保存当前节点的后继节点
            ListNode* next = head->next;
            // 将当前节点的指针指向前一个节点
            head->next = last;
            // 更新前一个节点为当前节点
            last = head;
            // 更新当前节点为后继节点
            head = next;
        }
        // 翻转链表完成，返回头节点
        return last;
    }
};
```

</div></div>

<div data-tab-item="python" class="tab-item " data-tab-group="default"><div class="highlight">

```python
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 如果链表为空或链表只有一个元素，则直接返回head
        if head == None or head.next==None:
            return head
        # 递归反转链表后面的部分
        last = self.reverseList(head.next)
        """
        反转之前的链表
        head      --> 3 --> 4 --> 5 --> null
        last      --> 5 --> null
        """
        # 将链表的下一个节点的后继指针指向当前节点
        head.next.next = head
        """
        反转之后的链表
        last      --> 5 --> 4 --> 3 --> null
                          ↑
        head      --> 4 ---┘
        """
        # 将当前节点的后继指针指向null
        head.next = None
        """
        反转之后的链表
        last      --> 5 --> 4 --> 3 --> null
        head      --> null
        """
        # 返回反转后的链表
        return last
```

</div></div>

<div data-tab-item="java" class="tab-item active" data-tab-group="default"><div class="highlight">

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode last = reverseList(head.next);/**<extend up -200>![](https://labuladong.github.io/pictures/反转链表/3.jpg) */
        head.next.next = head;/**<extend up -200>![](https://labuladong.github.io/pictures/反转链表/4.jpg) */
        head.next = null;/**<extend up -200>![](https://labuladong.github.io/pictures/反转链表/5.jpg) */
        return last;
    }
}
```

</div></div>

<div data-tab-item="go" class="tab-item " data-tab-group="default"><div class="highlight">

```go
// 注意：go 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    // 如果链表为空或者链表只有一个节点，直接返回head
    if head == nil || head.Next == nil {
        return head
    }
    // 递归处理下一个节点
    last := reverseList(head.Next)
    // 对于当前节点：
    // 原来指向下一个节点的指针反转指向上一个节点
    head.Next.Next = head
    // 原来指向下一个节点的指针指向nil
    head.Next = nil
    // 返回链表的最后一个节点，即反转后链表的头节点
    return last
}
```

</div></div>

<div data-tab-item="javascript" class="tab-item " data-tab-group="default"><div class="highlight">

```javascript
// 注意：javascript 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  if (head === null || head.next === null) {
    return head;
  }
  var last = reverseList(head.next);/**<extend up -200>![](https://labuladong.github.io/pictures/反转链表/3.jpg) */
  head.next.next = head;/**<extend up -200>![](https://labuladong.github.io/pictures/反转链表/4.jpg) */
  head.next = null;/**<extend up -200>![](https://labuladong.github.io/pictures/反转链表/5.jpg) */
  return last;
};
```

</div></div>
</div></div>

<hr /><details open hint-container details><summary style="font-size: medium"><strong>🍭🍭 算法可视化 🍭🍭</strong></summary><div id="data_reverse-linked-list" data="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"></div><div class="resizable aspect-ratio-container" style="height: 100%;">
<div id="iframe_reverse-linked-list"></div></div>
</details><hr /><br />

**类似题目**：
  - [92. 反转链表 II 🟠](/problems/reverse-linked-list-ii)
  - [剑指 Offer 24. 反转链表 🟢](/problems/fan-zhuan-lian-biao-lcof)
  - [剑指 Offer II 024. 反转链表 🟢](/problems/UHnkqh)

</details>
</div>

