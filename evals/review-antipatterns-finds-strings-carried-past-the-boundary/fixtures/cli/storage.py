"""Where the rows come from."""


def rows_for(environment):
    if environment == "production":
        return [["order", "1"]]
    if environment == "stagng":
        return [["order", "staging-sample"]]
    return [["order", "sample"]]
