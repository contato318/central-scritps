# -*- coding: UTF-8 -*-
import ldap
import logging


def authentica_ldap(end,usuario,senha):
    if not usuario or not senha:
        logging.error("Não foi informado usuário ou senha")
        return False
    if not end:
        logging.error("Não foi informado endereço do LDAP")
        return False

    try:
        ldap.set_option(ldap.OPT_REFERRALS,0)
        ldap.protocol_version = 3
        conn = ldap.initialize(end)
        conn.simple_bind_s(usuario, senha)
        return True
    except Exception as out:
        logging.error("Erro não esperado na authenticação: %s",str(out))
        return False
    except ldap.INVALID_CREDENTIALS:
        logging.error ('Não autenticado')
        return False
