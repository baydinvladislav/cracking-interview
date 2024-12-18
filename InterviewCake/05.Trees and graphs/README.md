# Trees and graphs
+ [Balanced Binary Tree](#balanced-binary-tree)
+ [Binary Search Tree Checker](#binary-search-tree-checker)
+ [2nd Largest Item in a Binary Search Tree](#2nd-largest-item-in-a-binary-search-tree)
+ [Graph Coloring](#graph-coloring)
+ [MeshMessage](#meshmessage)


## Balanced Binary Tree
Определить что разница между двумя любыми листами не более 1.

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Обойти в ширину по уровням, отслеживая мин. и макс. лист от корня.</li>
 <li>Вычислить разницу между мин. и макс. листами от корня.</li>
</ol>

</blockquote></details>

```python
from collections import deque


# my own 10.10.22
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_balanced(tree_root):
    queue = deque()
    queue.append((tree_root, 1))

    min_leaf, max_leaf = float('inf'), float('-inf')
    while queue:
        node, level = queue.popleft()

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

        if not node.left and not node.right:
            max_leaf = max(max_leaf, level)
            min_leaf = min(min_leaf, level)

    return max_leaf - min_leaf <= 1

```


## Binary Search Tree Checker
Определить что дерево является бинарным деревом поиска.

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Обойти рекурсивно дерево, сохраняя значения узлов в массив.</li>
 <li>Проверить массив на несовпадение порядка значений.</li>
</ol>

</blockquote></details>

```python
# my own
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_binary_search_tree(root):
    def in_order(node):
        if not node:
            return

        in_order(node.left)
        values.append(node.value)
        in_order(node.right)

    values = []
    in_order(root)

    for i in range(1, len(values)):
        if values[i - 1] > values[i]:
            return False

    return True

```


## 2nd Largest Item in a Binary Search Tree
Вернуть 2ой второй наибольший элемент.

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Обойти дерево in-order, получить отсортированный массив.</li>
 <li>Вернуть второй с конца элемент массива.</li>
</ol>

</blockquote></details>

<details><summary>Решение из курса:</summary><blockquote>
<ol>
 <li>Если у текущего узла при обходе нет правого узла и есть левый узел, то продолжить обход слева.</li>
 <li>Если у текущего узла есть правый узел и этого правого узла нет ни левого, ни правого узла, то вернуть текущий узел.</li>
 <li>Рекурсия по правой стороне дерева.</li>
</ol>

</blockquote></details>


```python
# my own solution
# Time Complexity: O(n)
# Space Complexity: O(n**n)
def find_second_largest(root_node):
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        values.append(node.value)
        dfs(node.right)

    values = []
    dfs(root_node)

    return values[-2]


# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if not root_node or not root_node.left and not root_node.right:
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if current.right and not current.right.left and not current.right.right:
            return current.value

        current = current.right

```


## MeshMessage
Найти наименьший путь от вершины до вершины ненаправленного, невзвешенного и оцикличного графа.

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Поиск в ширину.</li>
 <li>Отслеживаем из какой вершину в какую идем.</li>
 <li>Формируем путь.</li>
</ol>

</blockquote></details>


```python
from collections import deque


# my code based on their solution
# time: O(N(vertexes) + M(edges))
# space: O(N)
def get_path(graph, start_node, end_node):
    queue = deque([start_node])
    visited = {start_node}
    path = {start_node: None}
    while queue:
        node = queue.popleft()

        if node == end_node:
            # we found node then reconstruct the path
            reversed_shortest_path = []
            current_node = end_node
            while current_node:
                reversed_shortest_path.append(current_node)
                current_node = path[current_node]
            reversed_shortest_path.reverse()

            return reversed_shortest_path

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(node)
                path[neighbour] = node

    return None

```


## Graph Coloring
Дан граф и цвета. Раскрасить граф цветами, чтобы не было соседних вершин одного цвета.

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Пройти по каждому узлу.</li>
 <li>Для каждого узла вычисляем занятые его соседями цвета.</li>
 <li>Раскрашиваем узел в цвет, которого нет во множестве занятых соседями цветов.</li>
</ol>

</blockquote></details>


```python
# their solution
# Time Complexity: O(N + M) where N is the number of nodes and M is the number of edges.
# Space Complexity: O(D) where D is max graph degree
def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' % node.label)

        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        occupied_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])

        # Assign the first legal color
        for color in colors:
            if color not in occupied_colors:
                node.color = color
                break

```
