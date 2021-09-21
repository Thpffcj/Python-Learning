from IPy import IP
import math
import pandas as pd
import psycopg2

ip_to_number = {}

def ip_in_segment(segment, ip):
    print(ip_to_number)
    if str(segment).find('/') != -1:
        new_segment = IP(segment)
        # 属于该网段
        if ip in new_segment:
            return True
    else:
        start = str(segment).split('-')[0]
        end = str(segment).split('-')[1]

        start_ip = str(start).split('.')
        end_ip = str(end).split('.')
        current_ip = str(ip).split('.')

        start_num = 0
        end_num = 0
        ip_num = 0
        for i in range(3):
            if start in ip_to_number:
                start_num = ip_to_number.get(start)
            else:
                start_num = start_num + int(start_ip[3 - i]) * int(math.pow(256, i))
                 

            if end in ip_to_number:
                end_num = ip_to_number.get(end)
            else:
                end_num = end_num + int(end_ip[3 - i]) * int(math.pow(256, i))

            if ip in ip_to_number:
                ip_num = ip_to_number.get(ip)
            else:
                ip_num = ip_num + int(current_ip[3 - i]) * int(math.pow(256, i))

        # 属于该网段
        if ((start_num <= ip_num) & (ip_num <= end_num)):
            return True

def start():
    segments = {
        '192.168.1.0/26': '银川供电公司',
        '10.216.248.0-10.216.248.255': '银川供电公司'
    }

    firewall = ['192.168.1.63', '192.168.1.64','10.216.248.255', '10.216.249.0', '192.168.1.63']

    organization = []
    cur_segment = []
    source_ip = []
    des_ip = []
    des_port = []

    for segment in segments:
        for ip in firewall:
            if ip not in source_ip:
                if (ip_in_segment(segment, ip)):
                    organization.append(segments[segment])
                    cur_segment.append(segment)
                    source_ip.append(ip)
                    des_ip.append('')
                    des_port.append('')


    dic = {'所属组织': organization,
           'IP网段': cur_segment,
           '源端IP': source_ip,
           '对端IP': des_ip,
           '对端端口': des_port
           }
    df = pd.DataFrame(dic)
    print(df)
    # df.to_excel('test.xlsx', index=False)


def connect_database():
    conn = psycopg2.connect(database="test", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    ## 建立游标，用来执行数据库操作
    cursor = conn.cursor()
    ## 执行SQL SELECT命令
    cursor.execute('select * from firewall')
    ## 获取SELECT返回的元组
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    ## 关闭游标
    cursor.close()
    ## 关闭数据库连接
    conn.close()

if __name__ == '__main__':
    # connect_database()
    start()











