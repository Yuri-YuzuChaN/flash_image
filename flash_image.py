import hoshino
from hoshino import Service
from hoshino.typing import CQEvent
import re

sv = Service('flash_image', enable_on_default=False, visible=True)

@sv.on_message()
async def get_flash_image(bot, ev:CQEvent):
    if 'type=flash' not in str(ev.message[0]):
        return
    if ev.user_id == hoshino.config.SUPERUSERS[0]:
        return
    file = re.match(r"\[CQ:image,type=flash,file=(.*)\]", str(ev.message))
    md5 = file.group(1)[:-6].upper()
    
    img = f'闪照内容：[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/0-0-{md5}/0?term=2]'
    
    await bot.send(ev, img)
