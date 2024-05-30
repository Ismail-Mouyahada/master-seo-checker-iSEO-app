import re
import subprocess
import json
import tempfile
import os
import streamlit as st

def is_valid_url(url):
    # Regular expression to validate a URL
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # path
    return re.match(regex, url) is not None

def executer_lighthouse(url):
    try:
        # Create a temporary file to save the Lighthouse report
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp_file:
            tmp_file_path = tmp_file.name

        # Adjust the command for compatibility with Windows
        command = [
            'C:\\Users\\<YourUsername>\\AppData\\Roaming\\npm\\lighthouse.cmd',  # Full path to the Lighthouse executable
            url,
            '--output', 'json',
            '--output-path', tmp_file_path,
            '--quiet',
            '--chrome-flags="--headless"',
            '--only-categories=performance,seo'
        ]

        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode != 0:
            st.toast(f"Lighthouse returned an error: {result.stderr}", icon="⚠️")
            return None

        # Read the Lighthouse report from the temporary file
        with open(tmp_file_path, 'r') as f:
            report = json.load(f)

        # Remove the temporary file
        os.remove(tmp_file_path)

        return report

    except FileNotFoundError as e:
        st.toast(f"Error: Lighthouse not found. Make sure it is installed and accessible in the PATH.", icon="⚠️")
        return None
    except json.JSONDecodeError as e:
        st.toast(f"Error: The generated JSON report is invalid or corrupted.", icon="⚠️")
        return None
    except Exception as e:
        st.toast(f"Error executing Lighthouse: {e}", icon="⚠️")
        return None
