#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 28901295))
    API_HASH = os.environ.get("API_HASH", "88435449ad6d4438fa36ed156ff59b63")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5729182401:AAF96cHFyRfRK--BznUeybplrV8OyZIxbXU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "Join Channel - @MX_Networks")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001252405271")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "5627965010")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "AQBj16L_sBXWngUR-iJ5lj5ufmOIdxvKVOE7G2yBvvKf-mLpOdOKf8biFPSFNIJ6vJlHVOYT3qBccdLiU5CH4lj0TEXemJbbggurIQWGsng3FJsrqGS5SVblFOGcA1s_qqy2nmm5Lp3ced1VRFN3TbYlycFQm032H-5lIFXIgFizlAMCvi8ssTOqzaogYGeUtKh6vtXss00dESPKmdnYzY30rCitW43_tiO9zq5gPKgQbrLyEdLacZv-q-o6ugxrGq8LpHyVCXn4D2KLJtc09x-0H3OVmdRM9fYyBnNFZHy-sMJdMVr5ltEEok03Upigfv5k9BtlnDDyqen4_SKD8MOcAAAAAVcsK8MA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001617435227")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
