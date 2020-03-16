#Extrai numero_identificador, codigo_instituicao_empresa, nome_instituicao_empresa, codigo_orgao, nome_unidade, nome_orgao,
#       codigo_unidade, logradouro_complemento, pais, uf, cidade, bairro, ddd, telefone, home_page, ramal, caixa_postal do arquivo xml do lattes

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

counter = 0

for filename in os.listdir(folder):

    path = folder+'/'+filename

    arq  = open(path,'r',encoding='latin-1')
    text = arq.read()
    xmlContent = text
    arq.close()

    counter += 1

    print(filename, counter)
    
    
    numeroIdentificador = re.compile(r'NUMERO-IDENTIFICADOR="(.*?)"')
    nI = numeroIdentificador.findall(xmlContent)
    NUMERO_IDENTIFICADOR.append(str(nI[0]))
   

    codigoInstituicaoEmpresa = re.compile(r'CODIGO-INSTITUICAO-EMPRESA="(.*?)"')
    cIE = codigoInstituicaoEmpresa.findall(xmlContent)
    CODIGO_INSTITUICAO_EMPRESA.append(cIE[0])

    nomeEmpresa = re.compile(r'NOME-INSTITUICAO-EMPRESA="(.*?)"')
    nE = nomeEmpresa.findall(xmlContent)
    NOME_INSTITUICAO_EMPRESA.append(nE[0])

    codigoOrgao = re.compile(r'CODIGO-ORGAO="(.*?)"')
    cO = codigoOrgao.findall(xmlContent)
    CODIGO_ORGAO.append(cO[0])

    nomeUnidade = re.compile(r'NOME-UNIDADE="(.*?)"')
    nU = nomeUnidade.findall(xmlContent)
    NOME_UNIDADE.append(nU[0])

    nomeOrgao = re.compile(r'NOME-ORGAO="(.*?)"')
    nO = nomeOrgao.findall(xmlContent)
    NOME_ORGAO.append(nO[0])

    codigoUnidade = re.compile(r'CODIGO-UNIDADE="(.*?)"')
    cU = codigoUnidade.findall(xmlContent)
    CODIGO_UNIDADE.append(cU[0])

    logradouroComplemento = re.compile(r'LOGRADOURO-COMPLEMENTO="(.*?)"')
    lC = logradouroComplemento.findall(xmlContent)
    LOGRADOURO_COMPLEMENTO.append(lC[0])

    pais = re.compile(r'PAIS="(.*?)"')
    pS = pais.findall(xmlContent)
    PAIS_l.append(pS[0])

    UF = re.compile(r'UF="(.*?)"')
    uF = UF.findall(xmlContent)
    UF_l.append(uF[0])

    cep = re.compile(r'CEP="(.*?)"')
    cP = cep.findall(xmlContent)
    CEP_l.append(cP[0])

    cidade = re.compile(r'CIDADE="(.*?)"')
    cP = cidade.findall(xmlContent)
    CIDADE_l.append(cP[0])

    bairro = re.compile(r'BAIRRO="(.*?)"')
    bO = bairro.findall(xmlContent)
    BAIRRO_l.append(bO[0])

    ddd = re.compile(r'DDD="(.*?)"')
    dd = ddd.findall(xmlContent)
    DDD_l.append(dd[0])

    telefone = re.compile(r'TELEFONE="(.*?)"')
    tE = telefone.findall(xmlContent)
    TELEFONE_l.append(tE[0])

    ramal = re.compile(r'RAMAL="(.*?)"')
    rL = ramal.findall(xmlContent)
    RAMAL_l.append(rL[0])

    fax = re.compile(r'FAX="(.*?)"')
    fX = fax.findall(xmlContent)
    FAX_l.append(fX[0])

    caixaPostal = re.compile(r'CAIXA-POSTAL="(.*?)"')
    cP = caixaPostal.findall(xmlContent)
    CAIXA_POSTAl.append(cP[0])

    homePage = re.compile(r'HOME-PAGE="(.*?)"')
    hP = homePage.findall(xmlContent)
    HOME_PAGE.append(hP[0])

    print(filename,'Done')


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
                   'Home_Page':HOME_PAGE
                   })

df.to_csv('cvs_PosDr_Jr.csv', index=False, encoding='latin-1')