---

## Public and Private IP Address Checker

This Python script allows you to check your public and private IP addresses, as well as determine your NAT type using the STUN protocol. The script supports output in multiple languages, including Chinese (中文), English, French (Français), Russian (Русский), and Spanish (Español).

### Features
- Retrieve public IP address
- Retrieve private IP address
- Determine NAT type, external IP address, and external port
- Support for output in multiple languages

### Requirements
- Python 3.x
- `requests` library
- `stun` library

### Installation
Install the required libraries:

```bash
pip install requests
pip install stun
```

Download or clone this repository.

### Usage
Run the script:

```bash
python main.py
```

When prompted, choose the output language by entering the corresponding language name (e.g., 中文 for Chinese, English for English).

### Example Output
#### Chinese (中文)
```plaintext
公网ipv4地址: 114.5.1.4
私网ipv4地址: 172.20.10.3
NAT类型: Symmetric NAT
外部ipv4地址: 114.5.1.4
外部端口: 55118
ipv6地址: ['fe80::536a:b1e3:9889:271a', 'fe80::363d:afab:9e28:b7c6', 'fe80::f1c1:1b00:889c:66b0', 'fe80::2873:dac0:9870:a240', '2001:0:2841:fcb0:2873:dac0:9870:a240']
```

#### English
```plaintext
Public ipv4 Address: 115.192.45.67
Private ipv4 Address: 172.20.10.3
NAT Type: Symmetric NAT
External ipv4 Address: 115.192.45.67
External Port: 55152
IPv6 Address: ['fe80::536a:b1e3:9889:271a', 'fe80::363d:afab:9e28:b7c6', 'fe80::f1c1:1b00:889c:66b0', 'fe80::2873:dac0:9870:a240', '240e:0db8:85a3:0000:0000:8a2e:0370:7336']
```

#### French (Français)
```plaintext
Adresse ipv4 publique : 115.192.45.67
Adresse ipv4 privée : 172.20.10.3
Type de NAT : Symmetric NAT
Adresse ipv4 externe : 115.192.45.67
Port externe : 55155
Adresse IPv6: ['fe80::536a:b1e3:9889:271a', 'fe80::363d:afab:9e28:b7c6', 'fe80::f1c1:1b00:889c:66b0', 'fe80::2873:dac0:9870:a240', '240e:0db8:85a3:0000:0000:8a2e:0370:7336']
```

#### Russian (Русский)
```plaintext
Публичный ipv4-адрес: 115.192.45.67
Частный ipv4-адрес: 172.20.10.3
Тип NAT: Symmetric NAT
Внешний ipv4-адрес: 115.192.45.67
Внешний порт: 55155
IPv6 адрес: ['fe80::536a:b1e3:9889:271a', 'fe80::363d:afab:9e28:b7c6', 'fe80::f1c1:1b00:889c:66b0', 'fe80::2873:dac0:9870:a240', '240e:0db8:85a3:0000:0000:8a2e:0370:7336']
```

#### Spanish (Español)
```plaintext
Dirección ipv4 pública: 115.192.45.67
Dirección ipv4 privada: 172.20.10.3
Tipo de NAT: Symmetric NAT
Dirección ipv4 externa: 115.192.45.67
Puerto externo: 55155
Dirección IPv6: ['fe80::536a:b1e3:9889:271a', 'fe80::363d:afab:9e28:b7c6', 'fe80::f1c1:1b00:889c:66b0', 'fe80::2873:dac0:9870:a240', '240e:0db8:85a3:0000:0000:8a2e:0370:7336']
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### Contact
For any questions or suggestions, please open an issue or contact the repository owner.

---

