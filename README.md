---

# Nat_python
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
请选择输出语言（中文/English/Français/Русский/Español）： 中文
公网IP地址: 203.0.113.1
私网IP地址: 192.168.1.2
NAT类型: Full Cone NAT
外部IP地址: 203.0.113.1
外部端口: 54321
```

#### English
```plaintext
Please choose the output language (中文/English/Français/Русский/Español): English
Public IP Address: 203.0.113.1
Private IP Address: 192.168.1.2
NAT Type: Full Cone NAT
External IP Address: 203.0.113.1
External Port: 54321
```

#### French (Français)
```plaintext
Veuillez choisir la langue de sortie (中文/English/Français/Русский/Español): Français
Adresse IP publique : 203.0.113.1
Adresse IP privée : 192.168.1.2
Type de NAT : Full Cone NAT
Adresse IP externe : 203.0.113.1
Port externe : 54321
```

#### Russian (Русский)
```plaintext
Пожалуйста, выберите язык вывода (中文/English/Français/Русский/Español): Русский
Публичный IP-адрес: 203.0.113.1
Частный IP-адрес: 192.168.1.2
Тип NAT: Full Cone NAT
Внешний IP-адрес: 203.0.113.1
Внешний порт: 54321
```

#### Spanish (Español)
```plaintext
Por favor, elija el idioma de salida (中文/English/Français/Русский/Español): Español
Dirección IP pública: 203.0.113.1
Dirección IP privada: 192.168.1.2
Tipo de NAT: Full Cone NAT
Dirección IP externa: 203.0.113.1
Puerto externo: 54321
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### Contact
For any questions or suggestions, please open an issue or contact the repository owner.

---

