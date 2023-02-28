import sys

[sys.stdout.buffer.write(b"hello there!!\n") for _ in range(100_000)]

sys.stdout.flush()