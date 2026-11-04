"""English version of the landing page: (German, English) pairs applied to index.template.html.
Every German string must occur exactly once, so a changed template fails loudly instead of
leaving German text on the English page."""
from urllib.parse import quote

DE_SUBJ = "Loomy%20%E2%80%93%20bitte%20benachrichtigen"
DE_BODY = "Hallo%20Patrick%2C%0A%0Abitte%20gib%20mir%20Bescheid%2C%20sobald%20Loomy%20in%20Deutschland%20erh%C3%A4ltlich%20ist."
EN_SUBJ = quote("Loomy – please let me know", safe="")
EN_BODY = quote("Hi Patrick,\n\nplease let me know as soon as Loomy is available in Germany.", safe="")

PAIRS = [
    ('<html lang="de">', '<html lang="en">'),
    ('<title>Loomy Germany – Handgestrickt im Punjab, bald in Deutschland</title>',
     '<title>Loomy Germany – Hand-knitted in Punjab, coming to Germany</title>'),
    ('content="Loomy kommt nach Deutschland: handgestrickte Pullover und Cardigans aus dem Punjab, inspiriert von indischer Textilkunst. Die erste Ware ist bald da."',
     'content="Loomy is coming to Germany: hand-knitted jumpers and cardigans from Punjab, inspired by Indian textile art. The first pieces arrive soon."'),
    ('<link rel="canonical" href="https://loomy.clothing/">', '<link rel="canonical" href="https://loomy.clothing/en.html">'),
    ('<meta property="og:url" content="https://loomy.clothing/">', '<meta property="og:url" content="https://loomy.clothing/en.html">'),
    ('content="Loomy kommt endlich nach Deutschland"', 'content="Loomy is finally coming to Germany"'),
    ('content="Handgestrickte Pullover und Cardigans aus dem Punjab – Masche für Masche, inspiriert von indischer Textilkunst."',
     'content="Hand-knitted jumpers and cardigans from Punjab – stitch by stitch, inspired by Indian textile art."'),
    ('content="de_DE"', 'content="en_GB"'),
    ('<nav class="lang" aria-label="Sprache"><a href="./" hreflang="de" lang="de" aria-current="page">DE</a><a href="en.html" hreflang="en" lang="en">EN</a></nav>',
     '<nav class="lang" aria-label="Language"><a href="./" hreflang="de" lang="de">DE</a><a href="en.html" hreflang="en" lang="en" aria-current="page">EN</a></nav>'),
    ('aria-label="Logo-Animation: Das Loomy-Logo entsteht"', 'aria-label="Logo animation: the Loomy logo takes shape"'),
    ('<span>Ton an</span>', '<span>Sound on</span>'),
    ("on ? 'Ton aus' : 'Ton an'", "on ? 'Sound off' : 'Sound on'"),
    ('<p class="label">Bald in Deutschland</p>', '<p class="label">Coming to Germany</p>'),
    ('<h1>Loomy kommt <em>endlich</em> nach Deutschland.</h1>', '<h1>Loomy is <em>finally</em> coming to Germany.</h1>'),
    ('<p class="lead">Handgestrickte Pullover und Cardigans aus dem Punjab – Masche für Masche, inspiriert von indischer Textilkunst.</p>',
     '<p class="lead">Hand-knitted jumpers and cardigans from Punjab – stitch by stitch, inspired by Indian textile art.</p>'),
    ('>Sag mir Bescheid</a>', '>Let me know</a>'),
    ('<span class="hint">Eine Nachricht, sobald die Ware da ist. Kein Spam.</span>',
     '<span class="hint">One message when the first pieces arrive. No spam.</span>'),
    ('aria-label="Ein Faden läuft vom Punjab bis nach Deutschland"', 'aria-label="A thread runs from Punjab all the way to Germany"'),
    ('<span class="from">Punjab, Indien</span>', '<span class="from">Punjab, India</span>'),
    ('<span>rund 5.700 km Luftlinie</span>', '<span>about 5,700 km as the crow flies</span>'),
    ('<span class="to">Deutschland · ab sofort</span>', '<span class="to">Germany · from now on</span>'),
    ('<h2>Was mit Loomy nach Deutschland kommt.</h2>', '<h2>What Loomy brings to Germany.</h2>'),
    ('<h3>Von Hand gestrickt</h3>', '<h3>Knitted by hand</h3>'),
    ('<p>Jedes Stück entsteht Masche für Masche im Punjab – ohne Maschine, mit Zeit und Geduld.</p>',
     '<p>Every piece is made stitch by stitch in Punjab – no machines, just time and patience.</p>'),
    ('<h3>Indisches Erbe</h3>', '<h3>Indian heritage</h3>'),
    ('<p>Muster aus Phulkari-Stickerei, Kantha-Quilts und Dhurrie-Teppichen, neu übersetzt in Strick.</p>',
     '<p>Patterns from Phulkari embroidery, Kantha quilts and Dhurrie rugs, translated anew into knitwear.</p>'),
    ('<h3>Gute Wolle</h3>', '<h3>Good wool</h3>'),
    ('<p>Merino und Lammwolle – weich, warm und gemacht für lange Winter.</p>',
     '<p>Merino and lambswool – soft, warm and made for long winters.</p>'),
    ('<p class="label">Woher die Muster kommen</p>', '<p class="label">Where the patterns come from</p>'),
    ('<h2>Alte Textilkunst, neu in Strick.</h2>', '<h2>Old textile art, new in knitwear.</h2>'),
    ('<p>Jede Loomy-Kollektion greift eine Handwerkstradition auf, die in Indien seit Generationen weitergegeben wird.</p>',
     '<p>Every Loomy collection takes up a craft tradition that has been passed down in India for generations.</p>'),
    ('aria-label="Gestrickte Probe im Stil der Phulkari-Stickerei: goldene Rauten mit pinkem Kern auf Rot"',
     'aria-label="Knitted swatch in the style of Phulkari embroidery: golden diamonds with pink centres on red"'),
    ('<p>„Blumenarbeit“: Stickerei mit glänzendem Seidengarn auf grobem Baumwollstoff, Stich für Stich zu leuchtenden Flächen gelegt.</p>',
     '<p>“Flower work”: embroidery in glossy silk thread on coarse cotton, laid stitch by stitch into glowing surfaces.</p>'),
    ('aria-label="Gestrickte Probe im Stil der Kantha-Steppnaht: Reihen aus kurzen Stichen auf Indigo"',
     'aria-label="Knitted swatch in the style of Kantha quilting: rows of short stitches on indigo"'),
    ('<p class="origin">Bengalen</p>', '<p class="origin">Bengal</p>'),
    ('<p>Alte Saris, in Lagen übereinandergelegt und mit feinen Vorstichen zu Decken gesteppt – nichts wird weggeworfen.</p>',
     '<p>Old saris, layered on top of each other and quilted into blankets with fine running stitches – nothing goes to waste.</p>'),
    ('aria-label="Gestrickte Probe im Stil eines Dhurrie-Teppichs: Zackenbordüre und gestufte Rauten auf Blau"',
     'aria-label="Knitted swatch in the style of a Dhurrie rug: zigzag border and stepped diamonds on blue"'),
    ('<p>Flachgewebte Teppiche, wie sie in Jodhpur auf Handwebstühlen entstehen: klare Streifen, Stufen und Zacken.</p>',
     '<p>Flat-woven rugs, as they are made on hand looms in Jodhpur: clean stripes, steps and zigzags.</p>'),
    ('alt="Eine Frau im grünen Sari spinnt Garn an einem hölzernen Spinnrad"', 'alt="A woman in a green sari spins yarn on a wooden spinning wheel"'),
    ('<p class="label">Aus dem Atelier</p>', '<p class="label">From the workshop</p>'),
    ('<h2>Jedes Stück beginnt mit einem Faden.</h2>', '<h2>Every piece begins with a thread.</h2>'),
    ('<p class="body">Eingekauft und gestrickt wird im Punjab, in der Region, aus der viele unserer Muster stammen. Jeder Pullover geht dort durch viele Hände, bevor er die Reise nach Deutschland antritt.</p>',
     '<p class="body">The yarn is bought and knitted in Punjab, the region many of our patterns come from. Every jumper passes through many hands there before it sets off for Germany.</p>'),
    ('<p class="caption">Im Bild: Garn am Spinnrad.</p>', '<p class="caption">Pictured: yarn on the spinning wheel.</p>'),
    ('<h2>Dein Ansprechpartner in Deutschland.</h2>', '<h2>Your contact in Germany.</h2>'),
    ('<p class="body">Patrick bringt Loomy nach Deutschland und ist hier dein Ansprechpartner – für Fragen, Bestellungen und alles rund um die erste Lieferung.</p>',
     '<p class="body">Patrick is bringing Loomy to Germany and is your contact here – for questions, orders and everything about the first delivery.</p>'),
    ('<p class="contact"><b>Kontakt</b>', '<p class="contact"><b>Contact</b>'),
    ('<p class="label">Für Läden und Boutiquen</p>', '<p class="label">For shops and boutiques</p>'),
    ('<h2>Loomy in deinem Laden?</h2>', '<h2>Loomy in your shop?</h2>'),
    ('<p class="body">Du führst eine Boutique, einen Concept Store oder einen Laden für faire Mode und möchtest Loomy anbieten? Schreib uns. Wir schicken dir gern das Lookbook und alle Infos zu den Konditionen.</p>',
     '<p class="body">You run a boutique, a concept store or a shop for fair fashion and would like to carry Loomy? Write to us. We will gladly send you the lookbook and all details on terms.</p>'),
    ('<b>Händleranfragen</b>', '<b>Trade enquiries</b>'),
    ('?subject=H%C3%A4ndleranfrage%20Loomy', '?subject=' + quote("Trade enquiry Loomy", safe="")),
    ('<p class="label">Ab sofort in Deutschland</p>', '<p class="label">In Germany from now on</p>'),
    ('<p class="big">Die erste Ware ist <em>bald da.</em></p>', '<p class="big">The first pieces <em>arrive soon.</em></p>'),
    ('<p class="sub">Wir warten noch auf die erste Lieferung aus dem Punjab. Schreib uns, dann sagen wir dir Bescheid, sobald die ersten Stücke hier sind.</p>',
     '<p class="sub">We are still waiting for the first delivery from Punjab. Write to us and we will let you know as soon as the first pieces are here.</p>'),
    ('<h2>Sag uns Bescheid</h2>', '<h2>Get in touch</h2>'),
    ('<p>Schreib uns eine kurze E-Mail. Wir melden uns einmal bei dir, sobald die erste Ware in Deutschland ist.</p>',
     '<p>Send us a short email. We will get back to you once, as soon as the first pieces are in Germany.</p>'),
    ('>E-Mail schreiben</a>', '>Write an email</a>'),
    ('<span>Es öffnet sich kein Mailprogramm? Dann hier:</span>', '<span>No mail app opening? Try one of these:</span>'),
    ('>Adresse kopieren</button>', '>Copy address</button>'),
    ('>In Gmail schreiben</a>', '>Write in Gmail</a>'),
    ('>In Outlook schreiben</a>', '>Write in Outlook</a>'),
    ("'Kopiert: ' + mail + ' – einfach in dein Mailprogramm einfügen.' : 'Bitte von Hand kopieren: ' + mail",
     "'Copied: ' + mail + ' – just paste it into your mail app.' : 'Please copy by hand: ' + mail"),
    ('<p class="note">Oder direkt an: ', '<p class="note">Or write directly to: '),
    ('. Deine Adresse nutzen wir nur für diese eine Nachricht.</p>', '. We only use your address for this one message.</p>'),
    ('<a class="brand" href="#" title="Nach oben">', '<a class="brand" href="#" title="Back to top">'),
    ('alt="Loomy – nach oben"', 'alt="Loomy – back to top"'),
    ('<nav aria-label="Rechtliches">', '<nav aria-label="Legal">'),
    ('<a href="#kontakt">Kontakt</a>', '<a href="#kontakt">Contact</a>'),
    ('<a href="impressum.html">Impressum</a>', '<a href="impressum.html">Legal notice (German)</a>'),
    ('<a href="datenschutz.html">Datenschutz</a>', '<a href="datenschutz.html">Privacy (German)</a>'),
]


def to_english(text):
    # the mail subject/body appear three times each (mailto, Gmail, Outlook)
    text = text.replace(DE_SUBJ, EN_SUBJ).replace(DE_BODY, EN_BODY)
    text = text.replace('<p class="tr">Mit Liebe gestrickt im Punjab</p>', '<p class="tr">Knitted with love in Punjab</p>')
    for de, en in PAIRS:
        n = text.count(de)
        if n != 1:
            raise SystemExit(f"en_text.py: {n}x gefunden statt 1x: {de[:70]}")
        text = text.replace(de, en)
    return text
