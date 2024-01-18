import os
import jmcomic
from hoshino import Service
from hoshino.typing import CQEvent
from hoshino.config import NICKNAME
from jmcomic import JmAlbumDetail

sv = Service(
    name="禁漫ID转换为本子名",  # 功能名
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle="娱乐",  # 分组归类
    help_="发送【JM123456】触发，JM字母加数字id即可",  # 帮助说明

)
if type(NICKNAME) == str:
    NICKNAME = [NICKNAME]
path = os.path.join(os.path.dirname(__file__), 'config.yml')
client = jmcomic.create_option(path).new_jm_client()
print("初始化jm2name")


def create_all_messages_data(msg, ev: CQEvent):
    messages_data_list = [{
        "type": "node",
        "data": {
            "name": str(NICKNAME[0]),
            "user_id": str(ev.self_id),
            "content": str(msg)
        }
    }, {
        "type": "node",
        "data": {
            "name": str(NICKNAME[0]),
            "user_id": str(ev.self_id),
            "content": "这里是查询结果，若只显示这一句话则是被QQ拦截了。"
        }
    }]

    return messages_data_list


@sv.on_rex(r'^(JM|jm)\d+$')
async def I_dont_know_how_to_type_japanese(bot, ev: CQEvent):
    user_message = str(ev.message)
    target_numbers = user_message[2:]
    page = client.search_site(search_query=str(target_numbers))
    try:
        album: JmAlbumDetail = page.single_album
        send_messages_list = create_all_messages_data(album.name, ev)
        await bot.send_group_forward_msg(group_id=ev["group_id"], messages=send_messages_list)
    except Exception as e:
        print(e)
        send_messages_list = create_all_messages_data("未能查询到对应id，可能id不存在，或是需要登录才能浏览的隐藏本。", ev)
        await bot.send_group_forward_msg(group_id=ev["group_id"], messages=send_messages_list)
