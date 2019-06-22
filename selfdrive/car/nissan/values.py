from selfdrive.car import dbc_dict

class CAR:
  XTRAIL = "NISSAN X-TRAIL 2017 (JP)"

FINGERPRINTS = {
  CAR.XTRAIL: [{
    2: 5, 42: 6, 346: 6, 347: 5, 348: 8, 349: 7, 361: 8, 386: 8, 389: 8, 397: 8, 398: 8, 403: 8, 520: 2, 523: 6, 548: 8, 645: 8, 658: 8, 665: 8, 666: 8, 674: 2, 682: 8, 683: 8, 689: 8, 723: 8, 758: 3, 768: 2, 783: 3, 851: 8, 855: 8, 1041: 8, 1055: 2, 1104: 4, 1105: 6, 1107: 4, 1108: 8, 1111: 4, 1227: 8, 1228: 8, 1247: 4, 1266: 8, 1273: 7, 1342: 1, 1376: 6, 1401: 8, 1474: 2, 1497: 3, 2015: 8, 2016: 8, 2024: 8
  }],
}

DBC = {
  CAR.XTRAIL: dbc_dict('nissan_2017', None),
}
