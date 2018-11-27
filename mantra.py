import requests
import json

def search_rek(query):
  base_url        = "url_mantra"
  nama_fungsi     = "get_ref_rek_search"
  query_string    = "nama_rek=%s"%query
  url_complete    = "%s/%s/%s" %(base_url, nama_fungsi, query_string)
  headers         = {"AccessKey":"pr97byu1yt", "User-Agent":"MANTRA"}

  request_process  = requests.get(url_complete, headers=headers)

  return json.dumps(request_process.json(), separators=(',',':'))

search_rek(masukkan_query_nama_rekening_yg_dicari)