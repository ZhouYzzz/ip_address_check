from gmail_api import get_service, send_message, get_personal_email_address
from messages import create_message_raw
from ip_address_check import request_ip_info, serialize_dict_to_string


HOST_NAME = 'Untitled Server'


def main():
  ip_info = request_ip_info()
  if ip_info['status'] == 'success':
    ip = ip_info['query']
    detailed_info = serialize_dict_to_string(ip_info)

    service = get_service()
    email_add = get_personal_email_address(service)
    # print(email_add)
    # return
    mess_raw = create_message_raw(sender=email_add,
                                  to=email_add,
                                  subject='[IP Address Check] - [{Host}] - [{IP}]'.format(Host=HOST_NAME, IP=ip),
                                  message_text=detailed_info)
    # print(mess_raw)
    # return
    mess_id = send_message(service, user_id='me', message_raw=mess_raw)
    print(mess_id)
  else:
    raise ConnectionError('Network Failure')


if __name__ == '__main__':
  main()
