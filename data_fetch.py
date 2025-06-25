import pandas as pd

# URLs des Data_Sets
url_small = "https://raw.githubusercontent.com/Jehuty4949/NSL_KDD/master/Small%20Training%20Set.csv"
url_full = "https://raw.githubusercontent.com/Jehuty4949/NSL_KDD/master/KDDTrain+.csv"

# Chargement des datasets
df_small = pd.read_csv(url_small, header=None)
df_full = pd.read_csv(url_full, header=None)

# Definition des noms de colonnes 
columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
    "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate",
    "label", "difficulty"
]

# Attribution des noms de colonnes
df_small.columns = columns
df_full.columns = columns

# Aperçu des données
print("Smalltrain:", df_small.shape)
print(df_small.head(), "\n")
print("Full train:", df_full.shape)
print(df_full.head())
