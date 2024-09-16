# Nat_python
Sure! Here's a sample README file in English for your Python script:

---

# Public and Private IP Address Checker

This Python script allows you to check your public and private IP addresses, as well as determine your NAT type using the STUN protocol. The script supports output in both Chinese (zh-cn) and English (en-us).

## Features

- Retrieve public IP address
- Retrieve private IP address
- Determine NAT type, external IP address, and external port
- Support for output in Chinese and English

## Requirements

- Python 3.x
- `requests` library
- `stun` library

## Installation

1. Install the required libraries:
    ```sh
    pip install requests
    pip install stun
    ```

2. Download or clone this repository.

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. When prompted, choose the output language by entering `zh-cn` for Chinese or `en-us` for English.

## Example Output

### Chinese (zh-cn)
```
请选择输出语言 (zh-cn/en-us): zh-cn
公网IP地址: 203.0.113.1
私网IP地址: 192.168.1.2
NAT类型: Full Cone NAT
外部IP地址: 203.0.113.1
外部端口: 54321
```

### English (en-us)
```
请选择输出语言 (zh-cn/en-us): en-us
Public IP Address: 203.0.113.1
Private IP Address: 192.168.1.2
NAT Type: Full Cone NAT
External IP Address: 203.0.113.1
External Port: 54321
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Feel free to modify this README file to better suit your needs. If you have any other questions or need further assistance, let me know!
