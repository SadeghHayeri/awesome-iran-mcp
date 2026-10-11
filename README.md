<div align="center">

<img src="assets/banner.svg" alt="awesome-iran-mcp: 19 MCP servers and 308 tools that wire the Iranian web into AI agents" width="100%">

**English** · [فارسی](README.fa.md)

# awesome-iran-mcp

**Give your AI agent the Iranian web.**<br>
19 open-source MCP servers for Digikala, Snappfood, Jabama, MrBilit, Paziresh24, Taaghche and more.<br>
Search, compare prices in Toman, find free slots and today's deals from Claude, Cursor, VS Code or any MCP client.

[![Servers](https://img.shields.io/badge/servers-19-3fd6c9)](#the-servers)
[![Tools](https://img.shields.io/badge/tools-308-f4b54a)](TOOLS.md)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-io.github.sepehr071-7c3aed)](https://registry.modelcontextprotocol.io/?q=sepehr071)
[![License: MIT](https://img.shields.io/badge/license-MIT-16a34a)](LICENSE)
[![Stars](https://img.shields.io/github/stars/sepehr071/awesome-iran-mcp?style=social)](https://github.com/sepehr071/awesome-iran-mcp)

[Quick start](#quick-start) · [The servers](#the-servers) · [For AI agents](#for-ai-agents) · [All tools](TOOLS.md) · [FAQ](#faq)

</div>

---

## Why

Iranian websites are not built for AI agents. Most have no public API, prices come in Rial on one page and Toman
on the next, and every site hides its best deals behind a different menu. Each server here maps one site's real
(undocumented) API, tests it, and exposes it as clean MCP tools with prices in **Toman**.

Put a few of them together and one sentence does a day of tab-hopping (illustrative example):

> **You:** I'm flying Tehran to Kish next Thursday for 3 nights. Cheapest flight, a villa under 4 million Toman a
> night, and a dermatologist on the island with a free slot.
>
> **Agent:** *calls* `mrbilit` for flights → `jabama` and `otaghak` for stays → `paziresh24` for doctors
>
> | | Pick | Price (Toman) |
> |---|---|---:|
> | Flight | Thursday 07:40, economy, 2 seats left | 2,180,000 |
> | Stay | 2-bedroom villa near the beach, 4.8 stars | 3,650,000 / night |
> | Doctor | Dermatologist, Saturday 10:30, in-person | 450,000 |

## Quick start

Every server is a small Python package on PyPI, run with [`uvx`](https://docs.astral.sh/uv/). No API key and
no install step, except `payping-mcp` and `bale-mcp`, which act on your own account.

**One server** (Claude Code):

```bash
claude mcp add digikala -- uvx digikala-mcp
```

**Any MCP client** (Claude Desktop, Cursor, Windsurf, VS Code, ...):

```json
{
  "mcpServers": {
    "digikala": { "command": "uvx", "args": ["digikala-mcp"] },
    "jabama":   { "command": "uvx", "args": ["jabama-mcp"] }
  }
}
```

**All 19 at once:** clone this repo and open it in Claude Code. The [`.mcp.json`](.mcp.json) at the root
registers every server; approve the ones you want.

```bash
git clone https://github.com/sepehr071/awesome-iran-mcp
cd awesome-iran-mcp && claude
```

> [!TIP]
> 308 tools is a lot of context. Enable the servers for the task at hand rather than all of them.

## The servers

### 🛒 Shopping

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [digikala-mcp](https://github.com/sepehr071/digikala-mcp) | [Digikala](https://www.digikala.com) (incl. Fresh) | 23 | Search with feature filters, best picks for a budget, every seller, price history, reviews, deals |
| [technolife-mcp](https://github.com/sepehr071/technolife-mcp) | [Technolife](https://www.technolife.com) | 19 | Electronics: each seller's cash and installment price, specs, reviews, deals |
| [masterkala-mcp](https://github.com/sepehr071/masterkala-mcp) | [MasterKala](https://masterkala.com) | 14 | Gadgets and accessories: prices, specs, deals |
| [shopino-mcp](https://github.com/sepehr071/shopino-mcp) | [Shopino](https://shopino.app) | 14 | Fashion from thousands of shops: prices, sizes, stock, shop ratings |

### 💄 Beauty

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [khanoumi-mcp](https://github.com/sepehr071/khanoumi-mcp) | [Khanoumi](https://www.khanoumi.com) | 12 | Cosmetics, skin and hair care, perfume: prices, shades, reviews, deals |
| [asalbanoo-mcp](https://github.com/sepehr071/asalbanoo-mcp) | [Asal Banoo](https://asalbanooshop.com) | 12 | Cosmetics and hair care: prices, variants, deals |

### 🍕 Food and groceries

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [snapp-mcp](https://github.com/sepehr071/snapp-mcp) | [Snappfood](https://snappfood.ir) + SnappMarket | 21 | Cheapest dish near you, menus, FoodParty flash deals, groceries |
| [okala-mcp](https://github.com/sepehr071/okala-mcp) | [Okala](https://okala.com) | 16 | Grocery stores that deliver to you, prices across stores, deals |

### ✈️ Travel and stays

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [mrbilit-mcp](https://github.com/sepehr071/mrbilit-mcp) | [MrBilit](https://mrbilit.com) | 22 | Cheapest flights, trains, buses, taxis and hotels; seats and refund rules |
| [flytoday-mcp](https://github.com/sepehr071/flytoday-mcp) | [Flytoday](https://www.flytoday.ir) | 22 | Flights, trains, buses, hotels, villas; CIP, eSIM, visas, activities |
| [jabama-mcp](https://github.com/sepehr071/jabama-mcp) | [Jabama](https://www.jabama.com) | 21 | Stays with exact prices, group tours, events and theater tickets |
| [otaghak-mcp](https://github.com/sepehr071/otaghak-mcp) | [Otaghak](https://www.otaghak.com) | 15 | Villas and cottages: availability, exact stay price, reviews, hosts |

### 🩺 Health

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [paziresh24-mcp](https://github.com/sepehr071/paziresh24-mcp) | [Paziresh24](https://www.paziresh24.com) | 12 | Doctors, visit prices, reviews, free appointment slots |
| [doctoreto-mcp](https://github.com/sepehr071/doctoreto-mcp) | [Doctoreto](https://doctoreto.com) | 14 | Doctors, visit fees, free slots, reviews, clinics, labs, offers |

### 📚 Books

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [taaghche-mcp](https://github.com/sepehr071/taaghche-mcp) | [Taaghche](https://taaghche.com) | 12 | Ebooks and audiobooks: prices, discounts, reviews, bestsellers, free books |
| [fidibo-mcp](https://github.com/sepehr071/fidibo-mcp) | [Fidibo](https://fidibo.com) | 11 | Ebooks and audiobooks: prices, Fidibo Plus, reviews, bestsellers, free books |
| [30book-mcp](https://github.com/sepehr071/30book-mcp) | [30book](https://www.30book.com) | 14 | Printed books: list and discounted price, stock, editions, ISBN, deals |

### 💳 Your own accounts (need a token)

| Server | Site | Tools | What your agent can do |
|---|---|---:|---|
| [payping-mcp](https://github.com/sepehr071/payping-mcp) | [PayPing](https://www.payping.ir) | 21 | Read balance, sales, customers; create products, payment links, coupons, invoices |
| [bale-mcp](https://github.com/sepehr071/bale-mcp) | [Bale](https://bale.ai) messenger | 13 | Read and answer your bot's messages, ask and wait for replies, send files |

Every tool, with a one-line summary: [TOOLS.md](TOOLS.md).

## For AI agents

This repo is built to be read by agents as much as by people:

| File | What it is |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Which server to pick for which task, conventions, safety rules, how to work in this repo |
| [`servers.json`](servers.json) | Machine-readable catalog: package, version, category, env vars and every tool of each server |
| [`TOOLS.md`](TOOLS.md) | All 308 tools grouped by server, one line each |
| [`llms.txt`](llms.txt) | Short index for LLMs ([llmstxt.org](https://llmstxt.org)) |
| [`.mcp.json`](.mcp.json) | Ready-to-use config for every server |

Paste this into your agent to set it up:

```text
Read https://raw.githubusercontent.com/sepehr071/awesome-iran-mcp/main/AGENTS.md, then add the MCP servers I need for <task> to my MCP config.
```

## Shared conventions

- **Prices are always Toman**, even where the site's API returns Rial.
- **Read-only by design.** Shop, travel, health and book servers never log in, fill a basket, book or pay.
  `payping-mcp` and `bale-mcp` can write, but only to your own account, with your token, on your machine.
- **Images:** product, stay, hotel and doctor results carry an `image` URL where the site has one.
- **Proxy:** every server reads an optional `<NAME>_MCP_PROXY` env var (e.g. `DIGIKALA_MCP_PROXY`) for sites
  that block your IP. System proxy settings are ignored. See [`servers.json`](servers.json) for exact names.
- Same layout everywhere: `src/<pkg>/http.py`, `registry.py`, `server.py`, offline tests on recorded fixtures,
  `-m live` tests against the real site, published to PyPI and the [MCP Registry](https://registry.modelcontextprotocol.io).

## Working from source

Each server lives in its own repo and is pinned here as a git submodule under `servers/`.

```bash
git clone --recurse-submodules https://github.com/sepehr071/awesome-iran-mcp
cd awesome-iran-mcp/servers/digikala-mcp
uv sync && uv run pytest -q          # offline tests
uv run pytest -m live -q             # against the real site
```

Pull every server to its latest `main` and rebuild the catalog:

```bash
git submodule update --init --remote
python scripts/catalog.py            # rewrites servers.json, TOOLS.md, .mcp.json
python scripts/banner.py             # redraws both banners with the new counts
```

Bugs and feature requests for a server go to that server's own repo.

## FAQ

<details>
<summary><b>Are these official?</b></summary>

No. They are unofficial and not affiliated with any of the sites. They call the same endpoints the sites' own web
apps use. Those APIs are undocumented and can change; open an issue on the server's repo when one breaks.
</details>

<details>
<summary><b>A site times out or returns 403 from outside Iran.</b></summary>

Some sites block foreign IPs. Set that server's proxy variable, e.g. `DIGIKALA_MCP_PROXY=http://127.0.0.1:8080`,
to a proxy with an Iranian exit.
</details>

<details>
<summary><b>Can my agent order or pay for me?</b></summary>

No. The site servers are read-only on purpose. Your agent finds and compares; you buy.
</details>

<details>
<summary><b>Do I need Python?</b></summary>

You need [uv](https://docs.astral.sh/uv/getting-started/installation/). `uvx` downloads the right Python and the
package on first run.
</details>

## License

[MIT](LICENSE). Each server is MIT licensed in its own repo. Site names and trademarks belong to their owners.
