# Python耗时：约150ms（CPython）
import time
start = time.time()
sum(x*x for x in range(1_000_000))
diff = (time.time() - start)*1000
print(str(diff) + "ms")
