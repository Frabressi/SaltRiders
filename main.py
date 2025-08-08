import os
import shutil  # Importa il modulo per le operazioni sui file
from jinja2 import Template

# Importa da moduli personalizzati
import config
import map_generator
import blog_generator


def get_image_url_for_main_page(filename, lang_code, base_images_dir_name):
    """Calcola il path relativo dell'immagine per la pagina principale (index.html o en/index.html)."""
    if lang_code == 'it':
        # Da /index.html a /images/nome.jpg -> "images/nome.jpg"
        return f"{base_images_dir_name}/{filename}"
    else:
        # Da /en/index.html a /images/nome.jpg -> "../images/nome.jpg"
        return f"../{base_images_dir_name}/{filename}"


def build_site():
    """
    Funzione principale che costruisce l'intero sito.
    1. Pulisce e crea la cartella di output (_site).
    2. Copia gli asset statici (css, images).
    3. Genera le pagine del blog.
    4. Genera le pagine principali (index.html, en/index.html).
    """
    # --- 1. PREPARAZIONE DELLA CARTELLA DI OUTPUT (_site) ---
    # Se la cartella di output esiste, la eliminiamo per partire da una situazione pulita.
    if os.path.exists(config.BASE_OUTPUT_DIR):
        shutil.rmtree(config.BASE_OUTPUT_DIR)

    # Creiamo la cartella di output (_site) vuota.
    os.makedirs(config.BASE_OUTPUT_DIR)
    print(f"Cartella di output '{config.BASE_OUTPUT_DIR}' creata.")

    # --- 2. COPIA DEGLI ASSET STATICI ---
    # Copiamo le cartelle 'css' e 'images' dalla root del progetto dentro '_site'.
    # Questo assicura che il sito pubblicato abbia accesso allo stile e alle immagini.
    try:
        shutil.copytree(config.CSS_DIR_NAME, os.path.join(config.BASE_OUTPUT_DIR, config.CSS_DIR_NAME))
        shutil.copytree(config.IMAGES_DIR_NAME, os.path.join(config.BASE_OUTPUT_DIR, config.IMAGES_DIR_NAME))
        print(f"Asset statici '{config.CSS_DIR_NAME}' e '{config.IMAGES_DIR_NAME}' copiati in '{config.BASE_OUTPUT_DIR}'.")
    except FileNotFoundError as e:
        print(f"ATTENZIONE: Impossibile copiare una cartella statica: {e}")
        print("Assicurati che le cartelle 'css' e 'images' esistano nella root del progetto.")
        # Non interrompiamo lo script, ma avvisiamo l'utente.

    # --- 3. GENERAZIONE DELLE PAGINE ---
    # Creiamo la sottocartella /en dentro _site
    os.makedirs(os.path.join(config.BASE_OUTPUT_DIR, "en"), exist_ok=True)

    blog_active = hasattr(config, 'BLOG_POSTS_DIR') and config.BLOG_POSTS_DIR is not None
    if blog_active:
        # La cartella base per l'output del blog (es. '_site/blog')
        blog_output_dir_in_site = os.path.join(config.BASE_OUTPUT_DIR, config.BLOG_OUTPUT_DIR_BASE)
        os.makedirs(blog_output_dir_in_site, exist_ok=True)

        if not hasattr(config, 'BLOG_POST_TEMPLATE_STR') or not hasattr(config, 'BLOG_INDEX_TEMPLATE_STR'):
            print("ATTENZIONE: I template del blog non sono definiti in config.py!")

    html_template_main = Template(config.HTML_TEMPLATE_STR)

    for lang_code in ['it', 'en']:
        current_texts_for_lang = config.TEXT_CONTENT[lang_code].copy()

        # Genera la mappa Folium
        map_html_fragment = map_generator.generate_map_for_language(
            lang_code,
            current_texts_for_lang,
            config.MAP_DATA_COORDS
        )

        # Genera le pagine del blog (ora lo script del blog scriverà dentro _site/blog/...)
        blog_index_url_relative_to_main = None
        if blog_active:
            blog_config_paths = {
                'BLOG_POSTS_DIR': config.BLOG_POSTS_DIR,
                # Passiamo il percorso di output corretto DENTRO _site
                'BLOG_OUTPUT_DIR_BASE': os.path.join(config.BASE_OUTPUT_DIR, config.BLOG_OUTPUT_DIR_BASE),
            }
            site_config_for_blog = {
                'IMAGES_DIR_NAME': config.IMAGES_DIR_NAME,
                'CSS_DIR_NAME': config.CSS_DIR_NAME,
            }
            generated_blog_index_path = blog_generator.generate_blog_pages(
                current_texts_for_lang,
                lang_code,
                blog_config_paths,
                site_config_for_blog
            )

            # Calcola l'URL relativo per il link nella pagina principale
            if generated_blog_index_path:
                # L'URL relativo non cambia, perché è calcolato dal punto di vista del browser
                blog_index_url_relative_to_main = f"{config.BLOG_OUTPUT_DIR_BASE}/{lang_code}.html"


        # Prepara il contesto per il rendering della pagina principale
        render_context = {**current_texts_for_lang}
        render_context['map_html_fragment'] = map_html_fragment
        render_context['blog_index_url'] = blog_index_url_relative_to_main
        render_context['nav_blog'] = current_texts_for_lang.get('nav_blog', 'Blog')

        # Calcola i percorsi delle immagini per la pagina principale
        render_context['gg_photo_url'] = get_image_url_for_main_page(config.GG_PHOTO_FILENAME, lang_code, config.IMAGES_DIR_NAME)
        render_context['paco_photo_url'] = get_image_url_for_main_page(config.PACO_PHOTO_FILENAME, lang_code, config.IMAGES_DIR_NAME)
        render_context['surf_photo_url'] = config.SURF_PHOTO_URL_EXTERNAL
        render_context['bike_setup_photo_url'] = get_image_url_for_main_page(config.BIKE_SETUP_PHOTO_FILENAME, lang_code, config.IMAGES_DIR_NAME)
        render_context['grizl_photo_url'] = get_image_url_for_main_page(config.GRIZL_PHOTO_FILENAME, lang_code, config.IMAGES_DIR_NAME)
        render_context['ocean_crossing_photo_url'] = get_image_url_for_main_page(config.OCEAN_CROSSING_PHOTO_FILENAME, lang_code, config.IMAGES_DIR_NAME)

        # Calcola i link di navigazione tra le lingue
        if lang_code == 'it':
            render_context['brand_link_url'] = "index.html"
            render_context['it_page_url'] = "index.html"
            render_context['en_page_url'] = "en/index.html"
        else:
            render_context['brand_link_url'] = "../index.html"
            render_context['it_page_url'] = "../index.html"
            render_context['en_page_url'] = "index.html"

        # Renderizza l'HTML finale
        rendered_html_content = html_template_main.render(render_context)

        # Scrive il file HTML nella cartella di output corretta (_site o _site/en)
        if lang_code == 'it':
            output_path = os.path.join(config.BASE_OUTPUT_DIR, "index.html")
        else:
            output_path = os.path.join(config.BASE_OUTPUT_DIR, "en", "index.html")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered_html_content)
        print(f"Pagina principale in {lang_code.upper()} salvata in: {output_path}")


if __name__ == "__main__":
    # Assicurati che esista la variabile BASE_OUTPUT_DIR in config.py
    if not hasattr(config, 'BASE_OUTPUT_DIR'):
        print("ERRORE: La variabile 'BASE_OUTPUT_DIR' non è definita in config.py.")
        print("Aggiungi 'BASE_OUTPUT_DIR = \"_site\"' al tuo file di configurazione.")
    else:
        build_site()
        print("\n--- Processo di generazione del sito completato. ---")#

