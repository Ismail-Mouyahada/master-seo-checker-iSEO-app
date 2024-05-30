import subprocess
import json
import tempfile
import os
import streamlit as st

def executer_lighthouse(url):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp_file:
            tmp_file_path = tmp_file.name

        command = [
            'lighthouse', url,
            '--output', 'json',
            '--output-path', tmp_file_path,
            '--quiet',
            '--chrome-flags="--headless"',
            '--only-categories=performance,seo'
        ]

        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode != 0:
            st.toast(f"Lighthouse a retourné une erreur : {result.stderr}", icon="⚠️")
            return None

        with open(tmp_file_path, 'r') as f:
            report = json.load(f)

        os.remove(tmp_file_path)

        return report

    except FileNotFoundError as e:
        st.toast(f"Erreur : Lighthouse n'a pas été trouvé. Assurez-vous qu'il est installé et accessible dans le PATH.", icon="⚠️")
        return None
    except json.JSONDecodeError as e:
        st.toast(f"Erreur : Le rapport JSON généré est invalide ou corrompu.", icon="⚠️")
        return None
    except Exception as e:
        st.toast(f"Erreur lors de l'exécution de Lighthouse : {e}", icon="⚠️")
        return None
