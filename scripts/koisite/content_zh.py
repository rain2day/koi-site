"""Traditional Chinese content for the KOI public site.

Every factual claim here is traceable to the KOI application source or the
Firebase backend source. Three things must never appear: a price, a purchasable
"Lifetime" tier, and a support response-time promise. See
``docs/superpowers/specs/2026-08-05-koi-public-site-production-content-design.md``
in the application repository for the evidence behind each claim.
"""

from __future__ import annotations

EFFECTIVE_DATE = "2026 年 8 月 5 日"
PRIVACY_EFFECTIVE_DATE = "2026 年 9 月 20 日"
APPLE_EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"

UI = {
    "nav_label": "主要導覽",
    "nav_home": "首頁",
    "nav_privacy": "私隱政策",
    "nav_support": "支援",
    "nav_terms": "服務條款",
    "skip": "跳至主要內容",
    "switch_label": "English",
    "switch_aria": "Switch to English",
    "footer_rights": "© 2026 RaIN．KOI Keyboard",
    "footer_nav_label": "頁尾導覽",
    "footer_source": "本網站原始碼",
    "contents_label": "本頁內容",
    "footer_notice": (
        "本站的倉頡試打示範，使用衍生自 "
        "[rime-cangjie](https://github.com/rime/rime-cangjie)、"
        "[rime-essay](https://github.com/rime/rime-essay)（同為 LGPL-3.0）與 "
        "[Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)（MIT）的字表，"
        "並依 LGPL-3.0 發佈。倉頡輸入法由朱邦復先生發明。"
        "完整聲明見[第三方授權說明]"
        "(https://github.com/rain2day/koi-site/blob/main/THIRD-PARTY.md)。"
    ),
}

CREDIT_COSTS = {
    "kind": "table",
    "id": "credits",
    "heading": "每項 AI 操作需要多少 Credits",
    "intro": "只有在你主動要求 KOI Agent 執行操作時，才會扣減 Credits。日常打字、候選字與手寫辨識完全不需要 Credits。",
    "columns": ("操作", "Credits"),
    "rows": (
        ("回覆建議", "1"),
        ("改寫潤飾", "1"),
        ("翻譯", "1"),
        ("提問", "2"),
        ("生成貼圖", "6"),
        ("生成圖片", "18"),
    ),
    "caption": "圖像生成的運算成本較高，因此扣減較多 Credits。",
}


DEMO = {
    "kind": "demo",
    "id": "try",
    "heading": "一筆滑過，就是一個字",
    "intro": [
        "「香」的倉頡碼是 h、d、a——竹、木、日。一般做法是按三下。",
        "**在 KOI，你由 h 一路掃到 a 就完成了。**中途必然會掃過 g、f、s，而 KOI 知道你要的不是那三個字根。手指略為偏移，它一樣接得住。",
        "下面不是影片，是一個真正運作中的倉頡輸入法，就在你的瀏覽器內執行。逐鍵點按同樣可以，使用電腦則可直接用實體鍵盤。",
    ],
    "tries_label": "試著一筆滑過這幾組字根",
    "tries": (
        {"code": "hqi", "result": "我"},
        {"code": "onf", "result": "你"},
        {"code": "hda", "result": "香"},
        {"code": "etcu", "result": "港"},
        {"code": "nfwg", "result": "鯉"},
    ),
    "fallback": [
        "此示範需要啟用 JavaScript 才能運作。全站僅有的程式碼就是這個示範，而且不會連接任何伺服器。",
        "編碼對照：`hqi` 是「我」，`onf` 是「你」，`hda` 是「香」，`etcu` 是「港」。",
    ],
    "note": [
        "**與 app 相同**：滑行解碼，連容錯門檻、鄰鍵替代與轉角判定的數值都一致；鍵位排列、字根、候選次序（包括粵語字加權）、空白鍵輸出第一個候選、五碼上限，以及未開始組字時候選區顯示數字行。",
        "**示範沒有的部分**：雙指和弦輸入、學習紀錄、另外四種輸入法，以及 `z` 萬用字元。滑行解不出結果時，app 會再跑一次救援搜尋，示範不會——所以胡亂滑一筆，它會直接告訴你沒有對應候選，而不是硬湊一個。字表亦收窄至 3,030 個常用字，並非 app 內完整的 27,584 個。",
    ],
}


FILM = {
    "kind": "film",
    "id": "watch",
    "heading": "先看一次",
    "intro": [
        "手指離開 h，一路掃到 a。中途必然經過 g、f、s——**紅框是你要的字根，青框只是順路掃過**。KOI 分得出兩者的分別。",
    ],
    "sources": (
        {"source": "film/glide.webm", "type": "video/webm"},
        {"source": "film/glide.mp4", "type": "video/mp4"},
    ),
    "poster": "film/glide-poster.jpg",
    "width": 1280,
    "height": 860,
    "alt": "一筆滑行由 h 經過 g、f、d、s 到 a，候選字出現，「香」落字",
    "caption": "五秒，一筆，一個字。下面那個鍵盤你可以自己試。",
}


AGENT_FILM = {
    "kind": "film",
    "id": "agent-film",
    "heading": "看它草擬一句",
    "intro": [
        "訊息進來，選「回覆」，草稿即場出現，插入就等於送出。想要一張貼圖就選「貼圖」——透明背景，可以直接貼進對話。Credits 按實際操作扣減：回覆 1，貼圖 6。",
    ],
    "sources": (
        {"source": "film/agent-zh.webm", "type": "video/webm"},
        {"source": "film/agent-zh.mp4", "type": "video/mp4"},
    ),
    "poster": "film/agent-zh-poster.jpg",
    "width": 1280,
    "height": 860,
    "alt": "KOI Agent 草擬一句回覆並插入對話，然後生成一張透明背景的錦鯉貼圖，Credits 由 250 減至 243",
    "caption": "示範的是操作流程與扣數。實際回覆的措辭由模型生成，會隨對話而不同；片中的貼圖是為此片繪製的，並非模型輸出。",
}


LANDING = {
    "title": "KOI Keyboard — 為香港而設的中文鍵盤",
    "description": "倉頡、速成、筆劃、粵拼、注音，五種輸入方式共用一個鍵盤。手寫離線辨識，打字引擎完全不連網。iOS 16 或以上適用。",
    "eyebrow": "KOI Keyboard",
    "heading": "為香港而設的中文鍵盤",
    "hero": "landing",
    "lede": [
        "倉頡、速成、筆劃、粵拼、注音——五種輸入方式共用同一個鍵盤。",
        "手寫離線辨識，打字引擎完全不連網。",
    ],
    "status": {
        "label": "準備上架",
        "detail": "KOI 正在準備提交 App Store 審核。上架後此處會換成下載連結。",
    },
    "structured_data": True,
    "pond": True,
    "scripts": ("keyboard-demo.js", "stage.js"),
    "sections": [
        FILM,
        DEMO,
        {
            "kind": "scene",
            "id": "input-methods",
            "index": "01",
            "moment": "有人打倉頡，有人打速成，有人打粵拼；在台灣長大的打注音。要遷就身邊的人，往往就得在系統鍵盤清單裡多裝幾個。",
            "heading": "一個鍵盤，五種輸入方式",
            "lead": "五種模式都在 KOI 之內，切換即時完成，不必離開這個鍵盤。",
            "points": [
                {"title": "倉頡", "body": "原生鍵位排列，鍵帽同時顯示英文字母與倉頡字根。候選字按字頻排序，你經常選用的字會自動往前排。"},
                {"title": "速成", "body": "首尾碼輸入，與倉頡共用同一套鍵位，不需要重新記憶。"},
                {"title": "筆劃", "body": "五鍵筆劃輸入，支援 `*` 萬用字元——忘記中間幾劃，輸入一個星號一樣找得到。"},
                {"title": "粵拼", "body": "全拼與簡拼皆可，並可加上聲調數字收窄結果。輸出港式繁體中文。"},
                {"title": "注音（大千）", "body": "獨立注音鍵盤佈局，輸出台灣繁體中文。"},
                {"title": "英文", "body": "同一串按鍵會同時解碼為中文與英文候選，輸入英文不需要切換鍵盤。"},
            ],
        },
        {
            "kind": "showcase",
            "id": "screens",
            "heading": "實際畫面",
            "intro": "以下兩張都是 KOI 執行中的實際擷取畫面，並非示意圖。",
            "items": [
                {
                    "source": "shots/keyboard.png",
                    "alt": "KOI 鍵盤畫面，每個鍵帽同時顯示英文字母與倉頡字根，候選區顯示 0 至 9 數字行",
                    "caption": "鍵帽同時顯示英文字母與倉頡字根。未開始組字時，候選區顯示數字行。",
                    "badge": "實際擷取",
                },
                {
                    "source": "shots/settings.png",
                    "alt": "KOI 設定畫面，顯示輸入法、完整取用與同步狀態，下方是五種輸入模式選擇器",
                    "caption": "設定畫面：輸入法、完整取用與同步狀態一目了然，下方可直接選擇輸入模式。",
                    "badge": "實際擷取",
                },
            ],
        },
        {
            "kind": "scene",
            "id": "feel",
            "index": "02",
            "moment": "手指在六吋玻璃上滑過去，不會每一次都準。",
            "heading": "滑歪了，它照樣認得",
            "lead": "點按、滑行、兩者混合、雙指和弦，四種方式可以在同一個組字之內混用。打到一半改變主意，也不需要清空重來。",
            "points": [
                {"title": "滑行容錯", "body": "解碼容許最多兩個鍵被相鄰鍵取代。手指稍為偏移，輸入不會因此中斷。"},
                {"title": "打錯不落空", "body": "拆錯字時，KOI 會補上近似碼的候選，排在正常候選之後。候選區不會留下一片空白。"},
                {"title": "刪除與游標", "body": "按一下刪去最後一個碼，連按兩下清除整個組字；在空白鍵上左右掃動可以移動游標。"},
            ],
        },
        {
            "kind": "ink",
            "id": "handwriting",
            "heading": "沒有訊號的時候",
            "intro": [
                "地鐵車廂裡，訊號斷斷續續，而你要寫一個不知道怎麼拆的字。手寫模型內建在 app 之內——不必下載、不必連線，飛航模式下一樣寫得到。",
                "KOI 的手寫區以 Metal 渲染成一池水：落筆有漣漪、有折射、有波紋。下面這一方水借用了同一套筆跡渲染——你在鍵盤上滑行時看到的墨色，就是這一道。",
            ],
            "canvas_label": "可書寫的水面",
            "hint": "用手指或滑鼠在此書寫",
            "note": [
                "辨識模型在裝置上執行，沒有搬到瀏覽器，所以這裡只有筆跡與水，不會出字。app 內建香港繁體手寫模型，不需要下載、不需要連線，飛航模式下一樣寫得到。",
            ],
        },
        {
            "kind": "scene",
            "id": "agent",
            "index": "03",
            "moment": "你收到一段訊息，看了三次，還是不知道怎麼回。",
            "heading": "需要時才出現的 AI",
            "lead": "不必複製、不必跳去另一個 app。六種模式全部在鍵盤上完成——不開啟，它就完全不存在。",
            "points": [
                {"title": "自動", "body": "讀取你眼前的內容，自行判斷該做什麼。"},
                {"title": "提問", "body": "直接發問，答案可以直接插入。"},
                {"title": "回覆", "body": "根據對方的訊息草擬一個回覆。"},
                {"title": "改寫", "body": "潤飾、調整語氣、翻譯。"},
                {"title": "貼圖與圖片", "body": "生成透明背景貼圖，或完整場景圖片。"},
            ],
            "aside": "只有在你主動要求時才會扣減 Credits；日常打字、候選字與手寫辨識完全不需要。每項操作的消耗見[支援頁](route:support/)。",
        },
        AGENT_FILM,
        {
            "kind": "scene",
            "id": "privacy",
            "index": "04",
            "tone": "accent",
            "moment": "鍵盤是你打的每一個字都會經過的地方。你憑什麼相信它？",
            "heading": "所以它完全不連網",
            "lead": [
                "KOI 的輸入引擎——候選字產生、拆碼、學習紀錄——沒有任何網絡程式碼。**你打的字不會離開你的裝置。**",
            ],
            "points": [
                {"title": "沒有分析", "body": "沒有分析工具、沒有崩潰回報 SDK、沒有廣告識別碼。"},
                {"title": "沒有按鍵記錄", "body": "KOI 不會記錄你按過什麼。"},
                {"title": "唯一例外", "body": "你主動開啟 KOI Agent 並送出請求。除此之外沒有例外。"},
                {"title": "資料存放", "body": "學習紀錄與設定留在裝置上，或存放於由你自己控制的私人 iCloud。"},
            ],
            "aside": "逐項對照實作的說明見[私隱政策](route:privacy/)。",
        },
        {
            "kind": "scene",
            "id": "plus",
            "index": "05",
            "tone": "quiet",
            "moment": "換了新手機，用了一年的學習紀錄不見了。",
            "heading": "習慣跟著你走",
            "lead": "跨裝置同步是 KOI Plus 兩項功能之一。免費版本已經包含五種輸入法、手寫、學習與全部基本輸入功能；Plus 另加聯想輸入與同步，並附送每月 Credits。",
            "points": [
                {"title": "聯想輸入", "body": "落字之後接住推薦下一個詞或成句短語，減少逐個字拆碼。"},
                {"title": "跨裝置同步", "body": "設定與學習紀錄經你自己的私人 iCloud 同步。預設關閉，開啟後由你手動觸發。"},
            ],
            "aside": "訂閱與 Credits 的完整條款見[服務條款](route:terms/)，計算方式見[支援頁](route:support/)。",
        },
        {
            "kind": "scene",
            "id": "requirements",
            "index": "06",
            "tone": "quiet",
            "moment": "裝好 app 之後，鍵盤不會自己出現——iOS 不允許第三方鍵盤這樣做。",
            "heading": "開始使用",
            "lead": "你需要在 iOS 設定中加入鍵盤，一次就好。KOI 需要 iOS 16.0 或以上。",
            "points": [
                {"title": "完整取用", "body": "AI 功能、剪貼簿貼上、手寫模型更新，以及共用圖片庫存檔需要。不開啟的話，五種輸入法、候選字、學習與手寫全部照常運作。"},
                {"title": "字元覆蓋", "body": "候選字涵蓋基本多文種平面（BMP）內的漢字。"},
                {"title": "介面語言", "body": "app 介面為繁體中文（香港）。"},
            ],
            "aside": "安裝步驟、常見問題與疑難排解見[支援頁](route:support/)。",
        },
    ],
}


PRIVACY = {
    "title": "私隱政策 — KOI Keyboard",
    "description": "KOI Keyboard 的私隱政策：打字資料留在裝置、沒有分析工具、沒有廣告識別碼，以及 AI 功能實際傳送哪些資料。",
    "eyebrow": "KOI · 私隱",
    "heading": "私隱政策",
    "lede": "本政策說明 KOI Keyboard 實際處理哪些資料。每一項都與 app 及後端的實作相符，並非套用範本填空。",
    "updated": f"生效日期：{PRIVACY_EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "summary",
            "heading": "一分鐘概要",
            "bullets": [
                "你打的字**不會**離開裝置，除非你主動開啟 KOI Agent 並送出請求。",
                "KOI **沒有**加入任何分析、崩潰回報或廣告追蹤工具。",
                "KOI **不會**讀取你的廣告識別碼或裝置識別碼。",
                "學習紀錄與設定儲存在裝置上；如果你開啟同步，則儲存於**你自己**的私人 iCloud。",
                "我們不會出售你的資料，也不會將它用於廣告。",
            ],
            "after": "以下逐項說明。",
        },
        {
            "kind": "prose",
            "id": "not-collected",
            "heading": "我們不收集的資料",
            "body": "這一節比「我們收集什麼」更重要，所以放在前面。在 KOI 的程式碼裡，找不到以下任何一項：",
            "bullets": [
                "分析或使用統計 SDK（例如 Firebase Analytics、Mixpanel、Amplitude）",
                "崩潰回報 SDK（例如 Crashlytics、Sentry）",
                "廣告或歸因 SDK（例如 AppsFlyer、Adjust、Facebook SDK）",
                "廣告識別碼（IDFA）、供應商識別碼（IDFV）或 App 追蹤透明度（ATT）請求",
                "按鍵記錄——KOI 不會逐鍵記下你按過什麼",
                "瀏覽或讀取通訊錄、相片庫、位置或行事曆——KOI 無法瀏覽或讀取你的相片庫",
            ],
        },
        {
            "kind": "prose",
            "id": "typing",
            "heading": "你打的字",
            "body": [
                "KOI 的輸入引擎完全在你的裝置上運作。拆碼、產生候選字、排序、學習——全部屬本機運算，這部分的程式碼沒有任何網絡功能。",
                "你選過的字會讓 KOI 學習你的習慣，令下次輸入同一串碼時排得更前。這些學習紀錄存放在 app 的共用容器 `group.com.rainsday.koikeyboard` 之內，只有 KOI 讀取得到。",
                "刪除 KOI 時，這些本機資料會一併移除。",
            ],
        },
        {
            "kind": "prose",
            "id": "full-access",
            "heading": "「完整取用」權限",
            "body": [
                "iOS 的規定是：鍵盤擴充功能如果沒有開啟「允許完整取用」，便沒有網絡能力，亦不能使用 KOI 的共用容器。KOI 只會將權限用於以下明確功能：",
            ],
            "bullets": [
                "連接 KOI Agent（AI 功能）",
                "由剪貼簿貼上文字到 AI 輸入框——只有在你按下「貼上」的一刻才會讀取剪貼簿",
                "更新手寫辨識模型（基本模型已經內建，不更新一樣可用）",
                "將生成圖片寫入 KOI app 的本機共用圖片庫，方便 host app 稍後顯示",
            ],
            "after": [
                "不開啟這項權限，KOI 的五種輸入法、候選字、學習、手寫、符號與游標操作全部照常運作。你失去的只有上述功能。",
                "開啟權限本身**不會**觸發任何資料傳送。傳送只會在你主動使用相關功能時發生。",
            ],
        },
        {
            "kind": "prose",
            "id": "ai",
            "heading": "KOI Agent 實際傳送什麼",
            "body": [
                "當你開啟 KOI Agent 並送出請求，以下資料會傳送至 KOI 的伺服器（Google Cloud Functions，位於 `asia-east1`）：",
            ],
            "bullets": [
                "你輸入的指令文字",
                "目前輸入框的 context。KOI 會按以下次序分配上限：已選文字、選取範圍或游標之前的文字，最後是之後的文字。",
                "合併後的 context 上限為 2,000 個 Unicode scalar values 及 4,000 個 UTF-8 bytes。KOI Agent 畫面顯示的預覽，與該次操作實際送出的 context 完全相同。",
                "同一次對話之中先前的來回內容",
                "一個安裝識別碼（見下文「識別碼」一節）與一個 Firebase App Check 驗證權杖",
            ],
            "after": [
                "只有你明確按下 Agent 操作，例如「送出」、快捷操作、「重試」、確認較高 Credits 請求或「自由創作」後，KOI 才會送出 context。單純開啟 Agent 或查看預覽不會傳送。",
                "**不會**傳送的項目：截圖（KOI 沒有截圖功能）、你的剪貼簿內容（除非你自己按下「貼上」）、通訊錄，以及目前正在編輯的輸入框以外的內容。",
                "KOI 無法瀏覽或讀取你的相片庫；只有你在 KOI app 明確按下「儲存到相片」時，app 才會用 add-only 權限加入該張圖片，亦無法查看已有相片。",
                "伺服器的記錄只保留請求層面的資料：請求編號、路徑、狀態碼、耗時、由哪個模型處理、處理階段。**指令內容與周邊文字不會寫入記錄**。",
            ],
        },
        {
            "kind": "table",
            "id": "third-parties",
            "heading": "第三方服務",
            "intro": "以下是 KOI 實際接觸到的第三方。請留意「在裝置上」與「經網絡」的分別。",
            "columns": ("服務", "用途", "資料去向"),
            "rows": (
                ("Google ML Kit Digital Ink", "手寫辨識", "**在裝置上**運行，模型內建於 app，不會傳出筆跡"),
                ("Firebase App Check（經 Apple DeviceCheck）", "阻止伺服器被濫用", "裝置驗證權杖"),
                ("Firebase Authentication", "選用的「以 Apple 帳戶登入」", "見「帳戶與識別碼」"),
                ("Firebase Cloud Functions / Firestore", "AI 請求處理、Credits 帳目", "見「KOI Agent」與「購買」"),
                ("Cloudflare Workers", "為 Life Time Plus 的 AI 中文改錯請求提供驗證及轉送", "原句、候選字與會員驗證資料；文字不寫入 KOI 的 Worker 記錄或快取"),
                ("TypeSafe Jev", "為 Life Time Plus 的 AI 中文改錯選擇合適候選字", "原句及由本機字碼產生的候選字"),
                ("RevenueCat", "訂閱與購買狀態管理", "見「購買」"),
                ("OpenRouter", "將 AI 請求轉送到模型供應商", "你的指令與周邊文字"),
                ("Anthropic", "文字模型（Claude）", "你的指令與周邊文字"),
                ("OpenAI", "圖像生成模型", "你的圖像指令"),
                ("Brave Search", "生成圖片時的參考資料搜尋", "由伺服器產生的搜尋字詞"),
                ("Apple", "App Store、以 Apple 帳戶登入、DeviceCheck、iCloud", "由 Apple 的私隱政策管轄"),
            ),
            "caption": "這些供應商在自己的系統上如何保留與處理資料，受其各自的私隱政策管轄。",
        },
        {
            "kind": "prose",
            "id": "icloud",
            "heading": "iCloud 同步",
            "body": [
                "跨裝置同步**預設關閉**。開啟之前，KOI 會要求你確認目前登入的 iCloud 帳戶。",
                "同步的資料寫入你自己的**私人** iCloud 資料庫（容器 `iCloud.com.rainsday.koikeyboard`），並且使用 CloudKit 的加密欄位——金鑰繫於你的 iCloud 鑰匙圈，Apple 與 KOI 開發者都無法讀取內容。",
                "同步屬**手動觸發**，不會在背景自動運行。有兩項設定永遠不會同步：同步開關本身，以及輸入診斷開關。",
            ],
        },
        {
            "kind": "prose",
            "id": "identifiers",
            "heading": "帳戶與識別碼",
            "body": [
                "**安裝識別碼**：KOI 會產生一個隨機 UUID 來識別安裝。它不是裝置識別碼，不會跨 app 追蹤你，重新安裝 app 便會換成新的。伺服器收到之後，會先用一個保密的 pepper 做 SHA-256 雜湊，其後只以雜湊值作速率限制與購買綁定。",
                "**以 Apple 帳戶登入**：屬選用功能，只有在你希望跨裝置保留購買紀錄時才需要。KOI 向 Apple 索取的範圍**只有姓名**，並無索取電郵地址。Apple 只會在首次授權時提供姓名；KOI 會將姓名交給 Firebase Authentication 建立或更新登入帳戶。KOI 自己的 Firestore 帳戶及購買記錄只存 Firebase UID、範圍雜湊值、購買資料與時間戳，不另存姓名或電郵。",
                "**AI 中文改錯**：此實驗功能目前只供 Life Time Plus 使用。鍵盤會把當前完整句子及由本機字碼產生的有限候選字，經 Cloudflare Workers 傳送到 TypeSafe Jev 作語意選擇。Cloudflare 的會員驗證快取只保存雜湊後的會員決定，最多 60 秒，不包含輸入文字；KOI 的 Worker 不會把句子寫入記錄或持久儲存。TypeSafe Jev 對資料的處理由其私隱政策及服務條款管轄。",
                "後端資料庫（Firestore）拒絕一切用戶端直接讀寫，所有寫入都經伺服器程式碼處理。",
            ],
        },
        {
            "kind": "prose",
            "id": "purchases",
            "heading": "購買",
            "body": [
                "所有付款由 Apple 處理。KOI 看不到你的信用卡、付款方式或帳單地址。",
                "購買狀態經 RevenueCat 管理。RevenueCat 會將購買事件傳送到 KOI 的伺服器，內容包括：購買者識別碼、產品編號、交易編號、原始交易編號、購買時間、到期時間、週期類型、取消原因、商店與環境（正式或沙盒）。",
                "這些資料用來判斷你是否擁有 Plus 權限並計算 Credits 餘額，不會用於其他用途。",
            ],
        },
        {
            "kind": "prose",
            "id": "retention",
            "heading": "保留期限",
            "bullets": [
                "AI 請求記錄：只有請求層面的中繼資料，不含內容。",
                "生成圖片時的參考圖快取：伺服器記憶體內保留 **10 分鐘**，上限 24 項。",
                "沙盒環境的操作紀錄：**24 小時**。",
                "Credits 帳目與購買紀錄：保留至帳戶關閉，因為需要處理退款、爭議與權限判斷。",
                "本機學習紀錄與設定：保留在你的裝置上，刪除 app 即告消失。",
            ],
        },
        {
            "kind": "prose",
            "id": "children",
            "heading": "兒童",
            "body": "KOI 並非針對 13 歲以下兒童設計，亦不會刻意收集他們的個人資料。如果你認為有兒童向我們提供了個人資料，請聯絡我們，我們會予以刪除。",
        },
        {
            "kind": "prose",
            "id": "rights",
            "heading": "你的選擇與權利",
            "bullets": [
                "**不使用 AI**：不開啟 KOI Agent，就不會有任何文字傳出裝置。你亦可以在設定中關閉整個 AI 功能。",
                "**不開啟完整取用**：輸入法的核心功能照常運作。",
                "**不同步**：預設本來就不同步，開啟之後亦可隨時關閉。",
                "**刪除本機資料**：刪除 app 即會清除裝置上的學習紀錄與設定。",
                "**刪除 iCloud 資料**：在 iOS 設定 → 你的 Apple 帳戶 → iCloud 之中管理。",
                "**刪除伺服器資料**：電郵至 [privacy@rainsday.com](mailto:privacy@rainsday.com)。請留意，已完成的購買紀錄可能需要保留，以符合稅務與會計要求。",
            ],
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "政策更新",
            "body": "如果 KOI 處理資料的方式有所改變，本頁會隨之更新，並且一併修改頁頂的生效日期。涉及重大改變時，我們會在 app 內告知。",
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "聯絡",
            "bullets": [
                "私隱查詢：[privacy@rainsday.com](mailto:privacy@rainsday.com)",
                "一般支援：[support@rainsday.com](mailto:support@rainsday.com)",
            ],
        },
    ],
}


SUPPORT = {
    "title": "支援 — KOI Keyboard",
    "description": "KOI Keyboard 的安裝步驟、常見問題與疑難排解，包括完整取用權限、輸入法切換、手寫、同步與 Credits。",
    "eyebrow": "KOI · 支援",
    "heading": "支援",
    "lede": "安裝、常見問題與疑難排解。找不到答案，歡迎直接電郵我們。",
    "toc": True,
    "sections": [
        {
            "kind": "steps",
            "id": "install",
            "heading": "開始使用",
            "intro": "安裝 app 之後，還要在 iOS 設定中加入鍵盤，這一步是 iOS 的規定。",
            "items": [
                {
                    "title": "加入鍵盤",
                    "body": "iOS 設定 → 一般 → 鍵盤 → 鍵盤 → 加入新的鍵盤⋯ → 在「第三方鍵盤」中選擇 KOI。",
                },
                {
                    "title": "（選用）開啟完整取用",
                    "body": "在同一頁選擇 KOI，開啟「允許完整取用」。AI 功能、剪貼簿貼上、手寫模型更新，以及共用圖片庫存檔需要這項權限；不開啟的話，輸入法本身完全正常。",
                },
                {
                    "title": "切換到 KOI",
                    "body": "在任何輸入框長按地球鍵，於清單中選擇 KOI。之後在 KOI 之內就可以直接切換五種輸入模式。",
                },
            ],
        },
        {
            "kind": "faq",
            "id": "faq",
            "heading": "常見問題",
            "items": [
                {
                    "question": "為什麼要開啟「完整取用」？可以不開嗎？",
                    "answer": [
                        "iOS 規定第三方鍵盤如果沒有這項權限，就完全沒有網絡能力。KOI 需要它來連接 AI 功能、讀取剪貼簿（只在你按下「貼上」的一刻）、更新手寫模型，以及將生成圖片存入 app 的本機共用圖片庫。",
                        "不開啟完全沒有問題。五種輸入法、候選字、學習、手寫、符號與游標操作全部照常使用；你只是無法使用 AI、貼上、手寫模型更新及共用圖片庫存檔。",
                    ],
                },
                {
                    "question": "我打的字會傳送到什麼地方嗎？",
                    "answer": [
                        "不會。輸入引擎完全在裝置上運行，那部分程式碼沒有任何網絡功能。",
                        "唯一例外是你主動開啟 KOI Agent 並明確選擇操作時，會傳送你的指令，以及畫面所示的已選／之前／之後 context；上限為 2,000 個 Unicode scalar values 及 4,000 個 UTF-8 bytes。詳情見[私隱政策](route:privacy/)。",
                    ],
                },
                {
                    "question": "怎樣在五種輸入法之間切換？",
                    "answer": "在 KOI app 的設定中選擇中文輸入模式。倉頡、速成、筆劃、粵拼、注音各自有對應的鍵盤佈局。",
                },
                {
                    "question": "手寫需要連網嗎？",
                    "answer": "不需要。香港繁體手寫模型已經內建於 app 之內，飛航模式下一樣寫得到。連網只是用來更新模型，不更新亦照常可用。",
                },
                {
                    "question": "打錯碼或拆錯字怎麼辦？",
                    "answer": "KOI 會補上近似碼的候選，排在正常候選之後，所以候選區不會一片空白。如果想清除整個組字，連按兩下刪除鍵。",
                },
                {
                    "question": "為什麼有些字打不出來？",
                    "answer": [
                        "候選字覆蓋基本多文種平面（BMP）內的漢字。少數極罕用的擴充區字（Unicode Ext B 以上）暫時未有收錄。",
                        "如果是常用字卻找不到，請電郵告知我們，並附上你輸入的編碼與想要的字。",
                    ],
                },
                {
                    "question": "換了新 iPhone，設定與學習紀錄怎樣轉移？",
                    "answer": [
                        "開啟跨裝置同步（屬 Plus 功能）。同步使用你自己的私人 iCloud，不會經過 KOI 的伺服器。",
                        "同步屬手動觸發：在設定中按下同步，不會在背景自動執行。兩部裝置都要登入同一個 iCloud 帳戶。",
                    ],
                },
                {
                    "question": "Credits 是什麼？何時會扣減？",
                    "answer": [
                        "Credits 只用於 KOI Agent 的 AI 操作。日常打字、候選字與手寫辨識一律不需要 Credits。",
                        "回覆、改寫、翻譯各扣 1，提問扣 2，生成貼圖扣 6，生成圖片扣 18。",
                        "訂閱每月附送 250 Credits，每批由發放日起 60 日內有效；另行購買的 Credit 包不會過期。",
                    ],
                },
                {
                    "question": "如何取消訂閱？如何退款？",
                    "answer": [
                        "取消：iOS 設定 → 你的 Apple 帳戶 → 訂閱項目 → KOI → 取消訂閱。取消後仍可使用至當期結束。",
                        "退款由 Apple 處理，並非由 KOI 處理。請經 [reportaproblem.apple.com](https://reportaproblem.apple.com) 提出。",
                    ],
                },
                {
                    "question": "KOI 會收集我的使用資料嗎？",
                    "answer": "不會。app 之內沒有任何分析、崩潰回報或廣告追蹤工具，亦不會讀取廣告識別碼。",
                },
            ],
        },
        {
            "kind": "cards",
            "id": "troubleshooting",
            "heading": "疑難排解",
            "columns": 2,
            "items": [
                {
                    "title": "長按地球鍵找不到 KOI",
                    "body": "通常是還未在 iOS 設定中加入鍵盤，請回到「開始使用」的第一步。如果已經加入卻仍然找不到，重新啟動裝置通常可以解決。",
                },
                {
                    "title": "AI 顯示連線失敗",
                    "body": "請依序檢查：完整取用是否已開啟、網絡是否暢通、Credits 是否足夠。也可以在 KOI app 的設定中按「測試連線」確認。",
                },
                {
                    "title": "同步沒有反應",
                    "body": "請確認裝置已登入 iCloud、KOI 的同步開關已開啟，並且你已經手動按過同步——同步不會在背景自動進行。",
                },
                {
                    "title": "候選字排序不合心意",
                    "body": "KOI 會按你的選字習慣學習，多用幾天通常就會貼近你的用法。如果想重新開始，可以在設定中清除學習紀錄。",
                },
            ],
        },
        CREDIT_COSTS,
        {
            "kind": "definitions",
            "id": "credit-model",
            "heading": "Credits 如何計算",
            "items": [
                {
                    "term": "訂閱附送",
                    "detail": "月費與年費計劃每個月發放 250 Credits。年費為全年分十二次發放，並非一次全數發放。每批由發放日起 60 日內有效。",
                },
                {
                    "term": "另行購買",
                    "detail": "Credit 包分 100、300、800 三種，一次性購買，**不會過期**。但不包含聯想輸入與跨裝置同步。",
                },
                {
                    "term": "扣減時機",
                    "detail": "只在你要求 KOI Agent 執行操作時扣減。日常打字不涉及 Credits。",
                },
            ],
        },
        {
            "kind": "definitions",
            "id": "requirements",
            "heading": "系統需求",
            "items": [
                {"term": "系統版本", "detail": "iOS 16.0 或以上。"},
                {
                    "term": "完整取用權限",
                    "detail": "AI 功能、剪貼簿貼上、手寫模型更新，以及共用圖片庫存檔需要開啟「允許完整取用」。不開啟的話，五種輸入法、候選字、學習與手寫全部照常運作。",
                },
                {
                    "term": "字元覆蓋",
                    "detail": "候選字涵蓋基本多文種平面（BMP）內的漢字。部分極罕用的擴充區字（Ext B 以上）暫時無法輸入。",
                },
                {"term": "介面語言", "detail": "app 介面為繁體中文（香港）。"},
            ],
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "聯絡我們",
            "body": "回報問題時，請盡量附上 iOS 版本、KOI 版本、當時使用的輸入模式，以及重現步驟。",
            "bullets": [
                "一般支援：[support@rainsday.com](mailto:support@rainsday.com)",
                "私隱查詢：[privacy@rainsday.com](mailto:privacy@rainsday.com)",
            ],
        },
    ],
}


TERMS = {
    "title": "服務條款 — KOI Keyboard",
    "description": "KOI Keyboard 的服務條款：授權範圍、訂閱與 Credits 條款、AI 功能使用規範、免責聲明與管轄法律。",
    "eyebrow": "KOI · 條款",
    "heading": "服務條款",
    "lede": "本條款列明使用 KOI Keyboard 的規則。訂閱本身由 Apple 的標準條款管轄，本頁補充 KOI 特定的部分。",
    "updated": f"生效日期：{EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "scope",
            "heading": "本條款的範圍",
            "body": [
                "下載或使用 KOI Keyboard，即表示你同意本條款。如不同意，請勿使用本 app。",
                f"透過 App Store 購買的訂閱，同時受 [Apple 標準最終使用者授權合約]({APPLE_EULA}) 管轄。如果兩者有衝突，就購買與訂閱事宜以 Apple 的條款為準。",
            ],
        },
        {
            "kind": "prose",
            "id": "licence",
            "heading": "授權",
            "body": "我們授予你一項個人、非專屬、不可轉讓、可撤銷的授權，讓你在自己擁有或控制的 Apple 裝置上使用 KOI Keyboard。你不得對本 app 進行反向工程、拆解、出租或轉售，亦不得移除當中的專有標示。",
        },
        {
            "kind": "prose",
            "id": "subscriptions",
            "heading": "訂閱",
            "bullets": [
                "KOI Plus 以自動續期訂閱形式提供，設有月費與年費計劃。",
                "款項由你的 Apple 帳戶收取。除非在當期結束前至少 24 小時關閉自動續期，否則訂閱會自動續期。",
                "續期費用會在當期結束前 24 小時內收取。",
                "訂閱管理與關閉自動續期，可在 iOS 設定 → 你的 Apple 帳戶 → 訂閱項目 內進行。",
                "退款由 Apple 處理，並非由 KOI 處理。請經 [reportaproblem.apple.com](https://reportaproblem.apple.com) 提出。",
            ],
        },
        {
            "kind": "prose",
            "id": "credits",
            "heading": "KOI Credits",
            "bullets": [
                "Credits 是使用 KOI Agent 功能的內部計量單位。",
                "Credits **並非貨幣**，沒有現金價值，不可兌現、轉讓，亦不可在 KOI 以外使用。",
                "訂閱附送的 Credits 每月發放 250 個，**由發放日起 60 日內有效**，逾期未用即告失效。年費計劃是全年分十二次發放。",
                "另行購買的 Credit 包（100、300、800）**不會過期**，但不包含聯想輸入與跨裝置同步功能。",
                "訂閱結束後，未使用的訂閱 Credits 會失效；已購買的 Credit 包則予以保留。",
                "Credits 一經用於已完成的操作即不可退還。如果操作因為我們的系統故障而失敗，相關 Credits 會退回你的結餘。",
            ],
        },
        {
            "kind": "prose",
            "id": "ai-use",
            "heading": "AI 功能使用規範",
            "body": [
                "KOI Agent 由第三方 AI 模型提供支援。使用時，你同意不會利用它來：",
            ],
            "bullets": [
                "產生違法內容、騷擾或仇恨言論",
                "生成他人的性化描繪，或涉及未成年人的不當內容",
                "冒充他人或製造具誤導性的虛假資訊",
                "侵犯他人的知識產權或私隱",
                "以自動化方式大量發送請求，或試圖規避用量限制",
            ],
            "after": [
                "AI 產生的內容可能出錯或具誤導性，用於重要用途時請自行核實。我們不會就 AI 輸出的準確性作出保證。",
                "我們保留在發現濫用時暫停或終止服務存取的權利。",
            ],
        },
        {
            "kind": "prose",
            "id": "your-content",
            "heading": "你的內容",
            "body": [
                "你打的字、你的學習紀錄，以及你經 AI 功能產生的內容，都屬於你。我們不會取得當中的擁有權。",
                "為了完成你所要求的操作，我們需要將你送出的內容傳送至 AI 供應商處理。除此之外，我們不會使用你的內容。詳情見[私隱政策](route:privacy/)。",
            ],
        },
        {
            "kind": "prose",
            "id": "availability",
            "heading": "服務可用性與變更",
            "body": [
                "AI 功能依賴第三方服務，可能因為維護、供應商變動或其他因素而暫時無法使用。輸入法本身在離線狀態下依然運作。",
                "我們可能會新增、修改或移除功能。如果變更會實質削弱已付費功能，我們會事先在 app 內告知。",
            ],
        },
        {
            "kind": "prose",
            "id": "disclaimer",
            "heading": "免責聲明與責任限制",
            "body": [
                "KOI Keyboard 按「現狀」提供。在法律允許的最大範圍內，我們不作任何明示或默示的保證，包括適售性、特定用途適用性與不侵權的保證。",
                "在法律允許的最大範圍內，我們不會就任何間接、附帶、特別或衍生性損害承擔責任。任何情況下的總責任，均以你在申索前十二個月內就 KOI 支付的金額為限。",
                "部分司法管轄區不容許排除某些保證或責任，在該等地區，上述限制可能不適用於你。",
            ],
        },
        {
            "kind": "prose",
            "id": "termination",
            "heading": "終止",
            "body": "你可以隨時刪除 app 停止使用。如果你嚴重或重複違反本條款，我們可以暫停或終止你使用 AI 功能的權利。訂閱的取消與退款，仍然按 Apple 的程序處理。",
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "條款更新",
            "body": "本條款可能會更新，更新時會一併修改頁頂的生效日期。涉及重大改變時，我們會在 app 內告知。更新生效後繼續使用，即表示接受新版本。",
        },
        {
            "kind": "prose",
            "id": "law",
            "heading": "管轄法律",
            "body": "本條款受香港特別行政區法律管轄，並按其解釋。相關爭議提交香港法院處理。",
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "聯絡",
            "bullets": [
                "一般查詢：[support@rainsday.com](mailto:support@rainsday.com)",
                "私隱查詢：[privacy@rainsday.com](mailto:privacy@rainsday.com)",
            ],
        },
    ],
}


NOT_FOUND = {
    "title": "找不到頁面 — KOI Keyboard",
    "description": "你要求的 KOI Keyboard 頁面不存在或已經移動。",
    "eyebrow": "KOI · 404",
    "heading": "找不到頁面",
    "lede": "你要求的頁面不存在或已經移動。",
    "canonical": "https://koi.rainsday.com/404.html",
    "sections": [
        {
            "kind": "cards",
            "heading": "不妨試試以下頁面",
            "columns": 2,
            "items": [
                {"title": "首頁", "body": "[KOI Keyboard 產品介紹](route:)"},
                {"title": "私隱政策", "body": "[KOI 實際如何處理你的資料](route:privacy/)"},
                {"title": "支援", "body": "[安裝步驟、常見問題與疑難排解](route:support/)"},
                {"title": "服務條款", "body": "[訂閱、Credits 與使用規範](route:terms/)"},
            ],
        },
    ],
}


PAGES = {
    "": LANDING,
    "privacy/": PRIVACY,
    "support/": SUPPORT,
    "terms/": TERMS,
}
