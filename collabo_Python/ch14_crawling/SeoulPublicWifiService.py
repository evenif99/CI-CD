# 서울 열린 데이터 광장
# https://data.seoul.go.kr/
# 검색 키워드 : 서울 와이파이
# 목표 : 서울시 공공와이파이 서비스 위치 정보
# https://data.seoul.go.kr/dataList/OA-20883/S/1/datasetView.do
# 정보 crawling으로 csv 파일 제작하기

import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd

API_KEY = "466d466a5664696e39347765774863" # 발급 받은 API 인증키

def fetch_seoul_wifi_data():
    BASE_URL = f"http://openapi.seoul.go.kr:8088/{API_KEY}/xml/TbPublicWifiInfo/"
    print(BASE_URL)

    start_index = 1
    batch_size = 1000
    wifi_list = []

    while True:
        end_index = start_index + batch_size - 1
        print(f'시작 인덱스 : {start_index}, 끝 인덱스 : {end_index}')

        url = BASE_URL + str(start_index) + '/' + str(end_index) + '/'
        print(url)
        response = requests.get(url)  # 응답 받은 객체

        if response.status_code != 200: # 성공 못함
            print(f'데이터 패치 못함, 응답 상태 코드 : {response.status_code}')
            break
        # end if

        try:
            root = ET.fromstring(response.text)
            result_code = root.find('RESULT/CODE')
            if result_code is not None and result_code.text != 'INFO-000':
                print('API Error :', root.find('RESULT/MESSAGE').text)
                break
            # end inner for

            rows = root.findall('.//row')
            print(len(rows))
            if not rows:
                break
            # end if

            # 사전으로 변환하여 key 할당 후 value를 path값을 할당
            for onewifi in rows:
                subdata = [
                    onewifi.findtext('X_SWIFI_MGR_NO', 'N/A'),
                    onewifi.findtext('X_SWIFI_WRDOFC', 'N/A'),
                    onewifi.findtext('X_SWIFI_MAIN_NM', 'N/A'),
                    onewifi.findtext('X_SWIFI_ADRES1', 'N/A'),
                    onewifi.findtext('X_SWIFI_ADRES2', 'N/A'),
                    onewifi.findtext('X_SWIFI_INSTL_FLOOR', 'N/A'),
                    onewifi.findtext('X_SWIFI_INSTL_TY', 'N/A'),
                    onewifi.findtext('X_SWIFI_INSTL_MBY', 'N/A'),
                    onewifi.findtext('X_SWIFI_SVC_SE', 'N/A'),
                    onewifi.findtext('X_SWIFI_CMCWR', 'N/A'),
                    onewifi.findtext('X_SWIFI_CNSTC_YEAR', 'N/A'),
                    onewifi.findtext('X_SWIFI_INOUT_DOOR', 'N/A'),
                    onewifi.findtext('X_SWIFI_REMARS3', 'N/A'),
                    onewifi.findtext('LAT', 'N/A'),
                    onewifi.findtext('LNT', 'N/A'),
                    onewifi.findtext('WORK_DTTM', 'N/A')
                ]
                wifi_list.append(subdata)
            # end for

            start_index += batch_size

        except ET.ParseError as err:
            print(f'Xml 파싱 오류 : {err}')
            break
        # end try
    # end while

    print(f'데이터 갯수 : {len(wifi_list)}')
    print(f'자료 유형 : {type(wifi_list)}')

    return wifi_list
# end def
def save_to_csv(wifi_list, file_name):
    wifi_columns = ['관리번호', '자치구', '와이파이명', '도로명주소', '상세주소', '설치위치(층)', '설치유형', '설치기관', '서비스구분', '망종류', '설치년도', '실내외구분', 'wifi접속환경', 'Y좌표', 'X좌표', '작업일자']
    wifi_frame = pd.DataFrame(wifi_list, columns=wifi_columns)
    wifi_frame.to_csv(file_name, index=False, encoding='utf-8-sig')
    print(f'파일 저장 : {file_name}')
# end def save_to_csv

data = fetch_seoul_wifi_data()

dataOut = './../dataOut/'
filename = dataOut + 'seoul_wifi_location.csv'
save_to_csv(data, filename)