#!/bin/bash

certbot renew --quiet --post-hook "systemctl reload nginx"