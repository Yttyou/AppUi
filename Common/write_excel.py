import os

from Common.path_config import base_path
from TestCases.test_fan_list import data_lsit
from TestCases.test_chat import data_lsit2
import pandas as pd
def wtite_data():
    file_path = os.path.join(base_path, "automation script.xls")
    if os.path.exists(file_path):
        os.system("rm {} ".format(file_path))
    write = pd.ExcelWriter(file_path)
    d_f1 = data_lsit
    df1 = pd.DataFrame(d_f1)
    excel_header = ['执行顺序','模块名','脚本名称','脚本标题']#excel的标题
    df1.to_excel(write,sheet_name='NF',header=excel_header,index=False)

    d_f2 = data_lsit2
    df2 = pd.DataFrame(d_f2)
    df2.to_excel(write,sheet_name='聊天',header=excel_header,index=False)
    write.save()
