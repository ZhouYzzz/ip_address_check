import requests


def request_ip_info() -> dict:
  r = requests.get('http://ip-api.com/json')
  j = r.json()  # type: dict
  return j


def serialize_dict_to_string(d: dict) -> str:
  s = ['{key}: {value}'.format(key=k, value=v) for k, v in d.items()]
  s = '\n'.join(s)
  return s


if __name__ == '__main__':
  print(serialize_dict_to_string(request_ip_info()))
