import csv
import os
import json
import requests
import pandas as pd
import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

process_list_complete = []


def get_process_list_trial():
    """
    It generates the csv file containing the following parameter about the processes:
    a. processID
    b. creationTime
    c. startBlock
    d. endBlock
    e. entityId
    """

    url = "https://gw1.dev.vocdoni.net/dvote"
    a = True
    b = 0
    f = csv.writer(open("process.csv", "w"))
    f.writerow(['entityId', 'entityIndex', 'processId',
                'creationTime', 'startBlock', 'endBlock'])
    while a:
        params = {"request": {"from": b, "method": "getProcessList",
                              "sourceNetworkId": "", }, "id": "847", }
        process_list_response = requests.post(
            url=url, data=json.dumps(params)).json()
        process_list = process_list_response['response']['processList']

        for i in range(0, len(process_list)):
            process_list_complete.append(process_list[i])
            params1 = {"request": {"method": "getProcessInfo",
                                   "processId": process_list[i], }, "id": "410", }
            process_list_data = requests.post(
                url=url, data=json.dumps(params1)).json()
            process_info = process_list_data['response']['process']
            f.writerow([process_info['entityId'],
                        process_info['entityIndex'],
                        process_info['processId'],
                        process_info['creationTime'],
                        process_info['startBlock'],
                        process_info['endBlock']])
        b += 64
        if len(process_list) < 64:
            a = False


def get_votes():
    """
    It generates the csv file containing the following parameter about the Votes(Envelopes):
    a. process_id
    b. nullifier
    c. height
    d. weight
    """
    url = "https://gw1.dev.vocdoni.net/dvote"
    f = csv.writer(open("votes.csv", "w"))
    f.writerow(['process_id', 'nullifier', 'height', 'weight'])

    for i in range(0, len(process_list_complete)):
        c = True
        d = 0
        while c:
            time.sleep(5)
            params1 = {"request": {"from": d, "method": "getEnvelopeList",
                                   "processId": process_list_complete[i]}, "id": "356", }
            envelope_list_data = requests.post(
                url=url, data=json.dumps(params1), verify=False).json()
            if 'envelopes' in envelope_list_data['response'].keys():
                envelope_list = envelope_list_data['response']['envelopes']

                for j in range(0, len(envelope_list)):
                    time.sleep(5)
                    params2 = {"request": {"method": "getEnvelope",
                                           "nullifier": envelope_list[j]['nullifier']}, "id": "81", }
                    nullifier_details = requests.post(
                        url=url, data=json.dumps(params2), verify=False).json()
                    nullifier_info = nullifier_details['response']['envelope']
                    f.writerow([envelope_list[j]['process_id'],
                                envelope_list[j]['nullifier'],
                                envelope_list[j]['height'],
                                nullifier_info['weight']])

                d += 64
                if len(envelope_list) < 64:
                    c = False
            else:

                c = False


if __name__ == "__main__":
    print('Generating Process data')
    get_process_list_trial()
    print('Done!!')
    print(
        f'The number of processes in the list are: {len(process_list_complete)}')
    print('Generating Votes data')
    get_votes()
    print('Done!!')
