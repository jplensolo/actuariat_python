#-*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about elections
"""
import pandas
from urllib.error import HTTPError
from .data_exceptions import DataNotAvailableError


def elections_presidentielles(url=None):
    """
    download the data for the French elections from data.gouv.fr

    @param      url             url (None for default value)
    @return                     dictionaries of DataFrame

    The default url comes from
    `Election présidentielle 2012 - Résultats <https://www.data.gouv.fr/fr/datasets/election-presidentielle-2012-resultats-572124/>`_.
    You can get more at
    `Elections présidentielles 1965-2012 <https://www.data.gouv.fr/fr/datasets/elections-presidentielles-1965-2012-1/>`_.
    """
    if url is None:
        url = "http://static.data.gouv.fr/ff/e9c9483d39e00030815089aca1e2939f9cb99a84b0136e43056790e47bb4f0.xls"
    try:
        df = pandas.read_excel(url, sheetname=None)
    except HTTPError as e:
        raise DataNotAvailableError("unable to get data from " + url) from e
    return df
