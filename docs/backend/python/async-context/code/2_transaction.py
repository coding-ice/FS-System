class Transaction:
    def __enter__(self) -> "Transaction":
        print("打开事务")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_type is None:
            print("提交事务")
        else:
            print(f"回滚事务：{exc_type.__name__}")

        # False 表示不吞掉异常，异常仍会交给外层处理。
        return False


try:
    with Transaction():
        print("写入订单")
        raise ValueError("库存不足")
except ValueError as error:
    print(f"调用方处理错误：{error}")
