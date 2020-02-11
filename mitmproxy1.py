def response(flow):
    #------------------------------------------------
    #Script mitmproxy que guarda una sesion HTTP 
    #Los datos se guardan en un diccionario y archivo
    #-------------------------------------------------
    rFlow = {}
    rContent = ''
    #-----------------------------
    #Diccionario para Requests
    #-----------------------------
    rFlow['idRequest'] = flow.request.timestamp_start
    rFlow['rqMethod'] = flow.request.method
    rFlow['rqPath'] = flow.request.path
    rFlow['rqHttpVersion'] = flow.request.http_version
    rFlow['rqUrl'] = flow.request.url
    rFlow['rqCookies'] = flow.request.cookies.fields
    rFlow['rqHeaders'] = flow.request.headers
    rFlow['rqQuery'] = flow.request.query
    rFlow['rqBody'] = flow.request.content
    #-----------------------------
    #Diccionario para Responses
    #-----------------------------
    rFlow['rsStatusCode'] = flow.response.status_code
    rFlow['rsStatusText'] = flow.response.reason
    rFlow['rsHttpVersion'] = flow.response.http_version
    rFlow['rsCookies'] = flow.response.cookies
    rFlow['rsHeaders'] = flow.response.headers
    #rFlow['rsContent'] = flow.response.content
    rContent = flow.response.content
    flowFile(rFlow, rContent)
    
def flowFile(rFlow, rContent):
    try:
        os.mkdir('Content')
    except:
        pass

    flowDetails = open('flowDetails.txt','a')
    flowDetails.write(str(rFlow))
    flowDetails.write('\n')
    flowDetails.close()

    c = open('./Content/'+ str(rFlow['idRequest'])+ "_"  +str(str(rFlow['rqUrl']).replace('/','_')).replace(':','_'), 'w')
    c.write(str(rContent))
    c.close()
