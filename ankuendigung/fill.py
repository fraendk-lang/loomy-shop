"""Fill the Loomy pages with Patrick's contact and imprint data.

Edit DATA below, then run:  python3 fill.py
It writes index.html, en.html, impressum.html and datenschutz.html from the *.template.html files
and refuses to finish while a placeholder is still empty.
"""
import html, pathlib, re, sys
from en_text import to_english

DATA = {
    "EMAIL": "info@loomy.clothing",
    "EMAIL_HANDEL": "",     # leer lassen = gleiche Adresse wie EMAIL
    "FIRMA": "",            # Firmenname mit Rechtsform (leer = Patrick Samra als Person)
    "ADRESSE": "Altenrather Straße 150\n53797 Lohmar",  # Straße Nr., PLZ Ort
    "TELEFON": "",          # optional
    "REGISTER": "",         # optional, z. B. "Amtsgericht Köln, HRB 12345"
    "USTID": "",            # optional, z. B. "DE123456789"
    # Gruß auf Punjabi (Gurmukhi) am Anfang des Fadens. Erst eintragen, wenn Loomy den Text bestätigt hat.
    # Vorschau ohne Bestätigung: python3 fill.py --vorschau
    "PUNJABI": "",
    # Profile von Loomy Germany (volle Adresse mit https://). Leer = Symbol wird nicht gezeigt.
    "INSTAGRAM": "https://www.instagram.com/loomy_germany/",
    "FACEBOOK": "https://www.facebook.com/share/1DFY4FpsPG",
    "YOUTUBE": "",
}
PUNJABI_ENTWURF = "ਪੰਜਾਬ ਵਿੱਚ ਪਿਆਰ ਨਾਲ ਬੁਣਿਆ"   # „Mit Liebe gestrickt im Punjab“

here = pathlib.Path(__file__).parent
draft = "--entwurf" in sys.argv   # test build: empty fields show as "[folgt]"
d = dict(DATA)
if "--vorschau" in sys.argv and not d["PUNJABI"].strip():
    d["PUNJABI"] = PUNJABI_ENTWURF
missing = [k for k in ("EMAIL", "ADRESSE") if not d[k].strip()]
if missing and not draft:
    sys.exit("Noch leer: " + ", ".join(missing) + "  (Testfassung: python3 fill.py --entwurf)")
for k in missing:
    d[k] = "[folgt]"
d["EMAIL_HANDEL"] = d["EMAIL_HANDEL"] or d["EMAIL"]

esc = {k: html.escape(v.strip()) for k, v in d.items()}
esc["ADRESSE"] = esc["ADRESSE"].replace("\n", "<br>")
if esc["FIRMA"]:
    esc["VERTRETEN_BLOCK"] = "<p>Vertreten durch: Patrick Samra</p>"
else:
    esc["FIRMA"] = "Patrick Samra<br>Loomy Germany"
    esc["VERTRETEN_BLOCK"] = ""
esc["TELEFON_LINE"] = ("Telefon: %s<br>" % esc["TELEFON"]) if esc["TELEFON"] else ""
esc["TELEFON_TAIL"] = ("<br>Telefon: %s" % esc["TELEFON"]) if esc["TELEFON"] else ""
esc["REGISTER_BLOCK"] = ("<h2>Registereintrag</h2>\n  <p>%s</p>" % esc["REGISTER"]) if esc["REGISTER"] else ""
esc["USTID_BLOCK"] = ("<h2>Umsatzsteuer-ID</h2>\n  <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: %s</p>" % esc["USTID"]) if esc["USTID"] else ""

esc["PUNJABI_BLOCK"] = ('  <div class="greet">\n    <p class="pa" lang="pa">%s</p>\n    <p class="tr">Mit Liebe gestrickt im Punjab</p>\n  </div>' % esc["PUNJABI"]) if esc["PUNJABI"] else ""

ICONS = {
    "INSTAGRAM": ("Instagram", '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/>'),
    "FACEBOOK": ("Facebook", '<path d="M14 21v-7.5h2.6l.4-3H14V8.7c0-.9.3-1.5 1.6-1.5H17V4.5c-.3 0-1.2-.1-2.3-.1-2.3 0-3.7 1.4-3.7 3.9v2.2H8.5v3H11V21"/>'),
    "YOUTUBE": ("YouTube", '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.2v5.6l4.8-2.8z" fill="currentColor"/>'),
}
links = []
for key, (name, svg) in ICONS.items():
    url = d.get(key, "").strip()
    if not url:
        continue
    if not url.startswith("https://"):
        sys.exit(f"{key}: bitte die volle Adresse mit https:// eintragen")
    links.append('      <a href="%s" target="_blank" rel="noopener" aria-label="Loomy Germany auf %s" title="%s"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg></a>' % (html.escape(url, quote=True), name, name, svg))
esc["SOCIAL_BLOCK"] = ('    <nav class="social" aria-label="Social Media">\n%s\n    </nav>' % "\n".join(links)) if links else ""

pages = [(n, n) for n in ("index", "impressum", "datenschutz")] + [("index", "en")]
for src, name in pages:
    text = (here / f"{src}.template.html").read_text(encoding="utf-8")
    if name == "en":
        text = to_english(text.replace("{{PUNJABI_BLOCK}}", esc["PUNJABI_BLOCK"]))
    text = re.sub(r"\{\{(\w+)\}\}", lambda m: esc[m.group(1)], text)
    left = re.findall(r"\{\{\w+\}\}|\[[A-ZÄÖÜ][^\]]{2,40}\]", text)
    if left and not draft:
        sys.exit(f"{name}.html: offene Platzhalter {set(left)}")
    (here / f"{name}.html").write_text(text, encoding="utf-8")
    print("geschrieben:", f"{name}.html")
