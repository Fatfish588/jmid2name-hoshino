"""
该脚本的作用：测试当前ip可以访问哪些禁漫域名
"""
import jmcomic
from jmcomic import *

option = jmcomic.create_option('config.yml')

meta_data = {
    # 'proxies': ProxyBuilder.clash_proxy()
}

disable_jm_log()


def get_domain_ls():
    template = 'https://jmcmomic.github.io/go/{}.html'
    url_ls = [
        template.format(i)
        for i in range(300, 309)
    ]
    domain_set: Set[str] = set()

    def fetch_domain(url):
        from curl_cffi import requests as postman
        text = postman.get(url, allow_redirects=False, **meta_data).text
        for domain in JmcomicText.analyse_jm_pub_html(text):
            if domain.startswith('jm365.work'):
                continue
            domain_set.add(domain)

    multi_thread_launcher(
        iter_objs=url_ls,
        apply_each_obj_func=fetch_domain,
    )
    return domain_set


domain_set = get_domain_ls()
domain_status_dict = {}
print(f'获取到{len(domain_set)}个域名，开始测试')


def test_domain(domain: str):
    client = option.new_jm_client(domain_list=[domain], **meta_data)
    status = 'ok'

    try:
        client.get_album_detail('123456')
    except Exception as e:
        status = str(e.args)
        pass

    domain_status_dict[domain] = status


multi_thread_launcher(
    iter_objs=domain_set,
    apply_each_obj_func=test_domain,
)

for domain, status in domain_status_dict.items():
    print(f'{domain}: {status}')

