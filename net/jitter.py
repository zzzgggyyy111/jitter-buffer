"""抖动缓冲：重排、延迟与丢包隐藏：待实现的核心模块。"""


def reorder(packets):
    """按序号重排。"""
    raise NotImplementedError

def target_delay(jitter, interval):
    """目标延迟。"""
    raise NotImplementedError

def playout(buffer, now):
    """可播放包。"""
    raise NotImplementedError

def conceal(last, count):
    """丢包隐藏。"""
    raise NotImplementedError

def buffer_size(jitter, interval):
    """缓冲包数。"""
    raise NotImplementedError
