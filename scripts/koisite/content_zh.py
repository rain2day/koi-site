"""Traditional Chinese content for the KOI public site.

Every factual claim here is traceable to the KOI application source or the
Firebase backend source. Three things must never appear: a price, a purchasable
"Lifetime" tier, and a support response-time promise. See
``docs/superpowers/specs/2026-08-05-koi-public-site-production-content-design.md``
in the application repository for the evidence behind each claim.
"""

from __future__ import annotations

EFFECTIVE_DATE = "2026 年 8 月 5 日"
PRIVACY_EFFECTIVE_DATE = "2026 年 10 月 3 日"
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
            "heading": "一般輸入在本機處理",
            "lead": [
                "KOI 的輸入引擎在裝置上產生候選、拆碼及學習。**一般打字不會逐鍵傳到 KOI 伺服器。**",
            ],
            "points": [
                {"title": "本機輸入", "body": "候選排序及學習在裝置上處理；核心輸入不需要 AI。"},
                {"title": "資料分享", "body": "選用同步、同意後送出的 AI 請求，以及合資格內部測試帳戶的 JEV 背景診斷，各有清楚的資料分享說明。"},
                {"title": "服務資料", "body": "SDK 會處理診斷、效能及使用資料。KOI 不使用廣告識別碼或跨 app 廣告追蹤。"},
                {"title": "你的選擇", "body": "同步預設關閉，AI 分享可撤回；本機資料及圖片可按各自控制清除。"},
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
    "description": "KOI Keyboard 的資料處理說明：本機輸入、選用同步、AI 分享同意、服務供應商、資料保留及帳戶刪除。",
    "eyebrow": "KOI · 私隱",
    "heading": "私隱政策",
    "lede": "本政策說明 KOI Keyboard 如何處理本機輸入、帳戶與購買資料，以及你選擇使用的同步和 AI 功能。",
    "updated": f"生效日期：{PRIVACY_EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "summary",
            "heading": "概要",
            "bullets": [
                "一般打字、候選字排序及學習在裝置上處理。選用 iCloud 同步、送出 AI 請求，以及合資格測試帳戶的 JEV 背景診斷，會涉及下文說明的資料傳送。",
                "使用 AI 前須先明確同意「AI 資料分享」。你可以在 KOI app「AI 與 Credits」撤回同意，停止新的 AI 分享。",
                "KOI 使用帳戶、安裝及購買識別資料來提供登入、Credits、權限、恢復購買及安全防護。雜湊後的識別資料仍可能與帳戶或安裝關聯。",
                "隨附 SDK 會處理效能、診斷及使用資料，用於運作及改善其服務。",
                "KOI 不會出售你的資料，也不會將你的輸入內容用於廣告。",
            ],
        },
        {
            "kind": "prose",
            "id": "not-collected",
            "heading": "廣告與裝置權限",
            "body": [
                "KOI 沒有廣告或跨 app 廣告追蹤功能，亦不使用廣告識別碼 IDFA。服務所需的安裝識別碼及 SDK 識別資料與廣告追蹤分開處理。",
                "KOI 不會瀏覽通訊錄、位置、行事曆或你的既有相片庫。只有你在 KOI app 按下「儲存到相片」時，app 才會以僅限新增的權限加入該張生成圖片。",
                "鍵盤只在你按下「貼上」時讀取剪貼簿，將文字放入 AI 輸入框；其後送出的內容會按 AI 分享規則處理。",
            ],
        },
        {
            "kind": "prose",
            "id": "typing",
            "heading": "本機輸入與學習",
            "body": [
                "輸入引擎在裝置上拆碼、產生及排序候選字，並儲存你選過的候選和聯想資料，改善之後的輸入。",
                "學習資料和設定儲存在 KOI app 與鍵盤的共用容器。一般輸入不會逐鍵傳送到 KOI 的伺服器。下文分別說明選用同步、AI 請求及開發者診斷。",
                "刪除 KOI 帳戶會移除帳戶權限及相關同步資料；一般本機學習、設定與已儲存圖片有各自的清除方式，不會因帳戶刪除而全部清除。",
            ],
        },
        {
            "kind": "prose",
            "id": "full-access",
            "heading": "「完整取用」權限",
            "body": [
                "鍵盤的網絡功能及與 KOI app 共用資料需要「允許完整取用」。這包括 KOI Agent、合資格測試帳戶的 JEV 請求、手寫模型下載，以及共用生成圖片庫。",
                "開啟完整取用不會代替 AI 分享同意。你仍須明確同意後，才可送出新的 AI 請求。基本本機輸入功能可以在沒有完整取用時使用。",
            ],
        },
        {
            "kind": "prose",
            "id": "consent",
            "heading": "AI 分享同意與撤回",
            "body": [
                "KOI app「AI 與 Credits」及鍵盤首次執行 AI 操作時，會顯示「AI 資料分享」說明，列出資料、收件方、用途及保留方式，並提供「同意並繼續」和「取消」。顯示說明本身不會授予同意。",
                "同意以版本記錄在 KOI 的共用設定。沒有目前版本的同意時，新版客戶端會阻止新的 AI 分享；鍵盤操作仍須通過完整取用及上下文限制。",
                "在「AI 與 Credits」按下「已同意 AI 資料分享 · 撤回」，再確認「撤回同意」，可停止新的 AI 分享，包括 JEV。已送出的資料不能收回；撤回不會自動刪除已儲存結果或供應商既有記錄。你仍可取回及確認交付已完成的結果。",
            ],
        },
        {
            "kind": "prose",
            "id": "ai",
            "heading": "KOI Agent 傳送的資料",
            "body": [
                "當你同意並明確執行 Agent 操作，以下內容會經 KOI 的 Firebase／Google Cloud 服務及 OpenRouter，交由 OpenAI 模型處理。圖片理解亦可能使用 Microsoft Azure 提供的 OpenAI 模型。",
            ],
            "bullets": [
                "你送出的提示或指令，以及同一次對話中適用的來回內容。",
                "已預覽的輸入上下文：已選文字、游標或選取範圍之前的文字，再到之後的文字；合併上限為 2,000 個 Unicode scalar values 及 4,000 個 UTF-8 bytes。",
                "圖片功能所需的參考圖片及適用的圖片對話資料。",
            ],
            "after": [
                "這些內容用於理解要求、問答、改寫、回覆、翻譯或生成圖片。查看上下文預覽本身不會送出該段文字。",
                "KOI 的服務另外接收安裝及帳戶綁定識別資料、Firebase App Check 驗證資料，以及操作、交付及 Credits 核對所需的中繼資料。這些驗證資料供 KOI 的帳戶、安全及帳務服務使用，不會作為模型的提示或上下文傳送。",
                "需要最新資料的文字問答可能使用 OpenRouter 的網上搜尋與網頁讀取服務。圖片研究會向 Brave Search 傳送衍生搜尋字詞，並從來源網站擷取參考圖片；搜尋服務及來源網站會接觸相關查詢或請求。",
                "KOI 不自行用 Agent 內容訓練模型。文字請求會要求供應商零保留及不收集內容；這不是對所有圖片、搜尋、JEV、服務記錄或供應商處理作出零保留保證。各服務的政策連結及保留差異見下文。",
            ],
        },
        {
            "kind": "table",
            "id": "third-parties",
            "heading": "服務供應商",
            "intro": "以下服務處理功能所需的資料。供應商及其受託服務可能在你所在司法管轄區以外處理資料；KOI 不會因使用加密或雜湊而將所有資料視為匿名。",
            "columns": ("服務與政策", "用途", "涉及資料"),
            "rows": (
                ("[Firebase／Google Cloud](https://firebase.google.com/support/privacy)", "登入、App Check、AI 中介、帳目、暫存及安全防護", "姓名、帳戶及安裝識別資料、購買資料、AI 請求與加密結果、服務中繼資料"),
                ("[Google ML Kit](https://developers.google.com/ml-kit/ios-data-disclosure)", "裝置上的手寫辨識、模型下載及 SDK 診斷", "裝置及 app 資料、安裝識別碼、功能事件、效能、錯誤及設定語言"),
                ("[RevenueCat](https://www.revenuecat.com/privacy)", "購買、訂閱與恢復狀態", "app 使用者識別碼、購買及裝置／服務資料"),
                ("[OpenRouter](https://openrouter.ai/privacy)", "AI 模型路由、文字搜尋及網頁讀取", "提示、上下文、對話及參考圖片"),
                ("[OpenAI API 資料政策](https://developers.openai.com/api/docs/guides/your-data)", "文字與圖片模型", "AI 指令、上下文、對話及適用的圖片"),
                ("[Microsoft Azure 模型資料政策](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy)", "圖片理解", "圖片及相關文字"),
                ("[Cloudflare](https://www.cloudflare.com/privacypolicy/)", "JEV 驗證、速率限制及轉送", "帳戶／安裝驗證、網絡安全中繼資料及有限輸入片段"),
                ("[TypeSafe JEV](https://typesafe.ai/legal/privacy-policy)", "合資格測試帳戶的背景更正評估", "有限輸入句子及本機產生的候選替換"),
                ("[Brave Search API](https://api-dashboard.search.brave.com/privacy-policy)", "圖片參考資料搜尋", "由請求衍生的搜尋字詞"),
                ("參考資料來源網站", "提供網頁或參考圖片", "伺服器擷取該網站內容的請求；依各網站政策處理"),
                ("[Apple](https://www.apple.com/legal/privacy/)", "App Store、Apple 登入、裝置驗證及私人 CloudKit", "購買、登入／驗證及你選擇同步的資料"),
            ),
            "caption": "供應商政策與適用服務合約說明其處理方式；不應把一項文字請求設定理解為所有服務一律不保留資料。",
        },
        {
            "kind": "prose",
            "id": "icloud",
            "heading": "選用 iCloud 同步",
            "body": [
                "跨裝置同步預設關閉。你開啟並手動執行同步時，KOI 會將選定的鍵盤設定、學習候選及聯想資料寫入你自己的私人 Apple CloudKit 資料庫。",
                "同步內容使用 CloudKit 加密欄位。這項同步不會上傳每次按鍵，也不會同步 AI 分享同意或本機診斷開關。",
                "帳戶刪除會處理與該 KOI 帳戶綁定的同步資料。如 iCloud 身份或網絡狀態令清理未能完成，app 會保留清理狀態並提供重試；Apple 平台本身的保留和備份由其政策處理。",
            ],
        },
        {
            "kind": "prose",
            "id": "identifiers",
            "heading": "帳戶與識別碼",
            "body": [
                "KOI 為安裝建立 UUID，並使用 Firebase 帳戶或訪客識別碼提供購買、Credits、綁定、恢復及防濫用功能。伺服器亦使用安裝、帳戶或網絡資料的雜湊作核對和速率限制；可與帳戶或安裝關聯的雜湊仍屬識別資料。",
                "以 Apple 帳戶登入時，KOI 要求姓名範圍，並將 Apple 提供的姓名交給 Firebase Authentication 建立或更新帳戶。此登入流程沒有要求電郵範圍；Apple 與 Firebase 的登入資料處理仍依其政策及適用設定。",
                "KOI 的服務使用帳戶、安裝綁定與權限資料核准請求。Firebase／Google SDK 亦會處理其診斷資料；Google ML Kit 的官方披露列出裝置及 app 資料、安裝識別碼、效能、功能事件、錯誤和設定語言，用於診斷及使用分析。",
            ],
        },
        {
            "kind": "prose",
            "id": "diagnostics",
            "heading": "開發者診斷與 JEV 測試",
            "body": [
                "本機輸入診斷只會為獲授予 Lifetime Plus、且已驗證為 TestFlight／Sandbox 或 Xcode 環境的帳戶自動啟用，沒有手動開啟診斷的開關。App Store 正式環境不會啟用；一般帳戶不會因此記錄本機輸入診斷。",
                "這些本機記錄可包含輸入碼、已提交字元、刪除及更正評估事件，供開發測試。它們不會經 iCloud 同步，亦沒有自動上傳整份記錄的功能。合資格帳戶可使用清除控制；記錄按 30 天規則在本機維護時清理。",
                "JEV 背景評估另外需要目前版本的 AI 分享同意、完整取用及有效 Lifetime 資格。有限句子與候選替換會經 KOI Cloudflare 服務傳到 TypeSafe JEV；撤回 AI 分享會阻止新請求。此版本的 JEV 在背景評估，不會自動改字。",
                "Cloudflare 的會員授權快取最多保留 60 秒，不包含輸入文字；這不代表 Cloudflare 或 TypeSafe 的所有記錄都會在 60 秒刪除。TypeSafe 的公開政策表示不會用 Input 訓練或微調模型，其一般保留條款沒有固定刪除日數。",
            ],
        },
        {
            "kind": "prose",
            "id": "purchases",
            "heading": "購買與交易紀錄",
            "body": [
                "付款由 Apple 處理。KOI 使用 Apple 及 RevenueCat 的產品、交易、購買／訂閱狀態與 app 使用者識別資料，計算 Credits、提供 Plus、恢復購買、處理退款及防止重複入帳。",
                "KOI 保留與帳戶或訪客錢包關聯的 Credits 帳目及購買核對資料。帳戶刪除後，處理 Apple 退款及帳務所需的交易資料會移至私人審計資料，並以刪除帳戶的替代識別資料處理；這不會恢復原帳戶或已失去的 Credits。",
                "刪除 KOI 帳戶不會取消 Apple 訂閱。你可使用刪除確認畫面的「管理 Apple 訂閱」，或 iOS 設定中的 Apple 訂閱頁面取消。",
            ],
        },
        {
            "kind": "prose",
            "id": "reports",
            "heading": "服務記錄與結果舉報",
            "body": [
                "KOI 會處理請求編號、時間、處理階段、模型、狀態／錯誤分類、App Check 及速率限制資料，以運作和保護服務。KOI 的這些應用程式摘要不自動附上原始提示或生成內容；雲端平台亦會按其設定處理請求及網絡記錄。",
                "你另行確認舉報後，KOI 會收到結果類型、生成結果的 SHA-256 識別摘要及不安全內容原因，並存入安裝識別資料的 HMAC、App Check app 識別碼及時間戳。這個舉報不傳送帳戶 UID、完整提示、生成文字／圖片或對話紀錄。",
                "舉報中繼資料的刪除資格日期設為建立後 30 天，按非同步清理處理；不是保證在第 30 天即時完成實體刪除。帳戶刪除不會延長或重設這個日期。你直接聯絡支援時，亦會提供該通訊的地址、內容及附件。",
            ],
        },
        {
            "kind": "prose",
            "id": "retention",
            "heading": "資料保留與刪除時間",
            "bullets": [
                "AI 結果取回：生成文字及圖片可加密儲存在 Google Cloud Storage，與帳戶及操作關聯，供中斷後取回及核對交付。已接受結果的 app 取回期限設為最多 24 小時；未交付結果另有復原期限。儲存桶亦設定物件建立後一日的生命週期刪除規則，到期資料另會在帳戶後續服務請求中分批清理。儲存清理可先於 app 期限發生；生命週期刪除以非同步方式執行，並非保證完整 24 小時可取回，亦非保證所有 AI 資料在 24 小時內刪除。",
                "對話及圖片：目前對話暫留在鍵盤工作階段，可清除；已儲存圖片留在裝置的 KOI 圖片庫，直到你刪除。另存至 Apple 相片的副本須在相片 app 中管理。",
                "圖片參考快取：伺服器記憶體快取的期限為 10 分鐘，上限 24 項及 32 MiB；在快取存取及維護時移除到期項目。",
                "供應商處理：文字請求要求零保留及不收集內容。圖片、搜尋、JEV、安全、帳務及 SDK 資料有各自的政策與合約。Brave 的 Search API 公開通知列出搜尋查詢記錄最多保留 90 天供帳務及疑難排解，並保留法律義務例外。",
                "帳戶及購買：帳戶刪除會移除帳戶資料、有效綁定及 AI 結果；退款、財務核對、防濫用所需的交易、刪除與安全記錄可能繼續保留，沒有統一的刪除期限。雲端平台及備份另依其設定處理。可聯絡我們查詢具體記錄的保留及刪除。",
            ],
        },
        {
            "kind": "prose",
            "id": "children",
            "heading": "兒童",
            "body": "KOI 並非針對 13 歲以下兒童設計，亦不會刻意收集他們的個人資料。如果你認為有兒童向我們提供了個人資料，請聯絡我們處理。",
        },
        {
            "kind": "prose",
            "id": "rights",
            "heading": "你的選擇與帳戶刪除",
            "bullets": [
                "**撤回 AI 分享**：在 KOI app「AI 與 Credits」按「已同意 AI 資料分享 · 撤回」並確認。這會阻止新的 AI 分享，一般本機輸入仍可使用。",
                "**關閉同步**：同步預設關閉；你可停止手動同步並關閉開關。",
                "**刪除帳戶或訪客資料**：在「AI 與 Credits」的帳戶區按「刪除帳戶」或「刪除訪客資料」，閱讀披露並輸入「刪除」確認。Apple 登入帳戶須重新驗證；訪客刪除不要求 Apple 登入。未完成的清理會顯示重試或處理狀態。",
                "**刪除的影響**：相關帳戶／訪客 Credits 及該帳戶的 Lifetime Plus 會失去；帳戶權限、有效綁定、AI 分享同意、開發者診斷及相關同步資料會清理。一般本機學習、設定及圖片庫須使用各自的清除／刪除控制。交易審計及上文所列保留例外仍適用。",
                "**本機與相片資料**：在 KOI 的學習、診斷或圖片庫使用清除控制；相片 app 內的副本另行刪除。解除安裝可移除 app 目前的本機儲存；iCloud、裝置備份及供應商副本按各自的設定及政策處理。",
                "**查閱、更正或刪除查詢**：聯絡 [privacy@rainsday.com](mailto:privacy@rainsday.com)。如須確認資料擁有人，我們會要求適當的帳戶或交易證明；請勿傳送密碼或完整驗證權杖。",
            ],
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "政策更新",
            "body": "本頁會隨資料處理方式更新並修改生效日期。如 AI 收件方、分享資料或用途改變，KOI 會更新分享說明及同意版本，並要求重新同意。",
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "聯絡",
            "bullets": [
                "私隱查詢：[privacy@rainsday.com](mailto:privacy@rainsday.com)",
                "一般支援：[support@rainsday.com](mailto:support@rainsday.com) 或 [支援頁面](route:support/)。",
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
                        "一般輸入、候選排序及學習在裝置上處理，不會逐鍵傳到 KOI 伺服器。",
                        "明確同意 AI 分享並執行 KOI Agent 操作時，會傳送你的指令、適用對話及畫面已預覽的選取／之前／之後上下文；上下文上限為 2,000 個 Unicode scalar values 及 4,000 個 UTF-8 bytes。你可在「AI 與 Credits」撤回 AI 分享同意。",
                        "選用同步會將設定及學習資料送到你的私人 CloudKit。獲授予 Lifetime Plus 的合資格 TestFlight／Xcode 測試帳戶，也可能在同意及完整取用後進行 JEV 背景評估；App Store 正式版本不會啟用。收件方與保留方式見[私隱政策](route:privacy/)。",
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
                    "answer": "KOI 的服務及隨附 SDK 會處理操作、效能、診斷及使用資料，以提供及保護功能。KOI 不使用廣告識別碼或跨 app 廣告追蹤。詳情及你的選擇見[私隱政策](route:privacy/)。",
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
