frame_size = (1280, 720)

info_window_size = (810, 65)
info_window_rect = (235, 0, 810, 65)

status_window_size = (487, 155)
status_window_rect = (399, 565, 490, 154)

champion_names = {"없음" : "None", "가렌" : "Garen", "갈리오" : "Galio", "갱플랭크" : "Gangplank", "그라가스" : "Gragas",
                  "그레이브즈" : "Graves", "그웬" : "Gwen", "나르" : "Gnar", "나미" : "Nami", "나서스" : "Nasus",
                  "노틸러스" : "Nautilus", "녹턴" : "Nocturne", "누누와윌럼프" : "Nunu&Willump", "니달리" : "Nidalee",
                  "니코" : "Neeko", "닐라" : "Nilah", "다리우스" : "Darius", "다이애나" : "Diana",
                  "드레이븐" : "Draven", "라이즈" : "Ryze", "라칸" : "Rakan", "람머스" : "Rammus", "럭스" : "Lux",
                  "럼블" : "Rumble", "레나타글라스크" : "Renata_Glasc", "레넥톤" : "Renekton", "레오나" : "Leona",
                  "렉사이" : "Rek'Sai", "렐" : "Rell", "렝가" : "Rengar", "루시안" : "Lucian", "룰루" : "Lulu",
                  "르블랑" : "LeBlanc", "리븐" : "Riven", "리산드라" : "Lissandra", "리신" : "Lee_Sin", "릴리아" : "Lillia",
                  "마스터이" : "Master_Yi", "마오카이" : "Maokai", "말자하" : "Malzahar", "말파이트" : "Malphite",
                  "모데카이저" : "Mordekaiser", "모르가나" : "Morgana", "문도박사" : "Dr_Mundo",
                  "미스포츈" : "Miss_Fortune", "밀리오" : "Milio", "바드" : "Bard", "바루스" : "Varus", "바이" : "Vi",
                  "베이가" : "Veigar", "베인" : "Vayne", "벡스" : "Vex", "벨베스" : "Bel'Veth", "벨코즈" : "Vel'Koz",
                  "볼리베어" : "Volibear", "브라움" : "Braum", "브랜드" : "Brand", "블라디미르" : "Vladimir",
                  "블리츠크랭크" : "Blitzcrank", "비에고" : "Viego", "빅토르" : "Viktor", "뽀삐" : "Poppy",
                  "사미라" : "Samira", "사이온" : "Sion", "사일러스" : "Sylas", "샤코" : "Shaco", "세나" : "Senna",
                  "세라핀" : "Seraphine", "세주아니" : "Sejuani", "세트" : "Sett", "소나" : "Sona", "소라카" : "Soraka",
                  "쉔" : "Shen", "쉬바나" : "Shyvana", "스웨인" : "Swain", "스카너" : "Skarner", "시비르" : "Sivir",
                  "신드라" : "Syndra", "신지드" : "Singed", "신짜오" : "Xin_Zhao", "쓰레쉬" : "Thresh",
                  "아리" : "Ahri", "아무무" : "Amumu", "아우렐리온솔" : "Aurelion_Sol", "아이번" : "Ivern",
                  "아지르" : "Azir", "아칼리" : "Akali", "아크샨" : "Akshan", "아트록스" : "Aatrox", "아펠리오스" : "Aphelios",
                  "알리스타" : "Alistar", "애니" : "Annie", "애니비아" : "Anivia", "애쉬" : "Ashe", "야스오" : "Yasuo",
                  "에코" : "Ekko", "엘리스" : "Elise", "오공" : "Wukong", "오른" : "Ornn", "오리아나" : "Orianna", "올라프" : "Olaf",
                  "요네" : "Yone", "요릭" : "Yorick", "우디르" : "Udyr", "우르곳" : "Urgot", "워윅" : "Warwick",
                  "유미" : "Yuumi", "이렐리아" : "Irelia", "이블린" : "Evelynn", "이즈리얼" : "Ezreal",
                  "일라오이" : "Illaoi", "자르반4세" : "Jarvan_IV", "자야" : "Xayah", "자이라" : "Zyra", "자크" : "Zac", "잔나" : "Janna",
                  "잭스" : "Jax", "제드" : "Zed", "제라스" : "Xerath", "제리" : "Zeri", "제이스" : "Jayce",
                  "조이" : "Zoe", "직스" : "Ziggs", "진" : "Jhin", "질리언" : "Zilean", "징크스" : "Jinx",
                  "초가스" : "Cho'gath", "카르마" : "Karma", "카밀" : "Camille", "카사딘" : "Kassadin",
                  "카서스" : "Karthus", "카시오페아" : "Cassiopeia", "카이사" : "Kai'Sa", "카직스" : "Kha'Zix",
                  "카타리나" : "Katarina", "칼리스타" : "Kalista", "케넨" : "Kennen", "케이틀린" : "Caitlyn",
                  "케인" : "Kayn", "케일" : "Kayle", "코그모" : "Kog'Maw", "코르키" : "Corki", "퀸" : "Quinn",
                  "크산테" : "K'Sante", "클레드" : "Kled", "키아나" : "Qiyana", "킨드레드" : "Kindred", "타릭" : "Taric",
                  "탈론" : "Talon", "탈리야" : "Taliyah", "탐켄치" : "Tahm_Kench", "트런들" : "Trundle",
                  "트리스타나" : "Tristana", "트린다미어" : "Tryndamere", "트위스티드페이트" : "Twisted_Fate",
                  "트위치" : "Twitch", "티모" : "Teemo", "파이크" : "Pyke", "판테온" : "Pantheon",
                  "피들스틱" : "Filddlesticks", "피오라" : "Fiora", "피즈" : "Fizz", "하이머딩거" : "Heimerdinger",
                  "헤카림" : "Hecarim"}

champion_rect_blue = [(216, 10, 22, 22), (216, 40, 22, 22), (216, 69, 22, 22), (216, 99, 22, 22), (216, 128, 22, 22)]
champion_rect_red = [(251, 10, 22, 22), (251, 40, 22, 22), (251, 69, 22, 22), (251, 99, 22, 22), (251, 128, 22, 22)]

cs_rect_blue = [(187, 9, 20, 18), (187, 39, 20, 18), (187, 68, 20, 18), (187, 98, 20, 18), (187, 127, 20, 18)]
cs_rect_red = [(281, 9, 20, 18), (281, 39, 20, 18), (281, 68, 20, 18), (281, 98, 20, 18), (281, 127, 20, 18)]