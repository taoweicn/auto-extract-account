import requests
import re
import time
from bs4 import BeautifulSoup


def purchase():
    url = 'http://t.54rj.com/result/'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0',
    }

    # 交易码
    bills = []

    is_mock = False
    mock_bills = []
    if is_mock:
        for i in range(348500, 348600):
            mock_bills.append(2018021121001004870263000000 + i)

    count = 1
    is_success = True
    print('密码统一为： zxc009')
    final_result = time.asctime(time.localtime(time.time())) + ' 购买了 ' + str(len(bills) * 6) + '个\n密码统一为： zxc009\n'
    for bill in mock_bills if is_mock else bills:
        result = requests.post(url, headers=headers, data='bill=' + str(bill))
        soup = BeautifulSoup(result.text, 'html.parser')
        reg_str = r'([\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+)'
        mod = re.compile(reg_str)
        items = mod.findall(str(soup.textarea))
        if not items:
            is_success = False
            print('第' + str(bills.index(bill) + 1) + '个未提取到！')

        for item in items:
            print('账户', str(count), ': ', item[0][:-10])
            final_result += '账户' + str(count) + ': ' + item[0][:-10] + '\n'
            count += 1

    if is_success:
        purchase_records = open('data/manual_purchase_records.txt', 'a+')
        purchase_records.write(final_result)
        purchase_records.close()


purchase()
