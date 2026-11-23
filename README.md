# Fintech Telex News

This is the source archive for Fintech Telex. Read [African fintech news and analysis](https://fintechtelex.com/) covering digital payments, banking and the businesses connecting Africa with its diaspora.

## Find a published story

To cite a story, open `published.json`, find its entry and use the address in the `link` field. That address takes readers to the published article. For example, our [report on the African Development Bank’s diaspora initiative](https://fintechtelex.com/afdb-diaspora-initiative-124-billion-remittances/) looks at how money sent home by Africans abroad fits into a wider conversation about investment.

## Repository files

- `posts/articles.py` – article text (HTML), categories, tags and excerpts
- `images/` – featured images
- `make_images.py` – generates featured images
- `publish.py` – uploads images and posts to WordPress through the REST API
- `published.json` – post IDs and live links
