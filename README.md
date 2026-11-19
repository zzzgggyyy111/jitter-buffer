# 抖动缓冲：重排、延迟与丢包隐藏

语音包乱序到达后断续、抖动大时缓冲不够：重排没有按序号，目标延迟没有算抖动，播放窗口按序号而不是时间，丢包隐藏没有复制上一帧，缓冲大小没向上取整，空包崩，批量处理只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
net/__init__.py
net/jitter.py
tests/test_jitter.py
```

## 当前状态

`net/jitter.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_jitter.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 按序号重排
2. 目标延迟含抖动
3. 播放按时间窗口
4. 丢包复制上一帧
5. 缓冲大小向上取整
6. 空包兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `net/jitter.py`
后 15 条用例应全部通过。
