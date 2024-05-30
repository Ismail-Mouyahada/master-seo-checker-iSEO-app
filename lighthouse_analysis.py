import streamlit as st

def analyser_rapport_lighthouse(report):
    try:
        categories = report['categories']
        audits = report['audits']

        score_seo = categories['seo']['score'] * 100
        score_performance = categories['performance']['score'] * 100

        audits_seo = [
            {
                'id': audit['id'],
                'titre': audit['title'],
                'description': audit['description'],
                'score': audit['score'] * 100 if audit['score'] is not None else 'N/A',
                'couleur': 'green' if audit['score'] and audit['score'] == 1 else ('orange' if audit['score'] and audit['score'] < 1 else 'red')
            }
            for audit in audits.values() if audit['score'] is not None
        ]

        return score_seo, score_performance, audits_seo

    except KeyError as e:
        st.toast(f"Erreur : Clé manquante dans le rapport Lighthouse - {e}", icon="⚠️")
        return None, None, []
    except Exception as e:
        st.toast(f"Erreur lors de l'analyse du rapport : {e}", icon="⚠️")
        return None, None, []

def afficher_resultats_seo(score_seo, score_performance, audits_seo):
    st.header("Rapport d'Analyse SEO Lighthouse")

    # CSS personnalisé pour le fond et la mise en forme des cartes
    st.markdown("""
        <style>
            body {
                background-color: #f0f0f0;
            }
            .card {
                background-color: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin: 10px 0;
            }
            .card-header {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .card-metric {
                font-size: 30px;
                font-weight: bold;
            }
            .author {
                margin-top: 20px;
                font-size: 16px;
                color: grey;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div class="card">
                <div class="card-header">Score SEO</div>
                <div class="card-metric">{score_seo}</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="card">
                <div class="card-header">Score de Performance</div>
                <div class="card-metric">{score_performance}</div>
            </div>
        """, unsafe_allow_html=True)

    st.subheader("Audits SEO")

    for audit in audits_seo:
        couleur = audit['couleur']
        st.markdown(f"""
            <div style='border-left: 4px solid {couleur}; padding-left: 8px; margin-bottom: 8px; background-color: white; padding: 10px; border-radius: 5px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
                <strong>{audit['titre']}</strong> - {audit['description']} <br> 
                <strong>Score : {audit['score']}</strong>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="author">
            Créé par Ismail MOUYAHADA
        </div>
    """, unsafe_allow_html=True)
