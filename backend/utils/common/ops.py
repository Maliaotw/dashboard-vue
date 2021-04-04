from common.utils import request
import json


class Req:

    def healthz(self):
        return request.get('healthz')

    # SITE
    # ------------------------------------------------------------------------

    def get_site_list(self):
        return request.get('site')

    def create_site(self, data):
        '''op-site-tools'''
        return request.post('site', json=data)

    def get_site_bus_list(self, name):
        return request.get(f'site/{name}')

    # Domain
    # ------------------------------------------------------------------------

    def get_domain_list(self):
        return request.get('doamin')

    def create_domain(self, data):
        '''op-site-tools'''
        return request.post('doamin', json=data)

    def get_domain_Detail(self, name):
        return request.get(f'doamin/{name}')

    def create_domain_log(self, domain_id, status):
        return request.post('domainlog/create', json={'domain': domain_id, 'status': status})

    def update_domain_alert(self, name, status):
        '''
        name: str
        status: bool
        '''
        return request.put(f'domainalert/{name}/update', data=json.dumps({'status': status}))

    # REDIS
    # ------------------------------------------------------------------------

    def get_redis_bind_domain_list(self, name):
        '''獲取域名'''
        return request.get(f'redis/{name}', params={'type': 'domain'})

    def get_redis_bind_allow_ip(self, name):
        '''獲取後台白名單'''
        return request.get(f'redis/{name}', params={'type': 'allow_ip'})

    def create_redis_allow_ip(self, name, ip):
        '''添加後台白名單
        '''
        return request.post(f'redis/{name}', json={'ip': ip})

    def delete_redis_allow_ip(self, name, ip):
        '''刪除後台白名單
        '''
        return request.delete(f'redis/{name}', json={'ip': ip})

    # ALIYUN
    # ------------------------------------------------------------------------

    def get_aliyun_slb(self):
        return request.get('aliyun/slb')

    def get_aliyun_ssp_slb(self, name):
        return request.get(f'aliyun/ssp/{name}', params={'type': 'slb'})

    def get_aliyun_ssp_game(self, name):
        return request.get(f'aliyun/ssp/{name}', params={'type': 'game'})

    # CLOUDXNS
    # ------------------------------------------------------------------------

    def get_xns_list(self):
        '''以爬蟲進行模擬登入來篩選出哪些在高防
        @return:
        '''
        return request.get(f'xns')

    def get_xns_record(self, name):
        '''以API獲取線路紀錄
        @param name:
        @return:
        '''
        return request.get(f'xns/record/{name}')

    def update_xns_def_record(self, name, linkname):
        '''以API快速更改線路紀錄
        @param name:
        @param linkname:
        @return:
        '''
        if not linkname in ['slb', 'dproxy-cr1', 'dproxy-cr2', 'dproxy-cr3']:
            raise ValueError('輸入錯誤')
        return request.put(f'xns/record/{name}', data=json.dumps({'linkname': linkname}))

    def get_xns_record_detail(self, domain_id, name):
        """
        @param domain_id:
        @param name:
        @return:
        """
        return request.get(f'xns/{domain_id}', params={'name': name})

    def create_xns_record(self, domain_id, name, value, type):
        """以API新增解析紀錄
        @param domain_id: 域名ID
        @param name: 主機紀錄
        @param value: 記錄值
        @param type: 線路類型 (('A', 'A'), ('LINK', 'LINK'),('CNAME','CNAME'))
        @return:
        """
        return request.post('xns/create', json={"domain_id": domain_id, "name": name, "value": value, "type": type})

    def update_xns_record(self, record_id, name, value, type):
        """以API更改解析紀錄
        @param record_id: Record ID
        @param name: 主機紀錄
        @param value: 記錄值
        @param type: 線路類型 (('A', 'A'), ('LINK', 'LINK'),('CNAME','CNAME'))
        """
        return request.post('xns/create', json={"record_id": record_id, "name": name, "value": value, "type": type})

    # mail
    # ----------------------------

    def get_mail_quick(self):
        return request.get('quick')




    # Maintain
    # --------------------------
    def run_maintain_start(self, name, type, maintain_frontend, maintain_backend, maintain_start, maintain_end):
        '''

        @param name: 'cp998'
        @param type: 'fusion'
        @param maintain_frontend: "yes" or "no"
        @param maintain_backend: "yes" or "no"
        @param maintain_start: "2020/07/10 11:22"
        @param maintain_end: "2020/07/10 11:22"
        @return:
        '''
        data = {
            'name': name, 'type': type, 'maintain_frontend': maintain_frontend,
            'maintain_backend': maintain_backend, 'maintain_start': maintain_start, 'maintain_end': maintain_end
        }
        return request.post(f'maintain/start', json=data)

    def run_maintain_end(self, name, type):
        '''

        @param name: 'cp998'
        @param type: 'fusion'
        @return:
        '''
        data = {
            'name': name, 'type': type
        }
        return request.post(f'maintain/end', json=data)

    def get_maintain_satus(self, name):
        '''

        @param name: 'cp998'
        @return:
        '''
        return request.get(f'maintain/status', params={'name': name})


