import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v', '--capture=sys'])
    # 跑單項測試案例
    # pytest.main(['-s', '-v', '--capture=sys', 'accountManage/test_userLog.py'])