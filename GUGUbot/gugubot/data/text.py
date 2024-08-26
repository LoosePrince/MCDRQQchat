PLUGIN_METADATA = {
    'id': 'gugubot',
    'version': '1.1.3',
    'name': 'GUGUbot',
    'description': 'A bot connect mc and QQ',
    'author': 'XueK__',
    'dependencies': {
        'cool_q_api': '*',
    }
}
DEFAULT_CONFIG = {
    'group_id': [1234561, 1234562],
    'admin_id': [1234563, 1234564],
    'admin_group_id': [123321, 456654],
    'server_name': '',
    'is_main_server': True,
    'bound_notice': True,
    'whitelist_add_with_bound': False,
    'whitelist_remove_with_leave': True,
    'game_ip':'',
    'game_port':'',
    'font_limit':150,
    'command_prefix': "#",
    'style': '正常',
    'forward': {
        'mc_to_qq': True,
        'qq_to_mc': True
        },
    'command': {
        'list': True,
        'mc': True,
        'qq': True,
        'ban_word': True,
        'key_word': True,
        'ingame_key_word': True,
        'name':True,
        'whitelist':True,
        'shenhe':True
        },
    'dict_address' : {
        "bound_image_path": ".//config//GUGUbot//bound.jpg",
        'font_path': ".//config//GUGUbot//MicrosoftYaHei-01.ttf",
        "start_command_dict": './/config//GUGUbot//start_commands.json',
        "key_word_dict": './/config//GUGUbot//key_word.json',
        "ban_word_dict": './/config//GUGUbot//ban_word.json',
        "key_word_ingame_dict": './/config//GUGUbot//key_word_ingame.json',
        "uuid_qqid": './/config//GUGUbot//uuid_qqid.json',
        "whitelist": './/server//whitelist.json',
        "shenheman":'.//config//GUGUbot//shenheman.json',
        'shenhe_log':'.//config//GUGUbot//shenhe_log.txt'
        }
}

group_help_msg = '''命令帮助如下:
#玩家 -> 获取在线玩家列表
#假人 -> 获取在线假人列表
#服务器 -> 同时获取在线玩家和假人列表
#绑定 <游戏ID> -> 绑定你的游戏ID
#mc <消息> -> 向游戏内发送消息（可以触发游戏内关键词）
#风格 -> 机器人风格帮助
#游戏关键词 列表 -> 显示现有游戏内关键词列表
#删除假人 <假人名字> -> 删除游戏内指定假人

关键词相关：
#添加 <关键词> <回复> -> 添加游戏内关键词回复
#添加图片 <关键词> -> 添加关键词图片
#删除 <关键词> -> 删除关键词
#列表 -> 获取关键词回复列表
帮助 -> 查看关键词相关帮助
'''

admin_help_msg = '''管理员命令帮助如下
#绑定   -> 查看绑定相关帮助
#白名单 -> 查看白名单相关帮助
#启动指令 -> 查看启动指令相关帮助
#违禁词 -> 查看违禁词相关帮助
#关键词 -> 查看关键词相关帮助
#游戏内关键词 -> 查看游戏内关键词相关帮助
#uuid   -> 查看uuid 匹配相关帮助
#名字   -> 查看机器人名字相关帮助
#审核   -> 协助审核功能
'''

bound_help = '''#绑定 列表 -> 查看绑定列表
#绑定 查询 <QQ号> -> 查询绑定ID
#绑定 解绑 <QQ号> -> 解除绑定
#绑定 <QQ号> <游戏ID> -> 绑定新ID'''

whitelist_help = '''#白名单 添加 <target> -> 添加白名单成员
#白名单 列表 -> 列出白名单成员
#白名单 关   -> 关闭白名单
#白名单 开   -> 开启白名单
#白名单 重载 -> 重载白名单
#白名单 删除 <target> -> 删除白名单成员
<target> 可以是玩家名/目标选择器/UUID'''

start_command_help = '''启动指令菜单：
#启动指令 添加 <名称> <指令> -> 添加启动指令
#启动指令 列表 -> 查看现有启动指令
#启动指令 删除 <名称> -> 删除指定启动指令
#启动指令 开   -> 开启开服指令
#启动指令 关   -> 关闭开服指令
#启动指令 执行 -> 执行一遍开服指令
#启动指令 重载 -> 重载开服指令''' 

ban_word_help = '''违禁词相关指令：
#违禁词 添加 <违禁词> <违禁理由> -> 添加违禁词
#违禁词 列表 -> 显示违禁词列表及理由
#违禁词 删除 <违禁词> -> 删除指定违禁词
#违禁词 开   -> 开启违禁词
#违禁词 关   -> 关闭违禁词
#违禁词 重载 -> 重载违禁词'''

key_word_help = '''关键词相关指令：
#关键词 开   -> 开启关键词
#关键词 关   -> 关闭关键词
#关键词 重载 -> 重载关键词
#关键词 列表 -> 显示关键词列表
#添加 <关键词> <回复> -> 添加关键词
#删除 <关键词> -> 删除指定关键词'''

ingame_key_word_help = '''游戏内关键词相关指令：
#游戏关键词 开 -> 开启游戏内关键词
#游戏关键词 关 -> 关闭游戏内关键词
#游戏关键词 重载 -> 重载游戏内关键词'''

style_help = '''风格指令如下：
#风格        -> 风格帮助
#风格 列表   -> 风格列表
#风格 <风格> -> 切换至指定风格'''

uuid_help ='''uuid匹配指令如下：
#uuid        -> 查看uuid相关帮助
#uuid 列表   -> 查看uuid绑定表
#uuid 重载 -> 重新匹配uuid
#uuid 更新 <老ID> <新ID> -> 改白名单的名字'''

name_help = '''机器人名字相关指令如下：
#名字 -> 查看名字相关帮助
#名字 开 -> 机器人名字显示为在线人数
#名字 关 -> 机器人名字为特殊空白名字
(会占用少许服务器资源)
'''

shenhe_help = '''审核名单帮助：
#审核 开 -> 开启自动审核
#审核 关 -> 关闭自动审核
#审核 添加 <QQ号> <别名> -> 添加审核员的别名(匹配用)
#审核 删除 <QQ号> -> 删除审核员
#审核 列表 -> 审核员列表
'''

mc2qq_template = [
    "({}) {}",
    "[{}] {}",
    "{} 说：{}",
    "{} : {}",
    "冒着爱心眼的{}说：{}"
]

style = {
    '正常' : {
        'add_existed': '已存在该关键词~',
        'add_image_instruction': '请发送要添加的图片~',
        'add_image_fail': '图片保存失败~',
        'add_image_previous_no_done': '上一个关键词还未绑定，添加哒咩！',
        'add_success':'添加成功！',
        'authorization_pass': '已通过{}的申请awa',
        'authorization_reject': '已拒绝{}的申请awa',
        'authorization_request': '{} 申请进群, 请审核',
        'ban_word_find':'回复包含违禁词请修改后重发，维护和谐游戏人人有责。\n违禁理由：{}',
        'bound_add_whitelist': '已将您添加到服务器白名单',
        'bound_exist': '您已绑定ID: {}, 请联系管理员修改',
        'bound_success': '已成功绑定',
        'command_success' : '指令执行成功',
        'delete_success':'删除成功！',
        'del_no_exist': '该关键词不存在',
        'del_whitelist_when_quit': '{}已退群，白名单同步删除',
        'key_word_exist': '已有指定关键词,请删除(#删除 <关键词>)后重试 awa',
        'lack_parameter': '缺少参数，请参考 #帮助 里的说明',
        'list': '列表如下: \n{}',
        'no_player_ingame': f"现在没人游玩服务器",
        'no_word': '列表空空的',
        'player_api_fail': '未能通过api.miri.site获取到服务器信息，请检查服务器参数设置！（推荐开启rcon精准获取玩家信息）',
        'player_list':'在线玩家共{}人，{}列表: {}',
        'reload_success': '重载成功',
        'server_start':'服务器已启动',
    },
    '傲娇': {
        'ban_word_find':"本大小姐不听，才不告诉你是因为 {}",
        'no_player_ingame':'讷讷，为什么没人玩，为什么？大家都不爱我了吗awa',
        'player_list':'哼，这次就帮你数数，下次没那么容易了。\n现在有{}人，{}列表: {}',
        'server_start': '服务器启动啦！笨、笨蛋，人家可不是特地来告诉你们的!',
        'add_success':'哼..既然你都这么说了,那我就勉为其难帮你添加了！',
        'delete_success':'删除完了，才...才不是特别为你做的呢!',
        'key_word_exist': '已有指定关键词,请删除(#删除 <关键词>)后重试 awa',
        'lack_parameter': '笨死了，这都不会1w1，去看 #帮助 啦！',
        'del_no_exist': '累死我了，找了半天没这个词，大坏蛋！',
        'no_word': '快添点东西进来叭，才。。才不是人家寂寞了',
        'list': '列表如下: \n{}',
        'reload_success': '重载啦awa，快夸我！',
        'command_success' : '那么多指令，想累死本小姐嘛，才不做！什么，你说你准备了礼物，那我就勉为其难做点，哼'
    },
    "雌小鬼": {
        "ban_word_find": "呜呜呜，偶才不告诉你是因为 {} 呢！",
        "no_player_ingame": "呜呜，为什么没有人陪我玩呢？难道大家都讨厌我了吗？唔唔唔",
        "player_list": "大叔连这都不会，真是杂鱼！杂鱼杂鱼！\n现在有 {} 个人，{} 列表：{}",
        "server_start": "服务器终于启动了！杂鱼，不会连进都进不去吧！真是有够杂鱼的。",
        "add_success": "哼，既然你这么说了，我勉为其难地帮你添加了！",
        "delete_success": "删除成功啦，才不是为了你特别做的呢！",
        "key_word_exist": "已经有这个关键词了，请删除（#删除 <关键词>）后再试试呀。",
        "lack_parameter": "真是笨蛋，这都不会吗？去看看 #帮助 吧！",
        "del_no_exist": "累死我了，找了半天都没有这个词，大坏蛋！",
        "no_word": "快点加点东西进来嘛，我好无聊啊！才不是因为寂寞呢~",
        "list": "列表如下：\n{}",
        "reload_success": "又重载了，哼！快夸夸我吧！",
        "command_success": "那么多指令，你是想累死我吗？才不会做呢！什么？你准备了礼物？好吧，我勉为其难地做点东西，哼~"
    },
    "御姐": {
        "ban_word_find": "哼，不告诉你是因为 {} 这种事情，你也不配知道。",
        "no_player_ingame": "哼，竟然没有人来陪我玩，看来我的魅力还不够。",
        "player_list": "嘻嘻，我就帮你数数吧，现在总共有 {} 位玩家，{} 列表如下：{}",
        "server_start": "服务器终于启动了！不过，我并不是特地为了通知你们才说的。",
        "add_success": "嗯，既然你这么请求，姐姐就勉为其难地帮你添加了！",
        "delete_success": "删除完毕，姐姐可不是特意为你做的。",
        "key_word_exist": "这个关键词已经存在了，请删除（#删除 <关键词>）后重试。",
        "lack_parameter": "真是个无能之辈，连最基本的都不会，快去看看 #帮助 吧！",
        "del_no_exist": "找了半天都没有找到这个词，真是让人头疼！",
        "no_word": "快点给我一些东西吧，不然姐姐会感到无聊的。",
        "list": "以下是列表内容：\n{}",
        "reload_success": "已经重新加载了，你要不夸奖一下姐姐吗？",
        "command_success": "这么多指令，你是想让姐姐累死吗？姐姐可不会这么做！什么？你准备了礼物？好吧，姐姐就勉为其难地做点东西。"
    },
    "萝莉": {
        "ban_word_find": "呀~诶嘿嘿，不告诉你是因为 {} 啦！",
        "no_player_ingame": "呜呜呜，没有人来陪我玩耍了，难过死了！",
        "player_list": "嘻嘻，我来帮你数数哦，现在一共有 {} 个人，{} 列表是：{}",
        "server_start": "服务器启动啦！嘻嘻，我可不是特意来告诉你们的哦！",
        "add_success": "嘻嘻，既然你这么说了，那我就勉为其难地帮你添加啦！",
        "delete_success": "删除成功啦，可不是特别为你做的呢！",
        "key_word_exist": "这个关键词已经存在了呢，请删除（#删除 <关键词>）后重试哦！",
        "lack_parameter": "嗯？怎么连这个都不会呀，快去看看 #帮助 吧！",
        "del_no_exist": "唔...找了半天都没有这个词，大坏蛋！",
        "no_word": "呜呜，快给我点东西吧，不然我会好寂寞的！",
        "list": "下面是列表内容哦：\n{}",
        "reload_success": "呀呀，已经重新加载啦！夸夸我嘛~",
        "command_success": "好多指令呀，你是要累坏我吗？才不会做呢！嘻嘻~什么？你有礼物？好吧，我勉为其难地帮你做点东西啦~"
    },
    "波奇酱": {
        "ban_word_find": "咳咳，不告诉你 {} 是因为...没什么特别的理由。",
        "no_player_ingame": "唔...好害怕，为什么没有人来玩呢？大家都不喜欢我吗？",
        "player_list": "呃...好紧张，现在一共有 {} 个人，{} 列表如下：{}",
        "server_start": "服务器启动了...只是...不是为了特地告诉你们而已。",
        "add_success": "唔...既然你这么请求，我就勉为其难地帮你添加了。",
        "delete_success": "已经删除了...唔，不是特意为了你才这么做的。",
        "key_word_exist": "这个关键词已经存在了，请删除（#删除 <关键词>）后重试。",
        "lack_parameter": "唔唔唔...你竟然连最基本的都不会，去看看 #帮助 吧。",
        "del_no_exist": "好困扰...找了半天都找不到这个词，真是让人头疼。",
        "no_word": "唔唔...快点给我一些东西，否则我会感到更加害怕。",
        "list": "列表如下：\n{}",
        "reload_success": "重新加载完成...唔唔，有没有什么表扬的话？",
        "command_success": "这么多指令...你是想让我陷入恐惧中吗？唔，我不会做的！什么？你准备了礼物？唔唔...好吧，我勉为其难地做点东西。"
    },
    "病娇": {
        "ban_word_find": "嘻嘻嘻，怎么样？你猜不到 {} 是因为我喜欢看你迷茫的样子！",
        "no_player_ingame": "唔唔唔...都没有人来陪我玩耍了！你们都抛弃我了吗？！我会让你们后悔的！",
        "player_list": "哼，我勉为其难地帮你数数！现在一共有 {} 个人，{} 列表如下：{}",
        "server_start": "服务器启动了！嘻嘻嘻，你以为我是特地来告诉你的吗？不，我只是觉得这样做会让你更加困惑！",
        "add_success": "唔唔唔...既然你这么请求，我勉为其难地帮你添加了！但是别误会，这并不代表我对你有好感！",
        "delete_success": "删除成功了！嘻嘻嘻，我并没有特意为了你才这么做，我只是觉得这样做会让你更加绝望而已！",
        "key_word_exist": "这个关键词已经存在了！请删除（#删除 <关键词>）后重试。嘻嘻嘻，你真是个可笑的小丑！",
        "lack_parameter": "唔唔唔，你连这个都不会？真是个令人讨厌的笨蛋！快去看看 #帮助 吧！",
        "del_no_exist": "唔唔唔，找了半天都找不到这个词！你真是个让人发疯的家伙！我会让你付出代价的！",
        "no_word": "嘻嘻嘻，给我一些东西吧！否则我会让你体验到痛苦的滋味！你不会想看到我发狂的样子吧？",
        "list": "下面是列表内容哦：\n{}",
        "reload_success": "重新加载完成了！嘻嘻嘻，不必夸奖我，我只是觉得这样做会让你更加绝望而已！",
        "command_success": "这么多指令，你是想让我彻底发疯吗？唔唔唔，算了，我勉为其难地帮你做点东西！但是你必须付出代价！"
    },
    "中二病": {
        "ban_word_find": "你可看不出来，这个 {} 是我掌握的秘术，你无法窥探其中的奥秘！",
        "no_player_ingame": "唔，竟然没有人能够与我一同战斗，看来这个世界已经失去了勇者的存在！",
        "player_list": "哼，这么请求的话，我就勉为其难地为你点数一番！现在共有 {} 位勇者，{} 列表如下：{}",
        "server_start": "黑暗之力觉醒了！世界将被我带入深渊，这并非偶然，而是命运的安排！",
        "add_success": "你终于请求到了我的帮助，勇敢的冒险者！我将在有限的时间内为你添加！但请记住，这不代表我对你产生了任何好感！",
        "delete_success": "黑暗力量洗净了这个世界上的某个存在，你应该庆幸自己没有成为那个被消灭的人！",
        "key_word_exist": "这个关键词已经在我的掌控之下！在黑暗的领域中，你休想摆脱我的控制！",
        "lack_parameter": "无知的愚者，你不懂这个世界的秘密，去阅读 #帮助，也许你能窥探一些真相！",
        "del_no_exist": "在黑暗的境界中，你找不到任何痕迹，这个词根本不存在于我的领域中！",
        "no_word": "唔唔唔，这个世界需要更多的暗黑力量，只有这样才能引发真正的战斗！快给我更多的事物，让黑暗的力量永不停歇！",
        "list": "现在，我将揭开真相的面纱！以下是列表的真实内容：\n{}",
        "reload_success": "重新注入黑暗力量完成！勇敢的探险者，不必称赞我，你不懂这其中的牺牲与代价！",
        "command_success": "在无尽的命运中，你希望我屈从于你的命令吗？哈哈哈，不过，我愿意勉为其难地帮你完成一些事情！"
    }

}
