with open("redirects.txt") as f:
    # Filters out any empty lines
    redirect_list = list(filter(None, (line.rstrip().split(';') for line in f)))

routes = []

for subdirectory, url in redirect_list:
    routes.append(f"""\
                  
        location /{subdirectory} {{
            proxy_pass {url};
        }}
    """)

output_prefix = f"""\
http {{ 
  server {{
    listen 80;
"""

output_suffix = f"""\
}}
}}
"""

with open("nginx.conf", "w+") as fout:
    fout.write(output_prefix + "".join(routes) + output_suffix)