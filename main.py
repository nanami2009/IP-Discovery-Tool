import requests  # 导入requests库，用于发送HTTP请求
import socket  # 导入socket库，用于网络通信
import stun  # 导入stun库，用于获取NAT类型和外部IP地址

# 获取公网IP地址
def get_public_ip():
    try:
        # 通过访问api.ipify.org获取公网IP地址
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException:
        # 如果请求失败，返回None
        return None

# 获取私网IP地址
def get_private_ip():
    try:
        # 创建一个UDP socket连接到Google的DNS服务器
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('223.5.5.5', 80))
        # 获取本地IP地址
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error:
        # 如果获取失败，返回None
        return None

# 获取NAT类型
def get_nat_type():
    try:
        # 使用STUN协议获取NAT类型、外部IP地址和外部端口
        nat_type, external_ip, external_port = stun.get_ip_info()
        return nat_type, external_ip, external_port
    except Exception as e:
        # 如果获取失败，返回错误信息
        return str(e), None, None

def get_ipv6():
    host_name = socket.gethostname()
    addresses = socket.getaddrinfo(host_name, None, socket.AF_INET6)
    ipv6_addresses = [addr[4][0] for addr in addresses]
    return ipv6_addresses

if __name__ == '__main__':
    # 让用户选择输出语言
    while True:
        language = input("请选择输出语言(1.中文/2.English/3.Français/4.Русский/5.Español/q.exit): ").strip().lower()

        if language == 'q':
            print("Now you are quitting this process.")
            print("Thank you!")
            break

        # 获取并打印公网IP地址
        public_ip = get_public_ip()
        private_ip = get_private_ip()
        nat_type, external_ip, external_port = get_nat_type()
        ipv6_addresses = get_ipv6()

        if language == '1':
            # 输出中文结果
            print(f"公网ipv4地址: {public_ip}")
            print(f"私网ipv4地址: {private_ip}")
            print(f"NAT类型: {nat_type}")
            print(f"外部ipv4地址: {external_ip}")
            print(f"外部端口: {external_port}")
            print(f"ipv6地址: {ipv6_addresses}")
        elif language == '2':
            # 输出英文结果
            print(f"Public ipv4 Address: {public_ip}")
            print(f"Private ipv4 Address: {private_ip}")
            print(f"NAT Type: {nat_type}")
            print(f"External ipv4 Address: {external_ip}")
            print(f"External Port: {external_port}")
            print(f"IPv6 Address: {ipv6_addresses}")
        elif language == '3':
            # 输出法文结果
            print(f"Adresse ipv4 publique : {public_ip}")
            print(f"Adresse ipv4 privée : {private_ip}")
            print(f"Type de NAT : {nat_type}")
            print(f"Adresse ipv4 externe : {external_ip}")
            print(f"Port externe : {external_port}")
            print(f"Adresse IPv6: {ipv6_addresses}")
        elif language == '4':
            # 输出俄文结果
            print(f"Публичный ipv4-адрес: {public_ip}")
            print(f"Частный ipv4-адрес: {private_ip}")
            print(f"Тип NAT: {nat_type}")
            print(f"Внешний ipv4-адрес: {external_ip}")
            print(f"Внешний порт: {external_port}")
            print(f"IPv6 адрес: {ipv6_addresses}")
        elif language == '5':
            # 输出西班牙文结果
            print(f"Dirección ipv4 pública: {public_ip}")
            print(f"Dirección ipv4 privada: {private_ip}")
            print(f"Tipo de NAT: {nat_type}")
            print(f"Dirección ipv4 externa: {external_ip}")
            print(f"Puerto externo: {external_port}")
            print(f"Dirección IPv6: {ipv6_addresses}")
        else:
            # 无效的语言选择
            print("Invalid language selection. Please choose the right language.")
