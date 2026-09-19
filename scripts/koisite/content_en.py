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
PRIVACY_EFFECTIVE_DATE = "20 September 2026"
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
            "heading": "So the typing engine never goes online",
            "lead": [
                "KOI's input engine — candidate generation, code decomposition, learning history — contains no networking code at all. **What you type does not leave your device.**",
            ],
            "points": [
                {"title": "No analytics", "body": "No analytics tools, no crash-reporting SDK, no advertising identifier."},
                {"title": "No keystroke logging", "body": "KOI does not record the keys you press."},
                {"title": "One exception", "body": "You open KOI Agent yourself and send a request. There is no other exception."},
                {"title": "Where data sits", "body": "Learning history and settings stay on the device, or in a private iCloud that you control."},
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
    "description": "KOI Keyboard's privacy policy: typing stays on the device, no analytics, no advertising identifiers, and exactly what the AI features send.",
    "eyebrow": "KOI · Privacy",
    "heading": "Privacy Policy",
    "lede": "This policy describes what KOI Keyboard actually does with data. Every point matches the implementation in the app and the backend; none of it is filled-in boilerplate.",
    "updated": f"Effective date: {PRIVACY_EFFECTIVE_DATE}",
    "toc": True,
    "sections": [
        {
            "kind": "prose",
            "id": "summary",
            "heading": "The one-minute version",
            "bullets": [
                "What you type **does not** leave your device, unless you open KOI Agent yourself and send a request.",
                "KOI contains **no** analytics, crash-reporting or advertising tracking tools of any kind.",
                "KOI **does not** read your advertising identifier or any device identifier.",
                "Learning history and settings are stored on the device; if you turn sync on, they are stored in **your own** private iCloud.",
                "We do not sell your data and we do not use it for advertising.",
            ],
            "after": "Each point is set out in full below.",
        },
        {
            "kind": "prose",
            "id": "not-collected",
            "heading": "What we do not collect",
            "body": "This section matters more than “what we collect”, so it comes first. None of the following can be found anywhere in KOI's code:",
            "bullets": [
                "Analytics or usage-statistics SDKs (Firebase Analytics, Mixpanel, Amplitude and the like)",
                "Crash-reporting SDKs (Crashlytics, Sentry and the like)",
                "Advertising or attribution SDKs (AppsFlyer, Adjust, the Facebook SDK and the like)",
                "The advertising identifier (IDFA), the vendor identifier (IDFV) or App Tracking Transparency (ATT) prompts",
                "Keystroke logging — KOI does not record the keys you press",
                "Browsing or reading contacts, the photo library, location or calendars — KOI cannot browse or read your photo library",
            ],
        },
        {
            "kind": "prose",
            "id": "typing",
            "heading": "What you type",
            "body": [
                "KOI's input engine runs entirely on your device. Decomposition, candidate generation, ranking, learning — all of it is computed locally, and that part of the code has no networking capability whatsoever.",
                "The characters you choose teach KOI your habits, so the same code ranks them higher next time. This learning history is stored in the app's shared container `group.com.rainsday.koikeyboard`, which only KOI can read.",
                "Deleting KOI removes this local data along with it.",
            ],
        },
        {
            "kind": "prose",
            "id": "full-access",
            "heading": "The “Full Access” permission",
            "body": [
                "iOS rules: a keyboard extension without “Allow Full Access” has no networking capability and cannot use KOI's shared container. KOI uses the permission for these explicit features:",
            ],
            "bullets": [
                "Connecting to KOI Agent (the AI features)",
                "Pasting text from the clipboard into the AI input field — the clipboard is read only at the moment you press Paste",
                "Updating the handwriting recognition model (the base model is built in and works without updates)",
                "Saving generated images into KOI's shared local image library so the host app can show them later",
            ],
            "after": [
                "Without the permission, KOI's five input methods, candidates, learning, handwriting, symbols and cursor controls all keep working. The features above are the only things you lose.",
                "Granting the permission **does not** itself send any data. Data is sent only when you use the relevant feature.",
            ],
        },
        {
            "kind": "prose",
            "id": "ai",
            "heading": "What KOI Agent actually sends",
            "body": [
                "When you open KOI Agent and send a request, the following goes to KOI's servers (Google Cloud Functions, in `asia-east1`):",
            ],
            "bullets": [
                "The instruction text you entered",
                "Context from the active field. KOI allocates the limit in this order: selected text, text before the selection or cursor, then text after it.",
                "The combined context is limited to 2,000 Unicode scalar values and 4,000 UTF-8 bytes. The preview shown in KOI Agent is exactly the context sent with that action.",
                "The earlier turns of the same conversation",
                "An installation identifier (see “Accounts and identifiers” below) and a Firebase App Check attestation token",
            ],
            "after": [
                "KOI sends context only after you explicitly press an Agent action — for example Send, a quick action, Retry, Continue, or Freedom Create. Opening Agent or viewing the preview does not send it.",
                "**Not** sent: screenshots (KOI cannot take them), your clipboard contents (unless you press Paste yourself), your contacts, or content outside the text field currently being edited.",
                "KOI cannot browse or read your photo library. The KOI app can only use add-only permission after you tap Save to Photos; it cannot inspect existing photos.",
                "Server logs keep request-level data only: request id, path, status code, duration, which model handled it, and processing stage. **The instruction text and the surrounding text are never written to logs.**",
            ],
        },
        {
            "kind": "table",
            "id": "third-parties",
            "heading": "Third-party services",
            "intro": "These are the third parties KOI actually touches. Note the difference between “on the device” and “over the network”.",
            "columns": ("Service", "Purpose", "Where data goes"),
            "rows": (
                ("Google ML Kit Digital Ink", "Handwriting recognition", "Runs **on the device**; the model is built into the app and no ink is sent out"),
                ("Firebase App Check (via Apple DeviceCheck)", "Preventing abuse of the servers", "A device attestation token"),
                ("Firebase Authentication", "Optional Sign in with Apple", "See “Accounts and identifiers”"),
                ("Firebase Cloud Functions / Firestore", "AI request handling, Credit accounting", "See “KOI Agent” and “Purchases”"),
                ("Cloudflare Workers", "Authentication and relay for Life Time Plus AI Chinese correction requests", "The original sentence, local candidates and membership credentials; text is not written to KOI Worker logs or cache"),
                ("TypeSafe Jev", "Semantic candidate selection for Life Time Plus AI Chinese correction", "The original sentence and candidates generated locally from the input code"),
                ("RevenueCat", "Subscription and purchase state", "See “Purchases”"),
                ("OpenRouter", "Routing AI requests to model providers", "Your instruction and the surrounding text"),
                ("Anthropic", "Text models (Claude)", "Your instruction and the surrounding text"),
                ("OpenAI", "Image generation models", "Your image instruction"),
                ("Brave Search", "Reference lookups during image generation", "Search terms produced by the server"),
                ("Apple", "App Store, Sign in with Apple, DeviceCheck, iCloud", "Governed by Apple's privacy policy"),
            ),
            "caption": "How these providers retain and process data on their own systems is governed by their respective privacy policies.",
        },
        {
            "kind": "prose",
            "id": "icloud",
            "heading": "iCloud sync",
            "body": [
                "Cross-device sync is **off by default**. Before it is turned on, KOI asks you to confirm the iCloud account you are currently signed in to.",
                "Synced data is written to your own **private** iCloud database (container `iCloud.com.rainsday.koikeyboard`) using CloudKit encrypted fields — the key is tied to your iCloud Keychain, so neither Apple nor the KOI developer can read the contents.",
                "Sync is **triggered manually** and never runs in the background. Two settings never sync at all: the sync switch itself, and the input diagnostics switch.",
            ],
        },
        {
            "kind": "prose",
            "id": "identifiers",
            "heading": "Accounts and identifiers",
            "body": [
                "**Installation identifier**: KOI generates a random UUID to identify an installation. It is not a device identifier, it does not track you across apps, and reinstalling the app replaces it. On arrival the server hashes it with SHA-256 and a secret pepper, and only the hash is used, for rate limiting and for tying purchases to an installation.",
                "**Sign in with Apple**: optional, and needed only if you want purchase records to carry across devices. The only scope KOI requests from Apple is **your name**; it does not request an email address. Apple supplies the name only on first authorization; KOI passes it to Firebase Authentication to create or update the sign-in account. KOI's own Firestore account and purchase records store the Firebase UID, scoped hashes, purchase data and timestamps, and do not separately store your name or email.",
                "**AI Chinese correction**: this experimental feature is currently limited to Life Time Plus. The keyboard sends the current complete sentence and a bounded set of candidates generated locally from the input code through Cloudflare Workers to TypeSafe Jev for semantic selection. Cloudflare's membership cache stores only a hashed membership decision for up to 60 seconds and contains no input text; KOI's Worker does not write sentences to logs or persistent storage. TypeSafe Jev handles data under its own privacy policy and terms.",
                "The backend database (Firestore) rejects all direct client reads and writes; every write goes through server code.",
            ],
        },
        {
            "kind": "prose",
            "id": "purchases",
            "heading": "Purchases",
            "body": [
                "All payments are handled by Apple. KOI never sees your card, your payment method or your billing address.",
                "Purchase state is managed through RevenueCat, which sends purchase events to KOI's servers containing: the purchaser identifier, product id, transaction id, original transaction id, purchase time, expiry time, period type, cancellation reason, store, and environment (production or sandbox).",
                "This data is used to determine whether you have Plus and to work out your Credit balance. It is not used for anything else.",
            ],
        },
        {
            "kind": "prose",
            "id": "retention",
            "heading": "Retention",
            "bullets": [
                "AI request logs: request-level metadata only, with no content.",
                "Reference image cache during image generation: held in server memory for **10 minutes**, capped at 24 entries.",
                "Sandbox environment operation records: **24 hours**.",
                "Credit ledger and purchase records: kept until the account is closed, because they are needed for refunds, disputes and entitlement decisions.",
                "Local learning history and settings: kept on your device, and gone the moment you delete the app.",
            ],
        },
        {
            "kind": "prose",
            "id": "children",
            "heading": "Children",
            "body": "KOI is not designed for children under 13 and does not knowingly collect their personal data. If you believe a child has given us personal data, contact us and we will delete it.",
        },
        {
            "kind": "prose",
            "id": "rights",
            "heading": "Your choices and rights",
            "bullets": [
                "**Skip the AI**: if you never open KOI Agent, no text leaves the device. You can also switch the AI features off entirely in settings.",
                "**Skip Full Access**: the core input method works exactly the same without it.",
                "**Skip sync**: it is off to begin with, and you can turn it back off at any time.",
                "**Delete local data**: deleting the app clears the learning history and settings on your device.",
                "**Delete iCloud data**: manage it in iOS Settings → your Apple Account → iCloud.",
                "**Delete server data**: email [privacy@rainsday.com](mailto:privacy@rainsday.com). Note that completed purchase records may have to be retained to meet tax and accounting requirements.",
            ],
        },
        {
            "kind": "prose",
            "id": "changes",
            "heading": "Changes to this policy",
            "body": "If the way KOI handles data changes, this page is updated and the effective date at the top changes with it. For significant changes we will tell you in the app.",
        },
        {
            "kind": "prose",
            "id": "contact",
            "heading": "Contact",
            "bullets": [
                "Privacy enquiries: [privacy@rainsday.com](mailto:privacy@rainsday.com)",
                "General support: [support@rainsday.com](mailto:support@rainsday.com)",
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
                        "No. The input engine runs entirely on the device, and that part of the code has no networking capability.",
                        "The one exception is when you open KOI Agent yourself and explicitly choose an action: that sends your instruction plus the exact previewed selection/before/after context, capped at 2,000 Unicode scalar values and 4,000 UTF-8 bytes. See the [privacy policy](route:privacy/) for details.",
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
                    "answer": "No. The app contains no analytics, crash-reporting or advertising tracking tools, and it does not read the advertising identifier.",
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
