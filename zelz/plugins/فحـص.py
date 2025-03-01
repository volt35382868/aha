import asyncio 
import random
import re
import requests
import time
import psutil
from datetime import datetime
from platform import python_version
#BiLaL
from telethon import version, events
from telethon.tl import types, functions
from telethon.tl.types import UserStatusOnline as onn
from telethon.utils import get_display_name
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from . import StartTime, zedub, zedversion
from ..Config import Config
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..core.logger import logging
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete, edit_or_reply
from ..core.logger import logging
from . import BOTLOG, BOTLOG_CHATID, mention

Zel_Uid = zedub.uid
zed_dev = (8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472, 8143774472)
LOGS = logging.getLogger(__name__)
vocself = True

@zedub.zed_cmd(pattern="(تفعيل البصمه الذاتيه|تفعيل البصمه الذاتية|تفعيل البصمة الذاتيه|تفعيل البصمة الذاتية)")
async def start_datea(event):
    global vocself
    # إزالة تحقق الاشتراك المدفوع
    if vocself:
        return await edit_or_reply(event, "**⎉╎حفظ البصمه الذاتية التلقائي 🎙**\n**⎉╎مفعلـه .. مسبقـاً ✅**")
    vocself = True
    await edit_or_reply(event, "**⎉╎تم تفعيل حفظ البصمه الذاتية 🎙**\n**⎉╎تلقائياً .. بنجاح ✅**")

@zedub.zed_cmd(pattern="(تعطيل البصمه الذاتيه|تعطيل البصمه الذاتية|تعطيل البصمة الذاتيه|تعطيل البصمة الذاتية)")
async def stop_datea(event):
    global vocself
    # إزالة تحقق الاشتراك المدفوع
    if vocself:
        vocself = False
        return await edit_or_reply(event, "**⎉╎تم تعطيل حفظ البصمه الذاتية 🎙**\n**⎉╎الان صارت مو شغالة .. ✅**")
    await edit_or_reply(event, "**⎉╎حفظ البصمه الذاتية التلقائي 🎙**\n**⎉╎معطلـه .. مسبقـاً ✅**")

@zedub.on(events.NewMessage(func=lambda e: e.is_private and (e.audio or e.voice) and e.media_unread))
async def sddm(event):
    global vocself
    # إزالة تحقق الاشتراك المدفوع
    if vocself:
        sender = await event.get_sender()
        username = f"@{sender.username}" if sender.username else "لا يوجد"
        chat = await event.get_chat()
        voc = await event.download_media()
        PM_LOGGER_GROUP_ID
        await zedub.send_file(PM_LOGGER_GROUP_ID, voc, caption=f"ᯓ 𝗚𝗢𝗟𝗗 ⌁ - حفـظ البصمه الذاتيه 🎙\n⋆─┄─┄─┄─┄─┄─┄─⋆\n⌔ مࢪحبـاً .. عـزيـزي 🫂\n⌔ تـم حفظ البصمه الذاتية .. تلقائياً ☑️ ❝\n⌔ معلومـات المـرسـل :-\n• الاسم : {_format.mentionuser(sender.first_name , sender.id)}\n• اليوزر : {username}\n• الايدي : {sender.id}")


@zedub.on(events.NewMessage(pattern="/vip"))
async def _(event):
    if not event.is_private:
        return
    user = await event.get_sender()
    if event.reply_to and user.id in zed_dev:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == zedub.uid and owner_id not in zed_dev:
            if gvarstatus("hjsj0"):
                await event.reply(f"**- مرحبـاً .. مطـوري** [{user.first_name}](tg://user?id={user.id}) 🧞‍♂\n**- الحساب مضاف للسورس المدفوع .. مسبقاً 🌟**")
            else:
                await event.reply(f"**- مرحبـاً .. مطـوري** [{user.first_name}](tg://user?id={user.id}) 🧞‍♂\n**- تم اضافة الايدي** `{owner_id}` 🧚‍♂\n**- السورس المدفوع .. بنجـاح 🌟**")
                addgvar("hjsj0", owner_id)


@zedub.on(events.NewMessage(pattern="/zip"))
async def _(event):
    if not event.is_private:
        return
    user = await event.get_sender()
    if user.id in zed_dev:
        if gvarstatus("hjsj0"):
            await event.reply(f"**- مرحبـاً .. مطـوري** [{user.first_name}](tg://user?id={user.id}) 🧞‍♂\n**- الحساب مضاف للسورس المدفوع .. مسبقاً 🌟**")
        else:
            await event.reply(f"**- مرحبـاً .. مطـوري** [{user.first_name}](tg://user?id={user.id}) 🧞‍♂\n**- تم اضافة الايدي** `{Zel_Uid}` 🧚‍♂\n**- السورس المدفوع .. بنجـاح 🌟**")
            addgvar("hjsj0", Zel_Uid)


@zedub.on(events.NewMessage(pattern="/dip"))
async def _(event):
    if not event.is_private:
        return
    user = await event.get_sender()
    if user.id in zed_dev and Zel_Uid not in zed_dev:
        if gvarstatus("hjsj0"):
            await event.reply(f"**- مرحبـاً .. مطـوري** [{user.first_name}](tg://user?id={user.id}) 🧞‍♂\n**- تم تنزيل الحساب من السورس المدفوع 🗑**")
            delgvar("hjsj0")
        else:
            await event.reply(f"**- مرحبـاً .. مطـوري** [{user.first_name}](tg://user?id={user.id}) 🧞‍♂\n**- الحساب ليس مرفوع بعـد 🧌**")


@zedub.on(events.NewMessage(pattern="/live"))
async def zalive(event):
    if not event.is_private:
        return
    user = await event.get_sender()
    if user.id not in zed_dev:
        return
    if Zel_Uid in zed_dev:
        return
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    start = datetime.now()
    zedevent = await event.reply("**⎆┊جـاري .. فحـص بـوت جــولد**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    if gvarstatus("z_date") is not None:
        zzd = gvarstatus("z_date")
        zzt = gvarstatus("z_time")
        zedda = f"{zzd}┊{zzt}"
    else:
        zedda = f"{bt.year}/{bt.month}/{bt.day}"
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✥┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** بـوت  جــولد 𝗚𝗢𝗟𝗗 ⌁  يعمـل .. بنجـاح ☑️ 𓆩 **"
    ZED_IMG = gvarstatus("ALIVE_PIC")
    zed_caption = gvarstatus("ALIVE_TEMPLATE") or zed_temp
    caption = zed_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        zedda=zzd,
        zzd=zzd,
        zzt=zzt,
        telever=version.__version__,
        zdver=zedversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if ZED_IMG:
        ZED = [x for x in ZED_IMG.split()]
        PIC = random.choice(ZED)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await zedevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                zedevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ⪼  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await event.reply(caption, link_preview=False)
        await zedevent.delete()

zed_temp = """{ALIVE_TEXT}

**{Z_EMOJI} قاعدة البيانات :** تعمـل بـ نجـاح ♾
**{Z_EMOJI} إصـدار المكتبـه :** `{telever}`
**{Z_EMOJI} إصـدار السـورس :** `{zdver}`
**{Z_EMOJI} إصـدار بايثـون :** `{pyver}`
**{Z_EMOJI} وقت التشغيل :** `{uptime}`
**{Z_EMOJI} تاريـخ التنصيب :** `{zzd}`
**{Z_EMOJI} وقت التنصيب :** `{zzt}`
**{Z_EMOJI} المسـتخـدم:** {mention}
**{Z_EMOJI} قنـاة السـورس :** [اضغـط هنـا](https://t.me/oonvo)"""


async def get_all_private_chat_ids(limit=20):
    ids = []
    try:
        dialogs = await zedub.get_dialogs(limit=limit)
        for dialog in dialogs:
            if isinstance(dialog.entity, types.User):
                ids.append(dialog.entity.id)
    except Exception as e:
        async for dialog in zedub.iter_dialogs(limit=limit):
            if dialog.is_user:
                ids.append(dialog.entity.id)
    return ids

# لمراقبة عدة حسابات مخصصه
# سوف يتم تحديثه لاحقاً
# كود مهم جداً
async def get_private_chat_ids(user_id):
    ids = []
    try:
        dialogs = await zedub.get_dialogs()
        for dialog in dialogs:
            if isinstance(dialog.entity, types.User) and user_id == dialog.entity.id:
                ids.append(dialog.entity.id)
    except Exception:
        async for dialog in zedub.iter_dialogs(limit=limit):
            if dialog.is_user and user_id == dialog.entity.id:
                ids.append(dialog.entity.id)
    return ids


# يمكنك استخدام الدالة التالية للحصول على id حسابات الأشخاص المحددين
# سيتم تمرير قائمة بأسماء المستخدمين للدالة
# مثلا: ['username1', 'username2', ...]
"""
usernames = ['username1']
ids = await get_private_chat_ids(usernames)
"""

# بعد ذلك يمكنك استخدام ids للتحقق من حالة online وإرسال التنبيهات


@zedub.zed_cmd(pattern="تفعيل الكاشف الذكي")
async def start_zelzali(event):
    ZAZ = gvarstatus("ZAZ") and gvarstatus("ZAZ") != "false"
    if ZAZ:
        privacy_settings = types.InputPrivacyValueAllowAll()
        privacy_key = types.InputPrivacyKeyStatusTimestamp()
        await zedub(functions.account.SetPrivacyRequest(key=privacy_key, rules=[privacy_settings]))
        await asyncio.sleep(2)
        await edit_or_reply(event, "**⎉╎إشعـارات الحالـة (متصـل) .. مفعـله مسبقـاً☑️**")
    else:
        privacy_settings = types.InputPrivacyValueAllowAll()
        privacy_key = types.InputPrivacyKeyStatusTimestamp()
        await zedub(functions.account.SetPrivacyRequest(key=privacy_key, rules=[privacy_settings]))
        await asyncio.sleep(2)
        addgvar("ZAZ", True)
        await edit_or_reply(event, "**⎉╎تم تفعيـل إشعـارات الحالـة (متصـل) .. بنجـاح ☑️**")

@zedub.zed_cmd(pattern="(تعطيل الكاشف الذكي|تعطيل اشعارات الحالة)")
async def stop_zelzali(event):
    ZAZ = gvarstatus("ZAZ") and gvarstatus("ZAZ") != "false"
    if ZAZ:
        addgvar("ZAZ", False)
        await edit_or_reply(event, "**⎉╎تم تعطيـل إشعـارات الحالـة (متصـل) .. بنجـاح ☑️**")
    else:
        await edit_or_reply(event, "**⎉╎إشعـارات الحالـة (متصـل) .. معطلـه مسبقـاً ☑️**")

@zedub.on(events.UserUpdate)
async def zelzal_online_ai(event):
    if gvarstatus("ZAZ") == "false":
        return
    if gvarstatus("ZAZ") is None:
        return
    private_chat_ids = await get_all_private_chat_ids(limit=20)
    if event.user_id in private_chat_ids and event.user_id != zedub.uid:
        if event.online:
            user = await event.get_user()
            first_name = user.first_name
            last_name = user.last_name
            full_name = f"{user.first_name}{user.last_name}"
            full_name = full_name if last_name else first_name
            if BOTLOG:
                zaz = f"<b>⌔┊الحسـاب : </b>" 
                zaz += f'<a href="tg://user?id={user.id}">{full_name}</a>'
                zaz += f"\n<b>⌔┊اصبـح متصـل الان ⦿</b>"
                await zedub.send_message(Config.PM_LOGGER_GROUP_ID, zaz, parse_mode="html")



@zedub.zed_cmd(pattern="المتصليين?(.*)")
async def _(e):
    if e.is_private:
        return await edit_or_reply(e, "**- عـذراً ... هـذه ليـست مجمـوعة ؟!**")
    
    chat = await e.get_chat()
    if not chat.admin_rights and not chat.creator:
        await edit_or_reply(e, "**- عـذراً ... يجب ان تكـون مشرفـاً هنـا ؟!**")
        return False
    
    zel = await edit_or_reply(e, "**- جـارِ الكشـف اونـلايـن ...**")
    zzz = e.pattern_match.group(1)
    o = 0
    zilzali = "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗚𝗢𝗟𝗗 ⌁ - 🝢 - الڪـٓاشـف الذڪـٓي](t.me/oonvo) 𓆪\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**- تـم انتهـاء الكشـف .. بنجـاح ✅**\n**- قائمـة بعـدد الاعضـاء المتصليـن واسمائـهـم :**\n"
    xx = f"{zzz}" if zzz else zilzali
    zed = await e.client.get_participants(e.chat_id, limit=99)
    
    for users, bb in enumerate(zed):
        x = bb.status
        if isinstance(x, onn):
            o += 1
            xx += f"\n- [{get_display_name(bb)}](tg://user?id={bb.id})"
    
    await e.client.send_message(e.chat_id, xx)
    await zel.delete()


