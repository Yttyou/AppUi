from Common.get_to_sendemail import get_email_msg
import json
import requests

# 定义bug输出样式
bc_bug_content = '''**`{filename} 包` `功能回歸`測試報告**（測試時間：{start_time} - {end_time}）
---
測試設備：`{device_name}` | 系統版本：`{os_ver}`｜軟件版本：`{pkg_ver}`
        ---
**影響發版的問題：**
發現 `{len_bug}` 個 Bug 分佈如下，**[點擊可查看詳情](http://117.50.36.141/#/home/buglist)**
> {bug_detail_contet}

---
[點擊可查看詳細報告](http://117.50.36.141/#/home/overall)'''

bc_nobug_content = '''**`{filename} 包` `功能回歸`測試報告**（測試時間：{start_time} - {end_time}）
---
測試設備：`{device_name}` | 系統版本：`{os_ver}`｜軟件版本：`{pkg_ver}`
---
**測試 `100%` 通過，軟件可`正常發佈`**
---
[點擊可查看詳細報告](http://117.50.36.141/#/home/overall)'''


class AllureReportPush:

    def __init__(self):
        # self.PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc'
        self.PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/b8e14da1dafcebef91b78b9779779f9f'

    def get_bchook_content(self):
        # 设置 JSON 格式推送消息体
        allure_content = get_email_msg()[1]
        if allure_content[-2]:
            print(allure_content)
            bug_detail_contet = allure_content[-1].replace('Bug ', 'Bug') \
                .replace('Bug', ' Bug: `').replace('個', '` 个').replace('|', ' | ')
            webhook_content = bc_bug_content.format(filename=allure_content[0].replace('包', ''),
                                                    start_time=allure_content[1],
                                                    end_time=allure_content[2],
                                                    device_name=allure_content[3], os_ver=allure_content[4],
                                                    pkg_ver=allure_content[5],
                                                    len_bug=allure_content[6], bug_detail_contet=bug_detail_contet)
        else:
            webhook_content = bc_nobug_content.format(filename=allure_content[0].replace('包', ''),
                                                      start_time=allure_content[1],
                                                      end_time=allure_content[2],
                                                      device_name=allure_content[3], os_ver=allure_content[4],
                                                      pkg_ver=allure_content[5])
        return webhook_content

    def allure_report_pusher(self):
        #推送到BC
        webhook_content = self.get_bchook_content()
        push_payload = json.dumps({"text": webhook_content})
        header = {"Content-Type": "application/json"}
        requests.post(self.PUSH_WEB_HOOK, data=push_payload, headers=header)


if __name__ == '__main__':
    AllureReportPush().allure_report_pusher()

