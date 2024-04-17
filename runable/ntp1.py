import ntplib
from time import ctime

def get_ntp_time(server='pool.ntp.org'):
    try:
        client = ntplib.NTPClient()
        response = client.request(server)
        return ctime(response.tx_time)
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    ntp_server = 'pool.ntp.org'
    ntp_time = get_ntp_time(ntp_server)
    if ntp_time:
        print(f"NTP time from {ntp_server}: {ntp_time}")
