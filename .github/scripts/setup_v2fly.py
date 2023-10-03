import os.path


TLDs = ['.aaa', '.aarp', '.abarth', '.abb', '.abbott', '.abbvie', '.abc', '.able', '.abogado', '.abudhabi', '.ac',
        '.academy', '.accenture', '.accountant', '.accountants', '.aco', '.active', '.actor', '.ad', '.adac', '.ads',
        '.adult', '.ae', '.aeg', '.aero', '.aetna', '.af', '.afamilycompany', '.afl', '.africa', '.ag', '.agakhan',
        '.agency', '.ai', '.aig', '.aigo', '.airbus', '.airforce', '.airtel', '.akdn', '.al', '.alfaromeo', '.alibaba',
        '.alipay', '.allfinanz', '.allstate', '.ally', '.alsace', '.alstom', '.am', '.amazon', '.americanexpress',
        '.americanfamily', '.amex', '.amfam', '.amica', '.amsterdam', '.an', '.analytics', '.android', '.anquan',
        '.anz', '.ao', '.aol', '.apartments', '.app', '.apple', '.aq', '.aquarelle', '.ar', '.arab', '.aramco',
        '.archi', '.army', '.arpa', '.art', '.arte', '.as', '.asda', '.asia', '.associates', '.at', '.athleta',
        '.attorney', '.au', '.auction', '.audi', '.audible', '.audio', '.auspost', '.author', '.auto', '.autos',
        '.avianca', '.aw', '.aws', '.ax', '.axa', '.az', '.azure', '.ba', '.baby', '.baidu', '.banamex',
        '.bananarepublic', '.band', '.bank', '.bar', '.barcelona', '.barclaycard', '.barclays', '.barefoot',
        '.bargains', '.baseball', '.basketball', '.bauhaus', '.bayern', '.bb', '.bbc', '.bbt', '.bbva', '.bcg', '.bcn',
        '.bd', '.be', '.beats', '.beauty', '.beer', '.bentley', '.berlin', '.best', '.bestbuy', '.bet', '.bf', '.bg',
        '.bh', '.bharti', '.bi', '.bible', '.bid', '.bike', '.bing', '.bingo', '.bio', '.biz', '.bj', '.bl', '.black',
        '.blackfriday', '.blanco', '.blockbuster', '.blog', '.bloomberg', '.blue', '.bm', '.bms', '.bmw', '.bn', '.bnl',
        '.bnpparibas', '.bo', '.boats', '.boehringer', '.bofa', '.bom', '.bond', '.boo', '.book', '.booking', '.boots',
        '.bosch', '.bostik', '.boston', '.bot', '.boutique', '.box', '.bq', '.br', '.bradesco', '.bridgestone',
        '.broadway', '.broker', '.brother', '.brussels', '.bs', '.bt', '.budapest', '.bugatti', '.build', '.builders',
        '.business', '.buy', '.buzz', '.bv', '.bw', '.by', '.bz', '.bzh', '.ca', '.cab', '.cafe', '.cal', '.call',
        '.calvinklein', '.cam', '.camera', '.camp', '.cancerresearch', '.canon', '.capetown', '.capital', '.capitalone',
        '.car', '.caravan', '.cards', '.care', '.career', '.careers', '.cars', '.cartier', '.casa', '.case', '.caseih',
        '.cash', '.casino', '.cat', '.catering', '.catholic', '.cba', '.cbn', '.cbre', '.cbs', '.cc', '.cd', '.ceb',
        '.center', '.ceo', '.cern', '.cf', '.cfa', '.cfd', '.cg', '.ch', '.chanel', '.channel', '.charity', '.chase',
        '.chat', '.cheap', '.chintai', '.chloe', '.christmas', '.chrome', '.chrysler', '.church', '.ci', '.cipriani',
        '.circle', '.cisco', '.citadel', '.citi', '.citic', '.city', '.cityeats', '.ck', '.cl', '.claims', '.cleaning',
        '.click', '.clinic', '.clinique', '.clothing', '.cloud', '.club', '.clubmed', '.cm', '.cn', '.co', '.coach',
        '.codes', '.coffee', '.college', '.cologne', '.com', '.comcast', '.commbank', '.community', '.company',
        '.compare', '.computer', '.comsec', '.condos', '.construction', '.consulting', '.contact', '.contractors',
        '.cooking', '.cookingchannel', '.cool', '.coop', '.corsica', '.country', '.coupon', '.coupons', '.courses',
        '.cpa', '.cr', '.credit', '.creditcard', '.creditunion', '.cricket', '.crown', '.crs', '.cruise', '.cruises',
        '.csc', '.cu', '.cuisinella', '.cv', '.cw', '.cx', '.cy', '.cymru', '.cyou', '.cz', '.dabur', '.dad', '.dance',
        '.data', '.date', '.dating', '.datsun', '.day', '.dclk', '.dds', '.de', '.deal', '.dealer', '.deals', '.degree',
        '.delivery', '.dell', '.deloitte', '.delta', '.democrat', '.dental', '.dentist', '.desi', '.design', '.dev',
        '.dhl', '.diamonds', '.diet', '.digital', '.direct', '.directory', '.discount', '.discover', '.dish', '.diy',
        '.dj', '.dk', '.dm', '.dnp', '.do', '.docs', '.doctor', '.dodge', '.dog', '.doha', '.domains', '.doosan',
        '.dot', '.download', '.drive', '.dtv', '.dubai', '.duck', '.dunlop', '.duns', '.dupont', '.durban', '.dvag',
        '.dvr', '.dz', '.earth', '.eat', '.ec', '.eco', '.edeka', '.edu', '.education', '.ee', '.eg', '.eh', '.email',
        '.emerck', '.energy', '.engineer', '.engineering', '.enterprises', '.epost', '.epson', '.equipment', '.er',
        '.ericsson', '.erni', '.es', '.esq', '.estate', '.esurance', '.et', '.etisalat', '.eu', '.eurovision', '.eus',
        '.events', '.everbank', '.exchange', '.expert', '.exposed', '.express', '.extraspace', '.fage', '.fail',
        '.fairwinds', '.faith', '.family', '.fan', '.fans', '.farm', '.farmers', '.fashion', '.fast', '.fedex',
        '.feedback', '.ferrari', '.ferrero', '.fi', '.fiat', '.fidelity', '.fido', '.film', '.final', '.finance',
        '.financial', '.fire', '.firestone', '.firmdale', '.fish', '.fishing', '.fit', '.fitness', '.fj', '.fk',
        '.flickr', '.flights', '.flir', '.florist', '.flowers', '.flsmidth', '.fly', '.fm', '.fo', '.foo', '.food',
        '.foodnetwork', '.football', '.ford', '.forex', '.forsale', '.forum', '.foundation', '.fox', '.fr', '.free',
        '.fresenius', '.frl', '.frogans', '.frontdoor', '.frontier', '.ftr', '.fujitsu', '.fujixerox', '.fun', '.fund',
        '.furniture', '.futbol', '.fyi', '.ga', '.gal', '.gallery', '.gallo', '.gallup', '.game', '.games', '.gap',
        '.garden', '.gay', '.gb', '.gbiz', '.gd', '.gdn', '.ge', '.gea', '.gent', '.genting', '.george', '.gf', '.gg',
        '.ggee', '.gh', '.gi', '.gift', '.gifts', '.gives', '.giving', '.gl', '.glade', '.glass', '.gle', '.global',
        '.globo', '.gm', '.gmail', '.gmbh', '.gmo', '.gmx', '.gn', '.godaddy', '.gold', '.goldpoint', '.golf', '.goo',
        '.goodhands', '.goodyear', '.goog', '.google', '.gop', '.got', '.gov', '.gp', '.gq', '.gr', '.grainger',
        '.graphics', '.gratis', '.green', '.gripe', '.grocery', '.group', '.gs', '.gt', '.gu', '.guardian', '.gucci',
        '.guge', '.guide', '.guitars', '.guru', '.gw', '.gy', '.hair', '.hamburg', '.hangout', '.haus', '.hbo', '.hdfc',
        '.hdfcbank', '.health', '.healthcare', '.help', '.helsinki', '.here', '.hermes', '.hgtv', '.hiphop',
        '.hisamitsu', '.hitachi', '.hiv', '.hk', '.hkt', '.hm', '.hn', '.hockey', '.holdings', '.holiday', '.homedepot',
        '.homegoods', '.homes', '.homesense', '.honda', '.honeywell', '.horse', '.hospital', '.host', '.hosting',
        '.hot', '.hoteles', '.hotels', '.hotmail', '.house', '.how', '.hr', '.hsbc', '.ht', '.htc', '.hu', '.hughes',
        '.hyatt', '.hyundai', '.ibm', '.icbc', '.ice', '.icu', '.id', '.ie', '.ieee', '.ifm', '.iinet', '.ikano', '.il',
        '.im', '.imamat', '.imdb', '.immo', '.immobilien', '.in', '.inc', '.industries', '.infiniti', '.info', '.ing',
        '.ink', '.institute', '.insurance', '.insure', '.int', '.intel', '.international', '.intuit', '.investments',
        '.io', '.ipiranga', '.iq', '.ir', '.irish', '.is', '.iselect', '.ismaili', '.ist', '.istanbul', '.it', '.itau',
        '.itv', '.iveco', '.iwc', '.jaguar', '.java', '.jcb', '.jcp', '.je', '.jeep', '.jetzt', '.jewelry', '.jio',
        '.jlc', '.jll', '.jm', '.jmp', '.jnj', '.jo', '.jobs', '.joburg', '.jot', '.joy', '.jp', '.jpmorgan', '.jprs',
        '.juegos', '.juniper', '.kaufen', '.kddi', '.ke', '.kerryhotels', '.kerrylogistics', '.kerryproperties', '.kfh',
        '.kg', '.kh', '.ki', '.kia', '.kids', '.kim', '.kinder', '.kindle', '.kitchen', '.kiwi', '.km', '.kn', '.koeln',
        '.komatsu', '.kosher', '.kp', '.kpmg', '.kpn', '.kr', '.krd', '.kred', '.kuokgroup', '.kw', '.ky', '.kyoto',
        '.kz', '.la', '.lacaixa', '.ladbrokes', '.lamborghini', '.lamer', '.lancaster', '.lancia', '.lancome', '.land',
        '.landrover', '.lanxess', '.lasalle', '.lat', '.latino', '.latrobe', '.law', '.lawyer', '.lb', '.lc', '.lds',
        '.lease', '.leclerc', '.lefrak', '.legal', '.lego', '.lexus', '.lgbt', '.li', '.liaison', '.lidl', '.life',
        '.lifeinsurance', '.lifestyle', '.lighting', '.like', '.lilly', '.limited', '.limo', '.lincoln', '.linde',
        '.link', '.lipsy', '.live', '.living', '.lixil', '.lk', '.llc', '.llp', '.loan', '.loans', '.locker', '.locus',
        '.loft', '.lol', '.london', '.lotte', '.lotto', '.love', '.lpl', '.lplfinancial', '.lr', '.ls', '.lt', '.ltd',
        '.ltda', '.lu', '.lundbeck', '.lupin', '.luxe', '.luxury', '.lv', '.ly', '.ma', '.macys', '.madrid', '.maif',
        '.maison', '.makeup', '.man', '.management', '.mango', '.map', '.market', '.marketing', '.markets', '.marriott',
        '.marshalls', '.maserati', '.mattel', '.mba', '.mc', '.mcd', '.mcdonalds', '.mckinsey', '.md', '.me', '.med',
        '.media', '.meet', '.melbourne', '.meme', '.memorial', '.men', '.menu', '.meo', '.merckmsd', '.metlife', '.mf',
        '.mg', '.mh', '.miami', '.microsoft', '.mil', '.mini', '.mint', '.mit', '.mitsubishi', '.mk', '.ml', '.mlb',
        '.mls', '.mm', '.mma', '.mn', '.mo', '.mobi', '.mobile', '.mobily', '.moda', '.moe', '.moi', '.mom', '.monash',
        '.money', '.monster', '.montblanc', '.mopar', '.mormon', '.mortgage', '.moscow', '.moto', '.motorcycles',
        '.mov', '.movie', '.movistar', '.mp', '.mq', '.mr', '.ms', '.msd', '.mt', '.mtn', '.mtpc', '.mtr', '.mu',
        '.museum', '.music', '.mutual', '.mutuelle', '.mv', '.mw', '.mx', '.my', '.mz', '.na', '.nab', '.nadex',
        '.nagoya', '.name', '.nationwide', '.natura', '.navy', '.nba', '.nc', '.ne', '.nec', '.net', '.netbank',
        '.netflix', '.network', '.neustar', '.new', '.newholland', '.news', '.next', '.nextdirect', '.nexus', '.nf',
        '.nfl', '.ng', '.ngo', '.nhk', '.ni', '.nico', '.nike', '.nikon', '.ninja', '.nissan', '.nissay', '.nl', '.no',
        '.nokia', '.northwesternmutual', '.norton', '.now', '.nowruz', '.nowtv', '.np', '.nr', '.nra', '.nrw', '.ntt',
        '.nu', '.nyc', '.nz', '.obi', '.observer', '.off', '.office', '.okinawa', '.olayan', '.olayangroup', '.oldnavy',
        '.ollo', '.om', '.omega', '.one', '.ong', '.onl', '.online', '.onyourside', '.ooo', '.open', '.oracle',
        '.orange', '.org', '.organic', '.orientexpress', '.origins', '.osaka', '.otsuka', '.ott', '.ovh', '.pa',
        '.page', '.pamperedchef', '.panasonic', '.panerai', '.paris', '.pars', '.partners', '.parts', '.party',
        '.passagens', '.pay', '.pccw', '.pe', '.pet', '.pf', '.pfizer', '.pg', '.ph', '.pharmacy', '.phd', '.philips',
        '.phone', '.photo', '.photography', '.photos', '.physio', '.piaget', '.pics', '.pictet', '.pictures', '.pid',
        '.pin', '.ping', '.pink', '.pioneer', '.pizza', '.pk', '.pl', '.place', '.play', '.playstation', '.plumbing',
        '.plus', '.pm', '.pn', '.pnc', '.pohl', '.poker', '.politie', '.porn', '.post', '.pr', '.pramerica', '.praxi',
        '.press', '.prime', '.pro', '.prod', '.productions', '.prof', '.progressive', '.promo', '.properties',
        '.property', '.protection', '.pru', '.prudential', '.ps', '.pt', '.pub', '.pw', '.pwc', '.py', '.qa', '.qpon',
        '.quebec', '.quest', '.qvc', '.racing', '.radio', '.raid', '.re', '.read', '.realestate', '.realtor', '.realty',
        '.recipes', '.red', '.redstone', '.redumbrella', '.rehab', '.reise', '.reisen', '.reit', '.reliance', '.ren',
        '.rent', '.rentals', '.repair', '.report', '.republican', '.rest', '.restaurant', '.review', '.reviews',
        '.rexroth', '.rich', '.richardli', '.ricoh', '.rightathome', '.ril', '.rio', '.rip', '.rmit', '.ro', '.rocher',
        '.rocks', '.rodeo', '.rogers', '.room', '.rs', '.rsvp', '.ru', '.rugby', '.ruhr', '.run', '.rw', '.rwe',
        '.ryukyu', '.sa', '.saarland', '.safe', '.safety', '.sakura', '.sale', '.salon', '.samsclub', '.samsung',
        '.sandvik', '.sandvikcoromant', '.sanofi', '.sap', '.sapo', '.sarl', '.sas', '.save', '.saxo', '.sb', '.sbi',
        '.sbs', '.sc', '.sca', '.scb', '.schaeffler', '.schmidt', '.scholarships', '.school', '.schule', '.schwarz',
        '.science', '.scjohnson', '.scor', '.scot', '.sd', '.se', '.search', '.seat', '.secure', '.security', '.seek',
        '.select', '.sener', '.services', '.ses', '.seven', '.sew', '.sex', '.sexy', '.sfr', '.sg', '.sh', '.shangrila',
        '.sharp', '.shaw', '.shell', '.shia', '.shiksha', '.shoes', '.shop', '.shopping', '.shouji', '.show',
        '.showtime', '.shriram', '.si', '.silk', '.sina', '.singles', '.site', '.sj', '.sk', '.ski', '.skin', '.sky',
        '.skype', '.sl', '.sling', '.sm', '.smart', '.smile', '.sn', '.sncf', '.so', '.soccer', '.social', '.softbank',
        '.software', '.sohu', '.solar', '.solutions', '.song', '.sony', '.soy', '.spa', '.space', '.spiegel', '.sport',
        '.spot', '.spreadbetting', '.sr', '.srl', '.srt', '.ss', '.st', '.stada', '.staples', '.star', '.starhub',
        '.statebank', '.statefarm', '.statoil', '.stc', '.stcgroup', '.stockholm', '.storage', '.store', '.stream',
        '.studio', '.study', '.style', '.su', '.sucks', '.supplies', '.supply', '.support', '.surf', '.surgery',
        '.suzuki', '.sv', '.swatch', '.swiftcover', '.swiss', '.sx', '.sy', '.sydney', '.symantec', '.systems', '.sz',
        '.tab', '.taipei', '.talk', '.taobao', '.target', '.tatamotors', '.tatar', '.tattoo', '.tax', '.taxi', '.tc',
        '.tci', '.td', '.tdk', '.team', '.tech', '.technology', '.tel', '.telecity', '.telefonica', '.temasek',
        '.tennis', '.teva', '.tf', '.tg', '.th', '.thd', '.theater', '.theatre', '.tiaa', '.tickets', '.tienda',
        '.tiffany', '.tips', '.tires', '.tirol', '.tj', '.tjmaxx', '.tjx', '.tk', '.tkmaxx', '.tl', '.tm', '.tmall',
        '.tn', '.to', '.today', '.tokyo', '.tools', '.top', '.toray', '.toshiba', '.total', '.tours', '.town',
        '.toyota', '.toys', '.tp', '.tr', '.trade', '.trading', '.training', '.travel', '.travelchannel', '.travelers',
        '.travelersinsurance', '.trust', '.trv', '.tt', '.tube', '.tui', '.tunes', '.tushu', '.tv', '.tvs', '.tw',
        '.tz', '.ua', '.ubank', '.ubs', '.uconnect', '.ug', '.uk', '.um', '.unicom', '.university', '.uno', '.uol',
        '.ups', '.us', '.uy', '.uz', '.va', '.vacations', '.vana', '.vanguard', '.vc', '.ve', '.vegas', '.ventures',
        '.verisign', '.versicherung', '.vet', '.vg', '.vi', '.viajes', '.video', '.vig', '.viking', '.villas', '.vin',
        '.vip', '.virgin', '.visa', '.vision', '.vista', '.vistaprint', '.viva', '.vivo', '.vlaanderen', '.vn',
        '.vodka', '.volkswagen', '.volvo', '.vote', '.voting', '.voto', '.voyage', '.vu', '.vuelos', '.wales',
        '.walmart', '.walter', '.wang', '.wanggou', '.warman', '.watch', '.watches', '.weather', '.weatherchannel',
        '.webcam', '.weber', '.website', '.wed', '.wedding', '.weibo', '.weir', '.wf', '.whoswho', '.wien', '.wiki',
        '.williamhill', '.win', '.windows', '.wine', '.winners', '.wme', '.wolterskluwer', '.woodside', '.work',
        '.works', '.world', '.wow', '.ws', '.wtc', '.wtf', '.xbox', '.xerox', '.xfinity', '.xihuan', '.xin', '.测试',
        '.कॉम', '.परीक्षा', '.セール', '.佛山', '.ಭಾರತ', '.慈善', '.集团', '.在线', '.한국', '.ଭାରତ', '.大众汽车', '.点看', '.คอม',
        '.ভাৰত', '.ভারত', '.八卦', '\u200f.ישראל\u200e', '\u200f.موقع\u200e', '.বাংলা', '.公益', '.公司', '.香格里拉', '.网站',
        '.移动', '.我爱你', '.москва', '.испытание', '.қаз', '.католик', '.онлайн', '.сайт', '.联通', '.срб', '.бг', '.бел',
        '\u200f.קום\u200e', '.时尚', '.微博', '.테스트', '.淡马锡', '.ファッション', '.орг', '.नेट', '.ストア', '.アマゾン', '.삼성',
        '.சிங்கப்பூர்', '.商标', '.商店', '.商城', '.дети', '.мкд', '\u200f.טעסט\u200e', '.ею', '.ポイント', '.新闻', '.工行', '.家電',
        '\u200f.كوم\u200e', '.中文网', '.中信', '.中国', '.中國', '.娱乐', '.谷歌', '.భారత్', '.ලංකා', '.電訊盈科', '.购物', '.測試',
        '.クラウド', '.ભારત', '.通販', '.भारतम्', '.भारत', '.भारोत', '\u200f.آزمایشی\u200e', '.பரிட்சை', '.网店', '.संगठन',
        '.餐厅', '.网络', '.ком', '.укр', '.香港', '.亚马逊', '.诺基亚', '.食品', '.δοκιμή', '.飞利浦', '\u200f.إختبار\u200e', '.台湾',
        '.台灣', '.手表', '.手机', '.мон', '\u200f.الجزائر\u200e', '\u200f.عمان\u200e', '\u200f.ارامكو\u200e',
        '\u200f.ایران\u200e', '\u200f.العليان\u200e', '\u200f.اتصالات\u200e', '\u200f.امارات\u200e',
        '\u200f.بازار\u200e', '\u200f.موريتانيا\u200e', '\u200f.پاکستان\u200e', '\u200f.الاردن\u200e',
        '\u200f.موبايلي\u200e', '\u200f.بارت\u200e', '\u200f.بھارت\u200e', '\u200f.المغرب\u200e', '\u200f.ابوظبي\u200e',
        '\u200f.البحرين\u200e', '\u200f.السعودية\u200e', '\u200f.ڀارت\u200e', '\u200f.كاثوليك\u200e',
        '\u200f.سودان\u200e', '\u200f.همراه\u200e', '\u200f.عراق\u200e', '\u200f.مليسيا\u200e', '.澳門', '.닷컴', '.政府',
        '\u200f.شبكة\u200e', '\u200f.بيتك\u200e', '\u200f.عرب\u200e', '.გე', '.机构', '.组织机构', '.健康', '.ไทย',
        '\u200f.سورية\u200e', '.招聘', '.рус', '.рф', '.珠宝', '\u200f.تونس\u200e', '.大拿', '.ລາວ', '.みんな', '.グーグル', '.ευ',
        '.ελ', '.世界', '.書籍', '.ഭാരതം', '.ਭਾਰਤ', '.网址', '.닷넷', '.コム', '.天主教', '.游戏', '.vermögensberater',
        '.vermögensberatung', '.企业', '.信息', '.嘉里大酒店', '.嘉里', '\u200f.مصر\u200e', '\u200f.قطر\u200e', '.广东', '.இலங்கை',
        '.இந்தியா', '.հայ', '.新加坡', '\u200f.فلسطين\u200e', '.テスト', '.政务', '.xperia', '.xxx', '.xyz', '.yachts',
        '.yahoo', '.yamaxun', '.yandex', '.ye', '.yodobashi', '.yoga', '.yokohama', '.you', '.youtube', '.yt', '.yun',
        '.za', '.zappos', '.zara', '.zero', '.zip', '.zippo', '.zm', '.zone', '.zuerich', '.zw']
DIRECT = set([])
PROXY = set([])
REJECT = set([])
GEOLOCATION_NOT_CN = set([])

FILE_PREFIX = "ruleset-"
MAPPING = {
    "domain": "DOMAIN-SUFFIX,",
    "full": "DOMAIN,",
    "regexp": "URL-REGEX,",
    "kw": "DOMAIN-KEYWORD,",
    "tld": "DOMAIN-SUFFIX,",
}

BASE_DIR = r"."
FILE_LIST = [
    ("cn.txt", DIRECT),
    ("category-ads-all.txt", REJECT),
    ("geolocation-!cn.txt", PROXY),
]


# def get_tld() -> list:
#     text = httpx.get("http://www.iana.org/domains/root/db").text
#     soup = BeautifulSoup(text, "html.parser")
#     x = soup.find("table", {"id": "tld-table"})
#     tlds = [anchor.text for anchor in x.find_all("a")]
#
#     return tlds


def update_dataset():
    for fn, rule_bucket in FILE_LIST:
        with open(os.path.join(BASE_DIR, fn), "r", encoding="utf8") as rf:
            lines = [l.strip() for l in rf.readlines()]

        for line in lines:
            prefix, domain, *_ = line.split(":")
            if "." not in domain:
                if f".{domain}" in TLDs:
                    domain = f".{domain}"
                    prefix = "tld"
                else:
                    domain = rf"^{domain}\."
                    prefix = "regexp"

            try:
                if line.endswith("@ads"):
                    REJECT.add(f"{MAPPING[prefix]}{domain}")
                elif line.endswith("@!cn"):
                    GEOLOCATION_NOT_CN.add(f"{MAPPING[prefix]}{domain}")
                else:
                    rule_bucket.add(f"{MAPPING[prefix]}{domain}")
            except KeyError:
                print(line)
                continue

    with open(f"{FILE_PREFIX}v2fly-cn.conf", "w", encoding="utf8") as wf:
        wf.write("\n".join(sorted(list(DIRECT))))
    with open(f"{FILE_PREFIX}v2fly-ads.conf", "w", encoding="utf8") as wf:
        wf.write("\n".join(sorted(list(REJECT))))
    with open(f"{FILE_PREFIX}v2fly-proxy.conf", "w", encoding="utf8") as wf:
        wf.write("\n".join(sorted(list(PROXY))))
    with open(f"{FILE_PREFIX}v2fly-geolocation-!cn.conf", "w", encoding="utf8") as wf:
        wf.write("\n".join(sorted(list(GEOLOCATION_NOT_CN))))


if __name__ == "__main__":
    update_dataset()
