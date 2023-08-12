import ovh
import subprocess

OVH_ENDPOINT = 'ovh-eu'
OVH_APP_KEY = 'votre_clé_application'
OVH_APP_SECRET = 'votre_secret_application'
OVH_CONSUMER_KEY = 'votre_clé_utilisateur'
OVH_ZONE = 'votre_domaine.com'
OVH_RECORD_NAME = '_acme-challenge'
OVH_RECORD_TYPE = 'TXT'

client = ovh.Client(
    endpoint=OVH_ENDPOINT,
    application_key=OVH_APP_KEY,
    application_secret=OVH_APP_SECRET,
    consumer_key=OVH_CONSUMER_KEY
)

records = client.get('/domain/zone/{}/record'.format(OVH_ZONE))
record_id = None
for record in records:
    if record['subDomain'] == OVH_RECORD_NAME and record['fieldType'] == OVH_RECORD_TYPE:
        record_id = record['id']
        break

if record_id is None:
    print("Enregistrement DNS non trouvé.")
    exit(1)

command = [
    'certbot',
    'certonly',
    '--dns-ovh',
    '--dns-ovh-credentials', '/chemin/vers/ovh.ini',
    '-d', OVH_ZONE,
    '--preferred-challenges', 'dns'
]

try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print("La commande Certbot a échoué :", e)
    exit(1)

challenge_output_from_certbot = "le_contenu_du_challenge_obtenu_de_certbot"

challenge = client.post('/domain/zone/{}/record/{}/update'.format(OVH_ZONE, record_id),
                        target=challenge_output_from_certbot,
                        ttl=60)

print("Enregistrement DNS mis à jour pour le challenge Let's Encrypt.")
print("En attente de la propagation DNS...")

# Attendre ici la propagation DNS

print("Certificat obtenu et enregistrement DNS vérifié.")
