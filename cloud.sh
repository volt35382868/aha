#!/usr/bin/env bash

cat <<'EOF'
---------------------------------------
Installing zelz is in progress..                                                  
---------------------------------------                                                  


                                                  
Copyright (C) 2020-2024 by volt35382868@Github, < https://github.com/aha >.
This file is part of < https://github.com/volt35382868/aha > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/volt35382868/aha/blob/master/LICENSE >
All rights reserved.
EOF

gunicorn app:app --daemon && python -m zelz