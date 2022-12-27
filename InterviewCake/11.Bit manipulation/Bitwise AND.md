Операция AND принимает два бита и возвращает 1, если оба бита равны 1. 
В противном случае возвращает 0.

```python
# 1 & 1  →  1
# 1 & 0  →  0
# 0 & 1  →  0
# 0 & 0  →  0
```

Думайте об этом как о шланге с двумя концами. Оба конца должны быть открыты для прохода воды.

При выполнении AND над двумя целыми числами операция AND вычисляется для каждой пары битов 
(двух битов с одним и тем же индексом в каждом числе).

```python
# 5 & 6  # gives 4

# At the bit level:
#     0101  (5)
#   & 0110  (6)
#   = 0100  (4)

```