"""Traditional Chinese content for the KOI public site.

Every factual claim here is traceable to the KOI application source or the
Firebase backend source. Three things must never appear: a price, a purchasable
"Lifetime" tier, and a support response-time promise. See
``docs/superpowers/specs/2026-08-05-koi-public-site-production-content-design.md``
in the application repository for the evidence behind each claim.
"""

from __future__ import annotations

EFFECTIVE_DATE = "2026 年 8 月 5 日"
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
}

CREDIT_COSTS = {
    "kind": "table",
    "id": "credits",
    "heading": "每項 AI 操作扣幾多 Credits",
    "intro": "Credits 只喺你主動叫 KOI Agent 做嘢先會扣。日常打字、候選字、手寫辨識全部唔使 Credits。",
    "columns": ("操作", "Credits"),
    "rows": (
        ("回覆建議", "1"),
        ("改寫潤飾", "1"),
        ("翻譯", "1"),
        ("提問", "2"),
        ("生成貼圖", "6"),
        ("生成圖片", "18"),
    ),
    "caption": "圖像生成成本較高，所以扣數較多。",
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
    "sections": [
        {
            "kind": "cards",
            "id": "input-methods",
            "heading": "五種輸入方式，一個鍵盤",
            "intro": "唔使為咗轉輸入法而喺系統鍵盤列表入面兜圈。五種模式都喺 KOI 入面，切換即到。",
            "columns": 3,
            "items": [
                {
                    "title": "倉頡",
                    "meta": "字形",
                    "body": "原生鍵位排列，鍵帽同時顯示英文字母同倉頡字根。候選字按字頻排序，你揀得多嘅字會自動排前。",
                },
                {
                    "title": "速成",
                    "meta": "字形",
                    "body": "首尾碼輸入。同倉頡共用同一套鍵位，唔使重新學位置。",
                },
                {
                    "title": "筆劃",
                    "meta": "字形",
                    "body": "五鍵筆劃輸入，支援 `*` 萬用字元——唔記得中間幾劃，打個星號照樣搵得返。",
                },
                {
                    "title": "粵拼",
                    "meta": "拼音",
                    "body": "全拼、簡拼都收，可以加聲調數字收窄結果。輸出港式繁體中文。",
                },
                {
                    "title": "注音（大千）",
                    "meta": "拼音",
                    "body": "獨立注音鍵盤佈局，輸出台灣繁體中文。",
                },
                {
                    "title": "英文",
                    "meta": "同步解碼",
                    "body": "同一串輸入會同時解做中文同英文候選，打英文唔使切鍵盤。筆劃模式下停用。",
                },
            ],
        },
        {
            "kind": "showcase",
            "id": "screens",
            "heading": "實際畫面",
            "intro": "以下兩張都係 KOI 執行中嘅實際擷取畫面，唔係示意圖。",
            "items": [
                {
                    "source": "shots/keyboard.png",
                    "alt": "KOI 鍵盤畫面，每個鍵帽同時顯示英文字母同倉頡字根，候選區顯示 0 至 9 數字行",
                    "caption": "鍵帽同時顯示英文字母同倉頡字根。未開始組字嗰陣，候選區顯示數字行。",
                    "badge": "實際擷取",
                },
                {
                    "source": "shots/settings.png",
                    "alt": "KOI 設定畫面，顯示輸入法、完整取用同同步狀態，下面係五種輸入模式選擇器",
                    "caption": "設定畫面：輸入法、完整取用同同步狀態一眼睇晒，下面直接揀輸入模式。",
                    "badge": "實際擷取",
                },
            ],
        },
        {
            "kind": "cards",
            "id": "feel",
            "heading": "點打都得，唔使遷就鍵盤",
            "intro": "同一個組字，四種輸入方式可以撈埋一齊用。打到一半改變主意，唔使清空重來。",
            "columns": 2,
            "items": [
                {
                    "title": "點、滑、混合、雙指和弦",
                    "body": "逐鍵點都得，一筆滑過去都得，點一半再滑落去都得。兩隻手指同時㩒亦都收得，全部歸入同一個組字。",
                },
                {
                    "title": "滑歪咗都收得返",
                    "body": "滑行解碼容許最多兩個鍵位置換成隔籬鍵。手指郁咗少少唔會即刻死機。",
                },
                {
                    "title": "打錯碼唔會得個吉",
                    "body": "拆錯字嗰陣，KOI 會補上近似碼嘅候選，排喺正常候選後面。候選區唔會空白一片畀你乾等。",
                },
                {
                    "title": "刪除同游標",
                    "body": "㩒一下刪最後一個碼，連㩒兩下清走成個組字，長㩒拖住會加速。空白鍵左右掃可以郁游標。",
                },
            ],
        },
        {
            "kind": "cards",
            "id": "handwriting",
            "heading": "手寫，唔使連網",
            "intro": "手寫辨識模型直接封裝喺 app 入面，唔使下載、唔使連線、飛機模式一樣寫得。",
            "columns": 2,
            "items": [
                {
                    "title": "港式手寫模型",
                    "body": "用嘅係香港繁體手寫模型，唔係普通話或者簡體模型。寫慣嘅字形辨得返。",
                },
                {
                    "title": "水池筆跡",
                    "body": "手寫區用 Metal 渲染成一池水：落筆有漣漪、有折射、有波紋。強度可以喺設定調校，唔想動就調細。",
                },
            ],
        },
        {
            "kind": "cards",
            "id": "agent",
            "heading": "KOI Agent",
            "intro": "需要嘅時候先開，唔開就完全唔存在。六種模式，全部喺鍵盤上面搞掂，唔使跳出去其他 app。",
            "columns": 3,
            "items": [
                {"title": "自動", "body": "睇返你手上嘅內容自己判斷應該做咩。"},
                {"title": "提問", "body": "直接問，答案可以直接插入。"},
                {"title": "回覆", "body": "睇住對方訊息草擬一個回覆。"},
                {"title": "改寫", "body": "潤飾、改語氣、翻譯。"},
                {"title": "貼圖", "body": "生成透明背景貼圖。"},
                {"title": "圖片", "body": "生成完整場景圖片。"},
            ],
        },
        CREDIT_COSTS,
        {
            "kind": "callout",
            "tone": "privacy",
            "heading": "打字引擎完全不連網",
            "body": [
                "KOI 嘅輸入引擎——候選字產生、拆碼、學習紀錄——冇任何網絡程式碼。你打嘅字唔會離開部機。",
                "文字只會喺一種情況下傳出去：你主動開啟 KOI Agent 並且送出請求。除此之外冇例外。",
            ],
            "bullets": [
                "**冇**分析工具、**冇**崩潰回報 SDK、**冇**廣告識別碼",
                "**冇**記錄你嘅按鍵",
                "學習紀錄同自訂設定留喺裝置上，或者由你自己控制嘅私人 iCloud",
                "詳情見[私隱政策](route:privacy/)",
            ],
        },
        {
            "kind": "cards",
            "id": "plus",
            "heading": "KOI Plus",
            "intro": "免費版本已經包含五種輸入法、手寫、學習同全部基本輸入功能。Plus 加開兩項功能，另外附送每月 Credits。",
            "columns": 2,
            "items": [
                {
                    "title": "聯想輸入",
                    "body": "落字之後接住推薦下一個詞或者成句短語，減少逐個字拆碼。",
                },
                {
                    "title": "跨裝置同步",
                    "body": "設定同學習紀錄經你自己嘅私人 iCloud 同步。預設關閉，開咗之後由你手動㩒同步，唔會喺背景偷偷傳嘢。",
                },
            ],
        },
        {
            "kind": "definitions",
            "id": "credit-model",
            "heading": "Credits 點計",
            "items": [
                {
                    "term": "訂閱附送",
                    "detail": "月費同年費計劃每個月發放 250 Credits。年費係全年分十二次發放，唔係一次過畀晒。每批由發放日起 60 日內有效。",
                },
                {
                    "term": "另行購買",
                    "detail": "Credit 包分 100、300、800 三種，一次性購買，**唔會過期**。但唔包括聯想輸入同跨裝置同步。",
                },
                {
                    "term": "扣費時機",
                    "detail": "只喺你叫 KOI Agent 做嘢先扣。日常打字唔涉及 Credits。",
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
                    "detail": "AI 功能同剪貼簿貼上需要開啟「允許完整取用」。唔開嘅話，五種輸入法、候選字、學習同手寫全部照樣運作。詳情見[支援頁](route:support/)。",
                },
                {
                    "term": "字元覆蓋",
                    "detail": "候選字覆蓋基本多文種平面（BMP）內嘅漢字。部分極罕用嘅擴充區字（Ext B 以上）暫時打唔到。",
                },
                {"term": "介面語言", "detail": "app 介面為繁體中文（香港）。"},
            ],
        },
    ],
}


PRIVACY = {
    "title": "私隱政策 — KOI Keyboard",
    "description": "KOI Keyboard 的私隱政策：打字資料留在裝置、沒有分析工具、沒有廣告識別碼，以及 AI 功能實際傳送哪些資料。",
    "eyebrow": "KOI · 私隱",
    "heading": "私隱政策",
    "lede": "呢份政策講明 KOI Keyboard 實際上處理咩資料。每一項都對得返 app 同後端嘅實作，唔係範本填空。",
    "updated": f"生效日期：{EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "summary",
            "heading": "一分鐘概要",
            "bullets": [
                "你打嘅字**唔會**離開部機，除非你主動開啟 KOI Agent 送出請求。",
                "KOI **冇**安裝任何分析、崩潰回報或者廣告追蹤工具。",
                "KOI **唔會**讀取你嘅廣告識別碼或者裝置識別碼。",
                "學習紀錄同設定存喺裝置上；如果你開咗同步，會存喺**你自己**嘅私人 iCloud。",
                "我哋唔會出售你嘅資料，亦唔會攞去做廣告。",
            ],
            "after": "以下逐項講清楚。",
        },
        {
            "kind": "prose",
            "id": "not-collected",
            "heading": "我哋唔收集嘅嘢",
            "body": "呢一節比「我哋收集咩」更重要，所以擺喺前面。KOI 嘅程式碼入面搵唔到以下任何一項：",
            "bullets": [
                "分析或者使用統計 SDK（例如 Firebase Analytics、Mixpanel、Amplitude）",
                "崩潰回報 SDK（例如 Crashlytics、Sentry）",
                "廣告或者歸因 SDK（例如 AppsFlyer、Adjust、Facebook SDK）",
                "廣告識別碼（IDFA）、供應商識別碼（IDFV）或者 App 追蹤透明度（ATT）請求",
                "按鍵記錄——KOI 唔會逐個鍵記低你㩒過咩",
                "通訊錄、相片庫、位置或者行事曆存取",
            ],
        },
        {
            "kind": "prose",
            "id": "typing",
            "heading": "你打嘅字",
            "body": [
                "KOI 嘅輸入引擎完全喺你部裝置上運作。拆碼、產生候選字、排序、學習——全部係本機運算，呢個部分嘅程式碼冇任何網絡功能。",
                "你揀過嘅字會令 KOI 學識你嘅習慣，令下次同一串碼排得靠前啲。呢啲學習紀錄存喺 app 嘅共用容器 `group.com.rainsday.koikeyboard` 入面，只有 KOI 自己讀得到。",
                "刪除 KOI 就會連同呢啲本機資料一併移除。",
            ],
        },
        {
            "kind": "prose",
            "id": "full-access",
            "heading": "「完整取用」權限",
            "body": [
                "iOS 規定：鍵盤擴充功能如果冇開啟「允許完整取用」，就完全冇網絡能力。所以 KOI 需要呢個權限嚟做以下三件事：",
            ],
            "bullets": [
                "連接 KOI Agent（AI 功能）",
                "由剪貼簿貼上文字到 AI 輸入框——只喺你㩒「貼上」嗰刻先讀取剪貼簿",
                "更新手寫辨識模型（基本模型已經內建，唔更新一樣用得）",
            ],
            "after": [
                "唔開呢個權限，KOI 嘅五種輸入法、候選字、學習、手寫、符號、游標操作全部照樣運作。你會失去嘅只有上面三項。",
                "開啟權限本身**唔會**觸發任何資料傳送。傳送只會喺你主動使用相關功能嗰陣發生。",
            ],
        },
        {
            "kind": "prose",
            "id": "ai",
            "heading": "KOI Agent 實際傳送啲咩",
            "body": [
                "當你開啟 KOI Agent 並且送出請求，以下資料會傳去 KOI 嘅伺服器（Google Cloud Functions，位於 `asia-east1`）：",
            ],
            "bullets": [
                "你輸入嘅指令文字",
                "你當時所在輸入框嘅周邊文字，**上限 2,000 個 UTF-16 單位**——唔係成個文件，係游標附近一段",
                "同一次對話入面之前嘅來回內容",
                "一個安裝識別碼（見下文「識別碼」一節）同一個 Firebase App Check 驗證權杖",
            ],
            "after": [
                "**唔會**傳送嘅嘢：截圖（KOI 冇截圖功能）、你嘅剪貼簿內容（除非你自己㩒「貼上」）、通訊錄、其他 app 嘅內容。",
                "伺服器嘅記錄只保留請求層面嘅資料：請求編號、路徑、狀態碼、耗時、使用咗邊個模型、處理階段。**指令內容同周邊文字唔會寫入記錄**。",
            ],
        },
        {
            "kind": "table",
            "id": "third-parties",
            "heading": "第三方服務",
            "intro": "以下係 KOI 實際接觸到嘅第三方。留意「在裝置上」同「經網絡」嘅分別。",
            "columns": ("服務", "用途", "資料去向"),
            "rows": (
                ("Google ML Kit Digital Ink", "手寫辨識", "**在裝置上**運行，模型內建於 app，唔會傳出筆跡"),
                ("Firebase App Check（經 Apple DeviceCheck）", "阻止伺服器被濫用", "裝置驗證權杖"),
                ("Firebase Authentication", "選用的「以 Apple 帳戶登入」", "見「帳戶與識別碼」"),
                ("Firebase Cloud Functions / Firestore", "AI 請求處理、Credits 帳目", "見「KOI Agent」同「購買」"),
                ("RevenueCat", "訂閱同購買狀態管理", "見「購買」"),
                ("OpenRouter", "將 AI 請求轉送到模型供應商", "你嘅指令同周邊文字"),
                ("Anthropic", "文字模型（Claude）", "你嘅指令同周邊文字"),
                ("OpenAI", "圖像生成模型", "你嘅圖像指令"),
                ("Brave Search", "生成圖片時的參考資料搜尋", "由伺服器產生的搜尋字詞"),
                ("Apple", "App Store、以 Apple 帳戶登入、DeviceCheck、iCloud", "由 Apple 的私隱政策管轄"),
            ),
            "caption": "呢啲供應商喺佢哋自己系統上點樣保留同處理資料，受佢哋各自嘅私隱政策管轄。",
        },
        {
            "kind": "prose",
            "id": "icloud",
            "heading": "iCloud 同步",
            "body": [
                "跨裝置同步**預設關閉**。開啟之前，KOI 會要求你確認目前登入嘅 iCloud 帳戶。",
                "同步嘅資料寫入你自己嘅**私人** iCloud 資料庫（容器 `iCloud.com.rainsday.koikeyboard`），並且使用 CloudKit 的加密欄位——金鑰繫於你嘅 iCloud 鑰匙圈，Apple 同 KOI 開發者都讀唔到內容。",
                "同步係**手動觸發**嘅，唔會喺背景自動運行。有兩項設定永遠唔會同步：同步開關本身，同埋輸入診斷開關。",
            ],
        },
        {
            "kind": "prose",
            "id": "identifiers",
            "heading": "帳戶與識別碼",
            "body": [
                "**安裝識別碼**：KOI 會產生一個隨機 UUID 嚟識別安裝。呢個唔係裝置識別碼，唔會跨 app 追蹤你，重裝 app 就會換新。伺服器收到之後，會先用一個保密的 pepper 做 SHA-256 雜湊，之後只用雜湊值嚟做速率限制同購買綁定。",
                "**以 Apple 帳戶登入**：屬選用功能，只喺你想跨裝置保留購買紀錄時先需要。KOI 向 Apple 索取嘅範圍**只有姓名**，冇索取電郵地址。伺服器上嘅帳戶記錄只存一個隨機的範圍雜湊值同時間戳，冇姓名、冇電郵。",
                "後端資料庫（Firestore）拒絕一切用戶端直接讀寫，所有寫入都經伺服器程式碼處理。",
            ],
        },
        {
            "kind": "prose",
            "id": "purchases",
            "heading": "購買",
            "body": [
                "所有付款由 Apple 處理。KOI 睇唔到你嘅信用卡、付款方式或者帳單地址。",
                "購買狀態經 RevenueCat 管理。RevenueCat 會將購買事件傳送到 KOI 嘅伺服器，內容包括：購買者識別碼、產品編號、交易編號、原始交易編號、購買時間、到期時間、週期類型、取消原因、商店同環境（正式或沙盒）。",
                "呢啲資料用嚟決定你有冇 Plus 權限同計算 Credits 餘額，唔會用於其他用途。",
            ],
        },
        {
            "kind": "prose",
            "id": "retention",
            "heading": "保留期限",
            "bullets": [
                "AI 請求記錄：只有請求層面嘅中繼資料，唔含內容。",
                "生成圖片時的參考圖快取：伺服器記憶體內保留 **10 分鐘**，上限 24 項。",
                "沙盒環境的操作紀錄：**24 小時**。",
                "Credits 帳目同購買紀錄：保留至帳戶關閉，因為要處理退款、爭議同權限判斷。",
                "本機學習紀錄同設定：保留喺你部裝置，刪除 app 即消失。",
            ],
        },
        {
            "kind": "prose",
            "id": "children",
            "heading": "兒童",
            "body": "KOI 唔係針對 13 歲以下兒童設計，亦唔會刻意收集佢哋嘅個人資料。如果你認為有兒童向我哋提供咗個人資料，請聯絡我哋，我哋會刪除。",
        },
        {
            "kind": "prose",
            "id": "rights",
            "heading": "你嘅選擇同權利",
            "bullets": [
                "**唔用 AI**：唔開 KOI Agent，就唔會有任何文字傳出裝置。你亦可以喺設定入面關閉整個 AI 功能。",
                "**唔開完整取用**：輸入法核心功能照樣運作。",
                "**唔同步**：預設就係唔同步。開咗之後可以隨時關閉。",
                "**刪除本機資料**：刪除 app 即清除裝置上嘅學習紀錄同設定。",
                "**刪除 iCloud 資料**：喺 iOS 設定 → 你的 Apple 帳戶 → iCloud 入面管理。",
                "**刪除伺服器資料**：電郵 [privacy@rainsday.com](mailto:privacy@rainsday.com)。請留意，已完成嘅購買紀錄可能需要保留以符合稅務同會計要求。",
            ],
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "政策更新",
            "body": "如果 KOI 處理資料嘅方式有改變，呢一頁會更新，並且會改埋頁頂嘅生效日期。涉及重大改變時，我哋會喺 app 內告知。",
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
    "lede": "安裝、常見問題同疑難排解。搵唔到答案就直接電郵我哋。",
    "toc": True,
    "sections": [
        {
            "kind": "steps",
            "id": "install",
            "heading": "開始使用",
            "intro": "裝完 app 之後仲要喺 iOS 設定入面加入鍵盤，呢步係 iOS 規定嘅。",
            "items": [
                {
                    "title": "加入鍵盤",
                    "body": "iOS 設定 → 一般 → 鍵盤 → 鍵盤 → 加入新的鍵盤⋯ → 喺「第三方鍵盤」揀 KOI。",
                },
                {
                    "title": "（選用）開啟完整取用",
                    "body": "喺同一版揀 KOI，開啟「允許完整取用」。呢個權限只係 AI 功能同剪貼簿貼上先需要；唔開嘅話輸入法本身完全正常。",
                },
                {
                    "title": "切換到 KOI",
                    "body": "喺任何輸入框長㩒地球鍵，喺清單揀 KOI。之後喺 KOI 入面就可以直接切換五種輸入模式。",
                },
            ],
        },
        {
            "kind": "faq",
            "id": "faq",
            "heading": "常見問題",
            "items": [
                {
                    "question": "點解要開「完整取用」？唔開得唔得？",
                    "answer": [
                        "iOS 規定第三方鍵盤如果冇呢個權限，就完全冇網絡能力。KOI 需要佢嚟連接 AI 功能、讀取剪貼簿（只喺你㩒「貼上」嗰刻）同更新手寫模型。",
                        "唔開完全冇問題。五種輸入法、候選字、學習、手寫、符號、游標操作全部照用。你只係用唔到 AI 同貼上。",
                    ],
                },
                {
                    "question": "我打嘅字會唔會傳去邊？",
                    "answer": [
                        "唔會。輸入引擎完全喺裝置上運行，嗰部分程式碼冇任何網絡功能。",
                        "唯一例外係你主動開啟 KOI Agent 送出請求嗰陣，會傳送你嘅指令同游標附近最多 2,000 個 UTF-16 單位嘅文字。詳情見[私隱政策](route:privacy/)。",
                    ],
                },
                {
                    "question": "點樣喺五種輸入法之間切換？",
                    "answer": "喺 KOI app 嘅設定入面揀中文輸入模式。倉頡、速成、筆劃、粵拼、注音各自有對應嘅鍵盤佈局。",
                },
                {
                    "question": "手寫要唔要連網？",
                    "answer": "唔使。香港繁體手寫模型已經內建喺 app 入面，飛機模式一樣寫得。連網只係用嚟更新模型，唔更新照用。",
                },
                {
                    "question": "打錯碼／拆錯字點算？",
                    "answer": "KOI 會補上近似碼嘅候選，排喺正常候選後面，所以候選區唔會空白一片。如果想清走成個組字，連㩒兩下刪除鍵。",
                },
                {
                    "question": "點解有啲字打唔到？",
                    "answer": [
                        "候選字覆蓋基本多文種平面（BMP）內嘅漢字。少數極罕用嘅擴充區字（Unicode Ext B 以上）暫時未收。",
                        "如果係常用字但搵唔到，請電郵話我哋知，附上你打嘅碼同想要嘅字。",
                    ],
                },
                {
                    "question": "換咗新 iPhone，設定同學習紀錄點搬？",
                    "answer": [
                        "開啟跨裝置同步（屬 Plus 功能）。同步用你自己嘅私人 iCloud，唔會經 KOI 嘅伺服器。",
                        "同步係手動觸發嘅：喺設定入面㩒同步，唔會喺背景自動行。兩部機都要登入同一個 iCloud 帳戶。",
                    ],
                },
                {
                    "question": "Credits 係咩？幾時會扣？",
                    "answer": [
                        "Credits 只用喺 KOI Agent 嘅 AI 操作。日常打字、候選字、手寫辨識一律唔使 Credits。",
                        "回覆、改寫、翻譯各扣 1，提問扣 2，生成貼圖扣 6，生成圖片扣 18。",
                        "訂閱每月附送 250 Credits，每批由發放日起 60 日內有效；另行購買嘅 Credit 包唔會過期。",
                    ],
                },
                {
                    "question": "訂閱點取消？點退款？",
                    "answer": [
                        "取消：iOS 設定 → 你的 Apple 帳戶 → 訂閱項目 → KOI → 取消訂閱。取消後仍可用到當期完結。",
                        "退款由 Apple 處理，唔係由 KOI 處理。請經 [reportaproblem.apple.com](https://reportaproblem.apple.com) 提出。",
                    ],
                },
                {
                    "question": "KOI 收唔收集我嘅使用數據？",
                    "answer": "冇。app 入面冇任何分析、崩潰回報或者廣告追蹤工具，亦唔會讀取廣告識別碼。",
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
                    "title": "長㩒地球鍵見唔到 KOI",
                    "body": "通常係未喺 iOS 設定加入鍵盤。返去「開始使用」第一步。如果加咗仍然見唔到，重新啟動部機通常解決得到。",
                },
                {
                    "title": "AI 顯示連線失敗",
                    "body": "順序檢查：完整取用有冇開、網絡通唔通、Credits 夠唔夠。可以喺 KOI app 設定入面㩒「測試連線」確認。",
                },
                {
                    "title": "同步冇反應",
                    "body": "確認裝置已登入 iCloud、KOI 嘅同步開關已開啟，並且你已經手動㩒過同步——同步唔會自動喺背景進行。",
                },
                {
                    "title": "候選字排序唔啱心水",
                    "body": "KOI 會按你嘅揀選習慣學習，用多幾日通常會貼近返。如果想重新開始，可以喺設定入面清除學習紀錄。",
                },
            ],
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "聯絡我哋",
            "body": "報告問題嗰陣，如果可以請附上 iOS 版本、KOI 版本、用緊邊種輸入模式，同重現步驟。",
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
    "lede": "呢份條款講明使用 KOI Keyboard 嘅規則。訂閱本身由 Apple 嘅標準條款管轄，呢一頁補充 KOI 特定嘅部分。",
    "updated": f"生效日期：{EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "scope",
            "heading": "本條款嘅範圍",
            "body": [
                "下載或者使用 KOI Keyboard，即表示你同意呢份條款。唔同意嘅話，請唔好使用本 app。",
                f"透過 App Store 購買嘅訂閱，同時受 [Apple 標準最終使用者授權合約]({APPLE_EULA}) 管轄。如果兩者有衝突，就購買同訂閱事宜以 Apple 嘅條款為準。",
            ],
        },
        {
            "kind": "prose",
            "id": "licence",
            "heading": "授權",
            "body": "我哋授予你一項個人、非專屬、不可轉讓、可撤銷嘅授權，喺你擁有或控制嘅 Apple 裝置上使用 KOI Keyboard。你唔可以將 app 反向工程、拆解、出租、轉售，或者移除當中嘅專有標示。",
        },
        {
            "kind": "prose",
            "id": "subscriptions",
            "heading": "訂閱",
            "bullets": [
                "KOI Plus 以自動續期訂閱形式提供，設有月費同年費計劃。",
                "款項由你嘅 Apple 帳戶收取。除非喺當期結束前至少 24 小時關閉自動續期，否則訂閱會自動續期。",
                "續期費用會喺當期結束前 24 小時內收取。",
                "訂閱管理同關閉自動續期，喺 iOS 設定 → 你的 Apple 帳戶 → 訂閱項目 內進行。",
                "退款由 Apple 處理，唔係由 KOI 處理。請經 [reportaproblem.apple.com](https://reportaproblem.apple.com) 提出。",
            ],
        },
        {
            "kind": "prose",
            "id": "credits",
            "heading": "KOI Credits",
            "bullets": [
                "Credits 係使用 KOI Agent 功能嘅內部計量單位。",
                "Credits **唔係貨幣**，冇現金價值，唔可以兌現、轉讓或者喺 KOI 以外使用。",
                "訂閱附送嘅 Credits 每月發放 250 個，**由發放日起 60 日內有效**，逾期未用即失效。年費計劃係全年分十二次發放。",
                "另行購買嘅 Credit 包（100、300、800）**唔會過期**，但唔包含聯想輸入同跨裝置同步功能。",
                "訂閱結束後，未使用嘅訂閱 Credits 會失效；已購買嘅 Credit 包會保留。",
                "Credits 一經用於已完成嘅操作即不可退還。如果操作因為我哋嘅系統故障而失敗，相關 Credits 會退回你嘅結餘。",
            ],
        },
        {
            "kind": "prose",
            "id": "ai-use",
            "heading": "AI 功能使用規範",
            "body": [
                "KOI Agent 由第三方 AI 模型提供支援。使用時你同意唔會利用佢嚟：",
            ],
            "bullets": [
                "產生違法內容、騷擾或者仇恨言論",
                "生成他人嘅性化描繪，或者涉及未成年人嘅不當內容",
                "冒充他人或者製造具誤導性嘅虛假資訊",
                "侵犯他人嘅智慧財產權或者私隱",
                "以自動化方式大量發送請求，或者試圖規避用量限制",
            ],
            "after": [
                "AI 產生嘅內容可能出錯或者具誤導性。喺重要用途上請自行核實。我哋唔會就 AI 輸出嘅準確性作出保證。",
                "我哋保留喺發現濫用時暫停或者終止服務存取嘅權利。",
            ],
        },
        {
            "kind": "prose",
            "id": "your-content",
            "heading": "你嘅內容",
            "body": [
                "你打嘅字、你嘅學習紀錄，以及你經 AI 功能產生嘅內容，都屬於你。我哋唔會取得當中嘅擁有權。",
                "為咗完成你請求嘅操作，我哋需要將你送出嘅內容傳送至 AI 供應商處理。除此之外我哋唔會使用你嘅內容。詳情見[私隱政策](route:privacy/)。",
            ],
        },
        {
            "kind": "prose",
            "id": "availability",
            "heading": "服務可用性同變更",
            "body": [
                "AI 功能依賴第三方服務，可能因為維護、供應商變動或者其他因素而暫時無法使用。輸入法本身喺離線狀態下依然運作。",
                "我哋可能會新增、修改或者移除功能。如果變更會實質削弱已付費功能，我哋會事先喺 app 內告知。",
            ],
        },
        {
            "kind": "prose",
            "id": "disclaimer",
            "heading": "免責聲明同責任限制",
            "body": [
                "KOI Keyboard 按「現狀」提供。喺法律允許嘅最大範圍內，我哋不作任何明示或默示嘅保證，包括適售性、特定用途適用性同不侵權嘅保證。",
                "喺法律允許嘅最大範圍內，我哋唔會就任何間接、附帶、特別或衍生性損害承擔責任。就任何情況下嘅總責任，以你喺申索前十二個月內就 KOI 支付嘅金額為限。",
                "部分司法管轄區唔容許排除某些保證或者責任，喺該等地區上述限制可能唔適用於你。",
            ],
        },
        {
            "kind": "prose",
            "id": "termination",
            "heading": "終止",
            "body": "你可以隨時刪除 app 停止使用。如果你嚴重或者重複違反呢份條款，我哋可以暫停或者終止你使用 AI 功能嘅權利。訂閱嘅取消同退款依然按 Apple 嘅程序處理。",
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "條款更新",
            "body": "呢份條款可能會更新，更新時會改埋頁頂嘅生效日期。涉及重大改變時，我哋會喺 app 內告知。更新生效後繼續使用，即表示接受新版本。",
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
    "lede": "你要求嘅頁面唔存在或者已經搬咗。",
    "canonical": "https://koi.rainsday.com/404.html",
    "sections": [
        {
            "kind": "cards",
            "heading": "不如試下呢幾版",
            "columns": 2,
            "items": [
                {"title": "首頁", "body": "[KOI Keyboard 產品介紹](route:)"},
                {"title": "私隱政策", "body": "[KOI 實際點處理你嘅資料](route:privacy/)"},
                {"title": "支援", "body": "[安裝步驟、常見問題同疑難排解](route:support/)"},
                {"title": "服務條款", "body": "[訂閱、Credits 同使用規範](route:terms/)"},
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
