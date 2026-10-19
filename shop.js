// Loomy – Produktdaten und Warenkorb (Entwurf, ohne echte Kasse)
const PRODUCTS = [
  { id: 'rug', cat: 'cardigans', heritage: true, tag: 'Heritage', name: 'Rajasthani Rug Cardigan', desc: 'Inspiriert von den Dhurrie-Teppichen und Handwebstühlen aus Jodhpur.', img: 'rug.jpg', alt: 'Blauer Strick-Cardigan mit Dhurrie-Motiven, Rückansicht' },
  { id: 'kantha', cat: 'cardigans', heritage: true, tag: 'Heritage', name: 'Kantha Quilt Cardigan', desc: 'Inspiriert von den traditionellen Kantha-Quilts aus Bengalen.', img: 'kantha.jpg', alt: 'Cremefarbener Cardigan mit Kantha-Dreiecksmustern am Bügel' },
  { id: 'phulkari', cat: 'cardigans', heritage: true, tag: 'Heritage', name: 'Punjabi Phulkari Cardigan', desc: 'Trägt das Erbe der Phulkari-Stickerei aus dem Punjab weiter.', img: 'phulkari.jpg', alt: 'Brauner Cardigan mit pinken, orangen und gelben Phulkari-Motiven' },
  { id: 'parakeet', cat: 'pullover', heritage: true, tag: 'Heritage', name: 'Nostalgic Parakeet Sweater', desc: 'Motive wie vom indischen Geschirr der 80er und 90er Jahre.', img: 'parakeet.jpg', alt: 'Cremefarbener Pullover mit zwei gestrickten Sittichen' },
  { id: 'teeset', cat: 'pullover', heritage: true, tag: 'Heritage', name: '[Name] Sweater & Short Sleeve Tee', desc: 'Entworfen, eingekauft und gestrickt im Punjab, Indien.', img: 'teeset.jpg', alt: 'Naturfarbene Strickjacke und kurzärmeliger Strickpullover' },
  { id: 'lotus', cat: 'cardigans', tag: 'Cardigan', name: 'Lotus Petal Cardigan', desc: 'Lange Strickjacke mit grobem Blattzopf, angelehnt an Lotusblüten.', variants: [
    { label: 'Rot · Acryl', color: '#C42A21', img: 'lotus_red.jpg', alt: 'Roter Lotus Petal Cardigan' },
    { label: 'Schwarz · Merino', color: '#1E1C1C', img: 'lotus_black.jpg', alt: 'Schwarzer Lotus Petal Cardigan aus Merino' },
    { label: 'Mauve · Merino', color: '#9A6577', img: 'lotus_mauve.jpg', alt: 'Mauvefarbener Lotus Petal Cardigan aus Merino' },
    { label: 'Grün · Acryl, dick', color: '#4E9A2A', img: 'lotus_green.jpg', alt: 'Grüner Lotus Petal Cardigan, dick gestrickt' }
  ] },
  { id: 'chunky', cat: 'cardigans', tag: 'Chunky', name: 'Chunky Merino Cardigan', desc: 'Extra grob gestrickt aus dicker Merinowolle, mit Kontrastbündchen.', variants: [
    { label: 'Rosa', color: '#E0796F', img: 'chunky_pink.jpg', alt: 'Rosa Chunky-Merino-Cardigan mit Bündchen in Creme und Blau' },
    { label: 'Sand', color: '#D3BDA3', img: 'chunky_sand.jpg', alt: 'Sandfarbener Chunky-Merino-Cardigan' }
  ] },
  { id: 'chunkycrop', cat: 'cardigans', tag: 'Chunky', name: 'Chunky Merino Crop', desc: 'Kurz geschnitten in Creme und Navy, mit blauem Motiv auf der Brust.', img: 'chunky_crop.jpg', alt: 'Kurzer grober Merino-Strick in Creme und Navy' },
  { id: 'cover', cat: 'pullover', tag: 'Pullover', name: '[Name] Pullover', desc: 'Kraus gestrickt in Taupe und Braun, mit orangefarbenen Akzenten.', img: 'cover.jpg', alt: 'Taupefarbener Strickpullover mit orangefarbenen Akzenten' },
  { id: 'embroidered', cat: 'pullover', tag: 'Pullover', name: 'Classic Embroidered Sweater', desc: 'Aus Lammwolle, mit Blüten bestickt an Passe und Ärmeln.', img: 'embroidered.jpg', alt: 'Grüner Pullover mit rosa Blütenstickerei' },
  { id: 'striped', cat: 'pullover', tag: 'Pullover', name: '[Name] Streifenpullover', desc: 'Grün in Grün gestreift, mit Stickblüten an der Schulter.', img: 'striped.jpg', alt: 'Grün gestreifter Pullover mit Stehkragen' },
  { id: 'lavender', cat: 'pullover', tag: 'Kleid', name: 'Lavender Cabled Dress', desc: 'Strickkleid mit Zopfmuster und weitem Ausschnitt, auch schulterfrei.', img: 'lavender.jpg', alt: 'Lavendelfarbenes Strickkleid mit Zöpfen' },
  { id: 'bundi', cat: 'capes', tag: 'Jacke', name: 'Bundi Chunky Crochet Cozy', desc: 'Grobe Häkeljacke in Petrol mit Streifen in Gelb, Sand und Weiß.', img: 'bundi.jpg', alt: 'Petrolfarbene Häkeljacke mit bunten Streifen' },
  { id: 'balloon', cat: 'cardigans', tag: 'Cardigan', name: 'Balloon Sleeves Cardigan', desc: 'Dreifarbiger Strick-Cardigan mit Ballonärmeln und handgemachten Knöpfen.', img: 'balloon.jpg', alt: 'Cardigan in Weiß, Braun und Grün mit Ballonärmeln' },
  { id: 'pop', cat: 'cardigans', tag: 'Cardigan', name: 'Pop Colors Cardigan', desc: 'Kurzer Patchwork-Cardigan in Blau, Weiß und Gelb mit flauschigen Feldern.', img: 'patchwork.jpg', alt: 'Bunter Patchwork-Cardigan von hinten' },
  { id: 'bee', cat: 'pullover', tag: 'Pullover', name: 'Buzzing Hive', desc: 'Gehäkelter Baumwollpullover mit gestickter Biene und gestreiften Ärmeln.', img: 'bee.jpg', alt: 'Cremefarbener Pullover mit gestickter Biene' },
  { id: 'misty', cat: 'capes', tag: 'Jacke', name: 'Misty Netweave Jacke', desc: 'Graue Häkeljacke mit Blütenmuster an den Ärmeln und melierten Taschen.', img: 'jacket.jpg', alt: 'Graue Häkeljacke mit melierten Taschen' },
  { id: 'cape', cat: 'capes', tag: 'Cape', name: 'Oversized Cape', desc: 'Weites Häkel-Cape mit Rollkragen, Ärmeln und aufgesetzten Taschen.', img: 'cape.jpg', alt: 'Braunes Oversized-Häkelcape mit Rollkragen' }
];

const FILTERS = [
  { id: 'alle', label: 'Alle' },
  { id: 'heritage', label: 'Heritage' },
  { id: 'cardigans', label: 'Cardigans' },
  { id: 'pullover', label: 'Pullover & Kleider' },
  { id: 'capes', label: 'Capes & Jacken' }
];

const state = { filter: 'alle', variant: {}, cart: {} };
const byId = Object.fromEntries(PRODUCTS.map(p => [p.id, p]));
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function view(p) {
  const vi = state.variant[p.id] || 0;
  const v = p.variants ? p.variants[vi] : null;
  return { vi, img: 'img/' + (v ? v.img : p.img), alt: v ? v.alt : p.alt, label: v ? v.label : '', key: p.id + '|' + vi };
}

function renderFilters() {
  $('filters').innerHTML = FILTERS.map(f =>
    `<button type="button" data-filter="${f.id}" aria-pressed="${state.filter === f.id}">${esc(f.label)}</button>`
  ).join('');
}

function renderGrid() {
  const f = state.filter;
  const list = PRODUCTS.filter(p => f === 'alle' || p.cat === f || (f === 'heritage' && p.heritage));
  const cards = list.map(p => {
    const v = view(p);
    const inCart = state.cart[v.key] || 0;
    const swatches = p.variants ? `
      <div class="swatches" role="group" aria-label="Farbe wählen">
        ${p.variants.map((x, i) => `<button type="button" class="swatch" data-swatch="${p.id}:${i}" aria-pressed="${i === v.vi}" aria-label="${esc(x.label)}" title="${esc(x.label)}" style="background:${x.color}"></button>`).join('')}
        <span class="swatch-label">${esc(v.label)}</span>
      </div>` : '';
    return `
      <article class="card">
        <div class="pic"><img src="${v.img}" alt="${esc(v.alt)}" loading="lazy"><span class="tag">${esc(p.tag)}</span></div>
        <div class="row"><h3>${esc(p.name)}</h3><p class="price">[Preis]</p></div>
        <p class="desc">${esc(p.desc)}</p>
        ${swatches}
        <button type="button" class="add" data-add="${p.id}">${inCart ? `Im Warenkorb (${inCart})` : 'In den Warenkorb'}</button>
      </article>`;
  }).join('');
  $('grid').innerHTML = cards + `
    <article class="more">
      <p class="serif" style="font-size:24px">Mehr in Arbeit</p>
      <p class="desc" style="max-width:240px">Neue Stücke kommen laufend dazu. Trag dich unten ein, dann sagen wir Bescheid.</p>
    </article>`;
}

function renderCart() {
  const keys = Object.keys(state.cart);
  const count = keys.reduce((s, k) => s + state.cart[k], 0);
  $('cartBadge').textContent = count;
  $('cartCount').textContent = count + ' Artikel';
  if (!keys.length) {
    $('cartBody').innerHTML = '<p class="empty">Noch nichts drin. Stöber doch mal durch die Kollektion.</p>';
    return;
  }
  $('cartBody').innerHTML = keys.map(k => {
    const [id, vi] = k.split('|');
    const p = byId[id];
    const v = p.variants ? p.variants[Number(vi)] : null;
    const q = state.cart[k];
    return `
      <div class="line">
        <img src="img/${v ? v.img : p.img}" alt="">
        <div class="info">
          <p style="font-weight:600">${esc(p.name)}</p>
          ${v ? `<p class="sub">${esc(v.label)}</p>` : ''}
          <p class="sub" style="font-size:15px">[Preis]</p>
          <div class="qty">
            <button type="button" class="step" data-dec="${k}" aria-label="Menge verringern">−</button>
            <span>${q}</span>
            <button type="button" class="step" data-inc="${k}" aria-label="Menge erhöhen">+</button>
            <button type="button" class="remove" data-remove="${k}">Entfernen</button>
          </div>
        </div>
      </div>`;
  }).join('');
}

function setQty(key, q) {
  if (q <= 0) delete state.cart[key]; else state.cart[key] = q;
  renderCart(); renderGrid();
}

function openCart() { $('overlay').hidden = false; document.body.style.overflow = 'hidden'; $('closeCart').focus(); }
function closeCart() { $('overlay').hidden = true; document.body.style.overflow = ''; $('openCart').focus(); }

document.addEventListener('click', e => {
  const t = e.target.closest('button');
  if (!t) { if (e.target.id === 'overlay') closeCart(); return; }
  if (t.dataset.filter) { state.filter = t.dataset.filter; renderFilters(); renderGrid(); }
  else if (t.dataset.swatch) { const [id, i] = t.dataset.swatch.split(':'); state.variant[id] = Number(i); renderGrid(); }
  else if (t.dataset.add) { const k = view(byId[t.dataset.add]).key; setQty(k, (state.cart[k] || 0) + 1); openCart(); }
  else if (t.dataset.inc) setQty(t.dataset.inc, state.cart[t.dataset.inc] + 1);
  else if (t.dataset.dec) setQty(t.dataset.dec, state.cart[t.dataset.dec] - 1);
  else if (t.dataset.remove) setQty(t.dataset.remove, 0);
  else if (t.id === 'openCart') openCart();
  else if (t.id === 'closeCart') closeCart();
});
document.addEventListener('keydown', e => { if (e.key === 'Escape' && !$('overlay').hidden) closeCart(); });

renderFilters(); renderGrid(); renderCart();
