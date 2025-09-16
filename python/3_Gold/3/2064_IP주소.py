def ip_to_bin(ip): # 10진수 -> 2진수 변환 하는 그림 설명 만들기
    return ''.join([f'{int(x):08b}' for x in ip.split('.')])

def bin_to_ip(bin_str): # 2진수 -> 10진수 변환 하는 그림 설명 만들기
    return '.'.join([str(int(bin_str[i:i+8], 2)) for i in range(0, 32, 8)])

def find_network_address(ips): 
    bin_ips = [ip_to_bin(ip) for ip in ips] # 이미지 설명 필요
    
    # 공통된 접두사 찾기
    network_prefix = bin_ips[0] # 첫 아이피 고정 시키기
    for ip in bin_ips[1:]: 
        # 두 IP의 공통 접두사 구하기
        i = 0
        while i < len(network_prefix) and network_prefix[i] == ip[i]:
            i += 1
        network_prefix = network_prefix[:i]
    
    # 네트워크 주소는 공통된 접두사 + 나머지 부분을 0으로 채운 것
    network_address = network_prefix + '0' * (32 - len(network_prefix))
    
    # 네트워크 마스크는 공통된 접두사 길이만큼 1, 나머지는 0으로 채운 것
    subnet_mask = '1' * len(network_prefix) + '0' * (32 - len(network_prefix))
    
    return bin_to_ip(network_address), bin_to_ip(subnet_mask)

# 입력 처리
n = int(input())
ips = [input().strip() for _ in range(n)]

# 네트워크 주소와 마스크 계산
network_address, subnet_mask = find_network_address(ips)

# 결과 출력
print(network_address)
print(subnet_mask)