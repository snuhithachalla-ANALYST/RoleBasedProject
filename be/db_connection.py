from supabase import create_client

SUPABASE_URL = "https://qohvhapbufceopjzmqnp.supabase.co"
SUPABASE_KEY = "sb_publishable_UBOVa_bidzOLK9i593A6xQ_pT9gNzjN"

supabase_client_object = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)