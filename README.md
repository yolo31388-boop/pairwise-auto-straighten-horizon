# pairwise-auto-straighten-horizon

## 领域

游戏、图形与多媒体

## 主题

地平线自动拉直

## 说明

全图角度换算、内容保留裁切与共享基准。

初始状态下 `imaging/auto_straighten_horizon.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
