# Meta Submission Checklist — Summit Automates

**Goal:** get the Facebook + Instagram publishing permissions approved so users
can connect their own Pages / IG Business accounts and Summit can post to them.

**Two gates, in order:**
1. **Business Verification** — proves Summit Systems (Pvt) Ltd is a real company. Prerequisite for the publishing permissions.
2. **App Review** — proves each requested permission is used legitimately. Needs a demo video + a reviewer test account.

> Note: This is NOT the "Meta Tech Provider / Business Partner" program (that's
> an optional co-marketing track). What's below is the standard App Review path
> every app must pass to publish on a user's behalf.

Legend: ✅ have it · 🔧 I can do (code/Railway) · 👤 needs you (login/identity) · ⏳ in progress

---

## Gate 0 — Prerequisites (all green)

| Item | Status | Detail |
|---|---|---|
| Legal entity registered | ✅ | Summit Systems (Private) Limited, Corporate UIN 0324466 |
| Incorporation certificate (PDF) | ✅ | `C:\Users\maxpower\Downloads\INCORPORATION CERTIFICATE (SUMMIT SYSTEMS).pdf` |
| Business address | ✅ | Office # 3, First Floor, Mughal Market, Al-Rehman Arcade, G-13/2, Islamabad |
| Business email on domain | ✅ | admin@summitautomates.com |
| Public website | ✅ | https://summitautomates.com |
| Privacy Policy URL (live, HTTPS) | ✅ | https://app.summitautomates.com/privacy |
| Terms of Service URL (live, HTTPS) | ✅ | https://app.summitautomates.com/terms |
| Data Deletion URL (live, HTTPS) | ✅ | https://app.summitautomates.com/data-deletion |
| OAuth callback route works | ✅ | https://api.summitautomates.com/api/oauth/meta/callback |

---

## Gate 1 — Business Verification

| Item | Status | Who | Notes |
|---|---|---|---|
| Meta Business Suite / Business Manager account | 👤 | you | business.facebook.com → create if you don't have one |
| Business legal name | ✅ | — | Summit Systems (Private) Limited |
| Business registration number | ✅ | — | UIN 0324466 |
| Official business document upload | ✅→👤 | you | Upload the SECP incorporation PDF when prompted |
| Business address + phone | ✅ | — | Islamabad office; add a reachable phone |
| **Domain verification** (DNS TXT or meta-tag) | 🔧 | me+you | Meta gives a TXT token → you add it at Hostinger (like the Railway one) → I verify. OR I drop a meta-tag on the marketing site. |
| Submit verification | 👤 | you | ~3–7 business days for Meta to review |

---

## Gate 2 — App setup (developers.facebook.com)

| Item | Status | Who | Notes |
|---|---|---|---|
| Create app (type: Business) | 👤 | you | Gives you **App ID + App Secret** |
| App name | ✅ | — | Summit Automates |
| App contact email | ✅ | — | admin@summitautomates.com |
| App icon 1024×1024 PNG | ❌ | you/me | **Don't have a logo yet** — need to create one |
| App domains | ✅ | — | summitautomates.com, app., api. |
| Privacy / Terms / Data-deletion URLs | ✅ | — | entered from Gate 0 |
| OAuth redirect URI registered | ✅→🔧 | me | I paste the api. callback once app exists |
| `META_APP_ID` / `META_APP_SECRET` on Railway | ⏳ placeholder | 🔧 me | currently `placeholder` — you send me the real values, I swap them |
| Deauthorize callback | 🔧 | me | quick path: point at data-deletion URL. proper path: build `POST /api/oauth/meta/deauthorize` (~2h) |
| Switch app to **Live** mode | 👤 | you | required before review |

---

## Gate 3 — Permissions to request (App Review)

| Permission | Status | Justification ready? |
|---|---|---|
| `pages_show_list` | request | ✅ in kit |
| `pages_read_engagement` | request | ✅ in kit |
| `pages_manage_posts` | request (sensitive) | ✅ in kit |
| `business_management` | request | ✅ in kit |
| `instagram_basic` | request | ✅ in kit |
| `instagram_content_publish` | request (sensitive) | ✅ in kit |

Justification text is copy-paste ready in `OAUTH_REVIEW_SUBMISSION_KIT.md §A`.

---

## Gate 4 — Demo materials (the usual rejection cause)

| Item | Status | Who | Notes |
|---|---|---|---|
| Reviewer test login | ✅ | — | reviewer@summitautomates.com / Summit-Review-3e497f5a1666 |
| Demo data in reviewer account (niche + sample post) | ❌ | 🔧 me | I'll seed a realistic niche + generated post so the reviewer sees a populated app |
| Demo Facebook Page | ❌ | 👤 you | create "Summit Demo" Page |
| Demo Instagram Business account | ❌ | 👤 you | `@summit_demo`, linked to the demo Page |
| Real META creds wired so OAuth works for the video | ❌ | 🔧 me | blocked on you sending App ID/Secret |
| Screencast video (3–5 min) | ❌ | 👤 you | script is in the kit §A; record with Loom/OBS, upload unlisted to YouTube |

---

## Critical path — what to do in what order

1. **👤 You:** create Business Manager + start Business Verification, upload the SECP PDF. *(longest lead time — start first)*
2. **👤 You:** create the Meta app (Business type) → copy the **App ID + App Secret**.
3. **🔧 Me:** swap the Railway placeholders with your real App ID/Secret, register the callback URL, (optionally) build the deauthorize endpoint.
4. **👤 You + 🔧 me:** domain verification — Meta gives a token, you add it at Hostinger, I confirm.
5. **🔧 Me:** seed the reviewer account with a demo niche + sample post.
6. **👤 You:** create demo FB Page + IG Business account, link them.
7. **👤 You:** with creds wired, record the screencast (OAuth → generate → post → show it live).
8. **👤 You:** make a 1024×1024 logo (or I can generate a simple one).
9. **👤 You:** switch app to Live, submit App Review with the kit's justifications + video.

---

## Summary: HAVE vs NEED

**✅ HAVE (9):** legal entity + cert, address, business email, website, Privacy/Terms/Data-deletion live, working OAuth callback route, reviewer login, all permission justifications written.

**👤 NEED FROM YOU (8):** Business Manager acct, Business Verification submission, create Meta app (→ App ID/Secret), Live-mode switch, demo FB Page, demo IG Business account, screencast recording, domain-verification TXT at Hostinger.

**🔧 NEED FROM ME (5, mostly blocked on your App ID/Secret):** wire real creds into Railway, register callback URI, seed reviewer demo data, (optional) deauthorize endpoint, (optional) generate logo.

**❌ DON'T HAVE YET (1 hard blocker):** a logo / app icon (1024×1024 PNG).
