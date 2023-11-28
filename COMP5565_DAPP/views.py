import json
from django.http import JsonResponse
from . import functions

def processable_Diamonds(request):
    result = functions.viewAllProcessableDiamonds()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def carveable_Diamonds(request):
    result = functions.viewAllCarveableDiamonds()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def collectable_Diamonds(request):
    result = functions.viewAllCollectibleDiamond()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def designable_Diamonds(request, address):
    result = functions.viewAllDesignableDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def purchasable_Diamonds(request):
    result = functions.viewAllPurchaseableDiamond()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def owned_Diamonds(request, address):
    result = functions.viewOwnedDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def mine_diamonds(request, diamondID, companyNum, address):
    functions.mineDiamond(diamondID, companyNum, address)
    result = functions.getDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def process_diamonds(request, diamondID, companyNum, address):
    functions.processDiamond(diamondID, companyNum, address)
    result = functions.getDiamond(address)
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def login(request):
    result = functions.getCompany()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

def register(request, companyName, password, address, companyNum, companyType):
    functions.insertCompany(companyName, password, address, companyNum, companyType)
    result = functions.getCompany()
    json_result = json.dumps(result)
    return JsonResponse(json_result, safe=False)

