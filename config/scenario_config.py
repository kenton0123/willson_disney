# scenario_config.py
# Configuration for all 16 scenarios

# Each scenario is defined by its four key variables
# Format: [information_completeness, information_source, ai_self_rating, ai_public_rating]
# Values are: "Low" or "High"

SCENARIOS = {
    1: ["Low", "Low", "Low", "Low"],
    2: ["Low", "Low", "Low", "High"],
    3: ["Low", "Low", "High", "Low"],
    4: ["Low", "Low", "High", "High"],
    5: ["Low", "High", "Low", "Low"],
    6: ["Low", "High", "Low", "High"],
    7: ["Low", "High", "High", "Low"],
    8: ["Low", "High", "High", "High"],
    9: ["High", "Low", "Low", "Low"],
    10: ["High", "Low", "Low", "High"],
    11: ["High", "Low", "High", "Low"],
    12: ["High", "Low", "High", "High"],
    13: ["High", "High", "Low", "Low"],
    14: ["High", "High", "Low", "High"],
    15: ["High", "High", "High", "Low"],
    16: ["High", "High", "High", "High"]
}

# Content for low information completeness

HIGH_INFO_CONTENT = (
    "## 巴黎迪士尼乐园介绍 \n"
    "巴黎迪士尼乐园，原名欧洲迪士尼度假区，于 1992 年 4 月 12 日开业，标志着欧洲娱乐业的一个重要里程碑。建造迪士尼乐园的想法在 20 世纪 70 年代末开始成形，但直到 1983 年东京迪士尼乐园取得成功后，该计划才开始获得发展动力。 1987 年与法国当局签署协议，并于 1988 年开始建造。度假村自此成为欧洲主要的旅游目的地 [1]。\n\n"
    "## 设施 \n"
    "巴黎迪士尼乐园由两个主题乐园组成：迪士尼乐园和华特迪士尼影城。迪士尼乐园设有美国小镇大街、探险世界、边域世界等主题区，提供巨雷山、加勒比海盗等各种景点。华特迪士尼影城于 2002 年开业，专注于电影主题体验，包括「料理鼠王：冒险之旅」和「星际大战：银河边缘」等景点。度假村还包括几家酒店和迪士尼村，提供购物和餐饮，提供卓越而难忘的旅行体验 [2]。\n\n"
    "## 访客数量 \n"
    "近年来，巴黎迪士尼乐园的游客数量大幅增加。 2023年，该度假区共接待游客1,610万人次，略微打破了先前的游客人数纪录。迪士尼乐园吸引了 1,040 万游客，而华特迪士尼影城则吸引了 570 万游客，比前一年增加了 6.7%。巴黎迪士尼乐园自开幕以来已接待了超过 3.75 亿游客 [3]。\n\n"
    "## 近期值得关注的事件 \n"
    "最近值得关注的活动包括 2022 年庆祝巴黎迪士尼乐园成立 30 周年。该度假村也因其创新的体验和故事叙述而获得认可。此外，巴黎迪士尼乐园还扩大了其服务范围，增加了新的景点和主题区域，例如将于 2022 年开放的漫威复仇者联盟园区。这些发展帮助该度假村维持了欧洲领先旅游目的地的地位 [4]。\n\n"
)

# Content for high information completeness
LOW_INFO_CONTENT = (
    "## 巴黎迪士尼乐园介绍 \n"
    "巴黎迪士尼乐园，前身为欧洲迪士尼，于 1992 年开幕。这是一个拥有许多景点的大型公园。建造这个公园的想法很早以前就有了，但是却花了一段时间才建成。它位于巴黎附近，非常受游客欢迎[1]。\n\n"
    "## 设施 \n"
    "巴黎迪士尼乐园有两个主要园区：迪士尼乐园和华特迪士尼影城。这里有很多游乐设施和表演，但一次参观很难看完所有表演。公园很大，所以你需要仔细规划你的行程。这里还有一些酒店和一个名为迪士尼村的购物区。这是一个有趣的地方，特别是如果你喜欢迪士尼电影 [2]。\n\n"
    "## 访客数量 \n"
    "每年都有很多人参观巴黎迪士尼乐园。近年来，这里非常繁忙，来自世界各地的游客多达数百万。确切的数字令人印象深刻，但很明显，该公园是欧洲最受欢迎的旅游景点之一。在假日和夏季，公园似乎会变得更加繁忙 [3]。\n\n"
    "## 近期值得关注的事件 \n"
    "巴黎迪士尼乐园最近举办了一些令人兴奋的活动。他们最近庆祝了一个重要的周年纪念日，这是一件大事。公园也不断增加新的景点和区域，为游客增添乐趣。此外，巴黎迪士尼乐园还有一个不错的应用程序，可以帮助您规划行程并避免排长队。公园里的食物也相当不错，有很多主题餐厅和咖啡馆。总的来说，这是一个与家人或朋友共度时光的好地方[4]。\n\n"
)

# References for low information source quality
LOW_SOURCE_REFS = (
    "参考文献:\n"
    "1. 匿名. (2008). 我的巴黎迪士尼之旅！ 取自 https://n&tab=TT&sl=en&tl=zh-CN&op.com\n"
    "2. 特里. (2004). 与你分享我的巴黎迪士尼之旅。 取自 https://en&tl=zh-CN&text=make%20the%20below%\n"
    "3. 匿名. (2006). 参观巴黎迪士尼。 取自 https://%20uk%203%3A%0A%0A.html\n"
    "4. 威爾森. (n.d.). 巴黎迪士尼的体验。 取自 https://?q=21899&tip=sid&clean=0\n"
)

# References for high information source quality
HIGH_SOURCE_REFS = (
    "参考文献:\n"
    "1. 巴黎迪士尼乐园新闻. (2024 年). 历史。取自 https://news.disneylandparis.com/en/history/\n"
    "2. 兰伯特.（2023 年）. 通过技术提升游客体验：以巴黎迪士尼乐园为例。《主题公园与景点管理杂志》，15(1)，12-25。取自 https://www.jtpam.org/articles/technology-disneylandparis\n"
    "3. 艾瑞网.（2024 年）. 2023 年巴黎华特迪士尼影城游客量。取自https://news.iresearch.cn/attendance-at-the-disneyland-paris-walt-disney-studios-park-theme-park/\n"
    "4. 巴黎迪士尼乐园官方.（2024 年）. 巴黎迪士尼乐园近期活动。取自https://www.disneylandparis.com/en-usd/offers/\n"
)
