__author__ = 'Areo'
from TestFiles import allure_data_cal, allure_report_pusher, mem_consum_monitor, flow_consum_monitor
from TestFiles import allure_report_pusher_group
from Common import get_to_sendemail

if __name__ == '__main__':
    testrun_id = allure_data_cal.read_id()
    allure_data_cal.category_cal(testrun_id)  # 分类统计数据
    allure_data_cal.covered()  # 按 BP 统计覆盖、Passed、Failed 的情况
    allure_data_cal.rate_cal()  # 计算覆盖率，通过率
    allure_data_cal.zip_reconstruct(testrun_id)  # 重构 allure report
    allure_data_cal.del_ss()  # 删除超过期限的截图，防止撑爆硬盘

    # 数据读取，数据推送，数据的存储
    allure_report_pusher.load_jsons()  # 读取 json 文件
    # removed @ 2020.4
    # allure_report_pusher.init_po_push_payload()  # PO 报告内容
    # allure_report_pusher.init_qa_push_payload()  # QA 报告内容
    # allure_report_pusher.push_to_bearychat_po()  # 推送 PO 报告
    # allure_report_pusher.push_to_bearychat_qa()  # 推送 QA 报告
    allure_report_pusher.save_to_database()  # 存储数据至 MySql
    # allure_report_pusher.save_showdoc_page() #removed @ 2020.4

    # allure_report_pusher_group.load_json()
    # allure_report_pusher_group.init_push_text()
    # allure_report_pusher_group.push_to_bearychat()
    # 推送测试报告到 BC
    allure_report_pusher_group.AllureReportPush().allure_report_pusher()

    # 推送流量及内存监控报告到 BC
    flow_consum_monitor.run()
    mem_consum_monitor.run()

    # 发送邮件报告附带 PDF 测试报告
    get_to_sendemail.main_pdf_email()
