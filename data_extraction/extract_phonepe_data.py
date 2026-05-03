import os
import json
import pandas as pd

BASE_PATH = "../pulse/data"

# -------------------------------
# 1. Aggregated Transaction
# -------------------------------
def agg_transaction():
    path = os.path.join(BASE_PATH, "aggregated/transaction/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    for item in d["data"]["transactionData"]:
                        data.append([state, year, file.strip(".json"),
                                     item["name"],
                                     item["paymentInstruments"][0]["count"],
                                     item["paymentInstruments"][0]["amount"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","Type","Count","Amount"])


# -------------------------------
# 2. Aggregated User
# -------------------------------
def agg_user():
    path = os.path.join(BASE_PATH, "aggregated/user/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    if d["data"]["usersByDevice"]:
                        for item in d["data"]["usersByDevice"]:
                            data.append([state, year, file.strip(".json"),
                                         item["brand"],
                                         item["count"],
                                         item["percentage"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","Brand","Count","Percentage"])


# -------------------------------
# 3. Aggregated Insurance
# -------------------------------
def agg_insurance():
    path = os.path.join(BASE_PATH, "aggregated/insurance/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    for item in d["data"]["transactionData"]:
                        data.append([state, year, file.strip(".json"),
                                     item["name"],
                                     item["paymentInstruments"][0]["count"],
                                     item["paymentInstruments"][0]["amount"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","Type","Count","Amount"])


# -------------------------------
# 4. Map Transaction
# -------------------------------
def map_transaction():
    path = os.path.join(BASE_PATH, "map/transaction/hover/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    for item in d["data"]["hoverDataList"]:
                        data.append([state, year, file.strip(".json"),
                                     item["name"],
                                     item["metric"][0]["count"],
                                     item["metric"][0]["amount"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","District","Count","Amount"])


# -------------------------------
# 5. Map User
# -------------------------------
def map_user():
    path = os.path.join(BASE_PATH, "map/user/hover/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    for key, value in d["data"]["hoverData"].items():
                        data.append([state, year, file.strip(".json"),
                                     key,
                                     value["registeredUsers"],
                                     value["appOpens"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","District","Users","AppOpens"])


# -------------------------------
# 6. Map Insurance
# -------------------------------
def map_insurance():
    path = os.path.join(BASE_PATH, "map/insurance/hover/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    for item in d["data"]["hoverDataList"]:
                        data.append([state, year, file.strip(".json"),
                                     item["name"],
                                     item["metric"][0]["count"],
                                     item["metric"][0]["amount"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","District","Count","Amount"])


# -------------------------------
# 7. Top Transaction
# -------------------------------
def top_transaction():
    path = os.path.join(BASE_PATH, "top/transaction/country/india/state")
    data = []
    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):
                with open(os.path.join(path, state, year, file)) as f:
                    d = json.load(f)
                    for item in d["data"]["districts"]:
                        data.append([state, year, file.strip(".json"),
                                     item["entityName"],
                                     item["metric"]["count"],
                                     item["metric"]["amount"]])
    return pd.DataFrame(data, columns=["State","Year","Quarter","District","Count","Amount"])


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":

    os.makedirs("../outputs", exist_ok=True)

    agg_transaction().to_csv("../outputs/aggregated_transaction.csv", index=False)
    agg_user().to_csv("../outputs/aggregated_user.csv", index=False)
    agg_insurance().to_csv("../outputs/aggregated_insurance.csv", index=False)

    map_transaction().to_csv("../outputs/map_transaction.csv", index=False)
    map_user().to_csv("../outputs/map_user.csv", index=False)
    map_insurance().to_csv("../outputs/map_insurance.csv", index=False)

    top_transaction().to_csv("../outputs/top_transaction.csv", index=False)

    print("✅ ALL DATA EXTRACTED SUCCESSFULLY!")