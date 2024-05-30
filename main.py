import streamlit as st
from time import time
from url_validation import is_valid_url
from lighthouse_executor import executer_lighthouse
from lighthouse_analysis import analyser_rapport_lighthouse
from seo_results_display import afficher_resultats_seo
from pdf_generator import generer_rapport_pdf

# Rate limiting settings
RATE_LIMIT = 60  # 60 seconds between requests
last_request_time = 0

def main():
    global last_request_time
    st.set_page_config(layout="wide")
    st.title("iSEO Checker - Vérificateur de référencement naturel")
    st.markdown(
        """
        <style>
        body {
            transition: background-color 0.5s, color 0.5s;
        }
        @media (prefers-color-scheme: dark) {
            body {
                background-color: #2e2e2e;
                color: #ffffff;
            }
        }
        @media (prefers-color-scheme: light) {
            body {
                background-color: #ffffff;
                color: #000000;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add an image to the top of the landing page
    st.image("./imgs/banner.png", use_column_width=True)

    url = st.text_input("Entrez l'URL du site web que vous souhaitez analyser :")
    
    if st.button("Analyser"):
        if not url:
            st.toast("Veuillez entrer une URL.", icon="⚠️")
        elif not is_valid_url(url):
            st.toast("Veuillez entrer une URL valide.", icon="⚠️")
        else:
            current_time = time()
            if current_time - last_request_time < RATE_LIMIT:
                st.toast("Vous devez attendre avant de faire une autre requête. Veuillez réessayer plus tard.", icon="⚠️")
            else:
                last_request_time = current_time
                with st.spinner("Analyse en cours..."):
                    try:
                        rapport = executer_lighthouse(url)
                        if rapport:
                            score_seo, score_performance, audits_seo = analyser_rapport_lighthouse(rapport)
                            if score_seo is not None and score_performance is not None:
                                afficher_resultats_seo(score_seo, score_performance, audits_seo)
                                st.toast("Analyse terminée avec succès!", icon="✅")

                                pdf = generer_rapport_pdf(url, score_seo, score_performance, audits_seo)
                                if pdf:
                                    st.download_button(label="Télécharger le rapport PDF", data=pdf, file_name="rapport_seo.pdf", mime="application/pdf")
                            else:
                                st.toast("Erreur lors de l'analyse du rapport. Veuillez réessayer.", icon="⚠️")
                        else:
                            st.toast("Échec de l'analyse. Veuillez vérifier l'URL et réessayer.", icon="⚠️")
                    except Exception as e:
                        st.toast(f"Erreur lors de l'analyse : {e}", icon="⚠️")

if __name__ == "__main__":
    main()
