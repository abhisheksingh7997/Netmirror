mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headlines = true\n\
\n\
" > ~/.streamlit/config.toml