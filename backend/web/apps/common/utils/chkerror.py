

def except_handle(err):
    import sys
    import traceback
    error_class = err.__class__.__name__  # 取得錯誤類型
    detail = err.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    fileName = lastCallStack[0]  # 取得發生的檔案名稱
    lineNum = lastCallStack[1]  # 取得發生的行號
    funcName = lastCallStack[2]  # 取得發生的函數名稱
    errMsg = "-" * 100 + f"\n File \"{fileName}\",\n Line: {lineNum},\n In {funcName}: [{error_class}]\n {detail} \n" + "-" * 100
    return errMsg
