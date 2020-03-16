import re, os, shutil
import pandas as pd

NUMERO_IDENTIFICADOR = []
CODIGO_INSTITUICAO_EMPRESA = []
NOME_INSTITUICAO_EMPRESA = []
CODIGO_ORGAO = []
NOME_UNIDADE = []
NOME_ORGAO = []
CODIGO_UNIDADE = []
LOGRADOURO_COMPLEMENTO = []
PAIS_l = []
UF_l = []
CEP_l = []
CIDADE_l = []
BAIRRO_l = []
DDD_l = []
TELEFONE_l = []
HOME_PAGE = []
RAMAL_l = []
FAX_l = []
CAIXA_POSTAl = []

folder = '/home/dti/Documentos/Extrator_Endereco_IDLattes/files_xml'

for filename in os.listdir(folder):

    path = folder+'/'+filename

    arq  = open(path,'r',encoding='latin-1')

    row = arq.readline()
    while row:
        xmlContent = row
        row = arq.readline()
    arq.close()

    numeroIdentificador = re.compile(r'NUMERO-IDENTIFICADOR="(.*?)"')
    nI = numeroIdentificador.findall(xmlContent)
    print(nI[0])
    NUMERO_IDENTIFICADOR.append(str(nI[0]))

    codigoInstituicaoEmpresa = re.compile(r'CODIGO-INSTITUICAO-EMPRESA="(.*?)"')
    cIE = codigoInstituicaoEmpresa.findall(xmlContent)
    print(cIE[0])
    CODIGO_INSTITUICAO_EMPRESA.append(str(cIE[0]))

    nomeEmpresa = re.compile(r'NOME-INSTITUICAO-EMPRESA="(.*?)"')
    nE = nomeEmpresa.findall(xmlContent)
    print(nE[0])
    NOME_INSTITUICAO_EMPRESA.append(nE[0])

    codigoOrgao = re.compile(r'CODIGO-ORGAO="(.*?)"')
    cO = codigoOrgao.findall(xmlContent)
    if not cO[0]:
        print('vazio')
        CODIGO_ORGAO.append(cO[0])
    else:
        print(cO[0])
        CODIGO_ORGAO.append(str(cO[0]))

    nomeUnidade = re.compile(r'NOME-UNIDADE="(.*?)"')
    nU = nomeUnidade.findall(xmlContent)
    if not nU[0]:
        print('vazio')
        NOME_UNIDADE.append(nU[0])
    else:
        print(nU[0])
        NOME_UNIDADE.append(nU[0])

    nomeOrgao = re.compile(r'NOME-ORGAO="(.*?)"')
    nO = nomeOrgao.findall(xmlContent)
    if not nO[0]:
        print('vazio')
        NOME_ORGAO.append(nO[0])
    else:
        print(nO[0])
        NOME_ORGAO.append(nO[0])

    codigoUnidade = re.compile(r'CODIGO-UNIDADE="(.*?)"')
    cU = codigoUnidade.findall(xmlContent)
    if not cU[0]:
        print('vazio')
        CODIGO_UNIDADE.append(cU[0])
    else:
        print(cU[0])
        CODIGO_UNIDADE.append(cU[0])

    logradouroComplemento = re.compile(r'LOGRADOURO-COMPLEMENTO="(.*?)"')
    lC = logradouroComplemento.findall(xmlContent)
    if not lC[0]:
        print('vazio')
        LOGRADOURO_COMPLEMENTO.append(lC[0])
    else:
        print(lC[0])
        LOGRADOURO_COMPLEMENTO.append(lC[0])

    pais = re.compile(r'PAIS="(.*?)"')
    pS = pais.findall(xmlContent)
    if not pS[0]:
        print('vazio')
        PAIS_l.append(pS[0])
    else:
        print(pS[0])
        PAIS_l.append(pS[0])

    UF = re.compile(r'UF="(.*?)"')
    uF = UF.findall(xmlContent)
    if not uF[0]:
        print('vazio')
        UF_l.append(uF[0])
    else:
        print(uF[0])
        UF_l.append(uF[0])

    cep = re.compile(r'CEP="(.*?)"')
    cP = cep.findall(xmlContent)
    if not cP[0]:
        print('vazio')
        CEP_l.append(cP[0])
    else:
        print(cP[0])
        CEP_l.append(cP[0])

    cidade = re.compile(r'CIDADE="(.*?)"')
    cP = cidade.findall(xmlContent)
    if not cP[0]:
        print('vazio')
        CIDADE_l.append(cP[0])
    else:
        print(cP[0])
        CIDADE_l.append(cP[0])

    bairro = re.compile(r'BAIRRO="(.*?)"')
    bO = bairro.findall(xmlContent)
    if not bO[0]:
        print('vazio')
        BAIRRO_l.append(bO[0])
    else:
        print(bO[0])
        BAIRRO_l.append(bO[0])

    ddd = re.compile(r'DDD="(.*?)"')
    dd = ddd.findall(xmlContent)
    if not dd[0]:
        print('vazio')
        DDD_l.append(dd[0])
    else:
        print(dd[0])
        DDD_l.append(dd[0])

    telefone = re.compile(r'TELEFONE="(.*?)"')
    tE = telefone.findall(xmlContent)
    if not tE[0]:
        print('vazio')
        TELEFONE_l.append(tE[0])
    else:
        print(tE[0])
        TELEFONE_l.append(tE[0])

    ramal = re.compile(r'RAMAL="(.*?)"')
    rL = ramal.findall(xmlContent)
    if not rL[0]:
        print('vazio')
        RAMAL_l.append(rL[0])
    else:
        print(rL[0])
        RAMAL_l.append(rL[0])

    fax = re.compile(r'FAX="(.*?)"')
    fX = fax.findall(xmlContent)
    if not fX[0]:
        print('vazio')
        FAX_l.append(fX[0])
    else:
        print(fX[0])
        FAX_l.append(fX[0])

    caixaPostal = re.compile(r'CAIXA-POSTAL="(.*?)"')
    cP = caixaPostal.findall(xmlContent)
    if not cP[0]:
        print('vazio')
        CAIXA_POSTAl.append(cP[0])
    else:
        print(cP[0])
        CAIXA_POSTAl.append(cP[0])

    homePage = re.compile(r'HOME-PAGE="(.*?)"')
    hP = homePage.findall(xmlContent)
    if not hP[0]:
        print('vazio')
        HOME_PAGE.append(hP[0])
    else:
        print(hP[0])
        HOME_PAGE.append(hP[0])

    print('*******************')


df = pd.DataFrame({'Num_Id':NUMERO_IDENTIFICADOR,
                   'Cod_Int_Emp':CODIGO_INSTITUICAO_EMPRESA,
                   'Nome_Int_Emp':NOME_INSTITUICAO_EMPRESA,
                   'Cod_Org':CODIGO_ORGAO,
                   'Nome_Org':NOME_ORGAO,
                   'Cod_Uni':CODIGO_UNIDADE,
                   'Nome_Uni':NOME_UNIDADE,
                   'Logradouro':LOGRADOURO_COMPLEMENTO,
                   'Pais':PAIS_l,
                   'UF':UF_l,
                   'CEP':CEP_l,
                   'Cidade':CIDADE_l,
                   'Bairro':BAIRRO_l,
                   'DDD':DDD_l,
                   'Telefone':TELEFONE_l,
                   'Ramal':RAMAL_l,
                   'Fax':FAX_l,
                   'Caixa-Postal':CAIXA_POSTAl,
                   'Home_Page':HOME_PAGE})
df.to_csv('teste1.csv', index=False, encoding='latin-1')
'''
NUMERO-IDENTIFICADOR - ok
CODIGO-INSTITUICAO-EMPRESA - ok
NOME-INSTITUICAO-EMPRESA - ok
CODIGO-ORGAO - ok
NOME-UNIDADE - ok
NOME-ORGAO - ok
CODIGO-UNIDADE - ok
LOGRADOURO-COMPLEMENTO - ok
PAIS - ok
UF - ok
CEP - ok
CIDADE - ok
BAIRRO - ok
DDD - ok
TELEFONE - ok
HOME-PAGE
'''

