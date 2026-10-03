"""English content for the KOI public site.

Every factual claim here is traceable to the KOI application source or the
Firebase backend source, and mirrors ``content_zh`` claim for claim. Three
things must never appear: a price, a purchasable "Lifetime" tier, and a support
response-time promise. See
``docs/superpowers/specs/2026-08-05-koi-public-site-production-content-design.md``
in the application repository for the evidence behind each claim.

Internal links carry the ``en/`` prefix because ``RenderContext.href`` resolves a
``route:`` target against the language the document belongs to.
"""

from __future__ import annotations

EFFECTIVE_DATE = "5 August 2026"
PRIVACY_EFFECTIVE_DATE = "3 October 2026"
APPLE_EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"

UI = {
    "nav_label": "Main navigation",
    "nav_home": "Home",
    "nav_privacy": "Privacy",
    "nav_support": "Support",
    "nav_terms": "Terms",
    "skip": "Skip to main content",
    "switch_label": "繁體中文",
    "switch_aria": "切換至繁體中文",
    "footer_rights": "© 2026 RaIN · KOI Keyboard",
    "footer_nav_label": "Footer navigation",
    "footer_source": "Site source",
    "contents_label": "On this page",
    "footer_notice": (
        "The Cangjie typing demo on this site runs on a dictionary derived from "
        "[rime-cangjie](https://github.com/rime/rime-cangjie) and "
        "[rime-essay](https://github.com/rime/rime-essay) (both LGPL-3.0) and "
        "[Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus) (MIT), "
        "and is distributed under LGPL-3.0. The Cangjie input method was invented "
        "by Chu Bong-Foo. Full notices: "
        "[third-party licences]"
        "(https://github.com/rain2day/koi-site/blob/main/THIRD-PARTY.md)."
    ),
}

CREDIT_COSTS = {
    "kind": "table",
    "id": "credits",
    "heading": "What each AI action costs",
    "intro": "Credits are spent only when you ask KOI Agent to do something. Everyday typing, candidates and handwriting recognition never cost Credits.",
    "columns": ("Action", "Credits"),
    "rows": (
        ("Reply suggestion", "1"),
        ("Rewrite and polish", "1"),
        ("Translate", "1"),
        ("Ask a question", "2"),
        ("Generate a sticker", "6"),
        ("Generate an image", "18"),
    ),
    "caption": "Image generation costs more to run, so it costs more Credits.",
}


DEMO = {
    "kind": "demo",
    "id": "try",
    "heading": "One stroke, one character",
    "intro": [
        "The Cangjie code for 香 is h, d, a — the radicals 竹, 木, 日. The usual way to enter it is three presses.",
        "**In KOI you drag from h to a in one stroke.** The drag has to cross g, f and s on the way, and KOI knows those are not the radicals you meant. A finger that wanders still lands.",
        "What follows is not a video. It is a working Cangjie input method running inside your browser. Tapping key by key works too, and on a laptop you can type on your own keyboard.",
    ],
    "tries_label": "Strokes worth trying",
    "tries": (
        {"code": "hqi", "result": "我"},
        {"code": "onf", "result": "你"},
        {"code": "hda", "result": "香"},
        {"code": "etcu", "result": "港"},
        {"code": "nfwg", "result": "鯉"},
    ),
    "fallback": [
        "This demo needs JavaScript. The demo is the only scripted thing on the site, and it never contacts a server.",
        "For reference: `hqi` gives 我, `onf` gives 你, `hda` gives 香, and `etcu` gives 港.",
    ],
    "note": [
        "**Same as the app**: glide decoding, down to the tolerance thresholds, neighbour substitution and turn detection; key layout, radicals, candidate order including the Cantonese weighting, space committing the first candidate, the five-code ceiling, and the number row that becomes the candidate row once you start composing.",
        "**Not in the demo**: two-finger chorded entry, learning, the other four input methods, and the `z` wildcard. When a stroke decodes to nothing the app runs a second, best-first rescue search; the demo does not, so a meaningless stroke is told it has no reading rather than given an invented one. The dictionary is also cut down to 3,030 common characters rather than the 27,584 the app bundles.",
    ],
}


FILM = {
    "kind": "film",
    "id": "watch",
    "heading": "Watch it once",
    "intro": [
        "The finger leaves h and drags to a. It has to pass g, f and s on the way — **the red keys are the ones you meant, the teal ones you merely crossed**. KOI can tell the difference.",
    ],
    "sources": (
        {"source": "film/glide.webm", "type": "video/webm"},
        {"source": "film/glide.mp4", "type": "video/mp4"},
    ),
    "poster": "film/glide-poster.jpg",
    "width": 1280,
    "height": 860,
    "alt": "One stroke gliding from h through g, f, d and s to a, candidates appearing, and 香 committed",
    "caption": "Five seconds, one stroke, one character. The keyboard below is yours to try.",
}


AGENT_FILM = {
    "kind": "film",
    "id": "agent-film",
    "heading": "Watch it draft one",
    "intro": [
        "A message arrives, you pick Reply, the draft appears, and inserting it sends it. Want a sticker instead — pick Sticker, and it comes back on a transparent background, ready to drop into the conversation. Credits come off at the real rates: one for a reply, six for a sticker.",
    ],
    "sources": (
        {"source": "film/agent-en.webm", "type": "video/webm"},
        {"source": "film/agent-en.mp4", "type": "video/mp4"},
    ),
    "poster": "film/agent-en-poster.jpg",
    "width": 1280,
    "height": 860,
    "alt": "KOI Agent drafting a reply, inserting it into the conversation, then generating a koi sticker on a transparent background, with Credits falling from 250 to 243",
    "caption": "What this shows is the flow and the cost. The wording of a real reply comes from the model and varies with the conversation; the sticker here was drawn for this film, not generated by it.",
}


LANDING = {
    "title": "KOI Keyboard — a Chinese keyboard built for Hong Kong",
    "description": "Cangjie, Quick, Stroke, Jyutping and Zhuyin in one keyboard. Handwriting recognition runs on the device, and the typing engine has no networking code at all. Requires iOS 16.0 or later.",
    "eyebrow": "KOI Keyboard",
    "heading": "A Chinese keyboard built for Hong Kong",
    "hero": "landing",
    "lede": [
        "Cangjie, Quick, Stroke, Jyutping, Zhuyin — five input methods sharing one keyboard.",
        "Handwriting runs on the device. The typing engine has no networking code at all.",
    ],
    "status": {
        "label": "Preparing for release",
        "detail": "KOI is being prepared for App Store review. A download link will replace this notice once it is live.",
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
            "moment": "Some people type Cangjie, some type Quick, some type Jyutping; anyone who grew up in Taiwan types Zhuyin. Moving between them usually means installing several keyboards and cycling through the system list.",
            "heading": "One keyboard, five input methods",
            "lead": "All five modes live inside KOI, and switching is instant. You never leave this keyboard.",
            "points": [
                {"title": "Cangjie", "body": "The native key layout, with every keycap showing its English letter and its Cangjie radical together. Candidates are ordered by frequency, and the ones you pick often move towards the front."},
                {"title": "Quick", "body": "First-and-last-code input, on the same key layout as Cangjie. There are no new key positions to learn."},
                {"title": "Stroke", "body": "Five-key stroke input with `*` as a wildcard — forget a stroke in the middle and a star still finds the character."},
                {"title": "Jyutping", "body": "Full and abbreviated spellings both work, and a tone number narrows the results. Outputs Hong Kong Traditional Chinese."},
                {"title": "Zhuyin (Dachen)", "body": "A dedicated Zhuyin key layout that outputs Taiwan Traditional Chinese."},
                {"title": "English", "body": "The same keystrokes are decoded into Chinese and English candidates at once, so typing English needs no keyboard switch."},
            ],
        },
        {
            "kind": "showcase",
            "id": "screens",
            "heading": "Actual screens",
            "intro": "Both of these are captures of KOI running. Neither is a mock-up.",
            "items": [
                {
                    "source": "shots/keyboard.png",
                    "alt": "The KOI keyboard, every keycap showing both its English letter and its Cangjie radical, with the number row in the candidate area",
                    "caption": "Every keycap carries both its English letter and its Cangjie radical. Before a composition starts, the candidate row shows numbers.",
                    "badge": "Actual capture",
                },
                {
                    "source": "shots/settings.png",
                    "alt": "The KOI settings screen showing input method, Full Access and sync status, with the five input mode selector below",
                    "caption": "Settings: input method, Full Access and sync status at a glance, with the input mode picker right below.",
                    "badge": "Actual capture",
                },
            ],
        },
        {
            "kind": "scene",
            "id": "feel",
            "index": "02",
            "moment": "A finger dragged across six inches of glass does not land the same way twice.",
            "heading": "It reads the stroke you meant",
            "lead": "Tap, glide, mix the two, chord with two fingers — all four can be mixed inside a single composition. Change your mind halfway through and you do not have to clear it and start again.",
            "points": [
                {"title": "Glides that drift", "body": "Decoding tolerates up to two keys being substituted by a neighbouring key. A finger that wanders slightly does not derail the input."},
                {"title": "Wrong codes still land", "body": "When you decompose a character wrongly, KOI fills in candidates from near-miss codes and places them after the normal ones. The candidate row never goes blank."},
                {"title": "Delete and cursor", "body": "One press deletes the last code, two presses clear the whole composition; swipe left or right on the space bar to move the cursor."},
            ],
        },
        {
            "kind": "ink",
            "id": "handwriting",
            "heading": "When there is no signal",
            "intro": [
                "You are underground, the signal comes and goes, and the character you want is one you cannot decompose. The handwriting model is bundled inside the app — no download, no connection, nothing that waits on a signal.",
                "KOI's handwriting area is rendered in Metal as a pool of water: your strokes leave ripples, refraction and waves. The panel below borrows the same ink: the colour under your finger here is the one the keyboard draws when you glide.",
            ],
            "canvas_label": "A water surface you can write on",
            "hint": "Write here with a finger or a mouse",
            "note": [
                "Recognition is not in the browser — that model runs on the device — so what you get here is ink and water, and no characters. The app has a Hong Kong Traditional Chinese handwriting model built in: nothing to download, nothing to connect to, and it writes just as well in aeroplane mode.",
            ],
        },
        {
            "kind": "scene",
            "id": "agent",
            "index": "03",
            "moment": "A message comes in. You read it three times and still have no idea what to write back.",
            "heading": "AI that turns up only when you ask",
            "lead": "Nothing to copy, nowhere to jump to. Six modes, all handled on the keyboard — leave it closed and it is simply not there.",
            "points": [
                {"title": "Auto", "body": "Reads what you have in front of you and decides what to do."},
                {"title": "Ask", "body": "Ask directly, and insert the answer straight into the field."},
                {"title": "Reply", "body": "Draft a reply to the message you received."},
                {"title": "Rewrite", "body": "Polish, change the tone, translate."},
                {"title": "Stickers and images", "body": "Generate a sticker with a transparent background, or a full scene image."},
            ],
            "aside": "Credits are spent only when you ask for something; everyday typing, candidates and handwriting recognition never cost any. What each action costs is on the [support page](route:support/).",
        },
        AGENT_FILM,
        {
            "kind": "scene",
            "id": "privacy",
            "index": "04",
            "tone": "accent",
            "moment": "A keyboard is the one place every word you write has to pass through. Why would you trust one?",
            "heading": "Ordinary input runs locally",
            "lead": [
                "KOI's input engine generates candidates, decomposes codes and learns on your device. **Ordinary typing is not sent keystroke by keystroke to KOI servers.**",
            ],
            "points": [
                {"title": "Local input", "body": "Candidate ranking and learning run on your device. Core input does not need AI."},
                {"title": "Data sharing", "body": "Optional sync, AI requests submitted after consent, and background JEV diagnostics for eligible internal test accounts have specific sharing disclosures."},
                {"title": "Service data", "body": "SDKs process diagnostic, performance and usage data. KOI uses no advertising identifier or cross-app advertising tracking."},
                {"title": "Your choices", "body": "Sync is off by default, AI sharing can be withdrawn, and local data and images have their own clearing controls."},
            ],
            "aside": "The [privacy policy](route:privacy/) sets each of these against the implementation, point by point.",
        },
        {
            "kind": "scene",
            "id": "plus",
            "index": "05",
            "tone": "quiet",
            "moment": "You move to a new phone, and a year of learned habits stays behind on the old one.",
            "heading": "Your habits come with you",
            "lead": "Cross-device sync is one of the two things KOI Plus adds. The free version already includes all five input methods, handwriting, learning and every core typing feature; Plus adds predictive input and sync, along with a monthly allowance of Credits.",
            "points": [
                {"title": "Predictive input", "body": "After a character is committed, KOI offers the next word or a whole phrase, so there are fewer characters to decompose one by one."},
                {"title": "Cross-device sync", "body": "Settings and learning history sync through your own private iCloud. Off by default, and once it is on you trigger it yourself."},
            ],
            "aside": "The full subscription and Credit terms are in the [terms of service](route:terms/); how Credits are counted is on the [support page](route:support/).",
        },
        {
            "kind": "scene",
            "id": "requirements",
            "index": "06",
            "tone": "quiet",
            "moment": "Installing the app does not put the keyboard on your screen — iOS does not let a third-party keyboard do that by itself.",
            "heading": "Getting started",
            "lead": "You add the keyboard in iOS Settings, once. KOI needs iOS 16.0 or later.",
            "points": [
                {"title": "Full Access", "body": "Needed for AI, clipboard paste, handwriting-model updates, and shared image-library archiving. Without it, all five input methods, candidates, learning and handwriting keep working."},
                {"title": "Character coverage", "body": "Candidates cover the Han characters in the Basic Multilingual Plane (BMP)."},
                {"title": "Interface language", "body": "The app interface is in Traditional Chinese (Hong Kong)."},
            ],
            "aside": "Setup steps, common questions and troubleshooting are on the [support page](route:support/).",
        },
    ],
}


PRIVACY = {
    "title": "Privacy Policy — KOI Keyboard",
    "description": "How KOI Keyboard handles local input, optional sync, AI sharing consent, service providers, retention and account deletion.",
    "eyebrow": "KOI · Privacy",
    "heading": "Privacy Policy",
    "lede": "This policy explains how KOI Keyboard handles local input, account and purchase data, and the sync and AI features you choose to use.",
    "updated": f"Effective date: {PRIVACY_EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "summary",
            "heading": "Overview",
            "bullets": [
                "Ordinary typing, candidate ranking and learning run on your device. Optional iCloud sync, submitted AI requests and background JEV diagnostics for eligible test accounts involve the transfers described below.",
                "AI use requires explicit agreement to “AI 資料分享” (AI data sharing). You can withdraw consent in the KOI app's “AI 與 Credits” page to stop new AI sharing.",
                "KOI uses account, installation and purchase identifiers for sign-in, Credits, access, purchase recovery and security. Hashed identifiers can still be associated with an account or installation.",
                "Bundled SDKs process performance, diagnostic and usage data to operate and improve their services.",
                "KOI does not sell your data or use your input content for advertising.",
            ],
        },
        {
            "kind": "prose",
            "id": "not-collected",
            "heading": "Advertising and device permissions",
            "body": [
                "KOI has no advertising or cross-app advertising tracking feature and does not use IDFA. Installation identifiers and SDK data needed for the service are handled separately from advertising tracking.",
                "KOI does not browse your contacts, location, calendars or existing photo library. Only when you press “儲存到相片” (Save to Photos) does it use add-only permission to add that generated image.",
                "The keyboard reads the clipboard when you press Paste to put text into the AI input field. Content subsequently submitted is handled under the AI sharing rules.",
            ],
        },
        {
            "kind": "prose",
            "id": "typing",
            "heading": "Local input and learning",
            "body": [
                "The input engine decomposes codes, generates and ranks candidates on your device, and stores selected candidates and associations to improve later input.",
                "Learning data and settings are stored in the container shared by the KOI app and keyboard. Ordinary input is not sent keystroke by keystroke to KOI's servers. Optional sync, AI requests and developer diagnostics are described separately below.",
                "Deleting a KOI account removes account access and related synced data. Ordinary local learning, settings and saved images have their own clearing controls and are not all erased by account deletion.",
            ],
        },
        {
            "kind": "prose",
            "id": "full-access",
            "heading": "The “Full Access” permission",
            "body": [
                "The keyboard's network features and sharing data with the KOI app require “Allow Full Access”. This includes KOI Agent, JEV requests for eligible test accounts, handwriting model downloads and the shared generated-image library.",
                "Full Access does not replace AI sharing consent. You must explicitly agree before submitting new AI requests. Basic local input remains available without Full Access.",
            ],
        },
        {
            "kind": "prose",
            "id": "consent",
            "heading": "AI sharing consent and withdrawal",
            "body": [
                "The KOI app's “AI 與 Credits” page and the keyboard's first AI action show “AI 資料分享”, describing data, recipients, purposes and retention, with “同意並繼續” (Agree and Continue) and “取消” (Cancel). Displaying the notice does not grant consent.",
                "Consent is recorded by version in KOI's shared settings. Without consent to the current version, updated clients block new AI sharing. Keyboard actions also require Full Access and respect context limits.",
                "In “AI 與 Credits”, press “已同意 AI 資料分享 · 撤回” and confirm “撤回同意” to stop new AI sharing, including JEV. Already transmitted data cannot be recalled. Withdrawal does not automatically delete stored results or existing provider records. Retrieval and delivery acknowledgement of completed results remain available.",
            ],
        },
        {
            "kind": "prose",
            "id": "ai",
            "heading": "Data sent by KOI Agent",
            "body": [
                "When you agree and explicitly execute an Agent action, the following content passes through KOI's Firebase/Google Cloud service and OpenRouter to OpenAI models. Image understanding may also use OpenAI models provided by Microsoft Azure.",
            ],
            "bullets": [
                "Your submitted prompt or instruction and applicable earlier turns in the same conversation.",
                "Previewed input context: selected text, text before the cursor or selection, then text after it; the combined limit is 2,000 Unicode scalar values and 4,000 UTF-8 bytes.",
                "Reference images and applicable image conversation data needed for image features.",
            ],
            "after": [
                "This content supports understanding requests, answering questions, rewriting, replies, translation and image generation. Viewing the context preview does not itself submit that text.",
                "KOI services separately receive installation and account-binding identifiers, Firebase App Check verification data, and metadata needed to reconcile operations, delivery and Credits. KOI's account, security and accounting services use these verification data; they are not sent as model prompts or context.",
                "Text questions needing current information may use OpenRouter's web search and fetch services. Image research sends derived search terms to Brave Search and fetches references from source websites; those services and websites receive the corresponding queries or requests.",
                "KOI does not itself train models on Agent content. Text requests ask providers for zero retention and no content collection. This is not a zero-retention guarantee for all images, search, JEV, service logs or provider processing. Provider links and retention differences appear below.",
            ],
        },
        {
            "kind": "table",
            "id": "third-parties",
            "heading": "Service providers",
            "intro": "These services process data needed for their features. Providers and their service providers may process data outside your jurisdiction. KOI does not treat all encrypted or hashed data as anonymous.",
            "columns": ("Service and policy", "Purpose", "Data involved"),
            "rows": (
                ("[Firebase/Google Cloud](https://firebase.google.com/support/privacy)", "Sign-in, App Check, AI relay, accounting, temporary storage and security", "Name, account/installation identifiers, purchases, AI requests and encrypted results, service metadata"),
                ("[Google ML Kit](https://developers.google.com/ml-kit/ios-data-disclosure)", "On-device handwriting recognition, model downloads and SDK diagnostics", "Device/app information, installation identifiers, feature events, performance, errors and configured languages"),
                ("[RevenueCat](https://www.revenuecat.com/privacy)", "Purchase, subscription and restoration status", "App-user identifiers, purchases and device/service information"),
                ("[OpenRouter](https://openrouter.ai/privacy)", "AI routing, text search and web fetching", "Prompts, context, conversations and reference images"),
                ("[OpenAI API data policy](https://developers.openai.com/api/docs/guides/your-data)", "Text and image models", "AI instructions, context, conversations and applicable images"),
                ("[Microsoft Azure model data policy](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy)", "Image understanding", "Images and related text"),
                ("[Cloudflare](https://www.cloudflare.com/privacypolicy/)", "JEV authentication, rate limits and relay", "Account/installation verification, network security metadata and bounded input excerpts"),
                ("[TypeSafe JEV](https://typesafe.ai/legal/privacy-policy)", "Background correction evaluation for eligible test accounts", "Bounded input sentences and locally generated replacement candidates"),
                ("[Brave Search API](https://api-dashboard.search.brave.com/privacy-policy)", "Image-reference research", "Search terms derived from a request"),
                ("Reference-source websites", "Web content and reference images", "Server requests to fetch their content, handled under each site's policies"),
                ("[Apple](https://www.apple.com/legal/privacy/)", "App Store, Apple sign-in, device verification and private CloudKit", "Purchases, sign-in/verification and data you choose to sync"),
            ),
            "caption": "Provider policies and applicable service agreements describe their handling. A setting for a text request does not mean every service retains no data.",
        },
        {
            "kind": "prose",
            "id": "icloud",
            "heading": "Optional iCloud sync",
            "body": [
                "Cross-device sync is off by default. When you enable it and run a manual sync, KOI writes selected keyboard settings, learned candidates and associations to your private Apple CloudKit database.",
                "The sync payload uses CloudKit encrypted fields. Sync does not upload every keystroke or sync AI sharing consent or the local diagnostics flag.",
                "Account deletion handles synced data bound to that KOI account. If iCloud identity or network availability prevents completion, the app retains the cleanup state and offers a retry. Apple's platform retention and backups are governed by its policies.",
            ],
        },
        {
            "kind": "prose",
            "id": "identifiers",
            "heading": "Accounts and identifiers",
            "body": [
                "KOI creates an installation UUID and uses Firebase account or guest identifiers for purchases, Credits, binding, recovery and abuse prevention. The server also uses hashes of installation, account or network data for reconciliation and rate limits. Hashes that remain associated with an account or installation are still identifiers.",
                "For Sign in with Apple, KOI requests the name scope and passes the supplied name to Firebase Authentication to create or update the account. This flow does not request the email scope. Apple and Firebase still handle sign-in data under their policies and applicable settings.",
                "KOI services use account, installation-binding and entitlement data to admit requests. Firebase/Google SDKs also process their diagnostics. Google ML Kit's official disclosure lists device/app information, installation identifiers, performance, feature events, errors and configured languages for diagnostics and usage analytics.",
            ],
        },
        {
            "kind": "prose",
            "id": "diagnostics",
            "heading": "Developer diagnostics and JEV testing",
            "body": [
                "Local input diagnostics are enabled automatically only for accounts granted Lifetime Plus with a verified TestFlight/Sandbox or Xcode environment. There is no manual diagnostics enable switch. The App Store production environment is excluded, and ordinary accounts do not acquire local input diagnostics through this gate.",
                "These local records can include input codes, committed characters, deletion and correction-evaluation events for development testing. They are not synced through iCloud, and there is no automatic upload of the entire trail. Eligible accounts have a clear control; local maintenance applies a 30-day retention rule.",
                "Background JEV evaluation additionally requires current AI sharing consent, Full Access and valid Lifetime eligibility. Bounded sentences and replacement candidates pass through KOI's Cloudflare service to TypeSafe JEV. Withdrawing AI consent blocks new requests. JEV evaluates in the background in this version and does not automatically edit text.",
                "Cloudflare's membership authorization cache lasts at most 60 seconds and contains no input text. This does not mean all Cloudflare or TypeSafe records are deleted after 60 seconds. TypeSafe's published policy states it does not train or fine-tune models on Input; its general retention terms give no fixed deletion period.",
            ],
        },
        {
            "kind": "prose",
            "id": "purchases",
            "heading": "Purchases and transaction records",
            "body": [
                "Apple processes payments. KOI uses product, transaction, purchase/subscription status and app-user identifiers from Apple and RevenueCat to calculate Credits, provide Plus, restore purchases, handle refunds and prevent duplicate accounting.",
                "KOI retains Credits ledgers and purchase reconciliation data linked to accounts or guest wallets. After account deletion, transaction data needed for Apple refunds and accounting moves into a private audit record using replacement identifiers for the deleted account. This does not restore the original account or forfeited Credits.",
                "Deleting a KOI account does not cancel an Apple subscription. Use “管理 Apple 訂閱” (Manage Apple Subscriptions) on the deletion confirmation screen or Apple's subscription page in iOS Settings to cancel it.",
            ],
        },
        {
            "kind": "prose",
            "id": "reports",
            "heading": "Service records and result reports",
            "body": [
                "KOI processes request identifiers, timing, stages, models, status/error classifications, App Check and rate-limit data to operate and protect the service. These application summaries do not automatically attach raw prompts or generated content. Cloud platforms also process request and network logs under their configuration.",
                "After separate report confirmation, KOI receives the result type, a SHA-256 digest identifying the generated result and an unsafe-content reason. It stores these with an installation HMAC, App Check app identifier and timestamps. This report does not send your account UID, full prompt, generated text/image or conversation history.",
                "Report metadata becomes eligible for asynchronous deletion 30 days after creation. This is not a guarantee of physical deletion immediately on day 30. Account deletion does not extend or reset that date. If you contact support directly, you also provide your correspondence address, message and attachments.",
            ],
        },
        {
            "kind": "prose",
            "id": "retention",
            "heading": "Retention and deletion timing",
            "bullets": [
                "AI result recovery: generated text and images may be stored encrypted in Google Cloud Storage, linked to an account and operation, for recovery and delivery reconciliation. Accepted results have an app retrieval deadline of up to 24 hours; undelivered results have a separate recovery deadline. The bucket also has a lifecycle deletion rule one day after object creation, and expired data is cleaned in batches on subsequent account requests. Storage cleanup may precede the app deadline. Lifecycle deletion is asynchronous: neither a full 24 hours of availability nor physical deletion of all AI data within 24 hours is guaranteed.",
                "Conversations and images: the current conversation is held temporarily in the keyboard session and can be cleared. Saved images remain in the local KOI library until you delete them. Copies saved to Apple Photos must be managed in the Photos app.",
                "Image-reference cache: the server-memory cache has a 10-minute expiry, capped at 24 entries and 32 MiB. Expired entries are removed during cache access and maintenance.",
                "Provider processing: text requests ask for zero retention and no content collection. Images, search, JEV, security, accounting and SDK data have separate policies and agreements. Brave's published Search API notice describes query logs retained up to 90 days for billing and troubleshooting, subject to legal obligations.",
                "Accounts and purchases: account deletion removes account data, active bindings and AI results. Transaction, deletion and security records needed for refunds, financial reconciliation and abuse prevention may remain without a single deletion deadline. Cloud-platform data and backups follow their configured handling. Contact us about retention and deletion of specific records.",
            ],
        },
        {
            "kind": "prose",
            "id": "children",
            "heading": "Children",
            "body": "KOI is not designed specifically for children under 13 and does not knowingly collect their personal data. Contact us if you believe a child has provided us personal data so we can address it.",
        },
        {
            "kind": "prose",
            "id": "rights",
            "heading": "Your choices and account deletion",
            "bullets": [
                "**Withdraw AI sharing**: in the KOI app's “AI 與 Credits” page, press “已同意 AI 資料分享 · 撤回” and confirm. New AI sharing stops and ordinary local input remains available.",
                "**Stop sync**: sync is off by default; you can stop manual syncing and turn the switch off.",
                "**Delete an account or guest data**: in the account section of “AI 與 Credits”, press “刪除帳戶” (Delete Account) or “刪除訪客資料” (Delete Guest Data), read the disclosure and type “刪除” to confirm. Apple accounts require reauthentication; guest deletion does not require Apple sign-in. Incomplete cleanup displays a retry or processing state.",
                "**Deletion effects**: associated account/guest Credits and that account's Lifetime Plus are forfeited. Account access, active bindings, AI consent, developer diagnostics and related synced data are cleaned up. Ordinary local learning, settings and the image library use their own clear/delete controls. Transaction audits and the retention exceptions above still apply.",
                "**Local and photo data**: use KOI's learning, diagnostics or image-library clearing controls. Delete Photos copies separately. Uninstalling removes the app's current local storage; iCloud, device backups and provider copies follow their own settings and policies.",
                "**Access, correction or deletion enquiries**: contact [privacy@rainsday.com](mailto:privacy@rainsday.com). We may request appropriate account or transaction evidence to verify ownership. Do not send passwords or full verification tokens.",
            ],
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "Policy updates",
            "body": "We update this page and its effective date when data handling changes. Changes to AI recipients, shared data or purposes will update the sharing notice and consent version and require renewed agreement.",
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "Contact",
            "bullets": [
                "Privacy enquiries: [privacy@rainsday.com](mailto:privacy@rainsday.com)",
                "General support: [support@rainsday.com](mailto:support@rainsday.com) or the [support page](route:support/).",
            ],
        },
    ],
}


SUPPORT = {
    "title": "Support — KOI Keyboard",
    "description": "Setup steps, common questions and troubleshooting for KOI Keyboard, covering Full Access, switching input methods, handwriting, sync and Credits.",
    "eyebrow": "KOI · Support",
    "heading": "Support",
    "lede": "Setup, common questions and troubleshooting. If the answer is not here, email us directly.",
    "toc": True,
    "sections": [
        {
            "kind": "steps",
            "id": "install",
            "heading": "Getting started",
            "intro": "Installing the app is not enough — iOS requires you to add the keyboard in Settings as well.",
            "items": [
                {
                    "title": "Add the keyboard",
                    "body": "iOS Settings → General → Keyboard → Keyboards → Add New Keyboard… → choose KOI under “Third-Party Keyboards”.",
                },
                {
                    "title": "(Optional) Turn on Full Access",
                    "body": "On the same screen, select KOI and turn on “Allow Full Access”. It is needed for AI, clipboard paste, handwriting-model updates, and shared image-library archiving; without it the input method itself is completely normal.",
                },
                {
                    "title": "Switch to KOI",
                    "body": "In any text field, press and hold the globe key and pick KOI from the list. From there you can switch between the five input modes inside KOI itself.",
                },
            ],
        },
        {
            "kind": "faq",
            "id": "faq",
            "heading": "Common questions",
            "items": [
                {
                    "question": "Why does KOI need “Full Access”? Can I leave it off?",
                    "answer": [
                        "iOS gives a third-party keyboard no networking capability at all without this permission. KOI needs it to connect to the AI features, to read the clipboard (only at the moment you press Paste), to update the handwriting model, and to archive generated images in the app's shared image library.",
                        "Leaving it off is completely fine. The five input methods, candidates, learning, handwriting, symbols and cursor controls all still work. What you lose is AI access, paste, handwriting-model updates, and shared image-library archiving.",
                    ],
                },
                {
                    "question": "Does what I type get sent anywhere?",
                    "answer": [
                        "Ordinary input, candidate ranking and learning run on your device and are not sent keystroke by keystroke to KOI servers.",
                        "When you explicitly agree to AI sharing and execute a KOI Agent action, it sends your instruction, applicable conversation and the previewed selection/before/after context, capped at 2,000 Unicode scalar values and 4,000 UTF-8 bytes. You can withdraw AI sharing consent in “AI 與 Credits”.",
                        "Optional sync sends settings and learning data to your private CloudKit. Eligible TestFlight/Xcode test accounts granted Lifetime Plus may also run background JEV evaluation after consent and Full Access; App Store production builds are excluded. See the [privacy policy](route:privacy/) for recipients and retention.",
                    ],
                },
                {
                    "question": "How do I switch between the five input methods?",
                    "answer": "Choose the Chinese input mode in the KOI app's settings. Cangjie, Quick, Stroke, Jyutping and Zhuyin each have their own keyboard layout.",
                },
                {
                    "question": "Does handwriting need a connection?",
                    "answer": "No. The Hong Kong Traditional Chinese handwriting model is built into the app, so it writes just as well in aeroplane mode. A connection is used only to update the model, and it works without updating.",
                },
                {
                    "question": "What if I enter the wrong code or decompose a character wrongly?",
                    "answer": "KOI fills in candidates from near-miss codes and places them after the normal ones, so the candidate row never goes blank. To clear the whole composition, press delete twice in a row.",
                },
                {
                    "question": "Why can I not type certain characters?",
                    "answer": [
                        "Candidates cover the Han characters in the Basic Multilingual Plane (BMP). A small number of extremely rare extension characters (Unicode Ext B and beyond) are not included yet.",
                        "If a character is in common use and you cannot find it, email us with the code you typed and the character you wanted.",
                    ],
                },
                {
                    "question": "I have a new iPhone. How do I move my settings and learning history?",
                    "answer": [
                        "Turn on cross-device sync (a Plus feature). Sync uses your own private iCloud and does not pass through KOI's servers.",
                        "Sync is triggered manually: press sync in settings. It never runs in the background. Both devices have to be signed in to the same iCloud account.",
                    ],
                },
                {
                    "question": "What are Credits, and when are they spent?",
                    "answer": [
                        "Credits are used only for KOI Agent's AI actions. Everyday typing, candidates and handwriting recognition never cost Credits.",
                        "Reply, rewrite and translate cost 1 each, asking a question costs 2, generating a sticker costs 6, and generating an image costs 18.",
                        "A subscription grants 250 Credits each month, and each grant is valid for 60 days from the day it is issued; Credit packs bought separately do not expire.",
                    ],
                },
                {
                    "question": "How do I cancel a subscription, and how do refunds work?",
                    "answer": [
                        "To cancel: iOS Settings → your Apple Account → Subscriptions → KOI → Cancel Subscription. You keep access until the end of the current period.",
                        "Refunds are handled by Apple, not by KOI. Request one at [reportaproblem.apple.com](https://reportaproblem.apple.com).",
                    ],
                },
                {
                    "question": "Does KOI collect data about how I use it?",
                    "answer": "KOI services and bundled SDKs process operational, performance, diagnostic and usage data to provide and protect features. KOI uses no advertising identifier or cross-app advertising tracking. See the [privacy policy](route:privacy/) for details and your choices.",
                },
            ],
        },
        {
            "kind": "cards",
            "id": "troubleshooting",
            "heading": "Troubleshooting",
            "columns": 2,
            "items": [
                {
                    "title": "KOI is missing when I hold the globe key",
                    "body": "Usually the keyboard has not been added in iOS Settings — go back to the first step of Getting started. If it has been added and is still missing, restarting the device usually sorts it out.",
                },
                {
                    "title": "The AI says the connection failed",
                    "body": "Check in this order: Full Access is on, the network is reachable, and you have enough Credits. “Test connection” in the KOI app's settings will confirm it.",
                },
                {
                    "title": "Sync does nothing",
                    "body": "Check that the device is signed in to iCloud, that KOI's sync switch is on, and that you have pressed sync yourself — sync never runs in the background.",
                },
                {
                    "title": "Candidate order is not what I want",
                    "body": "KOI learns from what you pick, and after a few days of use it usually comes round. To start over, clear the learning history in settings.",
                },
            ],
        },
        CREDIT_COSTS,
        {
            "kind": "definitions",
            "id": "credit-model",
            "heading": "How Credits work",
            "items": [
                {
                    "term": "Included with a subscription",
                    "detail": "Monthly and annual plans both grant 250 Credits each month. An annual plan releases them in twelve grants across the year rather than all at once. Each grant is valid for 60 days from the day it is issued.",
                },
                {
                    "term": "Bought separately",
                    "detail": "Credit packs come in 100, 300 and 800. They are one-off purchases and **do not expire**. They do not include predictive input or cross-device sync.",
                },
                {
                    "term": "When Credits are spent",
                    "detail": "Only when you ask KOI Agent to do something. Everyday typing does not involve Credits.",
                },
            ],
        },
        {
            "kind": "definitions",
            "id": "requirements",
            "heading": "Requirements",
            "items": [
                {"term": "iOS version", "detail": "iOS 16.0 or later."},
                {
                    "term": "Full Access",
                    "detail": "AI, clipboard paste, handwriting-model updates, and shared image-library archiving need “Allow Full Access”. Without it, all five input methods, candidates, learning and handwriting keep working exactly as before.",
                },
                {
                    "term": "Character coverage",
                    "detail": "Candidates cover the Han characters in the Basic Multilingual Plane (BMP). Some extremely rare extension characters (Ext B and beyond) cannot be typed yet.",
                },
                {"term": "Interface language", "detail": "The app interface is in Traditional Chinese (Hong Kong)."},
            ],
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "Contact us",
            "body": "When reporting a problem, please include your iOS version, your KOI version, the input mode you were using, and the steps to reproduce it.",
            "bullets": [
                "General support: [support@rainsday.com](mailto:support@rainsday.com)",
                "Privacy enquiries: [privacy@rainsday.com](mailto:privacy@rainsday.com)",
            ],
        },
    ],
}


TERMS = {
    "title": "Terms of Service — KOI Keyboard",
    "description": "KOI Keyboard's terms of service: scope of the licence, subscription and Credit terms, acceptable use of the AI features, disclaimers and governing law.",
    "eyebrow": "KOI · Terms",
    "heading": "Terms of Service",
    "lede": "These terms set out the rules for using KOI Keyboard. Subscriptions themselves are governed by Apple's standard terms; this page covers the parts specific to KOI.",
    "updated": f"Effective date: {EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "scope",
            "heading": "Scope of these terms",
            "body": [
                "By downloading or using KOI Keyboard, you agree to these terms. If you do not agree, please do not use the app.",
                f"Subscriptions purchased through the App Store are also governed by the [Apple Standard End User Licence Agreement]({APPLE_EULA}). Where the two conflict, Apple's terms prevail on matters of purchase and subscription.",
            ],
        },
        {
            "kind": "prose",
            "id": "licence",
            "heading": "Licence",
            "body": "We grant you a personal, non-exclusive, non-transferable, revocable licence to use KOI Keyboard on Apple devices you own or control. You may not reverse engineer, decompile, rent or resell the app, or remove proprietary notices from it.",
        },
        {
            "kind": "prose",
            "id": "subscriptions",
            "heading": "Subscriptions",
            "bullets": [
                "KOI Plus is offered as an auto-renewing subscription, with monthly and annual plans.",
                "Payment is charged to your Apple Account. The subscription renews automatically unless auto-renewal is turned off at least 24 hours before the end of the current period.",
                "The renewal charge is taken within the 24 hours before the current period ends.",
                "Manage your subscription and turn off auto-renewal in iOS Settings → your Apple Account → Subscriptions.",
                "Refunds are handled by Apple, not by KOI. Request one at [reportaproblem.apple.com](https://reportaproblem.apple.com).",
            ],
        },
        {
            "kind": "prose",
            "id": "credits",
            "heading": "KOI Credits",
            "bullets": [
                "Credits are the internal unit of measure for using KOI Agent features.",
                "Credits are **not currency**. They have no cash value and cannot be redeemed, transferred or used outside KOI.",
                "Subscription Credits are granted at 250 per month and are **valid for 60 days from the day they are issued**; unused Credits lapse at the end of that window. Annual plans grant them in twelve instalments across the year.",
                "Credit packs bought separately (100, 300, 800) **do not expire**, but they do not include predictive input or cross-device sync.",
                "When a subscription ends, unused subscription Credits lapse; purchased Credit packs are retained.",
                "Credits spent on a completed action are non-refundable. If an action fails because of a fault in our systems, those Credits are returned to your balance.",
            ],
        },
        {
            "kind": "prose",
            "id": "ai-use",
            "heading": "Acceptable use of the AI features",
            "body": [
                "KOI Agent is powered by third-party AI models. In using it, you agree not to use it to:",
            ],
            "bullets": [
                "produce unlawful content, harassment or hate speech",
                "generate sexualised depictions of other people, or inappropriate content involving minors",
                "impersonate other people or create misleading false information",
                "infringe other people's intellectual property or privacy",
                "send requests in bulk by automated means, or attempt to circumvent usage limits",
            ],
            "after": [
                "AI output can be wrong or misleading. Verify it yourself where it matters. We make no warranty as to the accuracy of AI output.",
                "We reserve the right to suspend or terminate access to the service where we find abuse.",
            ],
        },
        {
            "kind": "prose",
            "id": "your-content",
            "heading": "Your content",
            "body": [
                "What you type, your learning history, and the content you produce with the AI features all belong to you. We take no ownership of any of it.",
                "To carry out the action you asked for, we need to send the content you submit to AI providers for processing. We do not use your content for anything else. See the [privacy policy](route:privacy/) for details.",
            ],
        },
        {
            "kind": "prose",
            "id": "availability",
            "heading": "Availability and changes",
            "body": [
                "The AI features depend on third-party services and may be temporarily unavailable because of maintenance, provider changes or other factors. The input method itself keeps working offline.",
                "We may add, change or remove features. If a change would materially reduce a paid feature, we will tell you in the app beforehand.",
            ],
        },
        {
            "kind": "prose",
            "id": "disclaimer",
            "heading": "Disclaimers and limitation of liability",
            "body": [
                "KOI Keyboard is provided “as is”. To the fullest extent permitted by law, we make no warranties of any kind, express or implied, including warranties of merchantability, fitness for a particular purpose and non-infringement.",
                "To the fullest extent permitted by law, we are not liable for any indirect, incidental, special or consequential damages. Our total liability in any circumstances is limited to the amount you paid for KOI in the twelve months before the claim.",
                "Some jurisdictions do not allow the exclusion of certain warranties or liabilities, and in those places the limits above may not apply to you.",
            ],
        },
        {
            "kind": "prose",
            "id": "termination",
            "heading": "Termination",
            "body": "You can stop using the app at any time by deleting it. If you breach these terms seriously or repeatedly, we may suspend or terminate your right to use the AI features. Subscription cancellation and refunds continue to follow Apple's process.",
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "Changes to these terms",
            "body": "These terms may be updated, and the effective date at the top will change when they are. For significant changes we will tell you in the app. Continuing to use KOI after an update takes effect means you accept the new version.",
        },
        {
            "kind": "prose",
            "id": "law",
            "heading": "Governing law",
            "body": "These terms are governed by and construed in accordance with the laws of the Hong Kong Special Administrative Region. Disputes arising from them are submitted to the Hong Kong courts.",
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "Contact",
            "bullets": [
                "General enquiries: [support@rainsday.com](mailto:support@rainsday.com)",
                "Privacy enquiries: [privacy@rainsday.com](mailto:privacy@rainsday.com)",
            ],
        },
    ],
}


NOT_FOUND = {
    "title": "Page not found — KOI Keyboard",
    "description": "The KOI Keyboard page you requested does not exist or has moved.",
    "eyebrow": "KOI · 404",
    "heading": "Page not found",
    "lede": "The page you requested does not exist or has moved.",
    "canonical": "https://koi.rainsday.com/404.html",
    "sections": [
        {
            "kind": "cards",
            "heading": "Try one of these",
            "columns": 2,
            "items": [
                {"title": "Home", "body": "[What KOI Keyboard does](route:)"},
                {"title": "Privacy", "body": "[How KOI actually handles your data](route:privacy/)"},
                {"title": "Support", "body": "[Setup, common questions and troubleshooting](route:support/)"},
                {"title": "Terms", "body": "[Subscriptions, Credits and acceptable use](route:terms/)"},
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
