#本代码实现功能：更好的优化下载数据，确保没有丢失
import time
import tushare as ts
pro = ts.pro_api()



    # 通过提供交易日数据'cal_date',以参数ts_code的形式下载get_daily
    # https://tushare.pro/document/2?doc_id=27

def get_daily(ts_code,start_date,end_date):
    for _ in range(3):
        try: #尝试获取数据
            df = pro.daily(ts_code = ts_code, start_date = start_date, end_date = end_date)

        except: #如果抛出异常，冷静1秒再try
            time.sleep(1)

        else: #如果顺利的没有抛出异常，返回结果吧亲。
            return df