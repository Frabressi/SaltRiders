### Passaggio 1: Caricare le Immagini del Post

1.  Apri l'app di GitHub o vai sul sito github.com e naviga nel tuo repository `pacific_trip`.

2.  Vai nella cartella `images/blog/`.

3.  Crea una nuova cartella per le immagini del tuo post. È una buona abitudine usare la data come nome (es. `08-15-25`).
    * Per farlo, clicca su `Add file` > `Create new file`.
    * Nella casella del nome, scrivi il nome della cartella seguito da una barra, ad esempio `08-15-25/`. GitHub creerà automaticamente la cartella. Potrebbe chiederti di creare un file "segnaposto" dentro, puoi chiamarlo `.gitkeep` e salvarlo.

4.  Entra nella nuova cartella che hai creato (es. `images/blog/08-15-25/`).

5.  Clicca su `Add file` > `Upload files`.

6.  Seleziona le foto dalla galleria del tuo telefono e caricale.

7.  **MOLTO IMPORTANTE:** Una volta caricate, prendi nota del percorso esatto di ogni immagine. Ad esempio: `images/blog/08-15-25/vele-al-tramonto.jpg`. Ti servirà tra poco.

### Passaggio 1: Caricare le Immagini del Post

1.  Apri l'app di GitHub o vai sul sito github.com e naviga nel tuo repository `pacific_trip`.

2.  Vai nella cartella `images/blog/`.

3.  Crea una nuova cartella per le immagini del tuo post. È una buona abitudine usare la data come nome (es. `08-15-25`).
    * Per farlo, clicca su `Add file` > `Create new file`.
    * Nella casella del nome, scrivi il nome della cartella seguito da una barra, ad esempio `08-15-25/`. GitHub creerà automaticamente la cartella. Potrebbe chiederti di creare un file "segnaposto" dentro, puoi chiamarlo `.gitkeep` e salvarlo.

4.  Entra nella nuova cartella che hai creato (es. `images/blog/08-15-25/`).

5.  Clicca su `Add file` > `Upload files`.

6.  Seleziona le foto dalla galleria del tuo telefono e caricale.

7.  **MOLTO IMPORTANTE:** Una volta caricate, prendi nota del percorso esatto di ogni immagine. Ad esempio: `images/blog/08-15-25/vele-al-tramonto.jpg`. Ti servirà tra poco.

### Passaggio 3: Compilare e Controllare con Attenzione

1.  **Modifica il Frontmatter:** Compila tutti i campi del template che hai incollato.
    * `title`: Metti il titolo vero.
    * `date`: Metti la data `AAAA-MM-GG`.
    * `author`: Metti il tuo nome.
    * `slug`: Metti un titolo breve per l'URL (es. `prima-settimana-canarie`).
    * `image`: Qui devi inserire il percorso **esatto** dell'immagine di copertina che hai caricato al Passaggio 1. Un errore qui e l'immagine non si vedrà.
    * `summary`: Scrivi il riassunto.

2.  **Scrivi il Post:** Scrivi la tua storia sotto la riga `---`.

3.  **Inserisci altre immagini:** Se vuoi aggiungere altre foto nel testo, usa la sintassi `![descrizione](percorso/immagine.jpg)`, usando sempre i percorsi esatti delle immagini che hai caricato.

4.  **IL CONTROLLO FINALE (DA FARE 3 VOLTE!):**
    Prima di pubblicare, rileggi tutto nel campo di testo e chiediti:
    * [ ] Il nome del file `.md` è corretto?
    * [ ] La data nel nome del file e nel campo `date` coincidono?
    * [ ] Il percorso dell'immagine di copertina in `image:` è **IDENTICO** a quello reale su GitHub? Controlla maiuscole, minuscole, trattini.
    * [ ] I percorsi di tutte le altre immagini sono corretti?
    * [ ] Non ci sono errori di battitura nel testo?

### Passaggio 4: Pubblicare il Post (Commit)

1.  In fondo alla pagina di modifica del file, vedrai un pulsante verde, di solito con scritto **"Commit new file"**.

2.  Cliccalo. Questo salverà il tuo post nel repository.

3.  **ATTENDI:** Una volta premuto, l'azione automatica si avvierà. Ha bisogno di circa **2-3 minuti** per ricostruire il sito e pubblicare le tue modifiche.

4.  **VERIFICA:** Dopo qualche minuto, apri il sito del tuo blog e controlla il risultato. Se tutto è andato bene, il tuo post sarà online e visibile correttamente.

### Passaggio 5: Correggere un Errore

Se noti un'immagine mancante o un errore di testo:

1.  Torna su GitHub (app o web).
2.  Vai nel file che contiene l'errore (il tuo file `.md` in `_posts/`).
3.  Clicca sull'icona della matita per modificarlo.
4.  Correggi l'errore (ad esempio, il percorso di un'immagine o una parola).
5.  Clicca sul pulsante verde in fondo **"Commit changes"**.

L'azione si riavvierà e in 2-3 minuti la versione corretta sarà online.