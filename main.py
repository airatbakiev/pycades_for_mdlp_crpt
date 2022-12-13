import base64
import pycades

store = pycades.Store()
store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CAPICOM_MY_STORE, pycades.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
certs = store.Certificates
assert(certs.Count != 0), "Certificates with private key not found"

signer = pycades.Signer()
signer.Certificate = certs.Item(1)
signer.Options = pycades.CAPICOM_CERTIFICATE_INCLUDE_END_ENTITY_ONLY

string_to_sign = "b1758253-9220-421a-8dee-c701f32e4c37" # insert your code
b = base64.b64encode(bytes(string_to_sign, 'utf-8'))
base64_str = b.decode('utf-8')

signedData = pycades.SignedData()
signedData.ContentEncoding = pycades.CADESCOM_BASE64_TO_BINARY
signedData.Content = base64_str
signature = signedData.SignCades(signer, pycades.CADESCOM_CADES_BES, True)
final_signature = ''.join(signature.splitlines())
print("--Signature--")
print(final_signature)
print("----")

_signedData = pycades.SignedData()
_signedData.ContentEncoding = pycades.CADESCOM_BASE64_TO_BINARY
_signedData.Content = signedData.Content
_signedData.VerifyCades(signature, pycades.CADESCOM_CADES_BES, True)
print("Verified successfully")
