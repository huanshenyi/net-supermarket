#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'images': [
            'https://sm.r10s.jp/item/51/4973450472351.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '輸入品',
            '輸入食品'
        ],
        'market_price': '￥397円',
        'name': 'グレートバリュー ピュアグレープシードオイル',
        'desc': 'グレープの種子を100％使用した健康効果の高いピュアな食用オイルです。さっぱりとしてクセがない為、炒め物や、揚げ物等、万能にご使用いただけます。',
        'sale_price': '￥368円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/10/8410013017810.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '輸入食品',
            '輸入お酒'
        ],
        'market_price': '￥798円',
        'name': 'ロンデル ゴールド セミセコ',
        'desc': 'シャンパンと同じ製法で造られたスペインの本格スパークリングワインです。細やかな泡に、りんご、洋ナシ、レモン、トロピカルフルーツのフレッシュな香り。甘みのある優しい味わいは、食前酒やデザートにぴったり。ワイン初心者にもおすすめです',
        'sale_price': '￥861円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/01/37000867401.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '輸入食品',
            '輸入日用品'
        ],
        'market_price': '￥597円',
        'name': 'ウルトラダウニー インフュージョン 柔軟剤 カシミアグロウ ホワイトローズと甘いバニラの香り',
        'desc': 'アメリカP&G社の1961年に発売された柔軟剤ブランド。アメリカでは売上No.1であり、日本でも香り柔軟剤の代名詞になっている程、愛されています。',
        'sale_price': '￥644円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/39/4973450428839.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '輸入食品',
            '輸入日用品'
        ],
        'market_price': '￥285円',
        'name': 'ランドリーハンガー',
        'desc': '使い勝手の良いハンガー１０本セットです！',
        'sale_price': '￥307円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/17/4902888229817.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '新商品',
            '菓子・飲料'
        ],
        'market_price': '￥165円',
        'name': '午後の紅茶 ストレートティークッキー',
        'desc': '午後の紅茶ストレートティーの味わいをイメージしたクッキー。',
        'sale_price': '￥178円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/88/4897036690888.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '新商品',
            '菓子・飲料'
        ],
        'market_price': '￥199円',
        'name': 'モンスター ウルトラ',
        'desc': '渇きを癒すリフレッシュモンスター！甘すぎないスッキリした味わい。どんなときでもリフレッシュできる微炭酸。スッキリなのにヤバイ、白いモンスター登場',
        'sale_price': '￥214円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/55/4964937050155.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '新商品',
            '食品'
        ],
        'market_price': '￥203円',
        'name': 'タピオカチーズティー',
        'desc': 'マスカルポーネチーズを使用したコクのあるタピオカチーズティ－です。',
        'sale_price': '￥188円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/32/4973655560532.jpg',
        ],
         'categorys': [
            'トップ',
            '当店のおすすめ',
            '新商品',
            'ペット'
        ],
        'market_price': '￥924円',
        'name': 'コロル ネコトイレ ベージュ',
        'desc': 'ゲージに入る省スペースのトイレです。おしっこが底面の手前で固まりやすい深型で、お手入れラクラク！固まる猫砂用です。上品でかわいいパステルカラーで、明るくハッピーな空間を演出します。',
        'sale_price': '￥997円',
        'goods_desc':''
    },
    {
        'images': [
            'http://sm.r10s.jp/item/35/4973450149635.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            'きほんのき',
            '食品・調味料'
        ],
        'market_price': '￥199円',
        'name': 'きほんのき 讃岐うどん （冷凍）',
        'desc': 'コシと喉越しの良さが特徴の冷凍うどん。お得な5食パック。',
        'sale_price': '￥185円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/08/4973450116408.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            'きほんのき',
            'お菓子・飲料・お酒'
        ],
        'market_price': '￥297円',
        'name': 'きほんのき 緑茶ティーバッグ',
        'desc': '国産茶葉100％使用で、便利な個包装タイプのティーバッグ緑茶です。',
        'sale_price': '￥275円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/04/4973450165604.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            'きほんのき',
            'キッチン用品'
        ],
        'market_price': '￥116円',
        'name': '食品用ラップ',
        'desc': '切りやすいプラスチック刃（植物由来）を使用。粘着付与剤などのあらゆる添加剤も0。燃やしても、ダイオキシン0のエコラップ。',
        'sale_price': '￥108円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/44/4973450116644.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            'きほんのき',
            'ホームクリーン'
        ],
        'market_price': '￥57円',
        'name': 'お風呂用洗剤 つめかえ用',
        'desc': '汚れを泡でつつんでスッキリ！レモンの香りの泡タイプのお風呂洗剤です。',
        'sale_price': '￥53円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/73/4973450791773.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            'きほんのき',
            'ホームクリーン'
        ],
        'market_price': '￥97円',
        'name': 'スポンジ ネットタイプ',
        'desc': 'ネットで浴槽や浴室小物の汚れをやさしく落とします。',
        'sale_price': '￥90円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/51/4973450153151.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '皆様のお墨付き',
            '冷凍食品'
        ],
        'market_price': '￥192円',
        'name': '7種の和風野菜ミックス （冷凍）',
        'desc': '指定農場で栽培し、旬に採った野菜を急速冷凍。さといも、人参、れんこん、ごぼう、いんげん、椎茸、たけのこ入り。',
        'sale_price': '￥178円',
        'goods_desc':''
    },
    {
        'images': [
            'https://sm.r10s.jp/item/19/4973450149819.jpg',
        ],
        'categorys': [
            'トップ',
            '当店のおすすめ',
            '皆様のお墨付き',
            '乳製品'
        ],
        'market_price': '￥189円',
        'name': '牛乳 成分無調整',
        'desc': '生乳100％使用。成分無調整。',
        'sale_price': '￥175円',
        'goods_desc': ''
    },
]

pass