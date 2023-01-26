#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 28901295))
    API_HASH = os.environ.get("API_HASH", "88435449ad6d4438fa36ed156ff59b63")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948630563:AAHPqTOZAcfhDuBiFMZPRYsvPAtVSle-bps") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001252405271")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "5627965010")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "1AZWarzgBu0_Xez5IEHtZE76vAj8rHnYixbAamtICkGnazg5W-2-X5UeCWDblP-DqmrE25hQLvQITH0P7t3hp3UBc3-i1HR6YXhRuqHcdcrg5szDuBIreqpCsm8-t3T5nUexrGbJkst68RD3MXusYCgXXCMF1BwI-UJPIKBJbr75xdlKdsdxJHqnX7z1KQ5rw6Jr5lUL7zzfGX7QDtYBVxFcSrpiNRlb0eHcPOJV64TwXJXXWIIRK--_6UgDlRpJPGpP9Yzq95bHEadpC-p3iQfWck7RYMx0iaBVKlH2NavEZw9_VKmVbe618fK5BJNMhFRdBmTT-V5v4i61-VxE8nFfKRIs1Hf8=")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001834718626")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
