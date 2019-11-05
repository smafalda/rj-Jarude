import requests
import boxsdk
from boxsdk import DevelopmentClient
import xlrd
from boxsdk import JWTAuth


auth = JWTAuth(
    client_id='jwlxr4bndsxby3zds6oatu1fwk58o3pt',
    client_secret='hJUxFdT2GDIQ84YyDUGingPdQKgWuwU6',
    enterprise_id='1760289',
    jwt_key_id='5sbvLtQ9tmywT5lV0Qmv8RL0lj4N9ihI',
    rsa_private_key_file_sys_path='MIIEpQIBAAKCAQEA0ak1ng2oRpstHxx+8F+9slfjnn9Asp4mKjQ4MyGtAns/kj786OPdR3tOJXe8DYZ1NiTrGzTb47TD3PbBWdZfoVgpv0AreirgQ76zzLIzFkUqMuFfPEF2iN87H8UJqiTOtZqB0Mqngp7NyRri3NGYNB2R8FzHCa/AXV/w0ZJyUHs1cC3YTQ/wBBsgk1e2Yqu2UOL5k/Phf+GxmJeWgJ6fs4W2AkJujW7KVe0Gn1CrNMN5mDazP2P/FFhPWW9mfSY542wbeTFLDl+2brM7pZvZ+EGyojTXfl4cAMed4dRwJuzZ1bpqB7Y177UkzPw51zLHvPz1zZnLyhxyqY2guZk8WQIDAQABAoIBADNW6/o3/ezMMtBbefoCd8EkJGi7YGxcrZvIDbr3lBX3eCmnouakZZsLZqdmGnZ1Zl5LzAZteyrXKN8CzXXiOKiZnh9m5z6TITd1izGksT3S0fKDnX5zyULa5u9woF05hiSSIReviDVEDcAhBUxtRof8dbAWB+cnUkOLKr0mzzdFgukER7FcXR6yxOGDs7D6R1pIVqRIcV8BcWj2G28El8cKBqqLRqnB+6yujvGzKVqh5A9+beRbz6ZG1xl46Yd+LZaV66BGeNkmVkM8jzFzj+0+Y2ZCgKwXYO3v0yVWiCI6F+WmWIhWhsA+7p3uPiRvaf99UwVcyFREjPpnhchuvwECgYEA6b9P+G0GdC1sEK5Gymfe5uEn/UEb2uvsmhLaUc+6lS/FmHU+qAzNfcpAQ41Uzq1HHmnZqm47YiubPaypGmrb15a0L5WYkROfG1ChFzvFkXcZgltCFitHZRZrfR/b+zDkhOkJ28MEIy9Bal0jVmOYSlLSHnZKrDN9p/wgzybaf60CgYEA5Z7itm/sqqAQwn2PLgK+o7f3dh/PxJvTI5uRzvI697Jt93Kx03Bpkj7w+rULgnd7Wyi1YyAgYalWQGC272o5M8VjZ1LYY7diLbl2qnFzOvbYzOq263XtagFRpWWtM/3oxsNep466grEMHwycdenQ4TqTs9IUdNHiaK8j0ZLtlN0CgYEAjW90TSZzHEMLu4AoV3rIVj1w+/20hB/zFztHHO+rv2+biWeQFRFCGdYSUo2m/jO877suuMBgcENgeM4LuG9mPKn0t0I2gbo0sMt13eAN6Ln/FnBvqYhgd9s8CQcJDZIFBCMaEv6Kd1u1ok1e/3vd/0Lj3wjGoDG727RkidPBrDUCgYEAv+rkooc50AKo/2XiXhp9LGl+s4QzK6jx+Dj2zXk4P/8qWj/K0WaLVmi1EVZwoEMtHywPLyKS7g2SwYwUWlb2KIc6ZgmgQvfrXzw8KolYPlhDLEKhUHvoS0l+7DbnZSU7gaWZX4Kz8Lf54Zmwy/z5UMac3RchceJa0hRQY8HiQSECgYEA02NbFwT517H0aMiQntXCKbimpxPbjtfkK7m49o4O4AFM2H3VAJuho3Xi+nAwHNJ6JZOcZgWfB0Tl4ShXxEhuvFzLMtt8nc8qvimLSRUOYgvBY9suwbwKzYDVcthwJsd1vEZJdIheKGGjj5IdW/E8gFPHTqsSGR95tzEIhG4yRdU=',
    rsa_private_key_passphrase='',
)
access_token = auth.authenticate_instance()

#from boxsdk import Client

#client = Client(auth)
#items = client.folder(folder_id='31436627801').get_items()
#idArq = items.get('id')

#file_info = client.file(isArq).get()
#if file_info.get('nome')=='ARC':#aqui passa a comparação do nome do arquivo
    #box_file = client.file(file_id=idArq).get()
    #output_file = open(box_file.name, 'wb')
    #box_file.download_to(output_file)